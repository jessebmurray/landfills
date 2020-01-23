import matplotlib
import matplotlib.pyplot as plt
from PIL import Image


types = ['paper', '  food', 'yard trimmings', 'wood', 'steel', 'rubber and leather', 'textiles', 'aluminum', 'plastic',
         'glass']

years = [1960, 1970, 1980, 1990, 2000, 2005, 2010, 2015, 2016, 2017]
years1 = list(range(1960, 2020, 5)) + [2016, 2017]

amounts = [[24910, 37390, 42560, 43570, 40450, 35080, 22000, 18280, 17660, 18350],
           [12200, 12750, 12740, 19800, 24200, 26370, 28620, 30250, 30680, 30630],
           [20000, 23110, 26950, 25560, 11900, 9990, 11690, 10800, 9640, 8650],
           [3030, 3710, 6860, 10000, 9910, 10690, 11120, 11070, 12250, 12140],
           [10250, 12150, 12000, 8720, 7860, 8550, 9310, 9970, 10310, 10430],
           [1510, 2710, 4000, 4590, 3880, 4130, 4400, 4490, 4790, 4950],
           [1710, 1970, 2320, 4270, 6280, 7570, 8900, 10540, 11130, 11150],
           [340, 790, 1390, 1500, 1940, 2230, 2390, 2490, 2640, 2650],
           [390, 2900, 6670, 13780, 19950, 23270, 24370, 26030, 26290, 26820],
           [6620, 12520, 14080, 8660, 8100, 8290, 7030, 6840, 6880, 6870]]
total_amounts = [73.4456976, 99.79035, 117.54396045, 127.41413325000002, 121.98916695, 123.53138145000001, 117.77982855000002, 118.62351059999999, 119.99335995000001, 120.32901840000001]

per_capita = [2.68, 2.96, 3.25, 3.25, 3.66, 3.83, 4.57, 4.52, 4.74, 4.69, 4.45, 4.48, 4.53, 4.51]

graphs_location = '/Users/jessemurray/Documents is here/Documents/Odd Projects/Landfill Volume/Graphs/'


for i in range(len(per_capita)):
    per_capita[i] = per_capita[i] * 0.453592 * 365 * 0.001

print(len(per_capita))
print(len(years1))

tick_size = 14
label_size = 15
legend_size = 14

# PLOTTING PER CAPITA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt.style.use('seaborn')

# plt.tick_params(labelsize=tick_size)
# plt.xlabel('Year', fontsize=label_size)
plt.xlabel('Year')

# plt.ylabel('Metric Tons/Person/Year', fontsize=label_size)
plt.ylabel('Metric Tons/Person/Year')


plt.plot(years1, per_capita, linestyle='--', marker='o', label='Per Capita MSW Generation')
# plt.legend(fontsize=legend_size)
plt.legend()

file_location0 = graphs_location + 'epa_per_capita1.png'

plt.savefig(file_location0, dpi=300)


# PLOTTING TOTAL AMOUNTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# plt.style.use('seaborn')
# # plt.style.use('seaborn-talk')
#
#
# # plt.tick_params(labelsize=tick_size)
# # plt.xlabel('Year', fontsize=label_size)
# plt.xlabel('Year')
# # plt.ylabel('Million Metric Tons', fontsize=label_size)
# plt.ylabel('Million Metric Tons')
#
# # plt.xlabel('Year')
# # plt.ylabel('Million Metric Tons')
#
# plt.plot(years, total_amounts, linestyle='--', marker='o', label='Total MSW Landfilled')
# plt.legend()
# # plt.legend(fontsize=legend_size)
#
# file_location0 = graphs_location + 'epa_previous_data.png'
#
# plt.show()
# # plt.savefig(file_location0, dpi=300)
#







# in_image = Image.open(file_location0)
# n = 0.2
# width, height = in_image.size
# out_image = in_image.resize((int(width * n), int(height * n)))
# out_image.save(file_location0)
# print(width * n)
# print(height * n)

# plt.show()




def main():
    extended_amounts = generate_new_amount_list(amounts)
    converted_extended_amounts = convert_extended_amounts(extended_amounts)
    print(converted_extended_amounts)
    print(converted_extended_amounts[-1][-1])
    print(len(converted_extended_amounts[0]))


def convert_extended_amounts(extended_amounts):
    converted_extended_amounts = []
    for amount_list in extended_amounts:
        converted_amount_list = []
        for value in amount_list:
            # convert from thousands of tons to millions of tons
            # then convert to millions of metric tons
            new_value = value * 0.001 * 0.907185
            converted_amount_list.append(new_value)
        converted_extended_amounts.append(converted_amount_list)
    return converted_extended_amounts















def generate_new_amount_list(all_amount_list):
    new_amount_list = []
    for amount_list in amounts:
        new_amount_list.append(generate_new_amounts(years, amount_list))
    return new_amount_list


def new_amount_index(year_list, amount_list, index):
    year_difference = year_list[index] - year_list[index - 1]
    this_years_amount = amount_list[index]
    previous_years_amount = amount_list[index - 1]
    increment = (this_years_amount - previous_years_amount) / year_difference
    return [previous_years_amount + (increment * y) for y in range(year_difference)]


def generate_new_amounts(year_list, amount_list):
    new_amounts = []
    for index in range(1, len(years)):
        new_amounts += new_amount_index(year_list, amount_list, index)
    new_amounts += [amount_list[-1]]
    return new_amounts


# main()


# total_amounts = [0] * len(amounts[0])
#
# for year_list in amounts:
#     for year_num in range(len(year_list)):
#         total_amounts[year_num] += year_list[year_num]
#
# for total_year_num in range(len(total_amounts)):
#     total_amounts[total_year_num] = total_amounts[total_year_num] * 0.001 * 0.907185
