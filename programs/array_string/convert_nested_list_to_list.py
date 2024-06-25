from typing import List, Optional


def return_list(num_list: List) -> List:
    result = []
    for i in range(0, len(num_list)):
        if type(num_list[i]) is list:
            result.extend(return_list(num_list[i]))
        else:
            result.append(num_list[i])
    return result


if __name__ == '__main__':
    nums = [1, 2, [3, [4], 5], 6]
    print(return_list(nums))
