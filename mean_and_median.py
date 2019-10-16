mean_and_median = [{'difference' : 0, 'value': []}]

def powerset(dummy_list):
    global subsets
    if len(dummy_list) <= 1:
        yield dummy_list
        yield []
    else:
        for iter in powerset(dummy_list[1:]):
            yield [dummy_list[0]] + iter
            yield iter

def is_length_even(current_subset):
    return (len(current_subset) % 2) == 0

def calculate_median(current_subset):
    # current_subset = current_subset.sort()
    median = 0
    if is_length_even(current_subset):
        first_median = current_subset[int(len(current_subset) / 2)]
        second_median = current_subset[int((len(current_subset) / 2) - 1)]
        median = (first_median + second_median ) / 2
    else:
        median = current_subset[int(len(current_subset) / 2) ]

    return median

def calculate_mean(current_subset):
    mean = 0
    for iterator in current_subset:
        mean += iterator
    mean = mean / len(current_subset)
    return mean

list = [1, 2, 3, 4]
filtered_subsets = []
for element in [x for x in powerset(list)]:
    if len(element) <= 2:
        pass
    else:
        filtered_subsets.append(element)

for element in filtered_subsets:
    mean_median_difference = (calculate_mean(element)) - (calculate_median(element))
    mean_and_median.append({'difference': mean_median_difference, 'value': element})

maximum = mean_and_median[0]

for iter in range(0, len(mean_and_median)):
        if mean_and_median[iter]['difference'] > maximum['difference']:
            maximum = mean_and_median[iter]
        else:
            pass

print(maximum['value'])
