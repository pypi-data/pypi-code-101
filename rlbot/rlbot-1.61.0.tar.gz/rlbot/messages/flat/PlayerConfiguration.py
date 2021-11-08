# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flat

import flatbuffers

class PlayerConfiguration(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPlayerConfiguration(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PlayerConfiguration()
        x.Init(buf, n + offset)
        return x

    # PlayerConfiguration
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PlayerConfiguration
    def VarietyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # PlayerConfiguration
    def Variety(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # PlayerConfiguration
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # PlayerConfiguration
    def Team(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PlayerConfiguration
    def Loadout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PlayerLoadout import PlayerLoadout
            obj = PlayerLoadout()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

# /// In the case where the requested player index is not available, spawnId will help
# /// the framework figure out what index was actually assigned to this player instead.
    # PlayerConfiguration
    def SpawnId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def PlayerConfigurationStart(builder): builder.StartObject(6)
def PlayerConfigurationAddVarietyType(builder, varietyType): builder.PrependUint8Slot(0, varietyType, 0)
def PlayerConfigurationAddVariety(builder, variety): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(variety), 0)
def PlayerConfigurationAddName(builder, name): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def PlayerConfigurationAddTeam(builder, team): builder.PrependInt32Slot(3, team, 0)
def PlayerConfigurationAddLoadout(builder, loadout): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(loadout), 0)
def PlayerConfigurationAddSpawnId(builder, spawnId): builder.PrependInt32Slot(5, spawnId, 0)
def PlayerConfigurationEnd(builder): return builder.EndObject()
