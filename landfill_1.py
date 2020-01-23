
"""


paper takes six weeks to decompose

"""

types = ['paper', 'glass', 'steel', 'aluminum', 'plastic', 'rubber and leather', 'textiles', 'wood', 'food',
         'yard trimmings']


millions_of_tons = [18.35, 6.87, 10.43, 2.65, 26.82, 4.95, 11.15, 12.14, 30.63, 8.65]

added_amounts = []
for element in millions_of_tons:
    added_amounts.append(element * 0.907185)

print(added_amounts)
print(len(added_amounts))
# added_amounts = [16.646844750000003, 6.23236095, 9.46193955, 2.40404025, 24.330701700000002, 4.49056575, 10.11511275,
# 11.0132259, 27.78707655, 7.84715025]



# sum = 0
# for element in millions_of_tons:
#     sum += element
# print(sum)
# print(sum / 139.59)
