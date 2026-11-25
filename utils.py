"""Finger counting with MediaPipe Hands.

Replaces the original ROI-based `utils` module, which was never committed.
"""
import cv2
import mediapipe as mp

_TIPS = (8, 12, 16, 20)   # index, middle, ring, little fingertip landmarks
_PIPS = (6, 10, 14, 18)   # the joint two below each tip


class Finger_counter:
    def __init__(self, max_hands=2, detection_confidence=0.7, tracking_confidence=0.5):
        self._hands = mp.solutions.hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
        )
        self._draw = mp.solutions.drawing_utils
        self._connections = mp.solutions.hands.HAND_CONNECTIONS

    @staticmethod
    def _count_one(landmarks, handedness):
        pts = landmarks.landmark
        raised = sum(pts[tip].y < pts[pip].y for tip, pip in zip(_TIPS, _PIPS))
        # The thumb folds sideways, so compare x instead of y. The image is
        # mirrored before processing, so MediaPipe's "Right" is the user's right hand.
        if handedness == "Right":
            raised += pts[4].x < pts[3].x
        else:
            raised += pts[4].x > pts[3].x
        return int(raised)

    def count_fingers(self, frame):
        """Return (annotated_frame, total raised fingers across detected hands)."""
        frame = cv2.flip(frame, 1)
        result = self._hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        total = 0
        if result.multi_hand_landmarks:
            for landmarks, info in zip(result.multi_hand_landmarks, result.multi_handedness):
                total += self._count_one(landmarks, info.classification[0].label)
                self._draw.draw_landmarks(frame, landmarks, self._connections)
        cv2.putText(frame, f"Fingers: {total}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.4, (0, 255, 0), 3, cv2.LINE_AA)
        return frame, total
