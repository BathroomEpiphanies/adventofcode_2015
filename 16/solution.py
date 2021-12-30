import sys


sues = {
    name:{k:int(v) for k,v in [d.split(': ') for d in data.split(', ')]}
    for name,data in [line.strip().split(': ',1) for line in sys.stdin.readlines()]
}


MFCSAM = {
    "children":    lambda x: x==3,
    "cats":        lambda x: x==7,
    "samoyeds":    lambda x: x==2,
    "pomeranians": lambda x: x==3,
    "akitas":      lambda x: x==0,
    "vizslas":     lambda x: x==0,
    "goldfish":    lambda x: x==5,
    "trees":       lambda x: x==3,
    "cars":        lambda x: x==2,
    "perfumes":    lambda x: x==1,
}
for name,data in sues.items():
    if all(MFCSAM[k](v) for k,v in data.items()):
        print('*1:',name.split(' ')[1])


MFCSAM.update({
    "cats":        lambda x: x>7,
    "trees":       lambda x: x>3,
    "pomeranians": lambda x: x<3,
    "goldfish":    lambda x: x<5,
})
for name,data in sues.items():
    if all(MFCSAM[k](v) for k,v in data.items()):
        print('*2:',name.split(' ')[1])

