import numpy as np
from scipy.signal import find_peaks


def detect_r_peaks(signal: np.ndarray, distance: int = 150, height: float = None) -> np.ndarray:
    """
    Detect R peaks in an ECG signal.

    Parameters
    ----------
    signal : np.array
        ECG signal
    distance : int
        Minimum distance between peaks
    height : float
        Minimum peak height

    Returns
    -------
    peaks : np.array
        Indices of detected peaks
    """
    peaks, _ = find_peaks(signal, distance=distance, height=height)
    return peaks


def moving_average(signal: np.ndarray, window_size: int = 5) -> np.ndarray:
    """
    Apply simple noise filtering using moving average.

    Parameters
    ----------
    signal : np.array
        ECG signal
    window_size : int
        Size of smoothing window

    Returns
    -------
    filtered : np.array
        Smoothed signal
    """
        
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')