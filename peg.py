h = {2,3,4,9,10,11,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,44,45,46}
x, c = input()+input()+input()+input()+input()+input()+input(), 0
for a in range(49):
    if a in h and x[a] == '.':
        d, m = divmod(a, 7)
        if m > 1 and x[a-1] == 'o' and x[a-2] == 'o': c += 1
        if m < 5 and x[a+1] == 'o' and x[a+2] == 'o': c += 1
        if d > 1 and x[a-7] == 'o' and x[a-14] == 'o': c += 1
        if d < 5 and x[a+7] == 'o' and x[a+14] == 'o': c += 1
print(c)