# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PFAS_SAT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import PFAS_SAT_rc

class Ui_PFAS_SAT(object):
    def setupUi(self, PFAS_SAT):
        if not PFAS_SAT.objectName():
            PFAS_SAT.setObjectName(u"PFAS_SAT")
        PFAS_SAT.resize(1200, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PFAS_SAT.sizePolicy().hasHeightForWidth())
        PFAS_SAT.setSizePolicy(sizePolicy)
        PFAS_SAT.setMinimumSize(QSize(1200, 900))
        icon = QIcon()
        icon.addFile(u":/icons/ICONS/PFAS_SAT_1.png", QSize(), QIcon.Normal, QIcon.Off)
        PFAS_SAT.setWindowIcon(icon)
        PFAS_SAT.setIconSize(QSize(48, 24))
        self.actionExit = QAction(PFAS_SAT)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSaveInventory = QAction(PFAS_SAT)
        self.actionSaveInventory.setObjectName(u"actionSaveInventory")
        icon1 = QIcon()
        icon1.addFile(u":/icons/ICONS/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveInventory.setIcon(icon1)
        self.actionHelp_Gui = QAction(PFAS_SAT)
        self.actionHelp_Gui.setObjectName(u"actionHelp_Gui")
        icon2 = QIcon()
        icon2.addFile(u":/icons/ICONS/Help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp_Gui.setIcon(icon2)
        self.actionFAQ = QAction(PFAS_SAT)
        self.actionFAQ.setObjectName(u"actionFAQ")
        self.actionAbout_PFAS_SAT = QAction(PFAS_SAT)
        self.actionAbout_PFAS_SAT.setObjectName(u"actionAbout_PFAS_SAT")
        self.actionReferences = QAction(PFAS_SAT)
        self.actionReferences.setObjectName(u"actionReferences")
        self.actionOptions = QAction(PFAS_SAT)
        self.actionOptions.setObjectName(u"actionOptions")
        icon3 = QIcon()
        icon3.addFile(u":/icons/ICONS/Create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOptions.setIcon(icon3)
        self.centralwidget = QWidget(PFAS_SAT)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.PFAS_SAT_1 = QTabWidget(self.centralwidget)
        self.PFAS_SAT_1.setObjectName(u"PFAS_SAT_1")
        self.PFAS_SAT_1.setEnabled(True)
        self.PFAS_SAT_1.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setKerning(True)
        self.PFAS_SAT_1.setFont(font)
        self.Start_tab = QWidget()
        self.Start_tab.setObjectName(u"Start_tab")
        self.gridLayout_2 = QGridLayout(self.Start_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Start_new_project = QPushButton(self.Start_tab)
        self.Start_new_project.setObjectName(u"Start_new_project")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setKerning(True)
        self.Start_new_project.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/ICONS/Next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_new_project.setIcon(icon4)

        self.gridLayout_2.addWidget(self.Start_new_project, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.Start_tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 2)

        self.PFAS_SAT_1.addTab(self.Start_tab, "")
        self.WM_tab = QWidget()
        self.WM_tab.setObjectName(u"WM_tab")
        self.gridLayout_24 = QGridLayout(self.WM_tab)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.groupBox_11 = QGroupBox(self.WM_tab)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_8 = QGridLayout(self.groupBox_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.WM_DefData = QRadioButton(self.groupBox_11)
        self.WM_DefData.setObjectName(u"WM_DefData")

        self.horizontalLayout_4.addWidget(self.WM_DefData)

        self.WM_UserData = QRadioButton(self.groupBox_11)
        self.WM_UserData.setObjectName(u"WM_UserData")

        self.horizontalLayout_4.addWidget(self.WM_UserData)

        self.WM_browse = QToolButton(self.groupBox_11)
        self.WM_browse.setObjectName(u"WM_browse")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WM_browse.sizePolicy().hasHeightForWidth())
        self.WM_browse.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.WM_browse)

        self.WM_DataPath = QLineEdit(self.groupBox_11)
        self.WM_DataPath.setObjectName(u"WM_DataPath")
        self.WM_DataPath.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_4.addWidget(self.WM_DataPath)

        self.WM_ImportData = QPushButton(self.groupBox_11)
        self.WM_ImportData.setObjectName(u"WM_ImportData")
        icon5 = QIcon()
        icon5.addFile(u":/icons/ICONS/Load.png", QSize(), QIcon.Normal, QIcon.Off)
        self.WM_ImportData.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.WM_ImportData)

        self.horizontalSpacer = QSpacerItem(381, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.gridLayout_8.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.WM_tab)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_7 = QGridLayout(self.groupBox_18)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.WM_table_prop = QTableView(self.groupBox_18)
        self.WM_table_prop.setObjectName(u"WM_table_prop")
        self.WM_table_prop.setMinimumSize(QSize(0, 400))

        self.gridLayout_7.addWidget(self.WM_table_prop, 1, 0, 1, 5)

        self.Def_Proc_models = QPushButton(self.groupBox_18)
        self.Def_Proc_models.setObjectName(u"Def_Proc_models")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Def_Proc_models.sizePolicy().hasHeightForWidth())
        self.Def_Proc_models.setSizePolicy(sizePolicy2)
        self.Def_Proc_models.setMinimumSize(QSize(0, 0))
        self.Def_Proc_models.setIcon(icon4)

        self.gridLayout_7.addWidget(self.Def_Proc_models, 2, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(483, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_10, 2, 3, 1, 1)

        self.Update_WM_prop = QPushButton(self.groupBox_18)
        self.Update_WM_prop.setObjectName(u"Update_WM_prop")
        icon6 = QIcon()
        icon6.addFile(u":/icons/ICONS/Update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Update_WM_prop.setIcon(icon6)

        self.gridLayout_7.addWidget(self.Update_WM_prop, 2, 1, 1, 1)

        self.Clear_WM_uncert = QPushButton(self.groupBox_18)
        self.Clear_WM_uncert.setObjectName(u"Clear_WM_uncert")
        icon7 = QIcon()
        icon7.addFile(u":/icons/ICONS/Remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Clear_WM_uncert.setIcon(icon7)

        self.gridLayout_7.addWidget(self.Clear_WM_uncert, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox_18)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.WM_Combo = QComboBox(self.groupBox_18)
        self.WM_Combo.setObjectName(u"WM_Combo")
        sizePolicy.setHeightForWidth(self.WM_Combo.sizePolicy().hasHeightForWidth())
        self.WM_Combo.setSizePolicy(sizePolicy)
        self.WM_Combo.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_5.addWidget(self.WM_Combo)

        self.WM_help = QPushButton(self.groupBox_18)
        self.WM_help.setObjectName(u"WM_help")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.WM_help.sizePolicy().hasHeightForWidth())
        self.WM_help.setSizePolicy(sizePolicy3)
        self.WM_help.setIcon(icon2)
        self.WM_help.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.WM_help)

        self.WM_Show_Uncertainty = QCheckBox(self.groupBox_18)
        self.WM_Show_Uncertainty.setObjectName(u"WM_Show_Uncertainty")

        self.horizontalLayout_5.addWidget(self.WM_Show_Uncertainty)

        self.WM_UncertaintyHelp = QPushButton(self.groupBox_18)
        self.WM_UncertaintyHelp.setObjectName(u"WM_UncertaintyHelp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.WM_UncertaintyHelp.sizePolicy().hasHeightForWidth())
        self.WM_UncertaintyHelp.setSizePolicy(sizePolicy4)
        self.WM_UncertaintyHelp.setIcon(icon2)
        self.WM_UncertaintyHelp.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.WM_UncertaintyHelp)

        self.horizontalSpacer_8 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.gridLayout_7.addLayout(self.horizontalLayout_5, 0, 0, 1, 5)

        self.WM_ExportData = QPushButton(self.groupBox_18)
        self.WM_ExportData.setObjectName(u"WM_ExportData")
        self.WM_ExportData.setIcon(icon1)

        self.gridLayout_7.addWidget(self.WM_ExportData, 2, 2, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_18, 1, 0, 1, 1)

        self.PFAS_SAT_1.addTab(self.WM_tab, "")
        self.PM_tab = QWidget()
        self.PM_tab.setObjectName(u"PM_tab")
        self.PM_tab.setEnabled(True)
        self.gridLayout_10 = QGridLayout(self.PM_tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame = QFrame(self.PM_tab)
        self.frame.setObjectName(u"frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label)

        self.ProcModel_Combo = QComboBox(self.frame)
        self.ProcModel_Combo.setObjectName(u"ProcModel_Combo")
        sizePolicy.setHeightForWidth(self.ProcModel_Combo.sizePolicy().hasHeightForWidth())
        self.ProcModel_Combo.setSizePolicy(sizePolicy)
        self.ProcModel_Combo.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_11.addWidget(self.ProcModel_Combo)

        self.PM_Help = QPushButton(self.frame)
        self.PM_Help.setObjectName(u"PM_Help")
        self.PM_Help.setIcon(icon2)
        self.PM_Help.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.PM_Help)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.gridLayout_10.addWidget(self.frame, 0, 0, 1, 2)

        self.groupBox_19 = QGroupBox(self.PM_tab)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout = QGridLayout(self.groupBox_19)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ProcModel_def_input = QRadioButton(self.groupBox_19)
        self.ProcModel_def_input.setObjectName(u"ProcModel_def_input")

        self.gridLayout.addWidget(self.ProcModel_def_input, 0, 0, 1, 1)

        self.ProcModel_user_input = QRadioButton(self.groupBox_19)
        self.ProcModel_user_input.setObjectName(u"ProcModel_user_input")

        self.gridLayout.addWidget(self.ProcModel_user_input, 0, 1, 1, 1)

        self.ProcModel_Brow_Input = QToolButton(self.groupBox_19)
        self.ProcModel_Brow_Input.setObjectName(u"ProcModel_Brow_Input")

        self.gridLayout.addWidget(self.ProcModel_Brow_Input, 0, 2, 1, 1)

        self.ProcModel_Input_path = QLineEdit(self.groupBox_19)
        self.ProcModel_Input_path.setObjectName(u"ProcModel_Input_path")

        self.gridLayout.addWidget(self.ProcModel_Input_path, 0, 3, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_19, 1, 0, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.groupBox = QGroupBox(self.PM_tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy6)
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ContWater = QCheckBox(self.groupBox_3)
        self.ContWater.setObjectName(u"ContWater")

        self.verticalLayout_11.addWidget(self.ContWater)

        self.ContSoil = QCheckBox(self.groupBox_3)
        self.ContSoil.setObjectName(u"ContSoil")

        self.verticalLayout_11.addWidget(self.ContSoil)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.ContactWater = QCheckBox(self.groupBox_5)
        self.ContactWater.setObjectName(u"ContactWater")

        self.verticalLayout_13.addWidget(self.ContactWater)

        self.LFLeach = QCheckBox(self.groupBox_5)
        self.LFLeach.setObjectName(u"LFLeach")

        self.verticalLayout_13.addWidget(self.LFLeach)

        self.WWTEffluent = QCheckBox(self.groupBox_5)
        self.WWTEffluent.setObjectName(u"WWTEffluent")

        self.verticalLayout_13.addWidget(self.WWTEffluent)

        self.WWTSol = QCheckBox(self.groupBox_5)
        self.WWTSol.setObjectName(u"WWTSol")

        self.verticalLayout_13.addWidget(self.WWTSol)

        self.RawWWTSol = QCheckBox(self.groupBox_5)
        self.RawWWTSol.setObjectName(u"RawWWTSol")

        self.verticalLayout_13.addWidget(self.RawWWTSol)

        self.DewWWTSol = QCheckBox(self.groupBox_5)
        self.DewWWTSol.setObjectName(u"DewWWTSol")

        self.verticalLayout_13.addWidget(self.DewWWTSol)

        self.DryWWTSol = QCheckBox(self.groupBox_5)
        self.DryWWTSol.setObjectName(u"DryWWTSol")

        self.verticalLayout_13.addWidget(self.DryWWTSol)

        self.ROC = QCheckBox(self.groupBox_5)
        self.ROC.setObjectName(u"ROC")

        self.verticalLayout_13.addWidget(self.ROC)

        self.SGAC = QCheckBox(self.groupBox_5)
        self.SGAC.setObjectName(u"SGAC")

        self.verticalLayout_13.addWidget(self.SGAC)

        self.SIER = QCheckBox(self.groupBox_5)
        self.SIER.setObjectName(u"SIER")

        self.verticalLayout_13.addWidget(self.SIER)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_15 = QGroupBox(self.groupBox)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.StabSoil = QCheckBox(self.groupBox_15)
        self.StabSoil.setObjectName(u"StabSoil")

        self.verticalLayout_14.addWidget(self.StabSoil)

        self.Solidi_Waste = QCheckBox(self.groupBox_15)
        self.Solidi_Waste.setObjectName(u"Solidi_Waste")

        self.verticalLayout_14.addWidget(self.Solidi_Waste)

        self.AFFF = QCheckBox(self.groupBox_15)
        self.AFFF.setObjectName(u"AFFF")

        self.verticalLayout_14.addWidget(self.AFFF)


        self.verticalLayout.addWidget(self.groupBox_15)


        self.gridLayout_6.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.MSW = QCheckBox(self.groupBox_4)
        self.MSW.setObjectName(u"MSW")

        self.verticalLayout_12.addWidget(self.MSW)

        self.C_D_Waste = QCheckBox(self.groupBox_4)
        self.C_D_Waste.setObjectName(u"C_D_Waste")

        self.verticalLayout_12.addWidget(self.C_D_Waste)

        self.Med_Waste = QCheckBox(self.groupBox_4)
        self.Med_Waste.setObjectName(u"Med_Waste")

        self.verticalLayout_12.addWidget(self.Med_Waste)

        self.MOSP = QCheckBox(self.groupBox_4)
        self.MOSP.setObjectName(u"MOSP")

        self.verticalLayout_12.addWidget(self.MOSP)


        self.verticalLayout_18.addWidget(self.groupBox_4)

        self.groupBox_17 = QGroupBox(self.groupBox)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.FW = QCheckBox(self.groupBox_17)
        self.FW.setObjectName(u"FW")

        self.verticalLayout_16.addWidget(self.FW)

        self.Compost = QCheckBox(self.groupBox_17)
        self.Compost.setObjectName(u"Compost")

        self.verticalLayout_16.addWidget(self.Compost)

        self.ADSolids = QCheckBox(self.groupBox_17)
        self.ADSolids.setObjectName(u"ADSolids")

        self.verticalLayout_16.addWidget(self.ADSolids)

        self.ADLiquids = QCheckBox(self.groupBox_17)
        self.ADLiquids.setObjectName(u"ADLiquids")

        self.verticalLayout_16.addWidget(self.ADLiquids)


        self.verticalLayout_18.addWidget(self.groupBox_17)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.CompRes = QCheckBox(self.groupBox_2)
        self.CompRes.setObjectName(u"CompRes")

        self.verticalLayout_10.addWidget(self.CompRes)

        self.MRFRes = QCheckBox(self.groupBox_2)
        self.MRFRes.setObjectName(u"MRFRes")

        self.verticalLayout_10.addWidget(self.MRFRes)

        self.CombRes = QCheckBox(self.groupBox_2)
        self.CombRes.setObjectName(u"CombRes")

        self.verticalLayout_10.addWidget(self.CombRes)

        self.AutoShredRes = QCheckBox(self.groupBox_2)
        self.AutoShredRes.setObjectName(u"AutoShredRes")

        self.verticalLayout_10.addWidget(self.AutoShredRes)


        self.verticalLayout_18.addWidget(self.groupBox_2)


        self.gridLayout_6.addLayout(self.verticalLayout_18, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ProcModel_clear = QPushButton(self.PM_tab)
        self.ProcModel_clear.setObjectName(u"ProcModel_clear")
        self.ProcModel_clear.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.ProcModel_clear)

        self.ProcModel_update = QPushButton(self.PM_tab)
        self.ProcModel_update.setObjectName(u"ProcModel_update")
        self.ProcModel_update.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.ProcModel_update)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.Check_Data = QPushButton(self.PM_tab)
        self.Check_Data.setObjectName(u"Check_Data")
        sizePolicy.setHeightForWidth(self.Check_Data.sizePolicy().hasHeightForWidth())
        self.Check_Data.setSizePolicy(sizePolicy)
        self.Check_Data.setMinimumSize(QSize(0, 0))
        self.Check_Data.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.Check_Data)


        self.gridLayout_10.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.PFAS_SAT_1.addTab(self.PM_tab, "")
        self.PM_Input_Tab = QWidget()
        self.PM_Input_Tab.setObjectName(u"PM_Input_Tab")
        self.gridLayout_25 = QGridLayout(self.PM_Input_Tab)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.groupBox_21 = QGroupBox(self.PM_Input_Tab)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_26 = QGridLayout(self.groupBox_21)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.Clear_PM_uncert = QPushButton(self.groupBox_21)
        self.Clear_PM_uncert.setObjectName(u"Clear_PM_uncert")
        self.Clear_PM_uncert.setIcon(icon7)

        self.gridLayout_26.addWidget(self.Clear_PM_uncert, 2, 0, 1, 1)

        self.PM_InputData_Table = QTableView(self.groupBox_21)
        self.PM_InputData_Table.setObjectName(u"PM_InputData_Table")
        self.PM_InputData_Table.setMinimumSize(QSize(0, 400))

        self.gridLayout_26.addWidget(self.PM_InputData_Table, 1, 0, 1, 5)

        self.horizontalSpacer_11 = QSpacerItem(483, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_11, 2, 3, 1, 1)

        self.Update_PM_Data = QPushButton(self.groupBox_21)
        self.Update_PM_Data.setObjectName(u"Update_PM_Data")
        self.Update_PM_Data.setIcon(icon6)

        self.gridLayout_26.addWidget(self.Update_PM_Data, 2, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.groupBox_21)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.PM_Input_model = QComboBox(self.groupBox_21)
        self.PM_Input_model.setObjectName(u"PM_Input_model")
        sizePolicy.setHeightForWidth(self.PM_Input_model.sizePolicy().hasHeightForWidth())
        self.PM_Input_model.setSizePolicy(sizePolicy)
        self.PM_Input_model.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_6.addWidget(self.PM_Input_model)

        self.PM_Input_Help = QPushButton(self.groupBox_21)
        self.PM_Input_Help.setObjectName(u"PM_Input_Help")
        self.PM_Input_Help.setIcon(icon2)
        self.PM_Input_Help.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.PM_Input_Help)

        self.PM_Show_Uncertainty = QCheckBox(self.groupBox_21)
        self.PM_Show_Uncertainty.setObjectName(u"PM_Show_Uncertainty")

        self.horizontalLayout_6.addWidget(self.PM_Show_Uncertainty)

        self.PM_UncertaintyHelp = QPushButton(self.groupBox_21)
        self.PM_UncertaintyHelp.setObjectName(u"PM_UncertaintyHelp")
        sizePolicy4.setHeightForWidth(self.PM_UncertaintyHelp.sizePolicy().hasHeightForWidth())
        self.PM_UncertaintyHelp.setSizePolicy(sizePolicy4)
        self.PM_UncertaintyHelp.setIcon(icon2)
        self.PM_UncertaintyHelp.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.PM_UncertaintyHelp)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.gridLayout_26.addLayout(self.horizontalLayout_6, 0, 0, 1, 5)

        self.Def_System = QPushButton(self.groupBox_21)
        self.Def_System.setObjectName(u"Def_System")
        sizePolicy2.setHeightForWidth(self.Def_System.sizePolicy().hasHeightForWidth())
        self.Def_System.setSizePolicy(sizePolicy2)
        self.Def_System.setMinimumSize(QSize(0, 0))
        self.Def_System.setIcon(icon4)

        self.gridLayout_26.addWidget(self.Def_System, 2, 4, 1, 1)

        self.PM_ExportData = QPushButton(self.groupBox_21)
        self.PM_ExportData.setObjectName(u"PM_ExportData")
        self.PM_ExportData.setIcon(icon1)

        self.gridLayout_26.addWidget(self.PM_ExportData, 2, 2, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_21, 0, 0, 1, 1)

        self.PFAS_SAT_1.addTab(self.PM_Input_Tab, "")
        self.SYS_tab = QWidget()
        self.SYS_tab.setObjectName(u"SYS_tab")
        self.gridLayout_9 = QGridLayout(self.SYS_tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_20 = QGroupBox(self.SYS_tab)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.FU_Label = QLabel(self.groupBox_20)
        self.FU_Label.setObjectName(u"FU_Label")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.FU_Label.setFont(font2)

        self.horizontalLayout_15.addWidget(self.FU_Label)

        self.FU = QComboBox(self.groupBox_20)
        self.FU.setObjectName(u"FU")
        self.FU.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_15.addWidget(self.FU)

        self.FU_amount = QLineEdit(self.groupBox_20)
        self.FU_amount.setObjectName(u"FU_amount")

        self.horizontalLayout_15.addWidget(self.FU_amount)

        self.FU_unit = QLabel(self.groupBox_20)
        self.FU_unit.setObjectName(u"FU_unit")
        self.FU_unit.setFont(font2)

        self.horizontalLayout_15.addWidget(self.FU_unit)

        self.InitProject_Buttom = QPushButton(self.groupBox_20)
        self.InitProject_Buttom.setObjectName(u"InitProject_Buttom")
        icon8 = QIcon()
        icon8.addFile(u":/icons/ICONS/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.InitProject_Buttom.setIcon(icon8)

        self.horizontalLayout_15.addWidget(self.InitProject_Buttom)

        self.reset = QPushButton(self.groupBox_20)
        self.reset.setObjectName(u"reset")
        self.reset.setIcon(icon7)

        self.horizontalLayout_15.addWidget(self.reset)

        self.horizontalSpacer_3 = QSpacerItem(345, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.gridLayout_9.addWidget(self.groupBox_20, 0, 0, 1, 1)

        self.splitter = QSplitter(self.SYS_tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.frame_5 = QFrame(self.splitter)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(1000, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.splitter_5 = QSplitter(self.frame_5)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.FU_Proc_Widget = QGroupBox(self.splitter_5)
        self.FU_Proc_Widget.setObjectName(u"FU_Proc_Widget")
        self.FU_Proc_Widget.setMinimumSize(QSize(400, 200))
        self.verticalLayout_2 = QVBoxLayout(self.FU_Proc_Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ProcessSetFrame = QFrame(self.FU_Proc_Widget)
        self.ProcessSetFrame.setObjectName(u"ProcessSetFrame")
        self.ProcessSetFrame.setFrameShape(QFrame.StyledPanel)
        self.ProcessSetFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.ProcessSetFrame)

        self.Set_ProcessSet = QPushButton(self.FU_Proc_Widget)
        self.Set_ProcessSet.setObjectName(u"Set_ProcessSet")
        self.Set_ProcessSet.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.Set_ProcessSet)

        self.splitter_5.addWidget(self.FU_Proc_Widget)
        self.FU_Param_Widget = QGroupBox(self.splitter_5)
        self.FU_Param_Widget.setObjectName(u"FU_Param_Widget")
        self.FU_Param_Widget.setMinimumSize(QSize(400, 200))
        self.gridLayout_4 = QGridLayout(self.FU_Param_Widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.FlowParams_TreeView = QTreeView(self.FU_Param_Widget)
        self.FlowParams_TreeView.setObjectName(u"FlowParams_TreeView")

        self.gridLayout_4.addWidget(self.FlowParams_TreeView, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Update_Flowparams = QPushButton(self.FU_Param_Widget)
        self.Update_Flowparams.setObjectName(u"Update_Flowparams")
        self.Update_Flowparams.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.Update_Flowparams)

        self.FA_Btm = QPushButton(self.FU_Param_Widget)
        self.FA_Btm.setObjectName(u"FA_Btm")
        self.FA_Btm.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.FA_Btm)

        self.MC_Btm = QPushButton(self.FU_Param_Widget)
        self.MC_Btm.setObjectName(u"MC_Btm")
        self.MC_Btm.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.MC_Btm)

        self.SA_Btm = QPushButton(self.FU_Param_Widget)
        self.SA_Btm.setObjectName(u"SA_Btm")
        self.SA_Btm.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.SA_Btm)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.splitter_5.addWidget(self.FU_Param_Widget)

        self.gridLayout_13.addWidget(self.splitter_5, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame_5)
        self.frame_8 = QFrame(self.splitter)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.FU_Network = QGroupBox(self.frame_8)
        self.FU_Network.setObjectName(u"FU_Network")
        sizePolicy6.setHeightForWidth(self.FU_Network.sizePolicy().hasHeightForWidth())
        self.FU_Network.setSizePolicy(sizePolicy6)
        self.FU_Network.setMinimumSize(QSize(600, 300))
        self.gridLayout_16 = QGridLayout(self.FU_Network)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.scrollArea = QScrollArea(self.FU_Network)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 31))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Network_ImageLable = QLabel(self.scrollAreaWidgetContents)
        self.Network_ImageLable.setObjectName(u"Network_ImageLable")
        self.Network_ImageLable.setScaledContents(False)

        self.gridLayout_3.addWidget(self.Network_ImageLable, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_16.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.FU_Network, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame_8)

        self.gridLayout_9.addWidget(self.splitter, 1, 0, 1, 1)

        self.PFAS_SAT_1.addTab(self.SYS_tab, "")
        self.FA_tab = QWidget()
        self.FA_tab.setObjectName(u"FA_tab")
        self.gridLayout_14 = QGridLayout(self.FA_tab)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.splitter_2 = QSplitter(self.FA_tab)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.groupBox_6 = QGroupBox(self.splitter_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_20 = QGridLayout(self.groupBox_6)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.Inventory_table = QTableView(self.groupBox_6)
        self.Inventory_table.setObjectName(u"Inventory_table")

        self.gridLayout_20.addWidget(self.Inventory_table, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.groupBox_6)
        self.Sankey_groupBox = QGroupBox(self.splitter_2)
        self.Sankey_groupBox.setObjectName(u"Sankey_groupBox")
        self.Sankey_groupBox.setMinimumSize(QSize(0, 400))
        self.gridLayout_15 = QGridLayout(self.Sankey_groupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.Sankey_layout = QVBoxLayout()
        self.Sankey_layout.setObjectName(u"Sankey_layout")

        self.gridLayout_15.addLayout(self.Sankey_layout, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.Sankey_groupBox)

        self.gridLayout_14.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.PFAS_SAT_1.addTab(self.FA_tab, "")
        self.MC_tab = QWidget()
        self.MC_tab.setObjectName(u"MC_tab")
        self.gridLayout_88 = QGridLayout(self.MC_tab)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.frame_2 = QFrame(self.MC_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.groupBox_13 = QGroupBox(self.frame_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setFont(font2)
        self.gridLayout_19 = QGridLayout(self.groupBox_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.frame_3 = QFrame(self.groupBox_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer_47 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_47, 0, 4, 1, 1)

        self.MC_uncertain_filter = QCheckBox(self.frame_3)
        self.MC_uncertain_filter.setObjectName(u"MC_uncertain_filter")
        sizePolicy2.setHeightForWidth(self.MC_uncertain_filter.sizePolicy().hasHeightForWidth())
        self.MC_uncertain_filter.setSizePolicy(sizePolicy2)
        self.MC_uncertain_filter.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setBold(False)
        font3.setWeight(50)
        font3.setKerning(True)
        self.MC_uncertain_filter.setFont(font3)

        self.gridLayout_17.addWidget(self.MC_uncertain_filter, 0, 2, 1, 1)

        self.MC_uncertain_update = QPushButton(self.frame_3)
        self.MC_uncertain_update.setObjectName(u"MC_uncertain_update")
        sizePolicy2.setHeightForWidth(self.MC_uncertain_update.sizePolicy().hasHeightForWidth())
        self.MC_uncertain_update.setSizePolicy(sizePolicy2)
        self.MC_uncertain_update.setFont(font3)
        self.MC_uncertain_update.setIcon(icon6)

        self.gridLayout_17.addWidget(self.MC_uncertain_update, 0, 6, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font3)

        self.gridLayout_17.addWidget(self.label_5, 0, 0, 1, 1)

        self.MC_unceratin_clear = QPushButton(self.frame_3)
        self.MC_unceratin_clear.setObjectName(u"MC_unceratin_clear")
        sizePolicy2.setHeightForWidth(self.MC_unceratin_clear.sizePolicy().hasHeightForWidth())
        self.MC_unceratin_clear.setSizePolicy(sizePolicy2)
        self.MC_unceratin_clear.setFont(font3)
        self.MC_unceratin_clear.setIcon(icon7)

        self.gridLayout_17.addWidget(self.MC_unceratin_clear, 0, 5, 1, 1)

        self.MC_UncertaintyHelp = QPushButton(self.frame_3)
        self.MC_UncertaintyHelp.setObjectName(u"MC_UncertaintyHelp")
        font4 = QFont()
        font4.setBold(False)
        font4.setWeight(50)
        self.MC_UncertaintyHelp.setFont(font4)
        self.MC_UncertaintyHelp.setIcon(icon2)
        self.MC_UncertaintyHelp.setIconSize(QSize(24, 24))

        self.gridLayout_17.addWidget(self.MC_UncertaintyHelp, 0, 3, 1, 1)

        self.MC_Model = QComboBox(self.frame_3)
        self.MC_Model.setObjectName(u"MC_Model")
        sizePolicy2.setHeightForWidth(self.MC_Model.sizePolicy().hasHeightForWidth())
        self.MC_Model.setSizePolicy(sizePolicy2)
        self.MC_Model.setMinimumSize(QSize(200, 0))
        self.MC_Model.setFont(font3)

        self.gridLayout_17.addWidget(self.MC_Model, 0, 1, 1, 1)

        self.MC_ExportData = QPushButton(self.frame_3)
        self.MC_ExportData.setObjectName(u"MC_ExportData")
        sizePolicy2.setHeightForWidth(self.MC_ExportData.sizePolicy().hasHeightForWidth())
        self.MC_ExportData.setSizePolicy(sizePolicy2)
        self.MC_ExportData.setFont(font4)
        self.MC_ExportData.setIcon(icon1)

        self.gridLayout_17.addWidget(self.MC_ExportData, 0, 7, 1, 1)


        self.gridLayout_19.addWidget(self.frame_3, 0, 0, 1, 1)

        self.MC_Uncertain_table = QTableView(self.groupBox_13)
        self.MC_Uncertain_table.setObjectName(u"MC_Uncertain_table")
        self.MC_Uncertain_table.setMinimumSize(QSize(0, 200))
        self.MC_Uncertain_table.setFont(font3)

        self.gridLayout_19.addWidget(self.MC_Uncertain_table, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_13, 0, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.frame_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setFont(font2)
        self.gridLayout_5 = QGridLayout(self.groupBox_14)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.MC_run = QPushButton(self.groupBox_14)
        self.MC_run.setObjectName(u"MC_run")
        sizePolicy2.setHeightForWidth(self.MC_run.sizePolicy().hasHeightForWidth())
        self.MC_run.setSizePolicy(sizePolicy2)
        self.MC_run.setFont(font3)
        self.MC_run.setIcon(icon8)

        self.gridLayout_5.addWidget(self.MC_run, 0, 8, 1, 1)

        self.MC_show = QPushButton(self.groupBox_14)
        self.MC_show.setObjectName(u"MC_show")
        sizePolicy2.setHeightForWidth(self.MC_show.sizePolicy().hasHeightForWidth())
        self.MC_show.setSizePolicy(sizePolicy2)
        self.MC_show.setFont(font3)
        icon9 = QIcon()
        icon9.addFile(u":/icons/ICONS/show.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MC_show.setIcon(icon9)

        self.gridLayout_5.addWidget(self.MC_show, 0, 11, 1, 1)

        self.MC_save = QPushButton(self.groupBox_14)
        self.MC_save.setObjectName(u"MC_save")
        sizePolicy2.setHeightForWidth(self.MC_save.sizePolicy().hasHeightForWidth())
        self.MC_save.setSizePolicy(sizePolicy2)
        self.MC_save.setFont(font3)
        self.MC_save.setIcon(icon1)

        self.gridLayout_5.addWidget(self.MC_save, 0, 12, 1, 1)

        self.label_68 = QLabel(self.groupBox_14)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font3)

        self.gridLayout_5.addWidget(self.label_68, 0, 0, 1, 1)

        self.MC_PBr = QProgressBar(self.groupBox_14)
        self.MC_PBr.setObjectName(u"MC_PBr")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.MC_PBr.sizePolicy().hasHeightForWidth())
        self.MC_PBr.setSizePolicy(sizePolicy7)
        self.MC_PBr.setMaximumSize(QSize(300, 16777215))
        self.MC_PBr.setValue(0)
        self.MC_PBr.setTextVisible(False)

        self.gridLayout_5.addWidget(self.MC_PBr, 0, 9, 1, 1)

        self.label_12 = QLabel(self.groupBox_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.gridLayout_5.addWidget(self.label_12, 0, 4, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_13, 0, 10, 1, 1)

        self.MC_PFAS = QComboBox(self.groupBox_14)
        self.MC_PFAS.setObjectName(u"MC_PFAS")
        sizePolicy.setHeightForWidth(self.MC_PFAS.sizePolicy().hasHeightForWidth())
        self.MC_PFAS.setSizePolicy(sizePolicy)
        self.MC_PFAS.setMinimumSize(QSize(200, 0))
        self.MC_PFAS.setFont(font4)

        self.gridLayout_5.addWidget(self.MC_PFAS, 0, 5, 1, 1)

        self.label_13 = QLabel(self.groupBox_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.gridLayout_5.addWidget(self.label_13, 0, 2, 1, 1)

        self.MC_N_runs = QSpinBox(self.groupBox_14)
        self.MC_N_runs.setObjectName(u"MC_N_runs")
        sizePolicy2.setHeightForWidth(self.MC_N_runs.sizePolicy().hasHeightForWidth())
        self.MC_N_runs.setSizePolicy(sizePolicy2)
        self.MC_N_runs.setMinimumSize(QSize(100, 0))
        self.MC_N_runs.setFont(font3)

        self.gridLayout_5.addWidget(self.MC_N_runs, 0, 1, 1, 1)

        self.MC_Seed = QSpinBox(self.groupBox_14)
        self.MC_Seed.setObjectName(u"MC_Seed")
        sizePolicy2.setHeightForWidth(self.MC_Seed.sizePolicy().hasHeightForWidth())
        self.MC_Seed.setSizePolicy(sizePolicy2)
        self.MC_Seed.setMinimumSize(QSize(70, 0))
        self.MC_Seed.setFont(font4)

        self.gridLayout_5.addWidget(self.MC_Seed, 0, 3, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_14, 1, 0, 1, 1)


        self.gridLayout_88.addWidget(self.frame_2, 0, 0, 1, 1)

        self.PFAS_SAT_1.addTab(self.MC_tab, "")
        self.SA_tab = QWidget()
        self.SA_tab.setObjectName(u"SA_tab")
        self.gridLayout_28 = QGridLayout(self.SA_tab)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.splitter_3 = QSplitter(self.SA_tab)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.groupBox_7 = QGroupBox(self.splitter_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy5.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy5)
        self.gridLayout_22 = QGridLayout(self.groupBox_7)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_22.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_22.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_22.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_22.addWidget(self.label_8, 3, 0, 1, 1)

        self.SA_Start = QLineEdit(self.groupBox_7)
        self.SA_Start.setObjectName(u"SA_Start")

        self.gridLayout_22.addWidget(self.SA_Start, 3, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_22.addWidget(self.label_9, 4, 0, 1, 1)

        self.SA_Unit_1 = QLabel(self.groupBox_7)
        self.SA_Unit_1.setObjectName(u"SA_Unit_1")
        self.SA_Unit_1.setMinimumSize(QSize(100, 0))

        self.gridLayout_22.addWidget(self.SA_Unit_1, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(555, 84, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_2, 3, 3, 3, 1)

        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_22.addWidget(self.label_10, 5, 0, 1, 1)

        self.SA_Stop = QLineEdit(self.groupBox_7)
        self.SA_Stop.setObjectName(u"SA_Stop")

        self.gridLayout_22.addWidget(self.SA_Stop, 4, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_22.addWidget(self.label_7, 6, 0, 1, 1)

        self.SA_Unit_2 = QLabel(self.groupBox_7)
        self.SA_Unit_2.setObjectName(u"SA_Unit_2")

        self.gridLayout_22.addWidget(self.SA_Unit_2, 4, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SA_Run = QPushButton(self.groupBox_7)
        self.SA_Run.setObjectName(u"SA_Run")
        self.SA_Run.setFont(font3)
        self.SA_Run.setIcon(icon8)

        self.horizontalLayout.addWidget(self.SA_Run)

        self.SA_Plot = QPushButton(self.groupBox_7)
        self.SA_Plot.setObjectName(u"SA_Plot")
        self.SA_Plot.setIcon(icon9)

        self.horizontalLayout.addWidget(self.SA_Plot)

        self.SA_Save = QPushButton(self.groupBox_7)
        self.SA_Save.setObjectName(u"SA_Save")
        self.SA_Save.setFont(font3)
        self.SA_Save.setIcon(icon1)

        self.horizontalLayout.addWidget(self.SA_Save)

        self.SA_Clear = QPushButton(self.groupBox_7)
        self.SA_Clear.setObjectName(u"SA_Clear")
        self.SA_Clear.setIcon(icon7)

        self.horizontalLayout.addWidget(self.SA_Clear)


        self.gridLayout_22.addLayout(self.horizontalLayout, 7, 0, 1, 4)

        self.SA_PFAS = QComboBox(self.groupBox_7)
        self.SA_PFAS.setObjectName(u"SA_PFAS")

        self.gridLayout_22.addWidget(self.SA_PFAS, 6, 1, 1, 1)

        self.SA_Category = QComboBox(self.groupBox_7)
        self.SA_Category.setObjectName(u"SA_Category")

        self.gridLayout_22.addWidget(self.SA_Category, 1, 1, 1, 3)

        self.SA_Parameter = QComboBox(self.groupBox_7)
        self.SA_Parameter.setObjectName(u"SA_Parameter")

        self.gridLayout_22.addWidget(self.SA_Parameter, 2, 1, 1, 3)

        self.SA_Model = QComboBox(self.groupBox_7)
        self.SA_Model.setObjectName(u"SA_Model")

        self.gridLayout_22.addWidget(self.SA_Model, 0, 1, 1, 3)

        self.SA_NStep = QSpinBox(self.groupBox_7)
        self.SA_NStep.setObjectName(u"SA_NStep")

        self.gridLayout_22.addWidget(self.SA_NStep, 5, 1, 1, 1)

        self.splitter_3.addWidget(self.groupBox_7)
        self.groupBox_10 = QGroupBox(self.splitter_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(300, 0))
        self.gridLayout_23 = QGridLayout(self.groupBox_10)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.SA_ParamInfo = QTextBrowser(self.groupBox_10)
        self.SA_ParamInfo.setObjectName(u"SA_ParamInfo")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.SA_ParamInfo.sizePolicy().hasHeightForWidth())
        self.SA_ParamInfo.setSizePolicy(sizePolicy8)

        self.gridLayout_23.addWidget(self.SA_ParamInfo, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.groupBox_10)

        self.gridLayout_28.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.SA_tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy6.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy6)
        self.groupBox_9.setMinimumSize(QSize(0, 500))
        self.gridLayout_21 = QGridLayout(self.groupBox_9)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.SA_Results = QTableView(self.groupBox_9)
        self.SA_Results.setObjectName(u"SA_Results")

        self.gridLayout_21.addWidget(self.SA_Results, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.groupBox_9, 1, 0, 1, 1)

        self.PFAS_SAT_1.addTab(self.SA_tab, "")

        self.gridLayout_11.addWidget(self.PFAS_SAT_1, 0, 0, 1, 1)

        PFAS_SAT.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PFAS_SAT)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuReferences = QMenu(self.menubar)
        self.menuReferences.setObjectName(u"menuReferences")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        PFAS_SAT.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PFAS_SAT)
        self.statusbar.setObjectName(u"statusbar")
        PFAS_SAT.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuReferences.menuAction())
        self.menuFile.addAction(self.actionSaveInventory)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp_Gui)
        self.menuReferences.addAction(self.actionReferences)
        self.menuTools.addAction(self.actionOptions)

        self.retranslateUi(PFAS_SAT)

        self.PFAS_SAT_1.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(PFAS_SAT)
    # setupUi

    def retranslateUi(self, PFAS_SAT):
        PFAS_SAT.setWindowTitle(QCoreApplication.translate("PFAS_SAT", u"PFAS SAT", None))
        self.actionExit.setText(QCoreApplication.translate("PFAS_SAT", u"Exit", None))
        self.actionSaveInventory.setText(QCoreApplication.translate("PFAS_SAT", u"Save Inventory", None))
        self.actionHelp_Gui.setText(QCoreApplication.translate("PFAS_SAT", u"Help Guides", None))
        self.actionFAQ.setText(QCoreApplication.translate("PFAS_SAT", u"FAQ", None))
        self.actionAbout_PFAS_SAT.setText(QCoreApplication.translate("PFAS_SAT", u"About PFAS_SAT", None))
        self.actionReferences.setText(QCoreApplication.translate("PFAS_SAT", u"References", None))
        self.actionOptions.setText(QCoreApplication.translate("PFAS_SAT", u"Options", None))
        self.Start_new_project.setText(QCoreApplication.translate("PFAS_SAT", u"Start New Project", None))
        self.textBrowser.setHtml(QCoreApplication.translate("PFAS_SAT", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#aa0000;\">PFAS SAT</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#aa0000;\">Developed at North Carolina State University</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/ICONS/PFAS_SAT.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Development Team:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Georgia,serif'; font-size:8pt; font-weight:600; color:#000000;\">Mojtaba Sardarmehni</span><span style=\" font-family:'Georgia,serif'; font-size:8pt; color:#000000;\">, Ph.D. Student</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Georgia,serif'; font-size:8pt; font-weight:600; color:#000000;\">Amanda Karam</span><span style=\" font-family:'Georgia,serif'; font-size:8pt; color:#000000;\">, Ph.D. Student </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Georgia,serif'; font-size"
                        ":8pt; font-weight:600; color:#000000;\">Dr. James W. Levis</span><span style=\" font-family:'Georgia,serif'; font-size:8pt; color:#000000;\">, Research Assistant Professor</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Georgia,serif'; font-size:8pt; font-weight:600; color:#000000;\">Dr. Detlef Knappe</span><span style=\" font-family:'Georgia,serif'; font-size:8pt; color:#000000;\">, S. James Ellen Distinguished Professor</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Georgia,serif'; font-size:8pt; font-weight:600; color:#000000;\">Dr. Morton Barlaz</span><span style=\" font-family:'Georgia,serif'; font-size:8pt; color:#000000;\">, Distinguished Univ. Prof. and Dept. Head</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Related Links:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Install: </span><a href=\"http://go.ncsu.edu/pfas_sat\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">http://go.ncsu.edu/pfas_sat</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Document: </span><a href=\"http://go.ncsu.edu/pfas_sat_docs\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">http://go.ncsu.edu/pfas_sat_docs</span></a></p>\n"
"<p style=\""
                        " margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Source Code: </span><a href=\"http://go.ncsu.edu/pfas_sat_source_code\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">http://go.ncsu.edu/pfas_sat_source_code</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Report bugs: </span><a href=\"http://go.ncsu.edu/pfas_sat_issues\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">http://go.ncsu.edu/pfas_sat_issues</span></a></p></body></html>", None))
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.Start_tab), QCoreApplication.translate("PFAS_SAT", u"Start", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("PFAS_SAT", u"Waste Material Properties File", None))
        self.WM_DefData.setText(QCoreApplication.translate("PFAS_SAT", u"Default", None))
        self.WM_UserData.setText(QCoreApplication.translate("PFAS_SAT", u"User Defined", None))
        self.WM_browse.setText(QCoreApplication.translate("PFAS_SAT", u"Browse", None))
        self.WM_ImportData.setText(QCoreApplication.translate("PFAS_SAT", u"Import", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("PFAS_SAT", u"Waste Material Properties", None))
        self.Def_Proc_models.setText(QCoreApplication.translate("PFAS_SAT", u"Define Process Models", None))
        self.Update_WM_prop.setText(QCoreApplication.translate("PFAS_SAT", u"Update", None))
        self.Clear_WM_uncert.setText(QCoreApplication.translate("PFAS_SAT", u"Clear Uncertainty", None))
        self.label_2.setText(QCoreApplication.translate("PFAS_SAT", u"Waste Materials:", None))
        self.WM_help.setText("")
        self.WM_Show_Uncertainty.setText(QCoreApplication.translate("PFAS_SAT", u"Show uncertainty distributions", None))
        self.WM_UncertaintyHelp.setText(QCoreApplication.translate("PFAS_SAT", u"Uncertainty Distributions Help", None))
        self.WM_ExportData.setText(QCoreApplication.translate("PFAS_SAT", u"Export Data", None))
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.WM_tab), QCoreApplication.translate("PFAS_SAT", u"Waste Materials Properties", None))
        self.label.setText(QCoreApplication.translate("PFAS_SAT", u"Process:", None))
        self.PM_Help.setText("")
        self.groupBox_19.setTitle(QCoreApplication.translate("PFAS_SAT", u"Process Model Input File", None))
        self.ProcModel_def_input.setText(QCoreApplication.translate("PFAS_SAT", u"Default", None))
        self.ProcModel_user_input.setText(QCoreApplication.translate("PFAS_SAT", u"User Defined", None))
        self.ProcModel_Brow_Input.setText(QCoreApplication.translate("PFAS_SAT", u"Browse", None))
        self.groupBox.setTitle(QCoreApplication.translate("PFAS_SAT", u"Input Flow Types", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PFAS_SAT", u"Contaminated", None))
        self.ContWater.setText(QCoreApplication.translate("PFAS_SAT", u"Contaminated Water", None))
        self.ContSoil.setText(QCoreApplication.translate("PFAS_SAT", u"Contaminated Soil", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("PFAS_SAT", u"Water Treatment", None))
        self.ContactWater.setText(QCoreApplication.translate("PFAS_SAT", u"Contact Water", None))
        self.LFLeach.setText(QCoreApplication.translate("PFAS_SAT", u"Landfill Leachate", None))
        self.WWTEffluent.setText(QCoreApplication.translate("PFAS_SAT", u"WWT Effluent", None))
        self.WWTSol.setText(QCoreApplication.translate("PFAS_SAT", u"WWT Screen Rejects", None))
        self.RawWWTSol.setText(QCoreApplication.translate("PFAS_SAT", u"Raw WWT Solids", None))
        self.DewWWTSol.setText(QCoreApplication.translate("PFAS_SAT", u"Dewatered WWT Solids", None))
        self.DryWWTSol.setText(QCoreApplication.translate("PFAS_SAT", u"Dried WWT Solids", None))
        self.ROC.setText(QCoreApplication.translate("PFAS_SAT", u"RO Concentrate", None))
        self.SGAC.setText(QCoreApplication.translate("PFAS_SAT", u"Spent Granular Activated Carbon", None))
        self.SIER.setText(QCoreApplication.translate("PFAS_SAT", u"Spent Ion Exchange Resin", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("PFAS_SAT", u"Other", None))
        self.StabSoil.setText(QCoreApplication.translate("PFAS_SAT", u"Stabilized Soil", None))
        self.Solidi_Waste.setText(QCoreApplication.translate("PFAS_SAT", u"Solidified Waste", None))
        self.AFFF.setText(QCoreApplication.translate("PFAS_SAT", u"Aqueous Film-Forming Foam", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PFAS_SAT", u"Solid Waste", None))
        self.MSW.setText(QCoreApplication.translate("PFAS_SAT", u"Municipal Solid Waste", None))
        self.C_D_Waste.setText(QCoreApplication.translate("PFAS_SAT", u"Construction and Demolition Waste", None))
        self.Med_Waste.setText(QCoreApplication.translate("PFAS_SAT", u"Medical Waste", None))
        self.MOSP.setText(QCoreApplication.translate("PFAS_SAT", u"Miscellaneous Off-Spec Products", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("PFAS_SAT", u"Compost", None))
        self.FW.setText(QCoreApplication.translate("PFAS_SAT", u"Food Waste", None))
        self.Compost.setText(QCoreApplication.translate("PFAS_SAT", u"Compost", None))
        self.ADSolids.setText(QCoreApplication.translate("PFAS_SAT", u"AD Solids", None))
        self.ADLiquids.setText(QCoreApplication.translate("PFAS_SAT", u"AD Liquids", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PFAS_SAT", u"Residuals", None))
        self.CompRes.setText(QCoreApplication.translate("PFAS_SAT", u"Compost Residuals", None))
        self.MRFRes.setText(QCoreApplication.translate("PFAS_SAT", u"Material Recovery Facility Residuals", None))
        self.CombRes.setText(QCoreApplication.translate("PFAS_SAT", u"Combustion Residuals", None))
        self.AutoShredRes.setText(QCoreApplication.translate("PFAS_SAT", u"Automobile Shredder Residuals", None))
        self.ProcModel_clear.setText(QCoreApplication.translate("PFAS_SAT", u"Clear", None))
        self.ProcModel_update.setText(QCoreApplication.translate("PFAS_SAT", u"Update", None))
        self.Check_Data.setText(QCoreApplication.translate("PFAS_SAT", u"Check Process Models Input Data", None))
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.PM_tab), QCoreApplication.translate("PFAS_SAT", u"Process Models", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("PFAS_SAT", u"Process Model Input Data", None))
        self.Clear_PM_uncert.setText(QCoreApplication.translate("PFAS_SAT", u"Clear Uncertainty", None))
        self.Update_PM_Data.setText(QCoreApplication.translate("PFAS_SAT", u"Update", None))
        self.label_11.setText(QCoreApplication.translate("PFAS_SAT", u"Process:", None))
        self.PM_Input_Help.setText("")
        self.PM_Show_Uncertainty.setText(QCoreApplication.translate("PFAS_SAT", u"Show uncertainty distributions", None))
        self.PM_UncertaintyHelp.setText(QCoreApplication.translate("PFAS_SAT", u"Uncertainty distributions help", None))
        self.Def_System.setText(QCoreApplication.translate("PFAS_SAT", u"Define System", None))
        self.PM_ExportData.setText(QCoreApplication.translate("PFAS_SAT", u"Export Data", None))
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.PM_Input_Tab), QCoreApplication.translate("PFAS_SAT", u"Process Models Input Data", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("PFAS_SAT", u"Starting Material", None))
        self.FU_Label.setText(QCoreApplication.translate("PFAS_SAT", u"Waste Material", None))
        self.FU_unit.setText(QCoreApplication.translate("PFAS_SAT", u"Unit", None))
        self.InitProject_Buttom.setText(QCoreApplication.translate("PFAS_SAT", u"Setup scenario", None))
        self.reset.setText(QCoreApplication.translate("PFAS_SAT", u"Reset", None))
        self.FU_Proc_Widget.setTitle(QCoreApplication.translate("PFAS_SAT", u"Treatment Processes", None))
        self.Set_ProcessSet.setText(QCoreApplication.translate("PFAS_SAT", u"Create Network", None))
        self.FU_Param_Widget.setTitle(QCoreApplication.translate("PFAS_SAT", u"Treatment Network Parameters", None))
        self.Update_Flowparams.setText(QCoreApplication.translate("PFAS_SAT", u"Update Network", None))
        self.FA_Btm.setText(QCoreApplication.translate("PFAS_SAT", u"Flow Analysis", None))
        self.MC_Btm.setText(QCoreApplication.translate("PFAS_SAT", u"Monte Carlo", None))
        self.SA_Btm.setText(QCoreApplication.translate("PFAS_SAT", u"Sensitivity Analysis", None))
        self.FU_Network.setTitle(QCoreApplication.translate("PFAS_SAT", u"Treatment Network", None))
        self.Network_ImageLable.setText("")
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.SYS_tab), QCoreApplication.translate("PFAS_SAT", u"Define System", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("PFAS_SAT", u"Results", None))
        self.Sankey_groupBox.setTitle(QCoreApplication.translate("PFAS_SAT", u"Sankey Diagram", None))
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.FA_tab), QCoreApplication.translate("PFAS_SAT", u"Flow Analysis", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("PFAS_SAT", u"Uncertainty Browser", None))
        self.MC_uncertain_filter.setText(QCoreApplication.translate("PFAS_SAT", u"Only show input variables with defined uncertainty", None))
        self.MC_uncertain_update.setText(QCoreApplication.translate("PFAS_SAT", u"Update", None))
        self.label_5.setText(QCoreApplication.translate("PFAS_SAT", u"Process Model", None))
        self.MC_unceratin_clear.setText(QCoreApplication.translate("PFAS_SAT", u"Clear", None))
        self.MC_UncertaintyHelp.setText(QCoreApplication.translate("PFAS_SAT", u"Uncertainty Distributions Help", None))
        self.MC_ExportData.setText(QCoreApplication.translate("PFAS_SAT", u"Export Data", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("PFAS_SAT", u"Run", None))
        self.MC_run.setText(QCoreApplication.translate("PFAS_SAT", u"Run", None))
        self.MC_show.setText(QCoreApplication.translate("PFAS_SAT", u"Show Results", None))
        self.MC_save.setText(QCoreApplication.translate("PFAS_SAT", u"Save results", None))
        self.label_68.setText(QCoreApplication.translate("PFAS_SAT", u"Nnmber of runs:", None))
        self.label_12.setText(QCoreApplication.translate("PFAS_SAT", u"Type of PFAS:", None))
        self.label_13.setText(QCoreApplication.translate("PFAS_SAT", u"Seed:", None))
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.MC_tab), QCoreApplication.translate("PFAS_SAT", u"Monte Carlo simulation", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("PFAS_SAT", u"Parameter", None))
        self.label_3.setText(QCoreApplication.translate("PFAS_SAT", u"Model:", None))
        self.label_6.setText(QCoreApplication.translate("PFAS_SAT", u"Parameter:", None))
        self.label_4.setText(QCoreApplication.translate("PFAS_SAT", u"Category:", None))
        self.label_8.setText(QCoreApplication.translate("PFAS_SAT", u"Min:", None))
        self.label_9.setText(QCoreApplication.translate("PFAS_SAT", u"Max:", None))
        self.SA_Unit_1.setText("")
        self.label_10.setText(QCoreApplication.translate("PFAS_SAT", u"Number of steps:", None))
        self.label_7.setText(QCoreApplication.translate("PFAS_SAT", u"Type of PFAS", None))
        self.SA_Unit_2.setText("")
        self.SA_Run.setText(QCoreApplication.translate("PFAS_SAT", u"Run", None))
        self.SA_Plot.setText(QCoreApplication.translate("PFAS_SAT", u"Plot Results", None))
        self.SA_Save.setText(QCoreApplication.translate("PFAS_SAT", u"Save results", None))
        self.SA_Clear.setText(QCoreApplication.translate("PFAS_SAT", u"Clear", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("PFAS_SAT", u"Parameter Information", None))
        self.SA_ParamInfo.setHtml(QCoreApplication.translate("PFAS_SAT", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("PFAS_SAT", u"Results", None))
        self.PFAS_SAT_1.setTabText(self.PFAS_SAT_1.indexOf(self.SA_tab), QCoreApplication.translate("PFAS_SAT", u"Sensitivity Analysis", None))
        self.menuFile.setTitle(QCoreApplication.translate("PFAS_SAT", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("PFAS_SAT", u"Help", None))
        self.menuReferences.setTitle(QCoreApplication.translate("PFAS_SAT", u"References", None))
        self.menuTools.setTitle(QCoreApplication.translate("PFAS_SAT", u"Tools", None))
    # retranslateUi

