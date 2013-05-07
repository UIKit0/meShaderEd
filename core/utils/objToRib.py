#===============================================================================
# objToRib.py
#===============================================================================
import os, sys
from PyQt4 import QtCore

from global_vars import app_global_vars, DEBUG_MODE

#
# SlInfo
#
class ObjToRib () :
  #
  # __init__
  #
  def __init__ ( self, objFileName = None ) :
    #
    self.rib = None
    self.objFileName = objFileName
    
    if self.objFileName is not None :
      self.readObj ()
  #
  # readObj
  #
  def readObj ( self ) :
    #
    if DEBUG_MODE : print '>> ObjToRib.readObjo ( %s )' % self.objFileName
