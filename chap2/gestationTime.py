from __future__ import division
import survey
import thinkstats
import math

table = survey.Pregnancies()
table.ReadRecords()

first_gestation_times = []
other_gestation_times = []
for pregnancies in table.records:
    if pregnancies.birthord == 1:
        first_gestation_times.append(pregnancies.prglength)
    elif pregnancies.birthord == 'NA':
        0
    else:
        other_gestation_times.append(pregnancies.prglength)

def variance(n):
    return thinkstats.Var(n)

print 'Mean of gestation time for first babies:', thinkstats.Mean(first_gestation_times)
print 'Mean of gestation time for other babies:', thinkstats.Mean(other_gestation_times)
print 'Standard deviation of gestation time for first babies: ', math.sqrt(variance(first_gestation_times))
print 'Standard deviation of gestation time for other babies: ', math.sqrt(variance(other_gestation_times))
