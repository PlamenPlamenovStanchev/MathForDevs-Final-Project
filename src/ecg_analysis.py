import numpy as np
from scipy.signal import find_peaks


def detect_r_peaks(signal, distance=150, height=None):
    """
    Detect R-peaks in an ECG signal.

    Parameters
    ----------
    signal : numpy array
        ECG signal
    distance : int
        Minimum distance between peaks
    height : float
        Minimum peak height

    Returns
    -------
    peaks : array
        Indices of detected peaks
    """

    peaks, _ = find_peaks(signal, distance=distance, height=height)

    return peaks