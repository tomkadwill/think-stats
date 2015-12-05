import Pmf

def RemainingLifetime(age, lifetimes):
    modified_lifetimes = []
    for lifetime in lifetimes:
        if lifetime > age:
            modified_lifetimes.append(lifetime)
    pmf = Pmf.MakePmfFromList(modified_lifetimes)
    pmf.Normalize()
    return pmf
