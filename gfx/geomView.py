#===============================================================================
# geomView.py
#
# 
#
#===============================================================================
import os, sys
import math

from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt4 import QtCore, QtGui 
from PyQt4.QtOpenGL import *
#
#
#
class GeomView ( QGLWidget ):
  #
  #
  def __init__ ( self, parent ):
    #
    QGLWidget.__init__ ( self, parent )
    
    self.state = 'idle' 
    self.panStartPos = None
    
    self.pixmap = None
    
    #self.setMinimumSize ( 500, 500 )
   
    # set scene
    #scene = QtGui.QGraphicsScene ( self )
    
    #scene.setSceneRect ( 0, 0, 256, 256 )
    #scene.setItemIndexMethod ( QtGui.QGraphicsScene.NoIndex )
    #self.setScene ( scene )
    
    # qt graphics stuff
    #self.setCacheMode ( QtGui.QGraphicsView.CacheBackground )
    #self.setRenderHint ( QtGui.QPainter.Antialiasing )
    
    #self.setTransformationAnchor ( QtGui.QGraphicsView.AnchorUnderMouse )
    #self.setResizeAnchor ( QtGui.QGraphicsView.AnchorViewCenter )
    #self.setDragMode ( QtGui.QGraphicsView.RubberBandDrag )
    
    #self.setMouseTracking ( False )
    
    #self.BgBrush = QtGui.QBrush ( QtGui.QColor ( 128, 128, 128 ) )  
    
    print '>> GeomView init'
  #
  #
  def initializeGL ( self ) :
    #
    print ">> GeomeView: initializeGL"
    
    #glClearColor(0.0, 0.0, 0.0, 0.0);
    #glEnable(GL_DEPTH_TEST);  
    # set viewing projection
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, 1.0, 1.0, 30.0)
  #
  #
  def resizeGL ( self, w, h) :
    #
    print ">> GeomeView: resizeGL (%d, %d)" % ( w, h )     
    
    #setup viewport, projection etc.:
    
    #glViewport(0, 0, w, h)
    #glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    #gluPerspective(40.0, 1.0, 1.0, 30.0)
    
  #
  #
  def paintGL ( self ) :
    #
    print ">> GeomeView: paintGL"
    
    # draw the scene:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Draw the spiral in 'immediate mode'
    # WARNING: You should not be doing the spiral calculation inside the loop
    # even if you are using glBegin/glEnd, sin/cos are fairly expensive functions
    # I've left it here as is to make the code simpler.
    radius = 1.0
    x = radius*math.sin(0)
    y = radius*math.cos(0)
    glColor(0.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    for deg in xrange(1000):
      glVertex( x, y, 0.0 )
      rad = math.radians(deg)
      radius -= 0.001
      x = radius*math.sin(rad)
      y = radius*math.cos(rad)
    glEnd()
    glEnableClientState(GL_VERTEX_ARRAY)
    
    spiral_array = []
    # Second Spiral using "array immediate mode" (i.e. Vertex Arrays)
    radius = 0.8
    x = radius*math.sin(0)
    y = radius*math.cos(0)
    glColor(1.0, 0.0, 0.0)
    for deg in xrange(820):
      spiral_array.append ( [x, y] )
      rad = math.radians(deg)
      radius -= 0.001
      x = radius*math.sin(rad)
      y = radius*math.cos(rad)

    glVertexPointerf(spiral_array)
    glDrawArrays( GL_LINE_STRIP, 0, len(spiral_array) )
    glFlush()

  #
  #
  def keyPressEvent ( self, event ) : 
    #
    print ">> GeomeView: keyPressEvent"
    QtGui.QGraphicsView.keyPressEvent ( self, event)
  #
  #  
  def wheelEvent ( self, event ):
    #
    #print ">> GeomeView: wheelEvent"
    # QtGui.QGraphicsView.wheelEvent( self, event)
    scale = -1.0
    if 'linux' in sys.platform: scale = 1.0     
    import math
    scaleFactor = math.pow( 2.0, scale * event.delta() / 600.0 )
    factor = self.matrix().scale( scaleFactor, scaleFactor ).mapRect( QtCore.QRectF( -1, -1, 2, 2 ) ).width()
    if factor < 0.07 or factor > 100: return
    self.scale ( scaleFactor, scaleFactor )      
  #
  #
  def mousePressEvent ( self, event ):
    #
    #print ">> GeomeView: mousePressEvent"
    if ( event.button() == QtCore.Qt.MidButton or 
      ( event.button() == QtCore.Qt.LeftButton and event.modifiers() == QtCore.Qt.ShiftModifier ) ) :  
      if self.state == 'idle':
        self.panStartPos = self.mapToScene( event.pos() )
        self.state = 'pan'
        return
    QtGui.QGraphicsView.mousePressEvent ( self, event )        
  #
  #
  def mouseDoubleClickEvent ( self, event ):
    #
    #print ">> GeomeView: mouseDoubleClickEvent"
    self.emit ( QtCore.SIGNAL( 'mouseDoubleClickEvent' ) ) 
    QtGui.QGraphicsView.mouseDoubleClickEvent ( self, event )
  #
  #  
  def mouseMoveEvent ( self, event ):
    #
    #print ">> GeomeView: mouseMoveEvent"
    if self.state == 'pan' :
      panCurrentPos = self.mapToScene( event.pos() )
      panDeltaPos = panCurrentPos - self.panStartPos
      # update view matrix
      self.setInteractive ( False )
      self.translate ( panDeltaPos.x(), panDeltaPos.y() )        
      self.setInteractive ( True )  
    else :
      QtGui.QGraphicsView.mouseMoveEvent ( self, event )        
  #
  #  
  def mouseReleaseEvent ( self, event ):        
    #
    #print ">> GeomeView: mouseReleaseEvent"
    if self.state == 'pan' :
      self.state = 'idle'  
      self.panStartPos = None
    QtGui.QGraphicsView.mouseReleaseEvent ( self, event )   
  #
  #
  def viewportEvent( self, event ):
    #case QEvent::TouchBegin:
    # case QEvent::TouchUpdate:
    # case QEvent::TouchEnd:
    if event.type() == QtCore.QEvent.TouchBegin :
      print ">> ImageView: QEvent.TouchBegin"
    return QtGui.QGraphicsView.viewportEvent ( self, event )
    
  #
  #
  def setImage ( self, imageName ) :
    #
    self.pixmap = QtGui.QPixmap() 
    wi = 256
    hi = 256   

    if imageName != '' :
      print ">> GeomeView: setImage name = %s" % imageName

      imageReader = QtGui.QImageReader ( imageName )

      if imageReader.canRead() :

        image = imageReader.read()
        if not self.pixmap.convertFromImage ( image ) :
          print ">> GeomeView: QPixmap can't convert %s" % imageName  
      else:
        print ">> GeomeView:  QImageReader can't read %s..." % imageName   
        # print imageReader.supportedImageFormats ()
        print ">> GeomeView: Lets try PIL module..."
        import Image
        image = Image.open ( imageName )
        # image.verify()

        import os
        from global_vars import app_global_vars

        tmpname = app_global_vars[ 'TempPath' ] + '/' + os.path.basename ( imageName + '.png' )
        print ">> GeomeView: Save %s ..." % tmpname 
        image.save ( tmpname )  

        self.pixmap = QtGui.QPixmap ( tmpname )

    if not self.pixmap.isNull():
      wi = self.pixmap.width()
      hi = self.pixmap.height() 
    else:
      print ">> GeomeView: isNull()"  

    self.scene().setSceneRect ( 0, 0, wi, hi )
    self.scene().update()
  #
  #
  def drawBackground( self, painter, rect ):
    #
    #print ">> GeomeView: drawBackground"
    painter.fillRect( rect, self.BgBrush )
    if self.pixmap is not None:
      #print ">> GeomeView: painter.drawPixmap"
      painter.drawPixmap ( 0, 0, self.pixmap )  
          
