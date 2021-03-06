#===============================================================================
# volumeNodeParam.py
#===============================================================================
import os, sys

from PyQt4 import QtCore

from core.node import Node
from core.nodeParam import NodeParam
from global_vars import app_global_vars, DEBUG_MODE
from core.meCommon import parseGlobalVars
#
# Volume
#
class VolumeNodeParam ( NodeParam ) :
  #
  # __init__
  #
  def __init__ ( self, xml_param = None, isRibParam = False ) :
    #
    NodeParam.__init__ ( self, xml_param, isRibParam )
    self.type = 'volume'
  #
  # encodedTypeStr
  #
  def encodedTypeStr ( self ): return 'V'
  #
  # copy
  #
  def copy ( self ):
    #
    newParam = VolumeNodeParam()
    self.copySetup ( newParam )
    return newParam