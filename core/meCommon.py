#===============================================================================
# meCommon.py
#
# 
#
#===============================================================================
import os, sys


from PyQt4 import QtCore
#
#
#
def findExecutable ( executable, path = None ):
  """Try to find 'executable' in the directories listed in 'path' (a
  string listing directories separated by 'os.pathsep'; defaults to
  os.environ['PATH']).  Returns the complete filename or None if not
  found
  """
  if path is None:
    path = os.environ['PATH']
  paths = path.split(os.pathsep)
  extlist = ['']
  if os.name == 'os2':
    (base, ext) = os.path.splitext(executable)
    # executable files on OS/2 can have an arbitrary extension, but
    # .exe is automatically appended if no dot is present in the name
    if not ext:
      executable = executable + ".exe"
  elif sys.platform == 'win32':
    pathext = os.environ['PATHEXT'].lower().split(os.pathsep)
    (base, ext) = os.path.splitext(executable)
    if ext.lower() not in pathext:
      extlist = pathext
  for ext in extlist:
    execname = executable + ext
    if os.path.isfile( execname ):
      return execname
    else:
      for p in paths:
        f = os.path.join(p, execname)
        if os.path.isfile(f):
          return f
  else:
    return None
#
#
#
def createMissingDirs ( dirList = None ):   
  #
  for dirName in dirList :
    #print '-> Check dir %s' % dirName    
    if not os.path.exists ( dirName ) : 
      print '-> Create missing dir %s' % dirName    
      os.makedirs ( dirName )

#
# Use this hack, as os.path.normpath doesn't work on windooze,
# but QtCore.QDir works fine ...
#
def normPath ( pathName ) :
  result = ''
  if pathName != '' :
    if ( sys.platform == 'win32' ) :
      result = str ( QtCore.QDir( pathName ).absolutePath() )  
    else :
      result = os.path.normpath ( str( pathName ) )
  return result  
#
# replace C:/ with //C/ for RIB search path names
#
def sanitizeSearchPath ( pathName ) :
  #print ':: sanitizeSearchPath %s' %  pathName
  sanitizedPath = pathName
  if ( sys.platform == 'win32' ) :
    if pathName[1:2] == ':' :
      sanitizedPath = ( '//' + pathName[0:1] + pathName[2:] )
  return sanitizedPath
#
# is pathname relative ? 
#
def isRelativePath ( pathName ) :
  isRelative = True
  if ( sys.platform == 'win32' ) :
    if pathName[1:2] == ':' : isRelative = False
  if pathName[0:1] == '\\' or pathName[0:1] == '/' : 
    isRelative = False
  return isRelative     
#
# get pathName relative to rootPath 
#
def toRelativePath ( rootPath, pathName ) :
  #print ':: toRelativePath %s' %  pathName
  relativePath = pathName
  if not isRelativePath ( pathName ) :
    if pathName.find ( rootPath ) != -1 :
      relativePath = pathName[ len( rootPath ) + 1 :  ]  
    
  return relativePath
#
# get full pathName from relative to rootPath 
#
def fromRelativePath ( rootPath, pathName ) :
  #print ':: fromRelativePath %s' %  pathName
  fullPath = pathName
  if isRelativePath ( pathName ) :
    fullPath = os.path.join ( rootPath, pathName )
    
  return fullPath  
#
# launch process
#
def launchProcess ( cmdList ) :
  #
  import subprocess, errno
  
  try:
    if ( sys.platform.startswith( 'linux' ) ):
      (sysname, nodename, release, version, machine) = os.uname()
      #print 'sysname = %s' % sysname
      #print 'release = %s' % release
      #print 'version = %s' % version
      if version.find( 'Ubuntu' ) != -1 :
        print 'Ubuntu'
        retval = os.popen( ' '.join( cmdList ) )
      else :
        retval = subprocess.call( cmdList )  
    else:        
      retval = subprocess.call( cmdList )
  except OSError, e:
    if e.errno != errno.EINTR : raise 
#
#
#
def getUniqueName  ( name, nameList ) :
  newName = name
  sfx = 0
  while newName in nameList :
    newName = name + str ( sfx )
    sfx += 1
  return newName  
  
  
