# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\ui_imageViewWidget.ui'
#
# Created: Tue Oct 30 13:51:50 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_imageViewWidget(object):
    def setupUi(self, imageViewWidget):
        imageViewWidget.setObjectName(_fromUtf8("imageViewWidget"))
        imageViewWidget.resize(479, 520)
        self.gridLayout = QtGui.QGridLayout(imageViewWidget)
        self.gridLayout.setMargin(4)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(imageViewWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.selector = QtGui.QComboBox(imageViewWidget)
        self.selector.setMinimumSize(QtCore.QSize(120, 20))
        self.selector.setMaximumSize(QtCore.QSize(16777215, 20))
        self.selector.setFrame(True)
        self.selector.setObjectName(_fromUtf8("selector"))
        self.horizontalLayout.addWidget(self.selector)
        self.btn_reset = QtGui.QToolButton(imageViewWidget)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout.addWidget(self.btn_reset)
        spacerItem = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.chk_auto = QtGui.QCheckBox(imageViewWidget)
        self.chk_auto.setObjectName(_fromUtf8("chk_auto"))
        self.horizontalLayout.addWidget(self.chk_auto)
        self.btn_render = QtGui.QPushButton(imageViewWidget)
        self.btn_render.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_render.setObjectName(_fromUtf8("btn_render"))
        self.horizontalLayout.addWidget(self.btn_render)
        self.horizontalLayout.setStretch(3, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.imageArea = ImageView(imageViewWidget)
        self.imageArea.setObjectName(_fromUtf8("imageArea"))
        self.gridLayout.addWidget(self.imageArea, 1, 0, 1, 1)

        self.retranslateUi(imageViewWidget)
        QtCore.QObject.connect(self.btn_render, QtCore.SIGNAL(_fromUtf8("clicked()")), imageViewWidget.updateViewer)
        QtCore.QObject.connect(self.btn_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.imageArea.resetZoom)
        QtCore.QMetaObject.connectSlotsByName(imageViewWidget)

    def retranslateUi(self, imageViewWidget):
        imageViewWidget.setWindowTitle(QtGui.QApplication.translate("imageViewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("imageViewWidget", "Node", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset.setToolTip(QtGui.QApplication.translate("imageViewWidget", "Reset zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset.setText(QtGui.QApplication.translate("imageViewWidget", "1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_auto.setText(QtGui.QApplication.translate("imageViewWidget", "auto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_render.setText(QtGui.QApplication.translate("imageViewWidget", "Update", None, QtGui.QApplication.UnicodeUTF8))

from gfx.imageView import ImageView
