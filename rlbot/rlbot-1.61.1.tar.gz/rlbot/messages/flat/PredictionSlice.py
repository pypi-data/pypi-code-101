# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flat

import flatbuffers

class PredictionSlice(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPredictionSlice(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PredictionSlice()
        x.Init(buf, n + offset)
        return x

    # PredictionSlice
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// The moment in game time that this prediction corresponds to.
# /// This corresponds to 'secondsElapsed' in the GameInfo table.
    # PredictionSlice
    def GameSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// The predicted location and motion of the object.
    # PredictionSlice
    def Physics(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Physics import Physics
            obj = Physics()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def PredictionSliceStart(builder): builder.StartObject(2)
def PredictionSliceAddGameSeconds(builder, gameSeconds): builder.PrependFloat32Slot(0, gameSeconds, 0.0)
def PredictionSliceAddPhysics(builder, physics): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(physics), 0)
def PredictionSliceEnd(builder): return builder.EndObject()
