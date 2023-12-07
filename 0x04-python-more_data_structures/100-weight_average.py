#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1 = 0
    sum2 = 0
    frequency_sum = 0

    if my_list:
        for i in my_list:
            weight, frequency = i
            sum1 += weight * frequency
            sum2 += frequency
            frequency_sum += frequency

        result = sum1 / sum2 if sum2 != 0 else 0
        return result

    else:
        return 0
