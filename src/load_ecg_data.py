import mne
import numpy as np


def load_ecg_signal(file_path):
    """
    Loads ECG signal from EDF file.

    Parameters
    ----------
    file_path : str
        Path to EDF file

    Returns
    -------
    signal : numpy array
        ECG signal values
    """

    raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
    
    signal = raw.get_data()[0]

    return signal