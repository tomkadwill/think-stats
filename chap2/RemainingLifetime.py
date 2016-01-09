import Pmf

# Usage:
# ages = [55, 63, 78, 64, 52, 88, 101, 11, 73]
# RemainingLifetime.RemainingLifetime(12, ages).Prob(55)
def RemainingLifetime(age, lifetimes):
    modified_lifetimes = []
    for lifetime in lifetimes:
        if lifetime > age:
            modified_lifetimes.append(lifetime)
    pmf = Pmf.MakePmfFromList(modified_lifetimes)
    pmf.Normalize()
    return pmf

# Question for Steven:

# I think this is saying: given these are the recorded ages of a population
# When I am 12 years old, what is probability of living until I am 55.
# Is that correct?

# Is this correct? Even though, when I put in the probability of living to
# an age that is not there it returns 0.


# For Tom:
# This doesn't seem right. Create a new file (keep this) and try again.
# The probability to living to 101 if you are 88 is 100%
# RemainingLifetime.RemainingLifetime(88, ages).Prob(101)
# but
# The probability of living to 55 if you are 54 is only 14%
# RemainingLifetime.RemainingLifetime(54, ages).Prob(55)
