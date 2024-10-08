import cv2
from numpy import ndarray, sum, percentile, zeros, zeros_like, uint8, uint64, logical_and, where
from typing import Tuple
import time

def d_fuzzy(path: str, width: int, height: int):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise IOError(f"Failed to open the video file: {path}") 
    frame_count = 0
    ret, frame = cap.read()
    start_time = time.time()
    if ret:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        start_time_2 = time.time()
        mu_dark, mu_medium, mu_light = calc_bands(frame_gray)
        end_time = time.time()
        execution_time = end_time - start_time_2
        N = 1        
        mu_prev = calc_mu_k2(frame_gray, mu_dark, mu_medium, mu_light)
        seq = zeros_like(mu_prev[0], dtype=uint64)
        
    else:
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break   
        N += 1
        frame_count += 1
        frame_gray : ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mu_curr = calc_mu_k(frame_gray, mu_dark, mu_medium, mu_light)
        seq += calc_seq(mu_prev, mu_curr)
        mu_prev = mu_curr
    qt = seq / N
    return qt        
  
def calc_bands(frame: ndarray) -> tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    
    mu_medium_min, mu_dark_max, mu_light_min, mu_medium_max = percentile(frame, [20,40,60,80],method='nearest')
    return (0, int(mu_dark_max)), (int(mu_medium_min), int(mu_medium_max)), (int(mu_light_min), 255)      

def calc_mu_k(frame: ndarray, mu_dark: Tuple[int, int], mu_medium: Tuple[int, int], mu_light: Tuple[int, int])  -> ndarray:
    
    mu_k = zeros((3, frame.shape[0], frame.shape[1]), dtype=uint8)
    mu_k[0] = logical_and(frame >= mu_dark[0], frame <= mu_dark[1]).astype(uint8)
    mu_k[1] = logical_and(frame >= mu_medium[0], frame <= mu_medium[1]).astype(uint8)
    mu_k[2] = logical_and(frame >= mu_light[0], frame <= mu_light[1]).astype(uint8)
    return mu_k

def calc_mu_k2(frame: ndarray, mu_dark: Tuple[int, int], mu_medium: Tuple[int, int], mu_light: Tuple[int, int])  -> ndarray:
    
    mu_k = zeros((3, frame.shape[0], frame.shape[1]), dtype=uint8)
    mu_k[0] = where((frame >= mu_dark[0]) & (frame <= mu_dark[1]), 1, 0)
    mu_k[1] = where((frame >= mu_medium[0]) & (frame <= mu_medium[1]), 1, 0)
    mu_k[2] = where((frame >= mu_light[0]) & (frame <= mu_light[1]), 1, 0)
    
    return mu_k

def calc_seq(mu_prev: ndarray, mu_curr: ndarray) -> ndarray:
  
  seq : ndarray = (mu_prev[:] == 1) & (mu_curr[:] == 0)
  return sum(seq.astype(uint64), axis=0)