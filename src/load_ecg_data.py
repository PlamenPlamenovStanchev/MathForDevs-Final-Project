import pyedflib


def load_ecg_signal(file_path):
    """
    Load ECG signal from EDF file.

    Parameters
    ----------
    file_path : str
        Path to EDF file

    Returns
    -------
    signal : np.array
        ECG signal values
    """
    f = pyedflib.EdfReader(file_path)
    signal = f.readSignal(0)
    f.close()

    return signal