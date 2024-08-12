from picamera2.previews.qt import QGlPicamera2
    

class CameraPreview(QGlPicamera2):

    def __init__(self, camera: any, width: int, height: int, keep_ar: bool):        
        super().__init__(camera, width=width, height=height, keep_ar=keep_ar)
