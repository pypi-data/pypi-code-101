import cv2
import mediapipe as mp
import math

class HandDetector:
    def __init__(self, detection_con=0.5, min_track_con=0.5):
        self.detectionCon = detection_con
        self.minTrackCon = min_track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=self.detectionCon,
                                         min_tracking_confidence=self.minTrackCon)

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        self.tip_ids = [4, 8, 12, 16, 20]
        self.fingerName = ["Thumb", "Index Finger", "Middle Finger", "Ring Finger", "Little Finger"]

    def find_hands(self, img, draw=True, flip_type=True):
        """
        When the image file is read with the OpenCV function read() ,
        the order of colors is BGR (blue, green, red). So here we are converting
        BGR image to RGB
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        """
        Processes an RGB image and returns the hand landmarks and handedness of each detected hand.
        It returns a NamedTuple object with two fields: a "multi_hand_landmarks" field that
        contains the hand landmarks on each detected hand and a "multi_handedness"
        field that contains the handedness (left v.s. right hand) of the detected
        hand.
        """
        self.results = self.hands.process(img_rgb)
        """
        hold the properties of all the hands
        """
        all_hands = []
        height, width, color = img.shape
        BBOX_OFFSET = 15

        if self.results.multi_hand_landmarks:
            """
            hand_type will contain the details of hands. {Right Hand , Left Hand}
            hand_lms will contain the landmarks of hands. one hand contains 21 landmarks.
            iterates on each hands at once
            """
            for hand_type, hand_lms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                """
                it will contain the different properties of hands
                lm_list--> coordinates of landmarks. (x,y)
                bbox--> coordinates of boundary box.
                """
                my_hand={}
                """
                it will contain the coordinates of landmarks
                lm_list--> coordinates of landmarks. (x,y)
                """
                mylm_list = []
                """ 
                it contains the x coordinates of landmarks
                """
                x_list = []
                """
                it contains the y coordinates of landmarks.
                """
                y_list = []
                """
                Extracts the landmarks from each hands and fit those landmarks with image shape (e.g. 640x480)
                and store it in mylm_list
                """
                for id, lm in enumerate(hand_lms.landmark):
                    px, py = int(lm.x * width), int(lm.y * height)
                    mylm_list.append([px, py])
                    x_list.append(px)
                    y_list.append(py)

                my_hand["lm_list"] = mylm_list

                """create a boundary box around the  each hand."""
                xmin, xmax = min(x_list), max(x_list)
                ymin, ymax = min(y_list), max(y_list)
                bbox = xmin, ymin, xmax, ymax

                my_hand["bbox"] = bbox

                if flip_type:
                    if hand_type.classification[0].label == "Right":
                        my_hand["type"] = "Left"
                    else:
                        my_hand["type"] = "Right"
                else:
                    my_hand["type"] = hand_type.classification[0].label

                all_hands.append(my_hand)

                """Draw the hands"""
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms,
                                                self.mp_hands.HAND_CONNECTIONS,
                                                self.mp_drawing_styles.get_default_hand_landmarks_style())

                    cv2.rectangle(img, (bbox[0]-BBOX_OFFSET, bbox[3]+BBOX_OFFSET),
                                  (bbox[2]+BBOX_OFFSET, bbox[1]-BBOX_OFFSET), (0, 255, 0), 2)

                    cv2.putText(img, my_hand["type"], (bbox[0], bbox[1]-30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        if draw:
            return all_hands, img
        else:
            return all_hands

    def fingers_up(self, my_hand):
        my_hand_type = my_hand["type"]
        mylm_list = my_hand["lm_list"]

        if self.results.multi_hand_landmarks:
            fingers = []

            ## Thumb
            if my_hand_type == "Right":
                if mylm_list[self.tip_ids[0]][0] > mylm_list[self.tip_ids[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if mylm_list[self.tip_ids[0]][0] < mylm_list[self.tip_ids[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            ## Fingers
            for id in range(1, 5):
                if mylm_list[self.tip_ids[id]][1] < mylm_list[self.tip_ids[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        return fingers

    def find_distance(self, p1, p2, img=None):
        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = (x1, y1, x2, y2, cx, cy)
        if img is not None:
            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
            return length, info, img
        else:
            return length, info


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        hands, img = detector.find_hands(img)

        if hands:
            hand1 = hands[0]
            lm_list1 = hand1["lm_list"]
            fingers1 = detector.fingers_up(hand1)

            if len(hands) == 2:
                hand2 = hands[1]
                lm_list2 = hand2["lm_list"]
                fingers2 = detector.fingers_up(hand2)
                length, info, img = detector.find_distance(lm_list1[8], lm_list2[8], img)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
