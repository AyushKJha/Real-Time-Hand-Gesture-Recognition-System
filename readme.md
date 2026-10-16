# Webcam Finger Counter
### An early computer-vision experiment.

A Python webcam demo intended to count raised fingers and display an annotated camera feed.

**Status: incomplete source snapshot.** The entry script imports `Finger_counter` from `utils`, but that module is missing from this repository. The checked-in `requirement.txt` is empty, so the project is not runnable from a fresh clone.

## What is present

[Finger Counter.py](Finger%20Counter.py) opens camera device 0 with OpenCV, passes frames to `count_fingers()`, and displays the returned image.

| Control | Action |
| --- | --- |
| `q` | Close the camera window |
| `s` | Save the displayed frame as `hand_counted_<number>.jpg` |

## What needs restoring

- The original `utils` module containing the finger-counting implementation.
- A dependency list verified against that implementation.
- A real demo recording and tested setup instructions.

The entry script alone does not establish which hand-tracking library or algorithm the missing implementation uses. There is currently no demo image, packaged executable, or APK in the repository.

## Project context

This is an early learning project in webcam processing and human–computer interaction. It remains here as a source snapshot while the missing implementation is recovered.

**Ayush Kumar Jha** · [Profile](https://github.com/AyushKJha)
