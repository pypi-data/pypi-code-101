import cv2
import numpy as np
import math

PLAYER_DEFAULTS: any = {
    'gates': [],
    'ksize': (21,21),
    'sigma_x': 0,
    'show': True,
    'debug': False
}

class Player:
    def __init__(self, file: str, config: dict=None, gates: list=None,
        ksize: tuple[int, int]=None, sigma_x: float=None, show: bool=None,
        debug: bool=False):
        
        self.video = cv2.VideoCapture(file)
        if self.video.read()[1] is None:
            raise ValueError("Video could not be read from file")

        # can be set from keyword args (cli/module import), config, 
        # and/or defaults. prefers keyword args > config > defaults
        self.gates = (gates or [Gate((g['x'], g['y']), g['width'], g['height'])
            for g in config['gates']] if config and config['gates']
            else PLAYER_DEFAULTS['gates'])
        self.ksize = (ksize or 
            (config['blur']['ksize']['height'], config['blur']['ksize']['width'])
            if config else PLAYER_DEFAULTS['ksize'])
        self.sigma_x = (sigma_x or config['blur']['sigma_x'] if config
            else PLAYER_DEFAULTS['sigma_x'])
        self.show = (show or config['show'] if config
            else PLAYER_DEFAULTS['show'])
        self.debug = (debug or config['debug'] if config
            else PLAYER_DEFAULTS['debug'])
        self.start_frame = 0 # TODO: make configurable
        self.text = ""

    def start(self):
        if not self.video.isOpened():
            print("Error opening video file")
        self.watch()
        self.end_video()

    def watch(self):
        initial_frame = None

        while True:
            check, frame = self.video.read()

            if not check:
                break
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            # convert to gray and smooth with noise
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur_frame = cv2.GaussianBlur(gray_frame, self.ksize, self.sigma_x)

            if initial_frame is None:
                initial_frame = blur_frame
                continue

            # Difference, threshold
            delta_frame = cv2.absdiff(initial_frame, blur_frame)
            threshold_frame = cv2.threshold(delta_frame, 6, 250, cv2.THRESH_BINARY)[1]

            # apply mask
            mask = np.zeros(frame.shape[:2], dtype="uint8")
            height, width, _ = frame.shape
            cv2.rectangle(mask, (0, int(height * 0.55)), (width, height), 255, -1)
            masked_threshold_frame = cv2.bitwise_and(
                threshold_frame, threshold_frame, mask=mask
            )

            (contours, _) = cv2.findContours(
                masked_threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                # filter out small contours
                if cv2.contourArea(c) < 3000:
                    continue

                (x, y, w, h) = cv2.boundingRect(c)
                self.track_objects(frame, x, y, w, h)

                if self.show:
                    rect = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    cv2.imshow("image_frame", rect)
                    cv2.putText(
                        frame,
                        self.text,
                        (10, 20),
                        cv2.FONT_HERSHEY_PLAIN,
                        2,
                        (0, 255, 0),
                        1,
                    )

            if self.debug and self.show:
                cv2.imshow("threshold_frame", masked_threshold_frame)
                cv2.imshow("blur_frame", blur_frame)
                cv2.imshow("delta_frame", delta_frame)
                cv2.imshow("Rectangular Mask", mask)

    def track_objects(self, frame, x, y, w, h):
        # count how many objects cross between a certain 
        # x threshold in a y range
        start, end = (x, y), (x + w, y + h)
        self.text = "Cars:"

        for gate in self.gates:
            gate.update(start, end)
            self.text += " (" + str(gate.counter) + " ," + str(gate.frame_countdown) + ")"
            if self.show:
                gate.show(frame, gate.get_centerpoint(start, end))

    def end_video(self):
        self.video.release()
        cv2.destroyAllWindows()

    def video_duration(self):
        fps = self.video.get(cv2.CAP_PROP_FPS)
        frame_count = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

        return frame_count / fps


class Gate:
    def __init__(self, start, width, height, intersection_tolerance=50):
        self.start = start
        self.end = (start[0] + width, start[1] + height)
        self.centerpoint = self.get_centerpoint(self.start, self.end)
        self.intersection_tolerance = intersection_tolerance
        self.counter = 0
        self.frame_countdown = 0

    def update(self, start, end):
        self.frame_countdown -= 1

        intersecting = self.intersect(start, end)
        on_cooldown = self.frame_countdown > 0
        object_centerpoint = self.get_centerpoint(start, end)
        within_tolerance = (
            self.get_distance(object_centerpoint, self.centerpoint)
            < self.intersection_tolerance
        )

        if intersecting and not on_cooldown and within_tolerance:
            self.counter += 1
            self.restart_countdown()

    def intersect(self, start, end):
        """Returns whether an object is intersecting with the gate"""
        return not (
            self.start[0] >= end[0]
            or self.end[0] <= start[0]
            or self.start[1] >= end[1]
            or self.end[1] <= start[1]
)

    def get_distance(self, start, end):
        """Returns the distance between two points"""
        return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

    def get_centerpoint(self, start, end):
        """Returns the center point of a gate"""
        return (int((start[0] + end[0]) / 2), int((start[1] + end[1]) / 2))

    def restart_countdown(self, frame_countdown=175):
        self.frame_countdown = frame_countdown

    def show(self, frame, object_centerpoint):
        distance = self.get_distance(object_centerpoint, self.centerpoint)
        gate = cv2.rectangle(frame, self.start, self.end, (255, 0, 0), 1)
        centerpoint_distance_line = cv2.line(
            frame, object_centerpoint, self.centerpoint, (0, 255, 0)
        )

        cv2.imshow("image_frame", gate)
        cv2.imshow("image_frame", centerpoint_distance_line)
        cv2.putText(
            frame,
            "{:.0f}".format(distance),
            object_centerpoint,
            cv2.FONT_HERSHEY_PLAIN,
            1,
            (0, 255, 0),
            1,
        )