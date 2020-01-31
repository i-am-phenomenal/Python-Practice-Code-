from itertools import permutations


def find_all_combinations(number):
    global combinations
    number_to_string = str(number)
    comb_string = ""
    for iter in range(0, len(number_to_string)):
        comb_string = comb_string + number_to_string[iter]
        for iter_1 in range(1, len(number_to_string)):
            comb_string = comb_string + number_to_string[iter_1]
            print(comb_string)
            combinations.append(comb_string)
    print(combinations)


def check_all_digits(updated_number):
    global number
    updated_to_string = str(updated_number)
    number_to_string = str(number)
    for digit in updated_to_string:
        if digit not in number_to_string:
            return False
        else:
            pass
    return True


def find_next_permutation():
    global condition_bool
    global updated_number
    while condition_bool:
        if check_all_digits(updated_number):
            print(updated_number)
            condition_bool = False
        else:
            updated_number = updated_number + 1
            pass


combinations = []
condition_bool = True
number = 1100
to_string = str(number)
combinations = [''.join(p) for p in permutations(to_string)]
for iter in range(0, len(combinations)):
    current_number = combinations[iter]
    to_integer = int(current_number)
    combinations[iter] = to_integer

combinations.sort()
for element in combinations:
    if element > number:
        print("NEXT GREATEST IS ==> ", element)
        break
    else:
        pass


# updated_number = number + 1
# find_all_combinations(number)
