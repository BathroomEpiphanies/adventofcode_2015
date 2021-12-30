import sys
import json
from collections.abc import Hashable

jsaf = json.loads(sys.stdin.readlines()[0].strip())

#def sum_all_except(jsaf, filtered):
#    try:
#        if isinstance(jsaf,Hashable) and jsaf in filtered:
#            raise
#        elif isinstance(jsaf,int):
#            return jsaf
#        elif isinstance(jsaf,list):
#            return sum(sum_all_except(l,filtered) for l in jsaf)
#        elif isinstance(jsaf,dict):
#            return sum(sum_all_except(v,filtered) for k,v in jsaf.items())
#    except:
#        return 0

def sum_all_except(jsaf, filtered):
    #print(jsaf)
    if isinstance(jsaf,Hashable) and jsaf in filtered:
        return 0
    elif isinstance(jsaf,int):
        return jsaf
    elif isinstance(jsaf,list):
        return sum(sum_all_except(l,filtered) for l in jsaf)
    elif isinstance(jsaf,dict) and not any(val in filtered for val in jsaf.values() if isinstance(val,Hashable)):
        return sum(sum_all_except(v,filtered) for k,v in jsaf.items())
    return 0

print('*1:',sum_all_except(jsaf,set()))
print('*2:',sum_all_except(jsaf,set(['red'])))
