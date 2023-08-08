from math import log10,pi,exp,floor,factorial;import sys
for line in sys.stdin:
    n=int(line.rstrip())
    print((n>1 and floor(0.5*log10(2*pi*n)+n*log10(n/exp(1))))+1)