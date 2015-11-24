import thinkstats
import math

# Suppose I grow several varieties in my garden,
# and one day I harvest three decorative pumpkins that are one pound each,
# two pie pumpkins that are three pounds each,
# and one Atlantic Giant pumpkin that weighs 591 pounds

def pumpkins():
    return [1, 1, 1, 3, 3, 591]

def calcPumpkinMean():
    return thinkstats.Mean(pumpkins())

def calcPumpkinVariance():
    return thinkstats.Var(pumpkins())

def calcPumpkinSd():
    return math.sqrt(calcPumpkinVariance())

print "Pumpkin mean: ", calcPumpkinMean()
print "Pumpkin variance: ", calcPumpkinVariance()
print "Pumpkin standard deviation: ", calcPumpkinSd()
