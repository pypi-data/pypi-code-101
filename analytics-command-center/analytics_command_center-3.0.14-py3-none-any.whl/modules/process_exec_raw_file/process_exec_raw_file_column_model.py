#
# rawColLogicalName: String,
# rawColOriginName: String,
# rawColDataType: String,
# rawColDataTypeLen: Int,
# rawColDataTypeDec: Int,
# rawColPosition: Int,
# rawColPosIni: Int,
# rawColPosEnd: Int,
# rawColApplyTrim: Boolean,
# rawColConvertNull: Boolean,
# rawColGetOriginCol: Boolean,
# rawColGetOriginSufix: String
#
class ProcessExecRawFileColumnModel:
    def __init__(self, **args):
        self.rawColLogicalName = args["rawColLogicalName"] if "rawColLogicalName" in args else ""
        self.rawColOriginName = args["rawColOriginName"] if "rawColOriginName" in args else ""
        self.rawColDataType = args["rawColDataType"] if "rawColDataType" in args else ""
        self.rawColDataTypeLen = args["rawColDataTypeLen"] if "rawColDataTypeLen" in args else 0
        self.rawColDataTypeDec = args["rawColDataTypeDec"] if "rawColDataTypeDec" in args else 0
        self.rawColPosition = args["rawColPosition"] if "rawColPosition" in args else 0
        self.rawColPosIni = args["rawColPosIni"] if "rawColPosIni" in args else 0
        self.rawColPosEnd = args["rawColPosEnd"] if "rawColPosEnd" in args else 0
        self.rawColApplyTrim = args["rawColApplyTrim"] if "rawColApplyTrim" in args else False
        self.rawColConvertNull = args["rawColConvertNull"] if "rawColConvertNull" in args else False
        self.rawColGetOriginCol = args["rawColGetOriginCol"] if "rawColGetOriginCol" in args else False
        self.rawColGetOriginSufix = args["rawColGetOriginSufix"] if "rawColGetOriginSufix" in args else ""
        self.args = args
        