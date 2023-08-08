for i in range(int(input())):
    x,c=input(),''
    if 'simon says'in x:c=x[11:]
    print(c)