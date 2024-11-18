import numpy as np


def run_averages(file_input='brain_sample.csv', file_output='brain_average.csv'):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes.
    The rows are intersections of the sagittal/horizontal planes.

    The result is the average for each sagittal/horizontal plane (rows).
    Parameters
    ----------
    file_input (str): 
        The file path for the input data, the collected sample.
    file_output (str):
        The file path for the output data, the calculated average.
    Returns
    -------
    file
        saves the output data to the file path provided in the file_output parameter.
    Example
    -------
    >>>run_averages(file_input, file_output)
    """
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')

    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    averages = planes.mean(axis=1)[np.newaxis, :]

    # write it out on my file
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')


