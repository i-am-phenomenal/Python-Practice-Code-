
def break_in_pairs(sliced):
    global pairs
    if len(sliced) > 2:
        first_element = sliced.pop(0)
        second_element = sliced.pop(0)
        pair = [first_element, second_element]
        pairs += [pair]
        break_in_pairs(sliced)

    else:
        pairs += [sliced]


def is_symmetric(elements):
    output = True
    for iter in range(0, len(elements), 2):
        if elements[iter] == elements[iter + 1][:: -1]:
            pass

        else:
            output = False
            return output

    return output


def check_pairs():
    global pairs
    first_half = pairs[0: int(len(pairs) / 2)]
    second_half = pairs[int(len(pairs) / 2): len(pairs)]
    last = first_half.pop(len(first_half) - 1)
    first = second_half.pop(0)
    return (is_symmetric(first_half)) and (is_symmetric(second_half)) and (last == first[:: -1])


def check_if_symmetric(sliced):
    global pairs
    break_in_pairs(sliced)
    if check_pairs():
        return True
    else:
        return False


# tree_array = ["1", "2", "2", "3", "#", "#",
#               "3", "2", "3", "3", "2", "4", "5", "5", "4", "2", "1", "1", "1", "1", "1", "1", "1"]
tree_array = ["10", "2", "2", "#", "1", "1", "#"]
pairs = []
tree_array.pop(0)
if tree_array[0] == tree_array[1]:
    if check_if_symmetric(tree_array[2:]):
        print("TREE IS SYMMETRIC  ")
    else:
        print("NOT SYMMETRIC")
