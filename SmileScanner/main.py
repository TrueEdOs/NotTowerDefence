import cv2


class Smile:
    def __init__(self):
        self.activated = True

        self.faceCascade = cv2.CascadeClassifier('SmileScanner/Cascades/haarcascade_frontalface_default.xml')
        self.smileCascade = cv2.CascadeClassifier('SmileScanner/Cascades/haarcascade_smile.xml')

        self.cap = cv2.VideoCapture('http://192.168.0.101:4747/mjpegfeed')
        self.cap.set(3, 640)  # set Width
        self.cap.set(4, 480)  # set Height

    def stop(self):
        self.activated = False

    def check_face(self):
        ret, img = self.cap.read()
        gray = None
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            smile = self.smileCascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.5,
                minNeighbors=15,
                minSize=(25, 25),
            )
            if smile is not None:
                self.stop()
