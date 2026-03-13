import pyedflib
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

    f = pyedflib.EdfReader(file_path)

    signal = f.readSignal(0)

    f.close()

    return signal