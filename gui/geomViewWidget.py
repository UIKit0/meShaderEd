#===============================================================================
# geomViewWidget.py
#
#
#
#===============================================================================

import os, sys
from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import QDir, QString, QModelIndex
from PyQt4.QtGui  import QFileSystemModel
from PyQt4.QtGui  import QFileIconProvider

from ui_geomViewWidget import Ui_geomViewWidget

from core.node import Node
from core.nodeLibrary import NodeLibrary
#
# GeomViewWidget
#
class GeomViewWidget ( QtGui.QWidget ):
  #
  # __init__
  #
  def __init__ ( self ):
    QtGui.QWidget.__init__ ( self )

    # This is always the same
    self.ui=Ui_geomViewWidget ( )
    self.ui.setupUi ( self )

    self.imageNodes = []

    #self.ui.treeView.setDragEnabled ( True )
    #self.ui.treeView.setRootIsDecorated( True )

    QtCore.QObject.connect( self.ui.geomView, QtCore.SIGNAL( 'mouseDoubleClickEvent' ), self.updateViewer )
    QtCore.QObject.connect( self.ui.selector, QtCore.SIGNAL( 'currentIndexChanged(int)' ), self.onViewerChanged )
    #QtCore.QObject.connect( self.ui, QtCore.SIGNAL( 'paramChanged()' ), self.onParamChanged )

    #self.updateGui()
  #
  #
  #self.emit( QtCore.SIGNAL( 'onGfxNodeParamChanged(QObject,QObject)' ), self, param.name )
  #
  #
  def currentImageNode ( self ) :
    #
    gfxNode = None
    idx = self.ui.selector.currentIndex ()
    if len ( self.imageNodes ) > 0 :
      gfxNode = self.imageNodes [ idx ]
    return gfxNode
  #
  # addViewer
  #
  def addViewer ( self, gfxNode ) :
    #
    self.imageNodes.append ( gfxNode )
    self.ui.selector.addItem ( gfxNode.node.label )
  #
  # removeViewer
  #
  def removeViewer ( self, gfxNode ) :
    #
    i = 0
    for i in range ( len ( self.imageNodes ) ) :
      if gfxNode ==  self.imageNodes [ i ] :
        self.imageNodes.pop ( i )
        self.ui.selector.removeItem ( i )
        #QtCore.QObject.disconnect ( gfxNode.node, QtCore.SIGNAL( 'onNodeParamChanged(QObject,QObject)' ), self.onNodeParamChanged )
        break
      i += 1
  #
  # onViewerChanged
  #
  def onViewerChanged ( self, idx ) :
    #
    if len ( self.imageNodes ) > 0 :
      print ">> ImageViewWidget: onViewerChanged to %s" % self.imageNodes [ idx ].node.label
      #QtCore.QObject.connect( self.imageNodes[ idx ].node, QtCore.SIGNAL( 'onNodeParamChanged(QObject,QObject)' ), self.onNodeParamChanged )
      self.updateViewer()
  #
  # updateViewer
  #
  def updateViewer ( self ) :
    #
    print ">> ImageViewWidget: updateViewer"
    idx = self.ui.selector.currentIndex ()
    if len ( self.imageNodes ) > 0 :
      gfxNode = self.imageNodes [ idx ]
      print ">> ImageViewWidget: getImageName on %s" % gfxNode.node.label

      imageName = gfxNode.node.computeNode ()

      print ">> ImageViewWidget: imageName = %s" % imageName

      self.ui.imageArea.setImage ( imageName )

      #imageParam = None
      #for param in gfxNode.node.inputParams :
      #  if param.name == 'image' :
      #    imageParam = param
      #    break
      #if imageParam is not None :
      #  print ">> ImageViewWidget: image = %s" % imageParam.value
      #  self.ui.imageArea.setImage ( imageParam.value )
  #
  # onNodeParamChanged
  #
  def onNodeParamChanged ( self, node, param ) :
    #
    print ">> ImageViewWidget: onNodeParamChanged %s %s" % ( node.label, param.name )
    if node == self.currentImageNode ().node :
      self.updateViewer ()
  #
  # onNodeLabelChanged
  #
  def onNodeLabelChanged ( self, gfxNode, newLabel ) :
    #
    print ">> ImageViewWidget: onNodeLabelChanged %s %s" % ( gfxNode.node.label, newLabel )
    i = 0
    for i in range ( len ( self.imageNodes ) ) :
      if gfxNode ==  self.imageNodes [ i ] :
        self.ui.selector.setItemText ( i, newLabel )
        break
      i += 1
