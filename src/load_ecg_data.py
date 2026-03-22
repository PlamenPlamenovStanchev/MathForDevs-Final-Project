import mne


def load_ecg_signal(file_path):
    """
    Load ECG signal from an EDF file using the MNE library.
    This function reads the raw EDF file, preloads the data into memory,
    and extracts the first channel's data array representing the ECG signal.

    Parameters
    ----------
    file_path : str
        Path to the EDF file

    Returns
    -------
    signal : np.ndarray
        A 1D array containing the ECG signal values from the first channel.
    """
    raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
    signal = raw.get_data()[0]
    return signal