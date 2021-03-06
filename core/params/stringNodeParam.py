#===============================================================================
# stringNodeParam.py
#===============================================================================
import os, sys

from PyQt4 import QtCore

from core.node import Node
from core.nodeParam import NodeParam
from global_vars import app_global_vars, DEBUG_MODE
from core.meCommon import parseGlobalVars
#
# String
#
class StringNodeParam ( NodeParam ) :
  #
  # __init__
  #
  def __init__ ( self, xml_param = None, isRibParam = False ) :
    #
    NodeParam.__init__ ( self, xml_param, isRibParam )
    self.type = 'string'
  #
  # encodedTypeStr
  #
  def encodedTypeStr ( self ) : return 's'
  #
  # copy
  #
  def copy ( self ) :
    #
    newParam = StringNodeParam ()
    self.copySetup ( newParam )
    return newParam
  #
  # valueFromStr
  #
  def valueFromStr ( self, strInput ) : return parseGlobalVars ( strInput )
  #
  # valueToStr
  #
  def valueToStr ( self, value ) :
    #
    ret_str = parseGlobalVars ( value )
    if not self.isRibParam : ret_str = str ( "\"" + value + "\"" )
    return ret_str
  #
  # getRangeValues
  #
  # if subtype == selector then return list of (label,value) pairs
  # It's supposed, that range is defined as "value1:value2:value3"
  # or "label1=value1:label2=value2:label3=value3:"
  #
  def getRangeValues ( self ) :
    #
    rangeList = []

    if self.range != '' : # and self.subtype == 'selector':
      tmp_list = str ( self.range ).split ( ':' )
      for s in tmp_list :
        pair = s.split ( '=' )
        if len ( pair ) > 1 :
          label = pair [0]
          value = pair [1]
        else :
          label = s
          value = s
        rangeList.append ( ( parseGlobalVars ( label ), parseGlobalVars ( value ) ) )
    return rangeList
