import numpy as np
from matplotlib import pyplot as plt
from functools import lru_cache

# Use 5% value

types = ['paper', 'food', 'yard trimmings', 'wood', 'steel', 'rubber and leather', 'textiles', 'aluminum', 'plastic',
          'glass']
decomp_times = [20, 0.1667,           5,     739.6,    200,                   80,        40,        200,      1000,
                 1000000]
added_amounts = [16.6468, 27.787,     7.8471, 11.0132, 9.4619,               4.4905,    10.1151,     2.4040,   24.3307,
                  6.2323]
densities = [0.520897, 0.4786257, 0.379697,   0.75, 4.15955888,             1.005, 0.400462, 1.4612392,     0.2754938,
             2.72]
# added_is_const = ['y', 'y',              'y',    'y',     'y',                  'y',         'y', 'y', 'y', 'y']
# CHANGE ADDED IS CONSTANT TO 'n' BY UNCOMMENTING THIS
added_is_const = ['n'] * 10
R_ = 0.05
R_EPSI = 0.001
#
# # NOT USED IN MAIN
historical_amounts = [[22.59797835, 23.73014523, 24.862312109999998, 25.99447899, 27.12664587, 28.258812750000004, 29.390979630000004, 30.52314651, 31.65531339, 32.78748027, 33.91964715, 34.388661795000004, 34.85767644, 35.326691085, 35.79570573, 36.264720375, 36.73373502, 37.202749665, 37.67176431, 38.140778955, 38.6097936, 38.701419285, 38.793044970000004, 38.884670655, 38.97629634, 39.067922025, 39.159547710000005, 39.251173395, 39.342799080000006, 39.434424765, 39.52605045, 39.24300873000001, 38.95996701, 38.67692529, 38.39388357, 38.11084185, 37.82780013, 37.54475841, 37.26171669, 36.97867497, 36.69563325, 35.72131656, 34.74699987, 33.77268318, 32.79836649000001, 31.824049799999997, 29.45085384, 27.07765788, 24.70446192, 22.33126596, 19.95807, 19.283124360000002, 18.60817872, 17.93323308, 17.25828744, 16.583341800000003, 16.0208871, 16.646844750000003], [11.067657, 11.117552175, 11.167447350000002, 11.217342525000001, 11.2672377, 11.317132875, 11.367028050000002, 11.416923225000001, 11.466818400000001, 11.516713575, 11.56660875, 11.565701565000001, 11.56479438, 11.563887195, 11.56298001, 11.562072825000001, 11.56116564, 11.560258455000001, 11.55935127, 11.558444085, 11.5575369, 12.19800951, 12.838482120000002, 13.478954730000002, 14.11942734, 14.75989995, 15.40037256, 16.04084517, 16.68131778, 17.32179039, 17.962263, 18.3614244, 18.7605858, 19.1597472, 19.5589086, 19.95807, 20.3572314, 20.7563928, 21.1555542, 21.5547156, 21.953877, 22.34759529, 22.741313580000003, 23.13503187, 23.52875016, 23.92246845, 24.330701700000002, 24.73893495, 25.1471682, 25.55540145, 25.9636347, 26.25937701, 26.555119320000003, 26.85086163, 27.14660394, 27.44234625, 27.8324358, 27.78707655], [18.1437, 18.425834535, 18.70796907, 18.990103605, 19.27223814, 19.554372675, 19.83650721, 20.118641745, 20.40077628, 20.682910815, 20.96504535, 21.31340439, 21.66176343, 22.010122470000002, 22.35848151, 22.706840550000003, 23.05519959, 23.403558630000003, 23.75191767, 24.10027671, 24.44863575, 24.322537035, 24.196438320000002, 24.070339605, 23.944240890000003, 23.818142175, 23.69204346, 23.565944745, 23.43984603, 23.313747315, 23.187648600000003, 21.94843389, 20.70921918, 19.47000447, 18.23078976, 16.99157505, 15.752360340000001, 14.513145630000002, 13.27393092, 12.034716210000001, 10.7955015, 10.44895683, 10.102412160000002, 9.75586749, 9.40932282, 9.06277815, 9.37122105, 9.67966395, 9.98810685, 10.29654975, 10.60499265, 10.44351372, 10.282034789999999, 10.120555860000001, 9.95907693, 9.797598, 8.7452634, 7.84715025], [2.74877055, 2.81045913, 2.87214771, 2.93383629, 2.99552487, 3.0572134500000003, 3.11890203, 3.1805906100000003, 3.2422791900000005, 3.30396777, 3.36565635, 3.6514196250000004, 3.9371829, 4.222946175000001, 4.50870945, 4.794472725, 5.080236, 5.365999275, 5.651762550000001, 5.937525825, 6.223289100000001, 6.5081451900000005, 6.79300128, 7.07785737, 7.36271346, 7.64756955, 7.93242564, 8.21728173, 8.50213782, 8.78699391, 9.07185, 9.063685335, 9.055520670000002, 9.047356005000001, 9.03919134, 9.031026675, 9.02286201, 9.014697345, 9.006532680000001, 8.998368015, 8.99020335, 9.131724210000002, 9.27324507, 9.41476593, 9.556286790000001, 9.69780765, 9.77582556, 9.853843470000001, 9.93186138, 10.00987929, 10.0878972, 10.078825349999999, 10.0697535, 10.06068165, 10.0516098, 10.04253795, 11.11301625, 11.0132259], [9.298646250000001, 9.4710114, 9.643376550000001, 9.8157417, 9.98810685, 10.160472, 10.332837150000001, 10.5052023, 10.67756745, 10.8499326, 11.02229775, 11.008689975, 10.9950822, 10.981474425, 10.96786665, 10.954258875, 10.9406511, 10.927043325, 10.91343555, 10.899827775, 10.88622, 10.58866332, 10.291106639999999, 9.993549960000001, 9.695993280000001, 9.3984366, 9.10087992, 8.803323240000001, 8.50576656, 8.20820988, 7.9106532000000005, 7.832635290000001, 7.75461738, 7.67659947, 7.5985815599999995, 7.520563650000001, 7.442545740000001, 7.36452783, 7.28650992, 7.20849201, 7.130474100000001, 7.25566563, 7.3808571600000015, 7.506048690000001, 7.6312402200000005, 7.756431750000001, 7.89432387, 8.032215990000001, 8.170108110000001, 8.30800023, 8.445892350000001, 8.56564077, 8.68538919, 8.80513761, 8.924886030000001, 9.04463445, 9.353077350000001, 9.46193955], [1.36984935, 1.47871155, 1.58757375, 1.6964359500000001, 1.80529815, 1.91416035, 2.02302255, 2.13188475, 2.24074695, 2.34960915, 2.45847135, 2.575498215, 2.6925250800000002, 2.809551945, 2.92657881, 3.0436056750000002, 3.16063254, 3.277659405, 3.3946862700000002, 3.511713135, 3.62874, 3.682263915, 3.7357878300000005, 3.7893117450000005, 3.84283566, 3.896359575, 3.9498834900000004, 4.003407405, 4.05693132, 4.110455235, 4.16397915, 4.099569015, 4.03515888, 3.970748745, 3.90633861, 3.8419284750000005, 3.77751834, 3.713108205, 3.6486980700000005, 3.5842879350000003, 3.5198778, 3.5652370500000004, 3.6105963, 3.6559555500000003, 3.7013148, 3.74667405, 3.7956620400000003, 3.8446500300000004, 3.89363802, 3.94262601, 3.991614, 4.00794333, 4.02427266, 4.04060199, 4.05693132, 4.07326065, 4.34541615, 4.49056575], [1.55128635, 1.57487316, 1.59845997, 1.62204678, 1.64563359, 1.6692204000000002, 1.6928072100000002, 1.71639402, 1.7399808300000001, 1.76356764, 1.78715445, 1.818905925, 1.8506574, 1.882408875, 1.91416035, 1.945911825, 1.9776633000000001, 2.0094147749999998, 2.04116625, 2.0729177250000004, 2.1046692, 2.281570275, 2.45847135, 2.6353724250000004, 2.8122735000000003, 2.989174575, 3.1660756500000002, 3.342976725, 3.5198778, 3.696778875, 3.8736799500000005, 4.056024135, 4.23836832, 4.420712505, 4.60305669, 4.7854008750000006, 4.96774506, 5.150089245, 5.33243343, 5.514777615, 5.697121800000001, 5.93117553, 6.16522926, 6.399282990000001, 6.63333672, 6.86739045, 7.10870166, 7.3500128700000005, 7.591324080000001, 7.832635290000001, 8.0739465, 8.37150318, 8.66905986, 8.96661654, 9.26417322, 9.561729900000001, 10.09696905, 10.11511275], [0.3084429, 0.34926622500000004, 0.39008955, 0.43091287500000003, 0.47173620000000005, 0.512559525, 0.55338285, 0.5942061750000001, 0.6350295, 0.675852825, 0.7166761500000001, 0.77110725, 0.8255383500000001, 0.87996945, 0.93440055, 0.9888316500000001, 1.0432627500000002, 1.09769385, 1.1521249500000001, 1.20655605, 1.26098715, 1.270966185, 1.28094522, 1.290924255, 1.30090329, 1.3108823250000001, 1.32086136, 1.330840395, 1.34081943, 1.3507984650000002, 1.3607775, 1.40069364, 1.4406097800000002, 1.48052592, 1.52044206, 1.5603582, 1.6002743400000001, 1.64019048, 1.68010662, 1.7200227600000002, 1.7599389, 1.81255563, 1.86517236, 1.9177890899999999, 1.97040582, 2.02302255, 2.05205247, 2.08108239, 2.1101123100000003, 2.13914223, 2.16817215, 2.18631585, 2.20445955, 2.22260325, 2.24074695, 2.25889065, 2.3949684, 2.40404025], [0.35380215000000004, 0.581505585, 0.8092090200000001, 1.036912455, 1.2646158900000002, 1.492319325, 1.7200227600000002, 1.9477261950000002, 2.17542963, 2.403133065, 2.6308365, 2.9728452450000002, 3.31485399, 3.656862735, 3.9988714800000005, 4.340880225, 4.68288897, 5.024897715, 5.36690646, 5.708915205, 6.0509239500000005, 6.695932485, 7.340941020000001, 7.985949555000001, 8.63095809, 9.275966625, 9.92097516, 10.565983695, 11.21099223, 11.856000765000001, 12.501009300000002, 13.060742445, 13.620475590000002, 14.180208735, 14.739941880000002, 15.299675025000003, 15.85940817, 16.419141315, 16.97887446, 17.538607605000003, 18.09834075, 18.70071159, 19.30308243, 19.90545327, 20.50782411, 21.11019495, 21.309775650000002, 21.50935635, 21.70893705, 21.90851775, 22.10809845, 22.409283870000003, 22.71046929, 23.01165471, 23.31284013, 23.61402555, 23.84989365, 24.330701700000002], [6.0055647, 6.5408038500000005, 7.076043, 7.611282150000001, 8.1465213, 8.68176045, 9.216999600000001, 9.75223875, 10.2874779, 10.82271705, 11.3579562, 11.49947706, 11.64099792, 11.78251878, 11.92403964, 12.0655605, 12.20708136, 12.34860222, 12.49012308, 12.63164394, 12.7731648, 12.28147053, 11.78977626, 11.29808199, 10.806387720000002, 10.314693450000002, 9.82299918, 9.33130491, 8.83961064, 8.34791637, 7.8562221, 7.805419740000001, 7.75461738, 7.703815020000001, 7.65301266, 7.602210300000001, 7.55140794, 7.500605580000001, 7.44980322, 7.399000860000001, 7.3481985, 7.38267153, 7.4171445600000006, 7.451617590000001, 7.486090620000001, 7.520563650000001, 7.29195303, 7.063342410000001, 6.83473179, 6.60612117, 6.37751055, 6.34303752, 6.30856449, 6.27409146, 6.23961843, 6.2051454, 6.2414328, 6.23236095]]
# call_it_years = [0,      0,                0,      0,       0,                  100,           0, 0, 0, 0, 0]
DEPTH = 24.08  # median depth from the EPA landfill data repository

# density is measured in metric tons per cubic meter
# DENSITY = 1.068
# depth is measured in meters
# DEPTH = 32.27
# median from the EPA repository
# DENSITY = 0.5934
# current_area = 525.37
# current_mass = 10743.28
gen_pal = ['xkcd:yellow tan', 'xkcd:deep orange', 'xkcd:deep green', 'xkcd:brown', 'xkcd:slate grey', 'xkcd:navy blue',
           'xkcd:purple', 'xkcd:silver', 'xkcd:nice blue', 'xkcd:ice']
graphs_location = '/Users/jessemurray/Documents is here/Documents/Odd Projects/Landfill Volume/Graphs/'
to_save = False
special_case_for_glass = False


def main():
    """
    If you'd like to know the of mass, volume, or area, enter calculation='mass', calculation='volume', or
    calculation='area', respectively. The default calculation argument is Mass. Mass is measured in millions of metric
    tons, volume in millions of cubic meters, area in millions of square meters.
    """

    # print(make_reference_list(decomp_times[9], added_amounts[9], R_, R_EPSI, 9))
    # print(generate_curve_list(9))

    # stack_plot_all_curve_lists(start_year=1960, stop_year=2040, no_decomposition=False, calculation='mass')
    # stack_plot_all_curve_lists(start_year=1960, stop_year=2019, no_decomposition=False)
    # percent_stack_area(start_year=1960, stop_year=2040, no_decomposition=False)

    # stack_plot_all_curve_lists(stop_year=2000, no_decomposition=False)

    # stack_plot_all_curve_lists(start_year=1960, stop_year=3000, no_decomposition=True)
    # percent_stack_area(start_year=1960, stop_year=3000, no_decomposition=True)

    # plot_summed_curve(start_year=1960, stop_year=2017, no_decomposition=False)

    # DONE
    # plot_reference_list(7)
    # plot_curve_list(7, start_year=1960, stop_year=2019, save=True)

    # plot_all_curve_lists()
    # plot_all_curve_lists([9])

    # stack_plot_all_curve_lists([9])
    # percent_stack_area([9])
    # plot_all_curve_lists([9])
    # plot_summed_curve([9], calculation='mass')
    # print(len(generate_curve_list(0)) + 1960)

    # FINISHED ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # bar_chart_list(decomp_times, save=True)
    # bar_chart_list(added_amounts, save=to_save)
    # bar_chart_list(steady_state_amounts(), save=to_save)
    # bar_chart_list(steady_state_years([9], start_year=1960), [9], save=to_save)
    return True


# ADDED NOT CONSTANT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def call_function(type_num, year):
    if special_case_for_glass is True:
        if type_num == 9:
            return type_9_output_added(year)
        else:
            return general_output_added(type_num, year)
    else:
        return general_output_added(type_num, year)


def type_9_output_added(year):
    # 2200 - 1960
    if year <= 240:
        return added_amounts[9]
    else:
        added_is_const[9] = 'y'
        return 0


def general_output_added(type_num, year):
    if year <= 56:
        return historical_amounts[type_num][year]
    # when year is 57...
    else:
        added_is_const[type_num] = 'y'
        return historical_amounts[type_num][year]


# CORE FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_reference_list(decomp_time, added_amount, R, R_epsi, type_num, calculation='mass'):
    if added_amount == 0:
        return [0]

    # calculate alpha (the rate constant)
    alpha = np.log(R) / decomp_time

    # calculate T, (presumably the length of the reference list and the number of years for which the amount is not
    # 0. Because it's the time up to when we reach R_epsi
    T = np.log(R_epsi) / alpha
    reference_list = []

    density = densities[type_num]

    if calculation == 'mass':
        for year in range(int(T) + 1):
            reference_list.append(added_amount * np.exp(alpha * year))
    elif calculation == 'volume':
        for year in range(int(T) + 1):
            reference_list.append(added_amount * np.exp(alpha * year) * (1 / density))
    elif calculation == 'area':
        for year in range(int(T) + 1):
            reference_list.append(added_amount * np.exp(alpha * year) * (1 / density) * (1 / DEPTH))
    return reference_list


def generate_curve_list(type_num, calculation='mass', stop_year=None, no_decomposition=False):
    decomp_time = decomp_times[type_num]
    r = R_
    r_epsi = R_EPSI

    if added_is_const[type_num] == 'y':
        # the curve goes list goes up to and includes the steady state amount, and has a length of the decomposition
        # time. Which you should expect given that it goes up to the length of the reference list, which itself goes
        # up to R epsilon

        if no_decomposition is True:
            curve_list = []
            sum = 0
            added_amount = added_amounts[type_num]
            for year in range(stop_year):
                sum += added_amount
                curve_list.append(sum)
            return curve_list
        else:
            added_amount = added_amounts[type_num]

            reference_list = make_reference_list(decomp_time, added_amount, r, r_epsi, type_num, calculation)

            curve_list = []
            sum = 0
            for year in range(len(reference_list)):
                # go up to but don't include the stop year
                if year == stop_year:
                    break
                sum += reference_list[year]
                curve_list.append(sum)

            return curve_list

    elif added_is_const[type_num] == 'n':

        if no_decomposition is True:
            curve_list = []
            sum = 0
            for year in range(stop_year):
                if added_is_const[type_num] == 'y':
                    sum += added_amounts[type_num]
                else:
                    sum += call_function(type_num, year)
                curve_list.append(sum)
            return curve_list

        else:
            curve_list = []
            reference_list = make_reference_list(decomp_time, 1, r, r_epsi, type_num, calculation)

            at_steady_state = False
            year = 0
            while not at_steady_state:
                # honor the stop year
                if year == stop_year:
                    break

                added_amount = call_function(type_num, year)
                current_reference_list = multiply_reference_list(tuple(reference_list), added_amount)

                if added_is_const[type_num] == 'y':
                    sum = 0
                    for y in range(len(current_reference_list)):
                        sum += current_reference_list[y]
                        try:
                            curve_list[year + y] += sum
                        except IndexError:
                            curve_list.append(sum)
                    # reset the added is constant condition
                    added_is_const[type_num] = 'n'
                    at_steady_state = True

                else:
                    for y in range(len(current_reference_list)):
                        try:
                            curve_list[year + y] += current_reference_list[y]
                        except IndexError:
                            curve_list.append(current_reference_list[y])

                year += 1

            # trim the curve list to the stop year
            if stop_year is not None:
                curve_list = curve_list[:stop_year]

            return curve_list


def sum_curve_lists(type_nums_to_exclude=(), additional_time=0, calculation='mass', stop_year=None,
                    no_decomposition=False):
    # updated 1.0
    summed_curve_list = []
    steady_state_times = []
    steady_state_amounts_ = []

    # sum the curve list for all the non-excluded types up to (and including) their steady state, but no further
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            curve_list = generate_curve_list(type_num, calculation, stop_year, no_decomposition)

            steady_state_times.append(len(curve_list))
            steady_state_amounts_.append(curve_list[-1])

            for year in range(len(curve_list)):
                if len(summed_curve_list) <= year:
                    summed_curve_list.append(curve_list[year])
                else:
                    summed_curve_list[year] += curve_list[year]

    # sum the steady states up to and including the longest curve list
    steady_state_heap = 0
    for year in range(max(steady_state_times)):
        summed_curve_list[year] += steady_state_heap
        for i in range(len(steady_state_times)):
            if year + 1 == steady_state_times[i]:
                steady_state_heap += steady_state_amounts_[i]

    # add the steady state heap for additional time, if requested
    for year in range(additional_time):
        summed_curve_list.append(steady_state_heap)

    return summed_curve_list


def steady_state_amounts(type_nums_to_exclude=(), calculation='mass'):
    # noinspection PyTypeChecker
    steady_states = [[calculation, 'steady_state_amounts'], []]
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            steady_states[1].append((generate_curve_list(type_num, calculation))[-1])
        else:
            steady_states[1].append(-1)
    return steady_states


def steady_state_years(type_nums_to_exclude=(), start_year=None):
    # noinspection PyTypeChecker
    steady_states = [['na', 'steady_state_years'], []]
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            steady_states[1].append(len(generate_curve_list(type_num)))
        else:
            steady_states[1].append(-1)
    if start_year is not None:
        steady_states[1] = [year + start_year for year in steady_states[1]]
    return steady_states


def stop_year_converter(start_year, stop_year):
    if stop_year is not None:
        if start_year is None:
            return stop_year
        else:
            return stop_year - start_year
    else:
        return None


@lru_cache(maxsize=None)
def multiply_reference_list(reference_list, added_amount):
    return [value * added_amount for value in reference_list]


# PLOTTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def plot_reference_list(type_num, calculation='mass', save=False):
    y = make_reference_list(decomp_times[type_num], added_amounts[type_num], R_, R_EPSI, type_num, calculation)
    x = []
    for i in range(len(y)):
        x.append(i)

    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    # plt.style.use('seaborn-darkgrid')

    plt.plot(x, y, label=types[type_num])
    plt.xlabel('Years of Decomposition')
    if calculation == 'mass':
        plt.ylabel('Million Metric Tons')
    elif calculation == 'volume':
        plt.ylabel('Million Cubic Meters')
    elif calculation == 'area':
        plt.ylabel('Square Kilometers')
    plt.title('Amount of Non-Decomposed Landfill Material')
    plt.legend()
    # save
    if save is True:
        name = graphs_location + 'reference_list_' + types[type_num] + '.png'
        plt.savefig(name, dpi=300)
    plt.show()


def plot_curve_list(type_num, calculation='mass', start_year=None, stop_year=None, no_decomposition=False,
                    billions=True, save=False):
    curve_stop_year = stop_year_converter(start_year, stop_year)
    y = generate_curve_list(type_num, calculation, curve_stop_year, no_decomposition)

    # make the x values (the years)
    x = []
    for x_value in range(len(y)):
        x.append(x_value)

    # add the start year
    if start_year is not None:
        x = [x_value + start_year for x_value in x]

    # convert to billions
    if billions is True and calculation == 'mass':
        y = [value / 1000 for value in y]

    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    # plt.style.use('seaborn-darkgrid')

    plt.plot(x, y, label=types[type_num])
    if start_year is None:
        plt.xlabel('Years into The Future')
    else:
        plt.xlabel('Year')
    if calculation == 'mass':
        if billions is True:
            plt.ylabel('Billion Metric Tons')
        else:
            plt.ylabel('Million Metric Tons')
    elif calculation == 'volume':
        plt.ylabel('Million Cubic Meters')
    elif calculation == 'area':
        plt.ylabel('Square Kilometers')
    if no_decomposition is False:
        plt.title('The Amount of Non-Decomposed Landfill Material')
    else:
        plt.title('The Amount of Decomposed and Non-Decomposed Landfill Material')
    plt.legend()

    # save
    if save is True:
        name = graphs_location + 'plot_curve_list_' + str(start_year) + '_' + str(stop_year) + '_no_decomp_' + \
               str(no_decomposition) + '.png'
        plt.savefig(name, dpi=300)
    plt.show()


def stack_plot_all_curve_lists(type_nums_to_exclude=(), additional_time=0, calculation='mass', start_year=None,
                               stop_year=None, no_decomposition=False, billions=True, save=False):
    y_group = []
    curve_stop_year = stop_year_converter(start_year, stop_year)
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            y = generate_curve_list(type_num, calculation, curve_stop_year, no_decomposition)
            y_group.append(y)
        elif type_num in type_nums_to_exclude:
            y_group.append([])

    # find the maximum length list, call that length maximum time
    max_time = 0
    for y in y_group:
        if len(y) > max_time:
            max_time = len(y)
    # add the additional time, if requested
    max_time += additional_time

    # fill in the shorter curve lists up to that maximum time
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            while len(y_group[type_num]) != max_time:
                y_group[type_num].append(y_group[type_num][-1])

    # make the x values (the years)
    x = []
    for x_value in range(max_time):
        x.append(x_value)

    # add the start year
    if start_year is not None:
        x = [x_value + start_year for x_value in x]

    # make the labels
    labels = []
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            labels.append(types[type_num])

    # sort the palette
    total_list_b = []
    for j in range(len(y_group)):
        if y_group[j]:
            b_tuple = tuple([y_group[j], gen_pal[j]])
            total_list_b.append(b_tuple)
    total_list_b.sort(key=lambda b: b[0][-1])
    new_gen_pal = [pair[1] for pair in total_list_b]

    # sort the plots in order of last value
    y_group = [y for y in y_group if y != []]
    total_list = []
    for i in range(len(labels)):
        a_tuple = tuple([y_group[i], labels[i]])
        total_list.append(a_tuple)
    total_list.sort(key=lambda a: a[0][-1])
    y_group = []
    for i in range(len(total_list)):
        y_group.append(total_list[i][0])
    labels = []
    for i in range(len(total_list)):
        labels.append(total_list[i][1])

    # convert to billions
    if billions is True and calculation == 'mass':
        for i in range(len(y_group)):
            y_group[i] = [value / 1000 for value in y_group[i]]

    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    # plt.style.use('seaborn-darkgrid')

    # make the stackplot
    plt.stackplot(x, y_group, labels=labels, alpha=0.8, colors=new_gen_pal)
    # plt.xscale('log')

    if start_year is None:
        plt.xlabel('Years into The Future')
    else:
        plt.xlabel('Year')
    if calculation == 'mass':
        if billions is True:
            plt.ylabel('Billion Metric Tons')
        else:
            plt.ylabel('Million Metric Tons')
    elif calculation == 'volume':
        plt.ylabel('Million Cubic Meters')
    elif calculation == 'area':
        plt.ylabel('Square Kilometers')
    if no_decomposition is False:
        plt.title('The Amount of Non-Decomposed Landfill Material')
    else:
        plt.title('The Amount of Decomposed and Non-Decomposed Landfill Material')
    plt.legend(loc='upper left')
    # save
    if save is True:
        name = graphs_location + 'stack_' + str(start_year) + '_' + str(stop_year) + '_no_decomp_' + \
               str(no_decomposition) + '.png'
        plt.savefig(name, dpi=300)
    plt.show()


def percent_stack_area(type_nums_to_exclude=(), additional_time=0, calculation='mass', start_year=None,
                       stop_year=None, no_decomposition=False, save=False):
    y_group = []
    curve_stop_year = stop_year_converter(start_year, stop_year)
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            y = generate_curve_list(type_num, calculation, curve_stop_year, no_decomposition)
            y_group.append(y)
        elif type_num in type_nums_to_exclude:
            y_group.append([])

    # find the maximum length list, call that length maximum time
    max_time = 0
    for y in y_group:
        if len(y) > max_time:
            max_time = len(y)
    # add the additional time, if requested
    max_time += additional_time

    # fill in the shorter curve lists up to that maximum time
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            while len(y_group[type_num]) != max_time:
                y_group[type_num].append(y_group[type_num][-1])
    y_group = [y for y in y_group if y != []]

    # make the x values (the years)
    x = []
    for x_value in range(max_time):
        x.append(x_value)

    # add the start year
    if start_year is not None:
        x = [x_value + start_year for x_value in x]

    # make the labels
    labels = []
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            labels.append(types[type_num])

    # make the list of total amounts for every year
    total_amounts = []
    for year in range(max_time):
        total_amounts.append(0)
        for y in y_group:
            total_amounts[year] += y[year]

    for y in y_group:
        for year in range(max_time):
            y[year] /= total_amounts[year]

    # sort the palette
    total_list_b = []
    for j in range(len(y_group)):
        if y_group[j]:
            b_tuple = tuple([y_group[j], gen_pal[j]])
            total_list_b.append(b_tuple)
    total_list_b.sort(key=lambda b: b[0][-1])
    new_gen_pal = [pair[1] for pair in total_list_b]

    # sort the plots in order of steady state amount
    total_list = []
    for i in range(len(labels)):
        a_tuple = tuple([y_group[i], labels[i]])
        total_list.append(a_tuple)
    total_list.sort(key=lambda a: a[0][-1])
    y_group = []
    for i in range(len(total_list)):
        y_group.append(total_list[i][0])
    labels = []
    for i in range(len(total_list)):
        labels.append(total_list[i][1])

    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    # plt.style.use('seaborn-darkgrid')

    # make the stackplot
    plt.stackplot(x, y_group, labels=labels, alpha=0.8, colors=new_gen_pal)

    if start_year is None:
        plt.xlabel('Years into The Future')
    else:
        plt.xlabel('Year')
    if no_decomposition is False:
        plt.title('The Proportion of Non-Decomposed Landfill Material')
    else:
        plt.title('The Proportion of Decomposed and Non-Decomposed Landfill Material')
    plt.margins(0, 0)
    plt.legend(loc='upper right')
    # save
    if save is True:
        name = graphs_location + 'percent_stack_' + str(start_year) + '_' + str(stop_year) + '_no_decomp_' + \
               str(no_decomposition) + '.png'
        plt.savefig(name, dpi=300)
    plt.show()


def plot_summed_curve(type_nums_to_exclude=(), additional_time=0, calculation='mass', start_year=None,
                      stop_year=None, no_decomposition=False, billions=True, save=False):
    curve_stop_year = stop_year_converter(start_year, stop_year)
    y = sum_curve_lists(type_nums_to_exclude, additional_time, calculation, curve_stop_year, no_decomposition)

    # convert to billions
    if billions is True and calculation == 'mass':
        y = [value / 1000 for value in y]

    # make the x values (the years)
    x = []
    for x_value in range(len(y)):
        x.append(x_value)

    # add the start year
    if start_year is not None:
        x = [x_value + start_year for x_value in x]

    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    # plt.style.use('seaborn-darkgrid')

    plt.plot(x, y, label='sum of all waste types')
    if start_year is None:
        plt.xlabel('Years into The Future')
    else:
        plt.xlabel('Year')
    if calculation == 'mass':
        if billions is True:
            plt.ylabel('Billion Metric Tons')
        else:
            plt.ylabel('Million Metric Tons')
    elif calculation == 'volume':
        plt.ylabel('Million Cubic Meters')
    elif calculation == 'area':
        plt.ylabel('Square Kilometers')
    if no_decomposition is False:
        plt.title('The Amount of Non-Decomposed Landfill Material')
    else:
        plt.title('The Amount of Decomposed and Non-Decomposed Landfill Material')
    plt.legend()
    # save
    if save is True:
        name = graphs_location + 'summed_curve_' + str(start_year) + '_' + str(stop_year) + '_no_decomp_' + \
               str(no_decomposition) + '.png'
        plt.savefig(name, dpi=300)
    plt.show()


def bar_chart_list(in_list, type_nums_to_exclude=(), Sorted=False, logarithmic=True, save=False):
    # fix types to make the labels fit on the bar chart
    types[2] = 'yard\ntrimmings'
    types[5] = 'rubber\nand\nleather'

    # make the list type and calculation labels
    if in_list == added_amounts:
        list_type = 'added_amounts'
        calculation = 'na'
    elif in_list == decomp_times:
        list_type = 'decomp_times'
        calculation = 'na'
    elif in_list == densities:
        list_type = 'densities'
        calculation = 'na'
    else:
        calculation = in_list[0][0]
        list_type = in_list[0][1]
        in_list = in_list[1]

    labels = []
    for i in range(len(types)):
        if i not in type_nums_to_exclude:
            labels.append(types[i])

    y = []
    for i in range(len(in_list)):
        if i not in type_nums_to_exclude:
            y.append(in_list[i])

    total_list = []
    for i in range(len(labels)):
        a_tuple = tuple([labels[i], y[i]])
        total_list.append(a_tuple)

    if Sorted:
        total_list.sort(key=lambda x: x[1], reverse=True)

        labels = []
        for i in range(len(total_list)):
            labels.append(total_list[i][0])

        y = []
        for i in range(len(total_list)):
            y.append(total_list[i][1])

    y_pos = np.arange(len(labels))

    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    # plt.style.use('seaborn-darkgrid')

    plt.bar(y_pos, y, align='center', alpha=0.8)
    plt.xticks(y_pos, labels)

    # Display the numbers as so: 7.43 ____ 10.6 ____ 100.8 ____ 1,000
    # add data labels
    for a, b in zip(y_pos, y):
        if b < 10:
            plt.text(a, b, str(round(b, 2)), ha='center', va='bottom', size=11)
        elif b < 1000:
            plt.text(a, b, str(round(b, 1)), ha='center', va='bottom', size=11)
        else:
            if list_type == 'steady_state_years':
                if b > 1000000:
                    plt.text(a, b, f'{int(b + 0.5):,}', ha='center', va='bottom', size=11)
                else:
                    plt.text(a, b, str(int(b + 0.5)), ha='center', va='bottom', size=11)
            else:
                plt.text(a, b, f'{int(b + 0.5):,}', ha='center', va='bottom', size=11)

    # make logarithmic
    # if logarithmic is True:
    #     if in_list != added_amounts:
    #         plt.yscale('log')

    # make y_labels
    if in_list == decomp_times:
        plt.ylabel('Years')
    elif in_list == added_amounts:
        plt.ylabel('Million Metric Tons')
    elif in_list == densities:
        plt.ylabel('Metric tons / $m^3$')

    else:
        if list_type == 'steady_state_amounts':
            if calculation == 'mass':
                plt.ylabel('Million Metric Tons')
            elif calculation == 'volume':
                plt.ylabel('Million Cubic Meters')
            elif calculation == 'area':
                plt.ylabel('Square Kilometers')
        elif list_type == 'steady_state_years':
            plt.ylabel('Year')

    # make titles
    # if in_list == decomp_times:
    #     pass
    #    #  plt.title('Years to Decompose')
    # elif in_list == added_amounts:
    #     pass
    #    # plt.title('Amount of each MSW type landfilled in 2017')
    # else:
    #     if list_type == 'steady_state_amounts':
    #         plt.title('Amount of Non-Decomposed Landfill Material At Steady State')
    #     elif list_type == 'steady_state_years':
    #         plt.title('Year at Steady State')

    # save
    if save is True:
        name = graphs_location + list_type + '.png'
        plt.savefig(name, dpi=300)
    #plt.show()


# NOT USED ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def plot_all_curve_lists(type_nums_to_exclude=(), additional_time=0, calculation='mass'):
    # seriously out of date, but it's okay because I don't really like this one. Suffers from spaghetti problem.
    y_group = []

    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            y = generate_curve_list(type_num, calculation)
            y_group.append(y)
        elif type_num in type_nums_to_exclude:
            y_group.append([])

    # find the maximum length list, call that length maximum time
    max_time = 0
    for y in y_group:
        if len(y) > max_time:
            max_time = len(y)
    # add the additional time, if requested
    max_time += additional_time

    # fill in the shorter curve lists up to that maximum time
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            while len(y_group[type_num]) != max_time:
                y_group[type_num].append(y_group[type_num][-1])

    # make the x values (the years)
    x = []
    for x_value in range(max_time):
        x.append(x_value)

    # make the labels
    labels = []
    for type_num in range(len(types)):
        if type_num not in type_nums_to_exclude:
            labels.append(types[type_num])

    # sort the plots in order of steady state amount
    y_group = [y for y in y_group if y != []]
    total_list = []
    for i in range(len(labels)):
        a_tuple = tuple([y_group[i], labels[i]])
        total_list.append(a_tuple)
    total_list.sort(key=lambda a: a[0][-1])
    y_group = []
    for i in range(len(total_list)):
        y_group.append(total_list[i][0])
    labels = []
    for i in range(len(total_list)):
        labels.append(total_list[i][1])

    plt.style.use('seaborn-talk')
    plt.style.use('seaborn-darkgrid')

    # plot the curves
    for i in range(len(labels)):
        plt.plot(x, y_group[i], label=labels[i])

    plt.xlabel('Years into The Future')
    if calculation == 'mass':
        plt.ylabel('Millions of Metric Tons')
    elif calculation == 'volume':
        plt.ylabel('Millions of Cubic Meters')
    elif calculation == 'area':
        plt.ylabel('Square Kilometers')
    plt.title('A Projection into the Future of the Amount of Non-Decomposed Landfill Material')
    # plt.grid()
    plt.legend()
    plt.show()


main()
