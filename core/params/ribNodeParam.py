#===============================================================================
# ribNodeParam.py
#===============================================================================
import os, sys

from PyQt4 import QtCore

from core.node import Node
from core.nodeParam import NodeParam
from global_vars import app_global_vars, DEBUG_MODE
from core.meCommon import parseGlobalVars
#
# RIB
#
class RibNodeParam ( NodeParam ) :
  #
  # __init__
  #
  def __init__ ( self, xml_param = None, isRibParam = False ) :
    #
    NodeParam.__init__ ( self, xml_param, isRibParam )
    self.type = 'rib'
  #
  # encodedTypeStr
  #
  def encodedTypeStr ( self ) : return 'R'
  #
  # copy
  #
  def copy ( self ) :
    #
    newParam = RibNodeParam ()
    self.copySetup ( newParam )
    return newParam