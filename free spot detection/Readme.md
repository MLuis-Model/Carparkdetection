## Overview
The Motion Detector is a simple tool that allows you to detect motion in a video file. The tool uses a set of pre-defined coordinates to track motion within a specified region of interest (ROI) in the video. The output of the tool is a video file where the frames containing motion are marked with a bounding box.

## Requirements
Python 3.6 or later
OpenCV
PyYAML

## Installation
Clone this repository to your local machine
Install the dependencies using pip install -r requirements.txt

## Usage
- Run the following command in the terminal:
python main.py

- Program flow
    1. Select the video file that you want to process.
    2. Select the parking slots you want to monitor.
    3. The tool will then analyze the video and generate a new video file with the motion detection bounding boxes.

