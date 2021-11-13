from udsp.DSP import *
from udsp.UDSP import *

"""
数据流处理器
Data Stream Processor

这个DSP能管理一个发送buffer和一个接收buffer，使用struct进行结构化。

def call_back(cmd, ds):
	if cmd == 1:
		print("收到了1号命令，1号命令的数据为:", ds.O('B'))  # 1号命令传输什么样的数据 需要双方事先约定

txbuf, rxbuf = bytearray(40), bytearray(40)

tx, rx = DSP(txbuf, rxbuf, None), DSP(rxbuf, txbuf, call_back)

tx.cmd = 1  # 设置命令号(默认命令号的内存占用1个字节，即不能超过256。由于协议要求， 0和0xff..是不能用的.)
tx.Encode('B', 155);

rx.Decode()
tx.TxReset()  # 发送完成后必须清除发送信息

# --------------------------------------

tx.EncodeCL(2)  # 修改命令号的内存占用为2，即命令号不能超过65536。 由于协议要求， 0和0xffff..是不能用的.
# 只能设置为1 2 4中的一种

rx.Decode()  # 对方收到后会自动修改命令号的内存占用，而不会进入call_back.
tx.TxReset()  # 发送完成后必须清除发送信息

#// -------- ####################################################### ----------------------

This DSP can manage a transmit buffer and a receive buffer, and use struct for structure.

def call_back(cmd, ds):
	if cmd == 1:
		print("Command 1 received. The data of command 1 is:", ds.O('B'))  # What kind of data should be transmitted by order 1? Both parties need to agree in advance

txbuf, rxbuf = bytearray(40), bytearray(40)

tx, rx = DSP(txbuf, rxbuf, None), DSP(rxbuf, txbuf, call_back)

tx.cmd = 1  # Set the command number (the memory of the default command number occupies 1 byte, that is, it cannot exceed 256. Due to protocol requirements, 0 and 0xff.. are unavailable.)
tx.Encode('B', 155);

rx.Decode()
tx.TxReset()  # After sending, the sending information must be cleared
# --------------------------------------

tx.EncodeCL(2)  # The memory consumption of modifying the command number is 2, that is, the command number cannot exceed 65536. 0 and 0xFFFF.. are not available due to protocol requirements
# Can only be set to one of 1 2 4

rx.Decode()  # After receiving the command, the other party will automatically modify the memory occupation of the command number without entering call_back.
tx.TxReset()  # After sending, the sending information must be cleared


"""




# Example
"""
from dsp import *
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
"""

#Example with uart(series)
"""
def func(cmd, ds):
	if cmd == 1:
		print(ds.O('B'))
udsp = UDSP("COM3", func)
while True:
	time.sleep(1)
	sdsp.Decode()
	#print(tmp)
"""

