import numpy as np
import typing as t

# R = 0.05
#
# k_constant = -1 * np.log(0.83) / 46
#
# decomposition_time = -1 * np.log(R) / k_constant
#
# print(decomposition_time)

# <739.6>


def average(in_list):
    return sum(in_list) / len(in_list)


# paper_list = [750, 1000, 700, 1100, 755, 925, 610, 755, 1000, 1200]
# print(sum(paper_list) / len(paper_list))
#
# food_list = [396, 463, 1368, 1000]
# print(average(food_list))
#
# yard_list = [250, 500, 300, 383, 640, 640]
# print(average(yard_list))

steel_list = [750, 1000, 13147.33, 13147.33]
print(average(steel_list))

rubber_leather_list = [1.2, 1.1, 0.86, 0.86]
print(average(rubber_leather_list))

textile_list = [600, 750]
print(average(textile_list))

aluminum_list = [250, 500, 4550.998, 4550.998]
print(average(aluminum_list))


def inch_to_cubic_yard(in_list):
    for i in range(len(in_list)):
        in_list[i] = (in_list[i] / (30 * 42 * 48)) * 46656
    return in_list


plastic_list_inch = [525, 630, 525, 595, 525, 700, 525, 700, 1100]
plastic_list = inch_to_cubic_yard(plastic_list_inch) + [150]
print('plastic', average(plastic_list))

glass_list = [2400, 2800, 2500, 2400, 2800, 2900, 2500, 3700, 2400, 2800]
print(average(glass_list))


densities = [520.897, 478.6257, 379.697, 750, 4159.55888, 1005, 400.462, 1461.2392, 275.4938, 2720]

densities = [value * 0.001 for value in densities]
print(densities)

added_amounts = [16.6468, 27.787,     7.8471, 11.0132, 9.4619,               4.4905,    10.1151,     2.4040,   24.3307,
                 6.2323]
densities = [0.520897, 0.4786257, 0.379697, 0.75, 4.15955888, 1.0050000000000001, 0.400462, 1.4612392, 0.2754938, 2.72]


added_sum = sum(added_amounts)
sum = 0
for i in range(10):
    sum += added_amounts[i] * densities[i]
weighted_mean_density = sum / added_sum
print(weighted_mean_density)
# 0.9000
