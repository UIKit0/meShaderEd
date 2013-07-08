"""
 geomView.py

"""
import os, sys
import math

from OpenGL.GL import *
#from OpenGL.GLU import *

from PyQt4 import QtCore, QtGui, QtOpenGL
#from PyQt4.QtOpenGL import * #QGLFunctions

PI = 3.14159
#
# GeomView
#
class GeomView ( QtOpenGL.QGLWidget ) : # , QGLFunctions
  #
  # __init__
  #
  def __init__ ( self, parent ) :
    #
    QtOpenGL.QGLWidget.__init__ ( self, 
                      QtOpenGL.QGLFormat ( QtOpenGL.QGL.SampleBuffers | QtOpenGL.QGL.DoubleBuffer ), # SingleBuffer | QtOpenGL.QGL.NoOverlay DoubleBuffer QtOpenGL.QGL.SampleBuffers | QtOpenGL.QGL.DirectRendering ),
                      parent ) # QtOpenGL.QGLFormat ( QtOpenGL.QGL.SampleBuffers ), 
    #self.makeCurrent ()
    
    self.state = 'idle'
    self.pressed = False
    self.panStartPos = None
    
    self.bgColor = [ .3, .3, .3, 0.0 ]
    self.fgColor = [ .45, .45, .45, 0.0 ]
    
    self.modelMatrix = QtGui.QMatrix4x4 ()
    self.projectionMatrix = QtGui.QMatrix4x4 ()
    self.fov = 60.0
    self.roll = 0.0
    self.zNear = 0.01
    self.zFar = 1000.0
    self.width = 0.0
    self.height = 0.0
    
    self.isProjDirty = True
    
    self.isGridVisible = True
    self.headLight = False

    self.modelMatrix.translate ( 0.0, 0.0, 10.0 )
    self.target = QtGui.QVector3D ( 0.0, 0.0, 0.0 )
    #orbit(-40, 45);
    #dolly(240);
    
    #self.setAutoBufferSwap ( True ) 
    
    self.geom_code = """
glEnableClientState ( GL_VERTEX_ARRAY )
spiral_array = []
# Second Spiral using "array immediate mode" (i.e. Vertex Arrays)
radius = 0.8
x = radius * math.sin ( 0 )
y = radius * math.cos ( 0 )
glColor ( 1.0, 0.0, 0.0 )
for deg in xrange ( 820 ):
  spiral_array.append ( [x, y] )
  rad = math.radians ( deg )
  radius -= 0.001
  x = radius * math.sin ( rad )
  y = radius * math.cos ( rad )

glVertexPointerf ( spiral_array )
glDrawArrays ( GL_LINE_STRIP, 0, len ( spiral_array ) )
glFlush ()



"""
    print '>> GeomView init'
  #
  # initializeGL
  #
  def initializeGL ( self ) :
    #
    print ">> GeomeView.initializeGL"
    
    glClearColor ( self.bgColor [0], self.bgColor [1], self.bgColor [2], 0 )
    glEnable ( GL_DEPTH_TEST )
    glDepthFunc ( GL_LEQUAL )
    glDepthMask ( GL_TRUE )
    glClearDepth ( 1.0 )
    #glClear ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  
    glEnable ( GL_BLEND )
    glBlendFunc ( GL_SRC_ALPHA , GL_ONE_MINUS_SRC_ALPHA )
  
    # lighting
    #glEnable ( GL_LIGHT0 )
    #glLightfv ( GL_LIGHT0, GL_AMBIENT, lightAmbient )
    #glLightfv ( GL_LIGHT0, GL_DIFFUSE, lightDiffuse )
  
  #
  # resizeGL
  #
  def resizeGL ( self, w, h ) :
    #
    print '>> GeomeView.resizeGL (%d, %d)' % ( w, h )
    
    self.width = w
    self.height = h
    if self.height == 0 : self.height = 1
    if self.width == 0 : self.width = 1
    self.isProjDirty = True
  #
  # prepareForDrawing
  #
  def prepareForDrawing ( self ) :
    #
    print '>> GeomeView.prepareForDrawing'
    self.setupProjection ()
    glViewport ( 0, 0, self.width, self.height )
  
    glMatrixMode ( GL_MODELVIEW )
    
    ( invertedMatrix, invertible ) = self.modelMatrix.inverted ()
    # print invertedMatrix
    glLoadMatrixf ( invertedMatrix.data () )
  
    #// gray-shaded
    #glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, grayAmbient);
    #glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, grayDiffuse);
    #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, whiteSpecular);
    #glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, defaultShininess);
  #
  # setupProjection
  #
  def setupProjection ( self ) :
    #
    print '>> GeomeView.setupProjection'
    glMatrixMode ( GL_PROJECTION )
    
    if self.isProjDirty :
      glLoadIdentity()

      height = float ( self.zNear * math.tan ( self.fov * PI / 360.0) )
      width = float ( height )
      aspect = float ( float ( self.width ) / float ( self.height ) )
      
      if aspect > 1.0 :
        height = float ( height / aspect )
      else :
        width = float ( height * aspect )
        
      print width, height, aspect 

      glFrustum ( -width, width, -height, height, self.zNear, self.zFar )
      params = glGetFloatv ( GL_PROJECTION_MATRIX )
      #print params
      #print params [0][0],  params [0][1],  params [0][2],  params [0][3]
      #print params [1][0],  params [1][1],  params [1][2],  params [1][3]
      #print params [2][0],  params [2][1],  params [2][2],  params [2][3]
      #print params [3][0],  params [3][1],  params [3][2],  params [3][3]
      self.projectionMatrix = QtGui.QMatrix4x4 ( params [0][0],  params [0][1],  params [0][2],  params [0][3], 
                                                 params [1][0],  params [1][1],  params [1][2],  params [1][3],
                                                 params [2][0],  params [2][1],  params [2][2],  params [2][3],
                                                 params [3][0],  params [3][1],  params [3][2],  params [3][3]
                                               )
      #print self.projectionMatrix
      #print self.projectionMatrix.data ()    
      self.isProjDirty = False
    else :
      pass
      #print '>> GeomeView.setupProjection ( glLoadMatrixf )'
      #glLoadMatrixf ( self.projectionMatrix.data () )
  #
  # updateGL
  #
  def updateGL ( self ) :
    #
    print ">> GeomeView.updateGL"
    QtOpenGL.QGLWidget.updateGL ( self )
  #
  # paintGL
  #
  def paintGL ( self ) :
    #
    print ">> GeomeView.paintGL"
    
    #glClearColor ( 0, 0, 0, 0 ) # ( self.bgColor [0], self.bgColor [1], self.bgColor [2], 0.0 )
    glClearColor ( self.bgColor [0], self.bgColor [1], self.bgColor [2], 0 )
    glClearDepth ( 1.0 )
    glClear ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ) # ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    #self.swapBuffers ()
    
  
    self.prepareForDrawing ()
  
    #glDisable ( GL_LIGHTING )
    #glShadeModel ( GL_FLAT )
  
    if self.isGridVisible : self.drawGrid ()
  
    #self.drawAxis();
  
    #glShadeModel ( GL_SMOOTH )
    #glEnable ( GL_LIGHTING )
    
    if self.headLight :
      # constrain light to camera
      lightPosition[0] = self.modelMatrix [3][0]
      lightPosition[1] = self.modelMatrix [3][1] + 100.0;
      lightPosition[2] = self.modelMatrix [3][2]
      glLightfv ( GL_LIGHT0, GL_POSITION, lightPosition )
    
    #self.prepareForDrawing ()
    
    #MainDrawRoutine::drawAll();

  #
  # drawGrid
  #
  def drawGrid ( self ) :
    #
    print ">> GeomeView.drawGrid"
    #print self.autoBufferSwap ()
    #glClear ( GL_DEPTH_BUFFER_BIT ) #| GL_DEPTH_BUFFER_BIT ) | GL_COLOR_BUFFER_BIT
    #glLoadIdentity ()
    
    """
    glColor3f ( self.fgColor [0], self.fgColor [1], self.fgColor [2] )
    glBegin ( GL_QUADS )
    glVertex3f ( 0,  -0.001, 0  )
    glVertex3f ( 0,  -0.001, 20 )
    glVertex3f ( 20, -0.001, 20 )
    glVertex3f ( 20, -0.001, 0 )
    glEnd ()
    
    glBegin ( GL_LINES )
    for i in range ( 20 ) :
      if i == 0 : 
        glColor3f ( .6, .3, .3 ) 
      else : 
        glColor3f ( .25, .25, .25 )
      glVertex3f ( i, 0, 0 )
      glVertex3f ( i, 0, 20 )
      if i==0 : 
        glColor3f ( .3, .3, .6 )
      else :
        glColor3f ( .25, .25, .25 )
      glVertex3f ( 0,  0, i )
      glVertex3f ( 20, 0, i )
    
    glEnd ()
    """
    
    count = 20
    scale = 1.0
    
    glColor3f ( 0.45, 0.45, 0.45 )
    glLineWidth ( 1.0 )
    glBegin ( GL_LINES )
    for w in range ( count ) :
      glVertex3f ( -count / 2 * scale, 0, ( w - count / 2 ) * scale )
      glVertex3f ( ( count - count / 2) * scale, 0, ( w - count / 2 ) * scale )
    for w in range ( count ) :
      glVertex3f ( ( w - count / 2 ) * scale, 0, -count / 2 * scale )
      glVertex3f ( ( w - count / 2 ) * scale, 0, ( count - count / 2 ) * scale )
    glEnd ()
    
    # draw 2 middle lines again
    glColor3f ( 0.9, 0.2, 0.2 )
    glLineWidth ( 1.0 )
    glBegin ( GL_LINES )
    glVertex3f ( -count / 2 * scale, 0, ( count / 2 - count / 2 ) * scale )
    glVertex3f ( ( count - ( count / 2 ) ) * scale, 0, ( count / 2 - count / 2 ) * scale )
    glVertex3f ( ( count / 2 - count / 2 ) * scale, 0, -count / 2 * scale )
    glVertex3f ( ( count / 2 - count / 2 ) * scale, 0, ( count - count / 2 ) * scale )
    glEnd ()
    
    # Draw the spiral in 'immediate mode'
    # WARNING: You should not be doing the spiral calculation inside the loop
    # even if you are using glBegin/glEnd, sin/cos are fairly expensive functions
    # I've left it here as is to make the code simpler.
    radius = 1.0
    x = radius * math.sin ( 0 )
    y = radius * math.cos ( 0 )
    glColor ( 0.0, 1.0, 0.0 )
    glBegin ( GL_LINE_STRIP )
    for deg in xrange ( 1000 ) :
      glVertex ( x, y, 0.0 )
      rad = math.radians ( deg )
      radius -= 0.001
      x = radius * math.sin ( rad )
      y = radius * math.cos ( rad )
    glEnd ()
    
    exec self.geom_code
  #
  # dolly
  #
  def dolly ( self, deltaSide ) :
    #
    if deltaSide != 0 :
      print '* deltaSide = %d' % deltaSide
      row0 = self.modelMatrix.row ( 0 )
      row1 = self.modelMatrix.row ( 1 )
      row2 = self.modelMatrix.row ( 2 ) # cam does dolly on its Z local axis (QtGui.QVector4D )
      dollyVec = QtGui.QVector3D ( row2.x (), row2.y (), row2.z () )
      translation = QtGui.QVector3D ( row0.w (), row1.w (), row2.w () )
      #print self.modelMatrix
      #print row2
      #print dollyVec
      #print translation
      dollyVec *= ( deltaSide * ( translation - self.target).length() * 0.01 )
      self.modelMatrix.translate ( dollyVec.x (), dollyVec.y (), dollyVec.z () )
      #print self.modelMatrix
  #
  # timerEvent
  #
  def timerEvent ( self, event ) :
    #
    print ">> GeomeView.timerEvent"
    self.updateGL ()  
  #
  # keyPressEvent
  #
  def keyPressEvent ( self, event ) :
    #
    print ">> GeomeView.keyPressEvent"
    QtGui.QWidget.keyPressEvent ( self, event)
  #
  # wheelEvent
  #
  def wheelEvent ( self, event ) :
    #
    print ">> GeomeView: wheelEvent ( event.delta = %f )" % event.delta ()
    if event.orientation() == QtCore.Qt.Vertical :
      self.dolly ( int ( event.delta () * -0.1 ) )
      self.isProjDirty = True
      self.updateGL ()
      
    QtGui.QWidget.wheelEvent ( self, event)
    
    """
    #if qWheelEvent.orientation() == QtCore.Qt.Vertical:
    #        self._viewport.dolly(int(qWheelEvent.delta() * -0.1))
    #        self.updateGL()
    #        self._dirtyCameraNodes()
    # QtGui.QGraphicsView.wheelEvent( self, event)
    scale = -1.0
    if 'linux' in sys.platform: scale = 1.0
    
    scaleFactor = math.pow ( 2.0, scale * event.delta () / 600.0 )
    factor = self.matrix ().scale ( scaleFactor, scaleFactor ).mapRect ( QtCore.QRectF ( -1, -1, 2, 2 ) ).width ()
    if factor < 0.07 or factor > 100: return
    self.scale ( scaleFactor, scaleFactor )
    """
  #
  # mousePressEvent
  #
  def mousePressEvent ( self, event ) :
    #
    #print ">> GeomeView: mousePressEvent"
    if ( event.button () == QtCore.Qt.MidButton or
        ( event.button () == QtCore.Qt.LeftButton and event.modifiers () == QtCore.Qt.ShiftModifier ) ) :
      if self.state == 'idle' :
        # self.panStartPos = self.mapToScene ( event.pos () )
        self.state = 'pan'
        return
    QtGui.QWidget.mousePressEvent ( self, event )
  #
  # mouseDoubleClickEvent
  #
  def mouseDoubleClickEvent ( self, event ) :
    #
    #print ">> GeomeView.mouseDoubleClickEvent"
    self.emit ( QtCore.SIGNAL ( 'mouseDoubleClickEvent' ) )
    QtGui.QWidget.mouseDoubleClickEvent ( self, event )
  #
  # mouseMoveEvent
  #
  def mouseMoveEvent ( self, event ) :
    #
    #print ">> GeomeView.mouseMoveEvent"
    if self.state == 'pan' :
      #panCurrentPos = self.mapToScene ( event.pos () )
      panDeltaPos = panCurrentPos - self.panStartPos
      # update view matrix
      self.setInteractive ( False )
      self.translate ( panDeltaPos.x (), panDeltaPos.y () )
      self.setInteractive ( True )
    else :
      QtGui.QWidget.mouseMoveEvent ( self, event )
  #
  # mouseReleaseEvent
  #
  def mouseReleaseEvent ( self, event ) :
    #
    #print ">> GeomeView.mouseReleaseEvent"
    if self.state == 'pan' :
      self.state = 'idle'
      self.panStartPos = None
    QtGui.QWidget.mouseReleaseEvent ( self, event )
  #
  # viewportEvent
  #
  def viewportEvent ( self, event ) :
    #case QEvent::TouchBegin:
    # case QEvent::TouchUpdate:
    # case QEvent::TouchEnd:
    if event.type () == QtCore.QEvent.TouchBegin :
      print ">> ImageView: QEvent.TouchBegin"
    return QtGui.QWidget.viewportEvent ( self, event )



