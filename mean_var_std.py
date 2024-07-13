import numpy as np # type: ignore

def calculate(list):
    """
    The function receives a list of 9 digits. numpy should create a 3x3 matrix and calculate the mean,
    variance, standard deviation, max, min and sum.
    The function returns a dictionary with the values as normal Python lists.
    If the input list has less than 9 elements, the function should raise a ValueError.
    """
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array([list[:3], list[3:6], list[6:]])
    mean_lst = [np.mean(matrix, 0).tolist(), np.mean(matrix, 1).tolist(), np.mean(matrix)]
    var_lst = [np.var(matrix, 0).tolist(), np.var(matrix, 1).tolist(), np.var(matrix)]
    std_lst = [np.std(matrix, 0).tolist(), np.std(matrix, 1).tolist(), np.std(matrix)]
    max_lst = [np.max(matrix, 0).tolist(), np.max(matrix, 1).tolist(), np.max(matrix)]
    min_lst = [np.min(matrix, 0).tolist(), np.min(matrix, 1).tolist(), np.min(matrix)]
    # apparently there are two ways to sum over matrix elements, but matrix.sum(index) returns a matrix
    sum_lst = [np.add.reduce(matrix, 0).tolist(), np.add.reduce(matrix, 1).tolist(), matrix.sum()]

    calculations = {
        'mean': mean_lst,
        'variance': var_lst,
        'standard deviation': std_lst,
        'max': max_lst,
        'min': min_lst,
        'sum': sum_lst
    }

    return calculations