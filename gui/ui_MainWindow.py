# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\ui_MainWindow.ui'
#
# Created: Thu Aug 02 01:02:59 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1113, 650)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 19))
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
        self.menuEdit = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.menuEdit.setFont(font)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuCommand = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.menuCommand.setFont(font)
        self.menuCommand.setObjectName(_fromUtf8("menuCommand"))
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
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setEnabled(False)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
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
        self.actionBuild = QtGui.QAction(MainWindow)
        self.actionBuild.setEnabled(False)
        self.actionBuild.setObjectName(_fromUtf8("actionBuild"))
        self.actionRender = QtGui.QAction(MainWindow)
        self.actionRender.setEnabled(False)
        self.actionRender.setObjectName(_fromUtf8("actionRender"))
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/ledoff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/show_icons/resources/ledon.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionReverseFlow.setIcon(icon10)
        self.actionReverseFlow.setObjectName(_fromUtf8("actionReverseFlow"))
        self.actionStraightLinks = QtGui.QAction(MainWindow)
        self.actionStraightLinks.setCheckable(True)
        self.actionStraightLinks.setIcon(icon10)
        self.actionStraightLinks.setObjectName(_fromUtf8("actionStraightLinks"))
        self.actionSnapGrid = QtGui.QAction(MainWindow)
        self.actionSnapGrid.setCheckable(True)
        self.actionSnapGrid.setIcon(icon10)
        self.actionSnapGrid.setObjectName(_fromUtf8("actionSnapGrid"))
        self.actionFitAll = QtGui.QAction(MainWindow)
        self.actionFitAll.setObjectName(_fromUtf8("actionFitAll"))
        self.actionFitSelected = QtGui.QAction(MainWindow)
        self.actionFitSelected.setObjectName(_fromUtf8("actionFitSelected"))
        self.actionZoomReset = QtGui.QAction(MainWindow)
        self.actionZoomReset.setObjectName(_fromUtf8("actionZoomReset"))
        self.actionNewParamView = QtGui.QAction(MainWindow)
        self.actionNewParamView.setObjectName(_fromUtf8("actionNewParamView"))
        self.actionNewImageView = QtGui.QAction(MainWindow)
        self.actionNewImageView.setObjectName(_fromUtf8("actionNewImageView"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionProjectSetup)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionRendererOptions)
        self.menuEdit.addAction(self.actionSettings)
        self.menuCommand.addAction(self.actionBuild)
        self.menuCommand.addAction(self.actionRender)
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
        self.toolBar.addAction(self.actionReverseFlow)
        self.toolBar.addAction(self.actionStraightLinks)

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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "meShaderEd", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.workArea), QtGui.QApplication.translate("MainWindow", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCommand.setTitle(QtGui.QApplication.translate("MainWindow", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.dockNodes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Library", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockPreview.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Image View", None, QtGui.QApplication.UnicodeUTF8))
        self.dockParam.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Node Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.dockGeom.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Geometry View", None, QtGui.QApplication.UnicodeUTF8))
        self.dockProject.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRendererOptions.setText(QtGui.QApplication.translate("MainWindow", "Renderer ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRendererOptions.setToolTip(QtGui.QApplication.translate("MainWindow", "Renderer Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreviewOptions.setText(QtGui.QApplication.translate("MainWindow", "Preview ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreviewOptions.setToolTip(QtGui.QApplication.translate("MainWindow", "Preview Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open existing project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setText(QtGui.QApplication.translate("MainWindow", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRender.setText(QtGui.QApplication.translate("MainWindow", "Render", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowNodes.setText(QtGui.QApplication.translate("MainWindow", "Nodes Library", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowNodes.setToolTip(QtGui.QApplication.translate("MainWindow", "Show Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowParameters.setText(QtGui.QApplication.translate("MainWindow", "Node Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowParameters.setToolTip(QtGui.QApplication.translate("MainWindow", "Show Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowGrid.setText(QtGui.QApplication.translate("MainWindow", "Show grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowGrid.setToolTip(QtGui.QApplication.translate("MainWindow", "Show grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowToolbar.setText(QtGui.QApplication.translate("MainWindow", "Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowPreview.setText(QtGui.QApplication.translate("MainWindow", "Image View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowPreview.setToolTip(QtGui.QApplication.translate("MainWindow", "Show Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowGeometry.setText(QtGui.QApplication.translate("MainWindow", "Geometry View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProjectSetup.setText(QtGui.QApplication.translate("MainWindow", "Project Setup ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReverseFlow.setText(QtGui.QApplication.translate("MainWindow", "Reverse Flow", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStraightLinks.setText(QtGui.QApplication.translate("MainWindow", "Staright Links", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStraightLinks.setToolTip(QtGui.QApplication.translate("MainWindow", "Draw Straight Links", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnapGrid.setText(QtGui.QApplication.translate("MainWindow", "Snap To Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnapGrid.setToolTip(QtGui.QApplication.translate("MainWindow", "Snap to grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFitAll.setText(QtGui.QApplication.translate("MainWindow", "Fit All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFitSelected.setText(QtGui.QApplication.translate("MainWindow", "Fit Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomReset.setText(QtGui.QApplication.translate("MainWindow", "1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewParamView.setText(QtGui.QApplication.translate("MainWindow", "New Parameter View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewImageView.setText(QtGui.QApplication.translate("MainWindow", "New Image View", None, QtGui.QApplication.UnicodeUTF8))

from nodeLibraryView import NodeLibraryView
from geomViewWidget import GeomViewWidget
from imageViewWidget import ImageViewWidget
from nodeParamView import NodeParamView
from gfx.WorkArea import WorkArea
import resources_rc
