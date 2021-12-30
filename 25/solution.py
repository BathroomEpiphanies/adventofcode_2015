import sys
import re


row,col = (int(n) for n in re.match(r'To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).',sys.stdin.readlines()[0]).groups())

def word(row,col):
    diagonal = (row-1)+(col-1)
    index = (diagonal+1)*diagonal//2+(col-1)
    return 20151125*pow(252533,index,33554393)%33554393

print('*1:',word(row,col))
print('*2:',None)
