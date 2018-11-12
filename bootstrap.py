test =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


import random

def get_medians(dataset, sample_size, iterations):
    medians = []
    for i in range(0, iterations):
        choices = []
        for x in range(0, sample_size):
            temp = random.randint(0, len(dataset)-1)
            while (temp in choices):
                temp = random.randint(0, len(dataset)-1)
            choices.append(temp)
        sample = []
        for index in choices:
            sample.append(dataset[index])
        sample.sort()
        if (len(sample) % 2 == 0):
            middle_one = len(sample) / 2
            middle_two = middle_one - 1
            middle_one = sample[middle_one]
            middle_two = sample[middle_two]
            medians.append(float(middle_one + middle_two)/2)
        else:
            medians.append(sample[(len(sample)/2)])
    return medians

m = get_medians(test, 4, 10)
print(m)

def get_frequency_count(medians):
    counts = {}
    for each in medians:
        if each in counts:
            counts[each] += 1
        else:
            counts[each] = 1
    return counts

print(get_frequency_count(m))
