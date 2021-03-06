#===============================================================================
# SettingsSetup.py
#
# ver. 1.0.0
# Author: Yuri Meshalkin (aka mesh) (yuri.meshalkin@gmail.com)
# 
# Dialog for managing meShaderEd settings
# 
#===============================================================================

import os, sys
from PyQt4 import QtCore, QtGui

from core.meCommon import *
from global_vars import app_global_vars

from ui_settingsSetup import Ui_SettingsSetup
#
#
#
class SettingsSetup ( QtGui.QDialog ):
  #
  #
  def __init__ ( self, app_settings ):
    QtGui.QDialog.__init__(self)

    self.app_settings = app_settings
          
    #self.debugPrint()
    self.buildGui()
  #
  #
  def buildGui ( self ):
    # build the gui created with QtDesigner
    self.ui = Ui_SettingsSetup ( )
    self.ui.setupUi ( self )
    
    ##font = QtGui.QFont()
    ##if( sys.platform == 'win32' ) :
      # Runing on windows, override font sizes from Designer to default 
    ##  font.setPointSize(8)
    ##else :
    ##  font.setPointSize(10)
    
    self.ui.lineEdit_temp.setText( self.app_settings.value('temp').toString() )
    self.ui.lineEdit_inc.setText( self.app_settings.value('include').toString() )
    self.ui.lineEdit_lib.setText( self.app_settings.value('lib').toString() )
    self.ui.lineEdit_nodes.setText( self.app_settings.value('nodes').toString() )
    self.ui.lineEdit_shaders.setText( self.app_settings.value('shaders').toString() )
    self.ui.lineEdit_textures.setText( self.app_settings.value('texture').toString() )
    self.ui.lineEdit_archives.setText( self.app_settings.value('archive').toString() )
  #
  #  
  def onBrowseTempDir ( self ):
    curDir = self.ui.lineEdit_temp.text()
    newDir = QtGui.QFileDialog.getExistingDirectory( self, "Select Temp Directory", curDir )
    if newDir != '' : 
      self.ui.lineEdit_temp.setText( normPath( newDir ) )
  #
  #  
  def onBrowseLibraryDir ( self ):
    curDir = self.ui.lineEdit_lib.text()
    newDir = QtGui.QFileDialog.getExistingDirectory( self, "Select Library Directory", curDir )
    if newDir != '' : 
      self.ui.lineEdit_lib.setText( normPath( newDir ) )
  #
  #  
  def onBrowseNodesDir ( self ):
    curDir = self.ui.lineEdit_nodes.text()
    newDir = QtGui.QFileDialog.getExistingDirectory( self, "Select Nodes Directory", curDir )
    if newDir != '' : 
      self.ui.lineEdit_nodes.setText( normPath( newDir ) )
  #
  #  
  def onBrowseIncludesDir ( self ):
    curDir = self.ui.lineEdit_inc.text()
    newDir = QtGui.QFileDialog.getExistingDirectory( self, "Select Includes Directory", curDir )
    if newDir != '' : 
      self.ui.lineEdit_inc.setText( normPath( newDir ) )
  #
  #  
  def onBrowseShadersDir ( self ):
    curDir = self.ui.lineEdit_shaders.text()
    newDir = QtGui.QFileDialog.getExistingDirectory( self, "Select Shaders Directory", curDir )
    if newDir != '' : 
      self.ui.lineEdit_shaders.setText( normPath( newDir ) )
  #
  #  
  def onBrowseTexturesDir ( self ):
    curDir = self.ui.lineEdit_textures.text()
    newDir = QtGui.QFileDialog.getExistingDirectory( self, "Select Directory", curDir )
    if newDir != '' : 
      self.ui.lineEdit_textures.setText( normPath( newDir ) )
  #
  #  
  def onBrowseArchivesDir ( self ):
    curDir = self.ui.lineEdit_archives.text()
    newDir = QtGui.QFileDialog.getExistingDirectory( self, "Select Directory", curDir )
    if newDir != '' : 
      self.ui.lineEdit_archives.setText( normPath( newDir ) )
  #
  #  
  def reject ( self ):
    self.done( 0 ) 
  #  
  #  
  def accept ( self ):
    #print ">> SettingsSetup: accept"
    
    temp_dir = normPath ( self.ui.lineEdit_temp.text() )
    inc_dir = normPath ( self.ui.lineEdit_inc.text() )
    lib_dir = normPath ( self.ui.lineEdit_lib.text() )
    nodes_dir = normPath ( self.ui.lineEdit_nodes.text() )
    
    shaders_dir = normPath ( self.ui.lineEdit_shaders.text() )
    textures_dir = normPath ( self.ui.lineEdit_textures.text() )
    archives_dir = normPath ( self.ui.lineEdit_archives.text() )
    
    self.app_settings.setValue( 'temp', temp_dir )
    self.app_settings.setValue( 'include', inc_dir )
    self.app_settings.setValue( 'lib', lib_dir )
    self.app_settings.setValue( 'nodes', nodes_dir )
    self.app_settings.setValue( 'shaders', shaders_dir )
    self.app_settings.setValue( 'texture', textures_dir )
    self.app_settings.setValue( 'archive', archives_dir )
    
    app_global_vars[ 'TempPath' ] = temp_dir
    
    app_global_vars[ 'LibPath' ] = lib_dir
    app_global_vars[ 'NodesPath' ] = nodes_dir
    
    app_global_vars[ 'IncludePath' ] = inc_dir
    app_global_vars[ 'ShaderPath' ] = shaders_dir
    app_global_vars[ 'TexturePath' ] = textures_dir
    
    app_global_vars[ 'TextureSearchPath' ] = sanitizeSearchPath ( textures_dir )
    app_global_vars[ 'ShaderSearchPath' ] = sanitizeSearchPath ( shaders_dir )
    app_global_vars[ 'ArchiveSearchPath' ] = sanitizeSearchPath ( archives_dir )
    
    createMissingDirs ( [temp_dir, lib_dir, nodes_dir, shaders_dir, textures_dir, archives_dir] ) # inc_dir, 
        
    #self.emit( QtCore.SIGNAL( "accepted()" ) )
    self.done( 0 ) 