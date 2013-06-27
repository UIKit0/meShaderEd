"""
 renderViewWidget.py

"""
import os, sys
from PyQt4 import QtCore, QtGui

from ui_renderViewWidget import Ui_renderViewWidget
import gui.ui_settings as UI
#
# RenderViewWidget
#
class RenderViewWidget ( QtGui.QWidget ) :
  #
  #  __init__
  #
  def __init__ ( self ) :
    #
    QtGui.QWidget.__init__ ( self )

    # This is always the same
    self.ui = Ui_renderViewWidget ()
    self.ui.setupUi ( self )

    self.imageNodes = []

    QtCore.QObject.connect ( self.ui.imageArea, QtCore.SIGNAL ( 'mouseDoubleClickEvent' ), self.updateViewer )
  #
  # updateViewer
  #
  def updateViewer ( self ) :
    #
    print ">> RenderViewWidget.updateViewer"
    
  
 

