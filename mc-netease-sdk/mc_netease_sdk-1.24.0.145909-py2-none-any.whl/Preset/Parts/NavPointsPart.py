# -*- coding: utf-8 -*-
from Meta.ClassMetaManager import sunshine_class_meta
from Meta.TypeMeta import PArray, PRelativeCoordinate, PBool, PDict
from Preset.Model import PartBaseMeta


@sunshine_class_meta
class NavPointsPartMeta(PartBaseMeta):
    CLASS_NAME = "NavPointsPart"
    PROPERTIES = {
        "preview": PBool(sort=6, text="预览路径", group='巡逻路径'),
        'patrolsPath': PArray(sort=7, text="路径", group='巡逻路径', childAttribute=PDict(
            sort=1, text='路径点', children={
                "point": PRelativeCoordinate(text="位置", tip="如果和前一点的距离大于 50, 巡逻可能失败")
            }))
    }


from Preset.Model.PartBase import PartBase

class NavPointsPart(PartBase):
    def __init__(self):
        # type: () -> None
        """
        导航路径零件
        """
        self.patrolsPath = None

