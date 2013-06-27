#===============================================================================
# renderView.py
#
# 
#
#===============================================================================
import os, sys
from PyQt4 import QtCore, QtGui
#
#
#
class RenderView ( QtGui.QGraphicsView ):
  #
  #
  def __init__ ( self, parent ):
    #
    QtGui.QGraphicsView.__init__( self, parent )
    
    self.state = 'idle' 
    self.panStartPos = None
    
    self.pixmap = None
   
    # set scene
    scene = QtGui.QGraphicsScene ( self )
    
    scene.setSceneRect ( 0, 0, 256, 256 )
    #scene.setItemIndexMethod ( QtGui.QGraphicsScene.NoIndex )
    self.setScene ( scene )
    
    # qt graphics stuff
    #self.setCacheMode ( QtGui.QGraphicsView.CacheBackground )
    self.setRenderHint ( QtGui.QPainter.Antialiasing )
    
    self.setTransformationAnchor ( QtGui.QGraphicsView.AnchorUnderMouse )
    self.setResizeAnchor ( QtGui.QGraphicsView.AnchorViewCenter )
    self.setDragMode ( QtGui.QGraphicsView.RubberBandDrag )
    
    self.setMouseTracking ( False )
    
    self.BgBrush = QtGui.QBrush ( QtGui.QColor ( 128, 128, 128 ) )  
    
    print '>> RenderView init'
  #
  #

  #
  #
  def keyPressEvent ( self, event ) : 
    #
    print ">> RenderView: keyPressEvent"
    QtGui.QGraphicsView.keyPressEvent ( self, event)
  #
  #  
  def wheelEvent ( self, event ):
    #
    #print ">> RenderView: wheelEvent"
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
    #print ">> RenderView: mousePressEvent"
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
    #print ">> RenderView: mouseDoubleClickEvent"
    self.emit ( QtCore.SIGNAL( 'mouseDoubleClickEvent' ) ) 
    QtGui.QGraphicsView.mouseDoubleClickEvent ( self, event )
  #
  #  
  def mouseMoveEvent ( self, event ):
    #
    #print ">> RenderView: mouseMoveEvent"
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
    #print ">> RenderView: mouseReleaseEvent"
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
      print ">> RenderView: QEvent.TouchBegin"
    return QtGui.QGraphicsView.viewportEvent ( self, event )
    
  #
  #
  def setImage ( self, imageName ) :
    #
    self.pixmap = QtGui.QPixmap() 
    wi = 256
    hi = 256   

    if imageName != '' :
      print ">> RenderView: setImage name = %s" % imageName

      imageReader = QtGui.QImageReader ( imageName )

      if imageReader.canRead() :

        image = imageReader.read()
        if not self.pixmap.convertFromImage ( image ) :
          print ">> RenderView: QPixmap can't convert %s" % imageName  
      else:
        print ">> RenderView:  QImageReader can't read %s..." % imageName   
        # print imageReader.supportedImageFormats ()
        print ">> RenderView: Lets try PIL module..."
        import Image
        image = Image.open ( imageName )
        # image.verify()

        import os
        from global_vars import app_global_vars

        tmpname = app_global_vars[ 'TempPath' ] + '/' + os.path.basename ( imageName + '.png' )
        print ">> RenderView: Save %s ..." % tmpname 
        image.save ( tmpname )  

        self.pixmap = QtGui.QPixmap ( tmpname )

    if not self.pixmap.isNull():
      wi = self.pixmap.width()
      hi = self.pixmap.height() 
    else:
      print ">> RenderView: isNull()"  

    self.scene().setSceneRect ( 0, 0, wi, hi )
    self.scene().update()
  #
  #
  def drawBackground( self, painter, rect ):
    #
    #print ">> RenderView: drawBackground"
    painter.fillRect( rect, self.BgBrush )
    if self.pixmap is not None:
      #print ">> RenderView: painter.drawPixmap"
      painter.drawPixmap ( 0, 0, self.pixmap )  
          
