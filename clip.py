# -*- coding: utf-8 -*-
import cv2
import sys
import os


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python extract_result.py ~/path/to/play.mp4')
        exit(1)

    video_name = sys.argv[1]
    video = cv2.VideoCapture(video_name)
    dir_name = sys.argv[1].split('.')[-2]
    os.mkdir(dir_name)

    video_cursor = 0

    # Set an initial value just to start first cycle of the while loop
    end_flag = True
    number = 0

    while end_flag is True:
        video_cursor += 1
        end_flag, frame = video.read()

        cv2.imwrite(
                f'{dir_name}/{number}.jpg',
                frame)
        number += 1

    video.release()
