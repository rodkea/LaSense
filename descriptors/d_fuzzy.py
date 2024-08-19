import cv2
import numpy as np
from .utils import yuv420_to_grayscale
from time import sleep

def d_fuzzy(path: str, width: int, height: int):
    with open(path, 'rb') as f:
        frame_size = width * height + 2 * (width // 2) * (height // 2)
        while True:
            yuv_frame = np.fromfile(f, dtype=np.uint8, count=frame_size)
            if yuv_frame.size < frame_size:
                break
            yuv_frame = yuv_frame.reshape((height + height // 2, width))
            gray_frame = yuv420_to_grayscale(yuv_frame, width, height)
            cv2.imshow('GrayScale', gray_frame)
            print("A")
            sleep(0.5   )
    
    cv2.destroyAllWindows()