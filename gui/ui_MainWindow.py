# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\ui_MainWindow.ui'
#
# Created: Sat Oct 19 22:54:00 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(963, 894)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setAcceptDrops(True)
        self.tabs.setTabPosition(QtGui.QTabWidget.North)
        self.tabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabs.setElideMode(QtCore.Qt.ElideNone)
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(False)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.workArea = WorkArea()
        self.workArea.setAcceptDrops(True)
        self.workArea.setObjectName(_fromUtf8("workArea"))
        self.tabs.addTab(self.workArea, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuRecent_Projects = QtGui.QMenu(self.menuFile)
        self.menuRecent_Projects.setObjectName(_fromUtf8("menuRecent_Projects"))
        self.menuRecent_Networks = QtGui.QMenu(self.menuFile)
        self.menuRecent_Networks.setObjectName(_fromUtf8("menuRecent_Networks"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.menuEdit.setFont(font)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuCommand = QtGui.QMenu(self.menubar)
        self.menuCommand.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.menuCommand.setFont(font)
        self.menuCommand.setObjectName(_fromUtf8("menuCommand"))
        self.menuCreateNode = QtGui.QMenu(self.menuCommand)
        self.menuCreateNode.setEnabled(True)
        self.menuCreateNode.setObjectName(_fromUtf8("menuCreateNode"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.menuWindow.setFont(font)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.menuHelp.setFont(font)
        self.menuHelp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockNodes = QtGui.QDockWidget(MainWindow)
        self.dockNodes.setMinimumSize(QtCore.QSize(150, 42))
        self.dockNodes.setFloating(False)
        self.dockNodes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockNodes.setObjectName(_fromUtf8("dockNodes"))
        self.nodeList_ctl = NodeLibraryView()
        self.nodeList_ctl.setObjectName(_fromUtf8("nodeList_ctl"))
        self.dockNodes.setWidget(self.nodeList_ctl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockNodes)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setBaseSize(QtCore.QSize(0, 0))
        self.toolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.TopToolBarArea)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockPreview = QtGui.QDockWidget(MainWindow)
        self.dockPreview.setBaseSize(QtCore.QSize(300, 0))
        self.dockPreview.setFloating(False)
        self.dockPreview.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockPreview.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockPreview.setObjectName(_fromUtf8("dockPreview"))
        self.imageView_ctl = ImageViewWidget()
        self.imageView_ctl.setObjectName(_fromUtf8("imageView_ctl"))
        self.dockPreview.setWidget(self.imageView_ctl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockPreview)
        self.dockParam = QtGui.QDockWidget(MainWindow)
        self.dockParam.setBaseSize(QtCore.QSize(300, 0))
        self.dockParam.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockParam.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockParam.setObjectName(_fromUtf8("dockParam"))
        self.nodeParam_ctl = NodeParamView()
        self.nodeParam_ctl.setObjectName(_fromUtf8("nodeParam_ctl"))
        self.dockParam.setWidget(self.nodeParam_ctl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockParam)
        self.dockGeom = QtGui.QDockWidget(MainWindow)
        self.dockGeom.setObjectName(_fromUtf8("dockGeom"))
        self.geomView_ctl = GeomViewWidget()
        self.geomView_ctl.setObjectName(_fromUtf8("geomView_ctl"))
        self.dockGeom.setWidget(self.geomView_ctl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockGeom)
        self.dockProject = QtGui.QDockWidget(MainWindow)
        self.dockProject.setObjectName(_fromUtf8("dockProject"))
        self.project_ctl = NodeLibraryView()
        self.project_ctl.setObjectName(_fromUtf8("project_ctl"))
        self.dockProject.setWidget(self.project_ctl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockProject)
        self.dockSwatch = QtGui.QDockWidget(MainWindow)
        self.dockSwatch.setObjectName(_fromUtf8("dockSwatch"))
        self.swatchParam_ctl = NodeSwatchParam()
        self.swatchParam_ctl.setObjectName(_fromUtf8("swatchParam_ctl"))
        self.dockSwatch.setWidget(self.swatchParam_ctl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockSwatch)
        self.actionRendererOptions = QtGui.QAction(MainWindow)
        self.actionRendererOptions.setObjectName(_fromUtf8("actionRendererOptions"))
        self.actionPreviewOptions = QtGui.QAction(MainWindow)
        self.actionPreviewOptions.setObjectName(_fromUtf8("actionPreviewOptions"))
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/file_icons/resources/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setToolTip(_fromUtf8("New Project"))
        self.actionNew.setStatusTip(_fromUtf8("Create a new project"))
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/file_icons/resources/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/file_icons/resources/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionSaveSelected = QtGui.QAction(MainWindow)
        self.actionSaveSelected.setEnabled(False)
        self.actionSaveSelected.setObjectName(_fromUtf8("actionSaveSelected"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icons/resources/copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon3)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icons/resources/editcut1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icons/resources/paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon5)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icons/resources/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon6)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icons/resources/redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon7)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionEditNode = QtGui.QAction(MainWindow)
        self.actionEditNode.setEnabled(True)
        self.actionEditNode.setObjectName(_fromUtf8("actionEditNode"))
        self.actionRenderPreview = QtGui.QAction(MainWindow)
        self.actionRenderPreview.setEnabled(True)
        self.actionRenderPreview.setObjectName(_fromUtf8("actionRenderPreview"))
        self.actionShowNodes = QtGui.QAction(MainWindow)
        self.actionShowNodes.setCheckable(True)
        self.actionShowNodes.setChecked(True)
        self.actionShowNodes.setObjectName(_fromUtf8("actionShowNodes"))
        self.actionShowParameters = QtGui.QAction(MainWindow)
        self.actionShowParameters.setCheckable(True)
        self.actionShowParameters.setChecked(True)
        self.actionShowParameters.setObjectName(_fromUtf8("actionShowParameters"))
        self.actionShowGrid = QtGui.QAction(MainWindow)
        self.actionShowGrid.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/grid_off.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/grid_on.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionShowGrid.setIcon(icon8)
        self.actionShowGrid.setObjectName(_fromUtf8("actionShowGrid"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionShowToolbar = QtGui.QAction(MainWindow)
        self.actionShowToolbar.setCheckable(True)
        self.actionShowToolbar.setChecked(True)
        self.actionShowToolbar.setObjectName(_fromUtf8("actionShowToolbar"))
        self.actionShowPreview = QtGui.QAction(MainWindow)
        self.actionShowPreview.setCheckable(True)
        self.actionShowPreview.setChecked(True)
        self.actionShowPreview.setObjectName(_fromUtf8("actionShowPreview"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icons/resources/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon9)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionShowGeometry = QtGui.QAction(MainWindow)
        self.actionShowGeometry.setCheckable(True)
        self.actionShowGeometry.setChecked(True)
        self.actionShowGeometry.setObjectName(_fromUtf8("actionShowGeometry"))
        self.actionProjectSetup = QtGui.QAction(MainWindow)
        self.actionProjectSetup.setObjectName(_fromUtf8("actionProjectSetup"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionReverseFlow = QtGui.QAction(MainWindow)
        self.actionReverseFlow.setCheckable(True)
        self.actionReverseFlow.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/ledoff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/ledon.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionReverseFlow.setIcon(icon10)
        self.actionReverseFlow.setVisible(False)
        self.actionReverseFlow.setObjectName(_fromUtf8("actionReverseFlow"))
        self.actionStraightLinks = QtGui.QAction(MainWindow)
        self.actionStraightLinks.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/straight_off.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/straight_on.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionStraightLinks.setIcon(icon11)
        self.actionStraightLinks.setObjectName(_fromUtf8("actionStraightLinks"))
        self.actionSnapGrid = QtGui.QAction(MainWindow)
        self.actionSnapGrid.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/snap_off.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/snap_on.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSnapGrid.setIcon(icon12)
        self.actionSnapGrid.setObjectName(_fromUtf8("actionSnapGrid"))
        self.actionFitAll = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/fit_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFitAll.setIcon(icon13)
        self.actionFitAll.setVisible(True)
        self.actionFitAll.setObjectName(_fromUtf8("actionFitAll"))
        self.actionFitSelected = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/fit_selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFitSelected.setIcon(icon14)
        self.actionFitSelected.setVisible(True)
        self.actionFitSelected.setObjectName(_fromUtf8("actionFitSelected"))
        self.actionZoomReset = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/zoom_reset.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomReset.setIcon(icon15)
        self.actionZoomReset.setObjectName(_fromUtf8("actionZoomReset"))
        self.actionNewParamView = QtGui.QAction(MainWindow)
        self.actionNewParamView.setObjectName(_fromUtf8("actionNewParamView"))
        self.actionNewImageView = QtGui.QAction(MainWindow)
        self.actionNewImageView.setObjectName(_fromUtf8("actionNewImageView"))
        self.actionDuplicate = QtGui.QAction(MainWindow)
        self.actionDuplicate.setObjectName(_fromUtf8("actionDuplicate"))
        self.actionDuplicateWithLinks = QtGui.QAction(MainWindow)
        self.actionDuplicateWithLinks.setObjectName(_fromUtf8("actionDuplicateWithLinks"))
        self.actionSelectAll = QtGui.QAction(MainWindow)
        self.actionSelectAll.setObjectName(_fromUtf8("actionSelectAll"))
        self.actionSelectBelow = QtGui.QAction(MainWindow)
        self.actionSelectBelow.setObjectName(_fromUtf8("actionSelectBelow"))
        self.actionSelectAbove = QtGui.QAction(MainWindow)
        self.actionSelectAbove.setObjectName(_fromUtf8("actionSelectAbove"))
        self.actionExportShader = QtGui.QAction(MainWindow)
        self.actionExportShader.setObjectName(_fromUtf8("actionExportShader"))
        self.actionShowSwatch = QtGui.QAction(MainWindow)
        self.actionShowSwatch.setObjectName(_fromUtf8("actionShowSwatch"))
        self.actionHideSwatch = QtGui.QAction(MainWindow)
        self.actionHideSwatch.setObjectName(_fromUtf8("actionHideSwatch"))
        self.actionHelpMode = QtGui.QAction(MainWindow)
        self.actionHelpMode.setCheckable(True)
        self.actionHelpMode.setObjectName(_fromUtf8("actionHelpMode"))
        self.actionViewComputedCode = QtGui.QAction(MainWindow)
        self.actionViewComputedCode.setObjectName(_fromUtf8("actionViewComputedCode"))
        self.menuRecent_Projects.addSeparator()
        self.menuRecent_Networks.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionSaveSelected)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionProjectSetup)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuRecent_Projects.menuAction())
        self.menuFile.addAction(self.menuRecent_Networks.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addAction(self.actionSelectBelow)
        self.menuEdit.addAction(self.actionSelectAbove)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDuplicate)
        self.menuEdit.addAction(self.actionDuplicateWithLinks)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionRendererOptions)
        self.menuEdit.addAction(self.actionSettings)
        self.menuCreateNode.addSeparator()
        self.menuCommand.addAction(self.menuCreateNode.menuAction())
        self.menuCommand.addAction(self.actionEditNode)
        self.menuCommand.addAction(self.actionViewComputedCode)
        self.menuCommand.addAction(self.actionExportShader)
        self.menuCommand.addSeparator()
        self.menuCommand.addAction(self.actionRenderPreview)
        self.menuCommand.addAction(self.actionShowSwatch)
        self.menuCommand.addAction(self.actionHideSwatch)
        self.menuWindow.addAction(self.actionShowToolbar)
        self.menuWindow.addAction(self.actionShowNodes)
        self.menuWindow.addAction(self.actionShowParameters)
        self.menuWindow.addAction(self.actionShowPreview)
        self.menuWindow.addAction(self.actionShowGeometry)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionNewParamView)
        self.menuWindow.addAction(self.actionNewImageView)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuView.addAction(self.actionShowGrid)
        self.menuView.addAction(self.actionSnapGrid)
        self.menuView.addAction(self.actionReverseFlow)
        self.menuView.addAction(self.actionStraightLinks)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFitAll)
        self.menuView.addAction(self.actionFitSelected)
        self.menuView.addAction(self.actionZoomReset)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuCommand.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFitAll)
        self.toolBar.addAction(self.actionFitSelected)
        self.toolBar.addAction(self.actionZoomReset)
        self.toolBar.addAction(self.actionShowGrid)
        self.toolBar.addAction(self.actionSnapGrid)
        self.toolBar.addAction(self.actionStraightLinks)
        self.toolBar.addAction(self.actionReverseFlow)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionProjectSetup, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onProjectSetup)
        QtCore.QObject.connect(self.actionShowGrid, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.onShowGrid)
        QtCore.QObject.connect(self.actionRendererOptions, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onRenderSettings)
        QtCore.QObject.connect(self.actionSnapGrid, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.onSnapGrid)
        QtCore.QObject.connect(self.actionReverseFlow, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.onReverseFlow)
        QtCore.QObject.connect(self.actionStraightLinks, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.onStraightLinks)
        QtCore.QObject.connect(self.actionDelete, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onDelete)
        QtCore.QObject.connect(self.actionFitAll, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onFitAll)
        QtCore.QObject.connect(self.actionFitSelected, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onFitSelected)
        QtCore.QObject.connect(self.actionZoomReset, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onZoomReset)
        QtCore.QObject.connect(self.actionNewParamView, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onNewParamView)
        QtCore.QObject.connect(self.actionNew, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onNew)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onSave)
        QtCore.QObject.connect(self.actionSaveAs, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onSaveAs)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onOpen)
        QtCore.QObject.connect(self.actionSettings, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onSettingsSetup)
        QtCore.QObject.connect(self.actionImport, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onImport)
        QtCore.QObject.connect(self.actionDuplicate, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onDuplicate)
        QtCore.QObject.connect(self.actionDuplicateWithLinks, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onDuplicateWithLinks)
        QtCore.QObject.connect(self.actionCopy, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onCopy)
        QtCore.QObject.connect(self.actionCut, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onCut)
        QtCore.QObject.connect(self.actionSelectAll, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onSelectAll)
        QtCore.QObject.connect(self.actionPaste, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onPaste)
        QtCore.QObject.connect(self.actionSelectAbove, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onSelectAbove)
        QtCore.QObject.connect(self.actionSelectBelow, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onSelectBelow)
        QtCore.QObject.connect(self.actionEditNode, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onEditNode)
        QtCore.QObject.connect(self.actionExportShader, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onExportShader)
        QtCore.QObject.connect(self.actionRenderPreview, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onRenderPreview)
        QtCore.QObject.connect(self.actionShowSwatch, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onShowSwatch)
        QtCore.QObject.connect(self.actionHideSwatch, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onHideSwatch)
        QtCore.QObject.connect(self.actionSaveSelected, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onSaveSelected)
        QtCore.QObject.connect(self.actionViewComputedCode, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onViewComputedCode)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "meShaderEd", None))
        self.tabs.setTabText(self.tabs.indexOf(self.workArea), _translate("MainWindow", "none", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuRecent_Projects.setTitle(_translate("MainWindow", "Recent Projects", None))
        self.menuRecent_Networks.setTitle(_translate("MainWindow", "Recent Networks", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuCommand.setTitle(_translate("MainWindow", "Command", None))
        self.menuCreateNode.setTitle(_translate("MainWindow", "Create Node", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Window", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.dockNodes.setWindowTitle(_translate("MainWindow", "Library", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar.setToolTip(_translate("MainWindow", "Enter to Help Mode", None))
        self.dockPreview.setWindowTitle(_translate("MainWindow", "Image View", None))
        self.dockParam.setWindowTitle(_translate("MainWindow", "Node Parameters", None))
        self.dockGeom.setWindowTitle(_translate("MainWindow", "Geometry View", None))
        self.dockProject.setWindowTitle(_translate("MainWindow", "Project", None))
        self.dockSwatch.setWindowTitle(_translate("MainWindow", "Node Preview", None))
        self.actionRendererOptions.setText(_translate("MainWindow", "Renderer ...", None))
        self.actionRendererOptions.setToolTip(_translate("MainWindow", "Renderer Options", None))
        self.actionPreviewOptions.setText(_translate("MainWindow", "Preview ...", None))
        self.actionPreviewOptions.setToolTip(_translate("MainWindow", "Preview Options", None))
        self.actionNew.setText(_translate("MainWindow", "&New", None))
        self.actionNew.setWhatsThis(_translate("MainWindow", "Click this option to create a new project", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionOpen.setText(_translate("MainWindow", "&Open", None))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open existing project", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("MainWindow", "&Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Quit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As ...", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))
        self.actionSaveSelected.setText(_translate("MainWindow", "Save Selected As ...", None))
        self.actionSaveSelected.setToolTip(_translate("MainWindow", "Save selected nodes", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionEditNode.setText(_translate("MainWindow", "Edit Node ...", None))
        self.actionEditNode.setShortcut(_translate("MainWindow", "Ctrl+E", None))
        self.actionRenderPreview.setText(_translate("MainWindow", "Render Preview", None))
        self.actionRenderPreview.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionShowNodes.setText(_translate("MainWindow", "Nodes Library", None))
        self.actionShowNodes.setToolTip(_translate("MainWindow", "Show Nodes", None))
        self.actionShowParameters.setText(_translate("MainWindow", "Node Parameters", None))
        self.actionShowParameters.setToolTip(_translate("MainWindow", "Show Parameters", None))
        self.actionShowGrid.setText(_translate("MainWindow", "Show grid", None))
        self.actionShowGrid.setToolTip(_translate("MainWindow", "Show grid", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionShowToolbar.setText(_translate("MainWindow", "Toolbar", None))
        self.actionShowPreview.setText(_translate("MainWindow", "Image View", None))
        self.actionShowPreview.setToolTip(_translate("MainWindow", "Show Preview", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del", None))
        self.actionShowGeometry.setText(_translate("MainWindow", "Geometry View", None))
        self.actionProjectSetup.setText(_translate("MainWindow", "Project Setup ...", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings ...", None))
        self.actionReverseFlow.setText(_translate("MainWindow", "Reverse Flow", None))
        self.actionStraightLinks.setText(_translate("MainWindow", "Staright Links", None))
        self.actionStraightLinks.setToolTip(_translate("MainWindow", "Draw Straight Links", None))
        self.actionSnapGrid.setText(_translate("MainWindow", "Snap To Grid", None))
        self.actionSnapGrid.setToolTip(_translate("MainWindow", "Snap to grid", None))
        self.actionFitAll.setText(_translate("MainWindow", "Fit All", None))
        self.actionFitAll.setShortcut(_translate("MainWindow", "F", None))
        self.actionFitSelected.setText(_translate("MainWindow", "Fit Selected", None))
        self.actionFitSelected.setShortcut(_translate("MainWindow", "Shift+F", None))
        self.actionZoomReset.setText(_translate("MainWindow", "Reset Zoom", None))
        self.actionZoomReset.setToolTip(_translate("MainWindow", "Reset Zoom", None))
        self.actionNewParamView.setText(_translate("MainWindow", "New Parameter View", None))
        self.actionNewImageView.setText(_translate("MainWindow", "New Image View", None))
        self.actionDuplicate.setText(_translate("MainWindow", "Duplicate", None))
        self.actionDuplicate.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.actionDuplicateWithLinks.setText(_translate("MainWindow", "Duplicate with links", None))
        self.actionDuplicateWithLinks.setShortcut(_translate("MainWindow", "Ctrl+Shift+D", None))
        self.actionSelectAll.setText(_translate("MainWindow", "Select All", None))
        self.actionSelectAll.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionSelectBelow.setText(_translate("MainWindow", "Select below", None))
        self.actionSelectBelow.setToolTip(_translate("MainWindow", "Select hierarchy below", None))
        self.actionSelectBelow.setShortcut(_translate("MainWindow", "Ctrl+Down", None))
        self.actionSelectAbove.setText(_translate("MainWindow", "Select above", None))
        self.actionSelectAbove.setToolTip(_translate("MainWindow", "Select hierarchy above", None))
        self.actionSelectAbove.setShortcut(_translate("MainWindow", "Ctrl+Up", None))
        self.actionExportShader.setText(_translate("MainWindow", "Export As Shader ...", None))
        self.actionExportShader.setShortcut(_translate("MainWindow", "Ctrl+T", None))
        self.actionShowSwatch.setText(_translate("MainWindow", "Show Swatch", None))
        self.actionShowSwatch.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.actionHideSwatch.setText(_translate("MainWindow", "Hide Swatch", None))
        self.actionHideSwatch.setShortcut(_translate("MainWindow", "Ctrl+Shift+H", None))
        self.actionHelpMode.setText(_translate("MainWindow", "Help", None))
        self.actionHelpMode.setShortcut(_translate("MainWindow", "Shift+F1", None))
        self.actionViewComputedCode.setText(_translate("MainWindow", "View Computed Code ...", None))
        self.actionViewComputedCode.setShortcut(_translate("MainWindow", "Ctrl+Alt+V", None))

from gfx.WorkArea import WorkArea
from nodeSwatchParam import NodeSwatchParam
from nodeLibraryView import NodeLibraryView
from nodeParamView import NodeParamView
from geomViewWidget import GeomViewWidget
from imageViewWidget import ImageViewWidget
import resources_rc
