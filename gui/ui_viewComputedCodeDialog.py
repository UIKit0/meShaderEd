# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\ui_viewComputedCodeDialog.ui'
#
# Created: Sat Oct 19 18:33:54 2013
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

class Ui_ViewComputedCodeDialog(object):
    def setupUi(self, ViewComputedCodeDialog):
        ViewComputedCodeDialog.setObjectName(_fromUtf8("ViewComputedCodeDialog"))
        ViewComputedCodeDialog.resize(681, 669)
        self.gridLayout = QtGui.QGridLayout(ViewComputedCodeDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.codeEdit = NodeCodeEditor(ViewComputedCodeDialog)
        self.codeEdit.setObjectName(_fromUtf8("codeEdit"))
        self.gridLayout.addWidget(self.codeEdit, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ViewComputedCodeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ViewComputedCodeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ViewComputedCodeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ViewComputedCodeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ViewComputedCodeDialog)

    def retranslateUi(self, ViewComputedCodeDialog):
        ViewComputedCodeDialog.setWindowTitle(_translate("ViewComputedCodeDialog", "Dialog", None))

from gui.nodeEditor.nodeCodeEditor import NodeCodeEditor
