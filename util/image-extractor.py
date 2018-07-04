# This script can be used to convert input video file into number of snapshots(images) taken and regular configurable interval
# author: shreyasn

import argparse
import os

import cv2
import pafy

from util.utility import is_url


def extract_images(video, image_path, interval=1):
    count = 0
    # check if video path string is url

    if video == "":
        print("Video file path cannot be empty.")
        exit(0)
    if is_url(video):
        video_pafy = pafy.new(video)
        video = video_pafy.getbest().url

    vid_cap = cv2.VideoCapture(video)

    try:
        while True:
            vid_cap.set(cv2.CAP_PROP_POS_MSEC, (count * (interval * 1000)))  # added this line
            success, frame = vid_cap.read()
            if success:
                cv2.imwrite(image_path + "\\frame%d.jpg" % count, frame)  # save frame as JPEG file
                count = count + 1
            else:
                break

    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--video", help="path to video")
    a.add_argument("--imagePath", help="path to images")
    args = a.parse_args()
    extract_images(args.video, args.imagePath)
