def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    complex_lst = [1, [2, [3, 4], 5], 6, [[7], 8]]
    print(deep_flatten(complex_lst))