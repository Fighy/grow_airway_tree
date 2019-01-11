# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/qt/view.ui'
#
# Created: Fri Jan 11 14:49:55 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_View(object):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(1154, 899)
        font = QtGui.QFont()
        font.setPointSize(11)
        View.setFont(font)
        self.horizontalLayout = QtGui.QHBoxLayout(View)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.controlPanel_widget = QtGui.QWidget(View)
        self.controlPanel_widget.setMinimumSize(QtCore.QSize(270, 0))
        self.controlPanel_widget.setObjectName("controlPanel_widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.controlPanel_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtGui.QGroupBox(self.controlPanel_widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.airwayIpnode_pushButton = QtGui.QPushButton(self.groupBox_3)
        self.airwayIpnode_pushButton.setObjectName("airwayIpnode_pushButton")
        self.gridLayout_4.addWidget(self.airwayIpnode_pushButton, 0, 1, 1, 1)
        self.airwayIpelem_pushButton = QtGui.QPushButton(self.groupBox_3)
        self.airwayIpelem_pushButton.setObjectName("airwayIpelem_pushButton")
        self.gridLayout_4.addWidget(self.airwayIpelem_pushButton, 1, 1, 1, 1)
        self.airwayIpelem_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.airwayIpelem_lineEdit.setFont(font)
        self.airwayIpelem_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.airwayIpelem_lineEdit.setObjectName("airwayIpelem_lineEdit")
        self.gridLayout_4.addWidget(self.airwayIpelem_lineEdit, 1, 0, 1, 1)
        self.airwayIpnode_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.airwayIpnode_lineEdit.setFont(font)
        self.airwayIpnode_lineEdit.setObjectName("airwayIpnode_lineEdit")
        self.gridLayout_4.addWidget(self.airwayIpnode_lineEdit, 0, 0, 1, 1)
        self.loadAirway_pushButton = QtGui.QPushButton(self.groupBox_3)
        self.loadAirway_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loadAirway_pushButton.setObjectName("loadAirway_pushButton")
        self.gridLayout_4.addWidget(self.loadAirway_pushButton, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.controlPanel_widget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.surfaceIpnode_lineEdit = QtGui.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.surfaceIpnode_lineEdit.setFont(font)
        self.surfaceIpnode_lineEdit.setObjectName("surfaceIpnode_lineEdit")
        self.gridLayout_5.addWidget(self.surfaceIpnode_lineEdit, 0, 0, 1, 1)
        self.surfaceIpnode_pushButton = QtGui.QPushButton(self.groupBox_4)
        self.surfaceIpnode_pushButton.setObjectName("surfaceIpnode_pushButton")
        self.gridLayout_5.addWidget(self.surfaceIpnode_pushButton, 0, 1, 1, 1)
        self.surfaceIpelem_lineEdit = QtGui.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.surfaceIpelem_lineEdit.setFont(font)
        self.surfaceIpelem_lineEdit.setObjectName("surfaceIpelem_lineEdit")
        self.gridLayout_5.addWidget(self.surfaceIpelem_lineEdit, 1, 0, 1, 1)
        self.surfaceIpelem_pushButton = QtGui.QPushButton(self.groupBox_4)
        self.surfaceIpelem_pushButton.setObjectName("surfaceIpelem_pushButton")
        self.gridLayout_5.addWidget(self.surfaceIpelem_pushButton, 1, 1, 1, 1)
        self.loadSurface_pushButton = QtGui.QPushButton(self.groupBox_4)
        self.loadSurface_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loadSurface_pushButton.setObjectName("loadSurface_pushButton")
        self.gridLayout_5.addWidget(self.loadSurface_pushButton, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_2 = QtGui.QGroupBox(self.controlPanel_widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridSize_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.gridSize_doubleSpinBox.setDecimals(1)
        self.gridSize_doubleSpinBox.setMinimum(1.0)
        self.gridSize_doubleSpinBox.setMaximum(50.0)
        self.gridSize_doubleSpinBox.setProperty("value", 6.0)
        self.gridSize_doubleSpinBox.setObjectName("gridSize_doubleSpinBox")
        self.gridLayout.addWidget(self.gridSize_doubleSpinBox, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.startNode_spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.startNode_spinBox.setMinimum(1)
        self.startNode_spinBox.setMaximum(500)
        self.startNode_spinBox.setProperty("value", 12)
        self.startNode_spinBox.setObjectName("startNode_spinBox")
        self.gridLayout.addWidget(self.startNode_spinBox, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.angleMax_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.angleMax_doubleSpinBox.setDecimals(1)
        self.angleMax_doubleSpinBox.setMaximum(180.0)
        self.angleMax_doubleSpinBox.setProperty("value", 60.0)
        self.angleMax_doubleSpinBox.setObjectName("angleMax_doubleSpinBox")
        self.gridLayout.addWidget(self.angleMax_doubleSpinBox, 2, 1, 1, 1)
        self.angleMin_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.angleMin_doubleSpinBox.setDecimals(1)
        self.angleMin_doubleSpinBox.setMaximum(180.0)
        self.angleMin_doubleSpinBox.setProperty("value", 20.0)
        self.angleMin_doubleSpinBox.setObjectName("angleMin_doubleSpinBox")
        self.gridLayout.addWidget(self.angleMin_doubleSpinBox, 3, 1, 1, 1)
        self.branchFraction_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.branchFraction_doubleSpinBox.setDecimals(1)
        self.branchFraction_doubleSpinBox.setMaximum(1.0)
        self.branchFraction_doubleSpinBox.setSingleStep(0.1)
        self.branchFraction_doubleSpinBox.setProperty("value", 0.4)
        self.branchFraction_doubleSpinBox.setObjectName("branchFraction_doubleSpinBox")
        self.gridLayout.addWidget(self.branchFraction_doubleSpinBox, 4, 1, 1, 1)
        self.lengthLimit_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.lengthLimit_doubleSpinBox.setDecimals(1)
        self.lengthLimit_doubleSpinBox.setMaximum(10.0)
        self.lengthLimit_doubleSpinBox.setSingleStep(0.1)
        self.lengthLimit_doubleSpinBox.setProperty("value", 1.5)
        self.lengthLimit_doubleSpinBox.setObjectName("lengthLimit_doubleSpinBox")
        self.gridLayout.addWidget(self.lengthLimit_doubleSpinBox, 5, 1, 1, 1)
        self.shortestLength_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.shortestLength_doubleSpinBox.setDecimals(1)
        self.shortestLength_doubleSpinBox.setMaximum(10.0)
        self.shortestLength_doubleSpinBox.setSingleStep(0.1)
        self.shortestLength_doubleSpinBox.setProperty("value", 1.5)
        self.shortestLength_doubleSpinBox.setObjectName("shortestLength_doubleSpinBox")
        self.gridLayout.addWidget(self.shortestLength_doubleSpinBox, 6, 1, 1, 1)
        self.rotationLimit_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.rotationLimit_doubleSpinBox.setDecimals(1)
        self.rotationLimit_doubleSpinBox.setMaximum(360.0)
        self.rotationLimit_doubleSpinBox.setSingleStep(10.0)
        self.rotationLimit_doubleSpinBox.setProperty("value", 180.0)
        self.rotationLimit_doubleSpinBox.setObjectName("rotationLimit_doubleSpinBox")
        self.gridLayout.addWidget(self.rotationLimit_doubleSpinBox, 7, 1, 1, 1)
        self.generate_pushButton = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_pushButton.sizePolicy().hasHeightForWidth())
        self.generate_pushButton.setSizePolicy(sizePolicy)
        self.generate_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.gridLayout.addWidget(self.generate_pushButton, 9, 0, 1, 2)
        self.reset_checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.reset_checkBox.setObjectName("reset_checkBox")
        self.gridLayout.addWidget(self.reset_checkBox, 8, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox = QtGui.QGroupBox(self.controlPanel_widget)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outputExnode_lineEdit = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.outputExnode_lineEdit.setFont(font)
        self.outputExnode_lineEdit.setObjectName("outputExnode_lineEdit")
        self.gridLayout_2.addWidget(self.outputExnode_lineEdit, 0, 0, 1, 1)
        self.outputExelem_lineEdit = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.outputExelem_lineEdit.setFont(font)
        self.outputExelem_lineEdit.setObjectName("outputExelem_lineEdit")
        self.gridLayout_2.addWidget(self.outputExelem_lineEdit, 1, 0, 1, 1)
        self.outputExnode_pushButton = QtGui.QPushButton(self.groupBox)
        self.outputExnode_pushButton.setObjectName("outputExnode_pushButton")
        self.gridLayout_2.addWidget(self.outputExnode_pushButton, 0, 1, 1, 1)
        self.outputExelem_pushButton = QtGui.QPushButton(self.groupBox)
        self.outputExelem_pushButton.setObjectName("outputExelem_pushButton")
        self.gridLayout_2.addWidget(self.outputExelem_pushButton, 1, 1, 1, 1)
        self.save_pushButton = QtGui.QPushButton(self.groupBox)
        self.save_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.save_pushButton.setObjectName("save_pushButton")
        self.gridLayout_2.addWidget(self.save_pushButton, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.info_pushButton = QtGui.QPushButton(self.controlPanel_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pushButton.sizePolicy().hasHeightForWidth())
        self.info_pushButton.setSizePolicy(sizePolicy)
        self.info_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.info_pushButton.setFlat(True)
        self.info_pushButton.setObjectName("info_pushButton")
        self.verticalLayout.addWidget(self.info_pushButton)
        self.horizontalLayout.addWidget(self.controlPanel_widget)
        self.sceneviewer_widget = SceneviewerWidget(View)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)
        self.sceneviewer_widget.setObjectName("sceneviewer_widget")
        self.horizontalLayout.addWidget(self.sceneviewer_widget)

        self.retranslateUi(View)
        QtCore.QMetaObject.connectSlotsByName(View)

    def retranslateUi(self, View):
        View.setWindowTitle(QtGui.QApplication.translate("View", "Grow airway tree", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("View", "Airway tree input", None, QtGui.QApplication.UnicodeUTF8))
        self.airwayIpnode_pushButton.setText(QtGui.QApplication.translate("View", ".ipnode", None, QtGui.QApplication.UnicodeUTF8))
        self.airwayIpelem_pushButton.setText(QtGui.QApplication.translate("View", ".ipelem", None, QtGui.QApplication.UnicodeUTF8))
        self.loadAirway_pushButton.setText(QtGui.QApplication.translate("View", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("View", "Surface input", None, QtGui.QApplication.UnicodeUTF8))
        self.surfaceIpnode_pushButton.setText(QtGui.QApplication.translate("View", ".ipnode", None, QtGui.QApplication.UnicodeUTF8))
        self.surfaceIpelem_pushButton.setText(QtGui.QApplication.translate("View", ".ipelem", None, QtGui.QApplication.UnicodeUTF8))
        self.loadSurface_pushButton.setText(QtGui.QApplication.translate("View", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("View", "Generating", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("View", "Angle min:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("View", "Grid size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("View", "Start node:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("View", "Shortest length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("View", "Angle max:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("View", "Branch fraction:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("View", "Length limit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("View", "Rotation limit:", None, QtGui.QApplication.UnicodeUTF8))
        self.generate_pushButton.setText(QtGui.QApplication.translate("View", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_checkBox.setText(QtGui.QApplication.translate("View", "Reset airway tree", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("View", "Saving", None, QtGui.QApplication.UnicodeUTF8))
        self.outputExnode_pushButton.setText(QtGui.QApplication.translate("View", ".exnode", None, QtGui.QApplication.UnicodeUTF8))
        self.outputExelem_pushButton.setText(QtGui.QApplication.translate("View", ".exelem", None, QtGui.QApplication.UnicodeUTF8))
        self.save_pushButton.setText(QtGui.QApplication.translate("View", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.info_pushButton.setText(QtGui.QApplication.translate("View", "Info", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    View = QtGui.QWidget()
    ui = Ui_View()
    ui.setupUi(View)
    View.show()
    sys.exit(app.exec_())

