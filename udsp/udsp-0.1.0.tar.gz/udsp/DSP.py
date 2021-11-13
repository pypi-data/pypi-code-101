from udsp.DS import *
FREE = 0
BUSY = 1
BUSY_UPDATE = 2
CMDTYPES = {  # 不支持3字节长度的cmd
    1: 'B',
    2: 'H',
    4: 'I',
}

class DSP:
    @property
    def cl(self):
        return self.__cl
    def _get_cmd(self):
        return self.__cmd
    def _set_cmd(self, v):
        if self.tx_state != FREE:
            raise Exception("[Error]: You can only change <cmd> before <Encode> and after <TxReset>.")
        self.__cmd = v
    cmd = property(_get_cmd, _set_cmd)

    def __init__(self, txbuf, rxbuf, callback):
        self.cb = callback
        self.__cl = 1  # 保留属性，禁止修改
        self.__cmd_type = CMDTYPES[self.__cl]

        self.__cmd = 0
        self.__cl_cmd = 0xfe  # (2^cl - 1) - 1

        self.Loading(txbuf, rxbuf)

    def Loading(self, *args):
        self.rx_state = FREE
        self.tx_state = FREE
        self.txbuf = args[0]
        self.rxbuf = args[1]

        self.TxReset()
        self.RxReset()


    def RxReset(self):
        self.rx_state = FREE
        self.rds = DS(self.rxbuf)  # 为下次接收做好准备

    def TxReset(self):
        if (self.tx_state == BUSY_UPDATE):
            self.tds.O(self.__cmd_type)
            self.__ChangeCL(self.tds.O('B'))
        self.tx_state = FREE
        self.tds = DS(self.txbuf)  # 为下次发送做好准备

    def Encode(self, fmt, *data):
        """
        编码数据到tx_buffer

        注意，在发送数据前至少应该Encode过一次
        你可以使用.Encode (None)来添加空数据.

        注意，发送完成后记得TxReset
        :param fmt: 适用于struct的fmt 可以为None
        :param data:
        :return:
        """
        if self.tx_state == FREE:
            self.tx_state = BUSY
            self.__LoadTxCmd()
        if fmt is None: return
        self.tds.I(fmt, *data)

    def EncodeCL(self, new_cl):
        """
        修改双方的cmd length

        注意，调用该函数会覆盖txbuf已有的内容.

        注意，发送完成后记得TxReset
        :param new_cl: 新的cl，只能为1 2 4中的一种
        :return:
        """
        self.TxReset()
        self.cmd = self.__cl_cmd
        self.Encode('B', 2)

    def Decode(self, length=None):
        """
        解析rxbuf中的数据
        自动调用回调以及RxReset
        :param length: rxbuf中有多少个byte的数据, 不传参数时全部进行解析
        :return:
        """
        if length is None: length = len(self.rxbuf)
        if not length: return
        while self.rx_state != FREE: ...
        self.rx_state = BUSY
        #debug# print("rxlength:", length)
        self.rds.len = length

        cmd = self.__ParseRxCmd()
        if cmd is None: return

        self.cb(cmd, self.rds)

        self.RxReset()

    def __LoadTxCmd(self):
        self.tds.I(self.__cmd_type, self.cmd)
        if self.cmd == self.__cl_cmd:
            self.tx_state = BUSY_UPDATE

    def __ParseRxCmd(self):
        rtn = self.rds.O(self.__cmd_type)
        if rtn == self.__cl_cmd:
            self.__ChangeCL(self.rds.O('B'))
            return
        return rtn

    def __ChangeCL(self, new_cl):
        if (new_cl == self.__cl): return
        new_type = CMDTYPES.get(new_cl)
        if (new_type is None):
            raise Exception("[Error]: Unsupported CL<:{}>.".format(self.__cl))

        self.__cl = new_cl
        self.__cmd_type = new_type
        self.__cl_cmd = 2 ** new_cl - 2

    @property
    def txlen(self):
        """
        允许通过该属性获取txbuf中有效数据的长度
        :return:
        """
        return self.tds.len

    @property
    def rxlen(self):
        """
        允许通过该属性获取rxbuf中有效数据的长度
        :return:
        """
        return self.rds.len
    def __str__(self):
        return "<DSPState>\n\t<cmd:>{}\n\t<cl:>{}\n\t<TxState:>{}\n\t<RxState:>{}\n".format(self.cmd, self.cl, self.tds, self.rds)
    def __repr__(self):
        return str(self)
    def __len__(self):
        return dict(tx=self.txlen, rx=self.rxlen)

if __name__ == '__main__':
    class Compound:
        def __init__(self, i, d):
            self.i = i
            self.d = d
        def __repr__(self):
            return "Compound: <i: {}; d: {}>".format(self.i, self.d)

    def callback(cmd, ds):
        if cmd == 1:
            print("Get CMD:1, int =", ds.O('I'))
        elif cmd == 2:
            print("Get CMD:2, compound =", Compound(*ds.O('Id')))

    ba1, ba2 = bytearray(60), bytearray(60)
    dsp1, dsp2 = DSP(ba1, ba2, callback), DSP(ba2, ba1, callback)

    print(dsp1, dsp2)

    dsp1.cmd = 1
    dsp1.Encode('I', 114514)
    dsp2.Decode(dsp1.txlen)
    dsp1.TxReset()

    dsp2.cmd = 2
    dsp2.Encode('Id', 114, .514)
    dsp1.Decode(dsp2.txlen)
    dsp2.TxReset()

    dsp1.EncodeCL(2)
    dsp2.Decode(dsp1.txlen)
    dsp1.TxReset()

    print(dsp1, dsp2)
