"""
Sort a dictionary by value.
"""
from collections import OrderedDict
import numpy as np


def sort_dict_by_value(dict1: dict) -> dict:
    print(dict1)

    # First method to solve
    keys = list(dict1.keys())
    values = list(dict1.values())
    sorted_values = sorted(values)
    print(sorted_values)
    # sorted_value_index = np.argsort(values)
    sorted_value_index = []
    for i in range(0, len(sorted_values)):
        sorted_value_index.append(values.index(sorted_values[i]))

    print(sorted_value_index)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    print(sorted_dict)


if __name__ == "__main__":
    d1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
    sort_dict_by_value(d1)
