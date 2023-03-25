import argparse
import yaml
from coordinates_generator import CoordinatesGenerator
from motion_detector import MotionDetector
from colors import *
import logging
import tkinter as tk
from tkinter import filedialog
import cv2

def main():
    logging.basicConfig(level=logging.INFO)

    data_file = "data/coordinates_1.yml"
    video_file_path = select_video_file()
    image_file = "first_frame.png"

    getFirstFrame(video_file_path, image_file)
    with open(data_file, "w+") as points:
        generator = CoordinatesGenerator(image_file, points, COLOR_RED)
        generator.generate()

    with open(data_file, "r") as data:
        points = yaml.load(data, Loader=yaml.SafeLoader)
        detector = MotionDetector(video_file_path, points,1)
        detector.detect_motion()


def select_video_file():
    root = tk.Tk()
    root.withdraw()

    video_file_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.flv;*.wmv")])

    if not video_file_path:
        raise ValueError("No video file selected")

    return video_file_path

def getFirstFrame(videofile, output_image_path):
    vidcap = cv2.VideoCapture(videofile)
    success, image = vidcap.read()
    if success:
        cv2.imwrite(output_image_path, image)

if __name__ == '__main__':
    main()
