import cv2
import mediapipe as mp
import time

class FaceMeshTracking():
    def __init__(self, static_mode = False, max_faces = 2, minDetectionConfidence = 0.5, minTrackingConfidence = 0.5, thickness = 1, circle_radius = 2):
        self.static_image = static_mode
        self.max_faces = max_faces
        self.minDetectionConfidence = minDetectionConfidence
        self.minTrackingConfidence = minTrackingConfidence
        self.thickness = thickness
        self.circle_radius = circle_radius


        self.mpFace = mp.solutions.face_mesh
        self.face = self.mpFace.FaceMesh(self.static_image, self.max_faces, self.minDetectionConfidence, self.minTrackingConfidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.drawSpecs = self.mpDraw.DrawingSpec(thickness = self.thickness, circle_radius = self.circle_radius)

    def findFaceMesh(self, img, draw = True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.results = self.face.process(imgRGB)
            #print(results.multi_hand_landmarks)
            faces = []

            if self.results.multi_face_landmarks:
                for faceLms in self.results.multi_face_landmarks:
                    if draw:

                        self.mpDraw.draw_landmarks(img, faceLms, self.mpFace.FACE_CONNECTIONS, self.drawSpecs, self.drawSpecs)

                    face = []

                    for id, lm in enumerate(faceLms.landmark):
                        height, width, channel = img.shape
                        cx, cy = int(lm.x*width), int(lm.y*height)
                        #print(id, cx, cy)
                        face.append([cx, cy])

                faces.append(face)

            return img, faces




def main():
    cap = cv2.VideoCapture(0)
    previousTime = 0
    currentTime = 0
    detector = FaceMeshTracking()

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces) != 0:
            print(len(faces))
        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime

        cv2.putText(img, "FPS: " + str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()