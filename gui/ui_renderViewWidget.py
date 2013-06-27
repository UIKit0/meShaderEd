# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\ui_renderViewWidget.ui'
#
# Created: Thu Jun 27 15:47:00 2013
#      by: PyQt4 UI code generator 4.10.2-snapshot-a8a14dd99d1e
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_renderViewWidget(object):
    def setupUi(self, renderViewWidget):
        renderViewWidget.setObjectName(_fromUtf8("renderViewWidget"))
        renderViewWidget.resize(623, 585)
        self.gridLayout = QtGui.QGridLayout(renderViewWidget)
        self.gridLayout.setMargin(4)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_reset = QtGui.QToolButton(renderViewWidget)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout.addWidget(self.btn_reset)
        spacerItem = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_render = QtGui.QPushButton(renderViewWidget)
        self.btn_render.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_render.setObjectName(_fromUtf8("btn_render"))
        self.horizontalLayout.addWidget(self.btn_render)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.imageArea = RenderView(renderViewWidget)
        self.imageArea.setObjectName(_fromUtf8("imageArea"))
        self.gridLayout.addWidget(self.imageArea, 1, 0, 1, 1)

        self.retranslateUi(renderViewWidget)
        QtCore.QObject.connect(self.btn_render, QtCore.SIGNAL(_fromUtf8("clicked()")), renderViewWidget.updateViewer)
        QtCore.QObject.connect(self.btn_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.imageArea.resetZoom)
        QtCore.QMetaObject.connectSlotsByName(renderViewWidget)

    def retranslateUi(self, renderViewWidget):
        renderViewWidget.setWindowTitle(_translate("renderViewWidget", "RenderView", None))
        self.btn_reset.setToolTip(_translate("renderViewWidget", "Reset zoom", None))
        self.btn_reset.setText(_translate("renderViewWidget", "1:1", None))
        self.btn_render.setText(_translate("renderViewWidget", "Update", None))

from gfx.renderView import RenderView
