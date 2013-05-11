#===============================================================================
# objReader.py
#===============================================================================
import os, sys
from PyQt4 import QtCore

from global_vars import app_global_vars, DEBUG_MODE

#
# ObjReader
#
class ObjReader () :
  #
  # __init__
  #
  def __init__ ( self, objFileName = None ) :
    #
    self.objFileName = objFileName
    
    if self.objFileName is not None :
      self.openObjFile ()
  #
  # openObjFile
  #
  def openObjFile ( self ) :
    #
    if DEBUG_MODE : print '>> ObjReader.openObjFile ( %s )' % self.objFileName
  #
  # readObjFile
  #
  def readObjFile ( self ) :
    #
    if DEBUG_MODE : print '>> ObjReader.readObjFile ( %s )' % self.objFileName