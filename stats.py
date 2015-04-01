#!/usr/bin/python
import pandas as pd
import math
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = [ i.split(', ') for i in data.splitlines() ]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype('float')
df['Tobacco'] = df['Tobacco'].astype('float')

print "Th mn fr Alchl nd Tbcc dtst is {0} nd {1} rspctivly".format(
    df['Alcohol'].mean(), df['Tobacco'].mean()
)
print "Th mdin fr Alchl nd Tbcc dtst is {0} nd {1} rspctivly".format(
    df['Alcohol'].median(), df['Tobacco'].median()
)
print "Th md fr Alchl nd Tbcc dtst is {0} nd {1} rspctivly".format(
    stats.mode(df['Alcohol'])[0][0], stats.mode(df['Tobacco'])[0][0]
)
print "Th rng fr Alchl nd Tbcc dtst is {0} nd {1} rspctivly".format(
    max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco'])
)
print "Th vrinc fr Alchl nd Tbcc dtst is {0} nd {1} rspctivly".format(
    df['Alcohol'].var(), df['Tobacco'].var()
)
print "Th SD fr Alchl nd Tbcc dtst is {0} nd {1} rspctivly".format(
    df['Alcohol'].std(), df['Tobacco'].std()
)

# print pd.DataFrame.__doc__
# print df

# find mean
# total_alcohol = 0
# total_tobacco = 0
# for row in data_rows:
#     total_alcohol += float(row[1])
#     total_tobacco += float(row[2])

# print 'mean alcohol = {0}'.format(total_alcohol / len(data_rows))
# print 'mean tobacco = {0}'.format(total_tobacco / len(data_rows))

# # find median
# alcohols = [ float(row[1]) for row in data_rows ]
# tobs = [ float(row[2]) for row in data_rows ]

# alcohols.sort()
# tobs.sort()

# print 'median al = {0}'.format(alcohols[len(alcohols)/2])
# print 'median al = {0}'.format(tobs[len(tobs)/2])

