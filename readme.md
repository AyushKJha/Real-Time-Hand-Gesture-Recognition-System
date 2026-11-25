<img src="docs/banner.svg" alt="OpenCV finger counter — webcam and hand landmark experiment" width="100%">

# Webcam Finger Counter
### An early computer-vision experiment.

A Python webcam demo intended to count raised fingers and display an annotated camera feed.

**Status:** runnable. Finger counting uses MediaPipe Hands landmarks in [utils.py](utils.py), which replaces the original module that was never committed.

## Run it

Use Python 3.9–3.12 (MediaPipe has no wheels for newer versions yet).

```bash
pip install -r requirements.txt
python "Finger Counter.py"
```

[Finger Counter.py](Finger%20Counter.py) opens camera device 0, counts raised fingers on up to two hands, and shows the annotated feed.

| Control | Action |
| --- | --- |
| `q` | Close the camera window |
| `s` | Save the displayed frame as `hand_counted_<number>.jpg` |

## How counting works

A finger counts as raised when its tip landmark sits above the joint below it. The thumb is compared sideways instead, using the detected handedness.

## Project context

This is an early learning project in webcam processing and human–computer interaction. It remains here as a source snapshot while the missing implementation is recovered.

**Ayush Kumar Jha** · [Profile](https://github.com/AyushKJha)
