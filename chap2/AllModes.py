import Pmf
import operator

def AllModes(hist):
    dic = {}
    for val, freq in hist.Items():
        dic[val] = freq

    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    print sorted_dic
