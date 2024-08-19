from numpy import ndarray

def yuv420_to_grayscale(yuv_frame : ndarray, width: int, height:int) -> ndarray:
    """
    Extracts de Y (luminance) componente from a YUV420 frame and returns it as a gray scale image.

    Args:
        yuv_frame (np.ndarray): The YUV420 frame as a NumPy Array.
        width (int): The width of the frame.
        height (int): The height of the frame.

    Return:
        np.array: The grayscale image extracted from the Y component.
    """
    y = yuv_frame[:height, :width]
    return y

