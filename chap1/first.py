from __future__ import division
import survey

table = survey.Pregnancies()
table.ReadRecords()

first_live = other_live = 0
for pregnancies in table.records:
    if pregnancies.outcome == 1:
        if pregnancies.birthord == 1:
            first_live += 1
        else:
            other_live += 1

print 'Total number of live births', first_live + other_live
print 'Number of live births for first babies: ', first_live
print 'Number of live births for other: ', other_live

first_total = other_total = first_count = other_count = 0
for pregnancies in table.records:
    if pregnancies.birthord == 1:
        first_count += pregnancies.prglength
        first_total += 1
    elif pregnancies.birthord == 'NA':
        0
    else:
        other_count += pregnancies.prglength
        other_total += 1

print 'Average pregnancy length for first babies: ', first_count / first_total
print 'Average pregnancy length for other: ', other_count / other_total
