S = 100
H = S / 2
for n in range(2, 11):
    S += 2 * H
    H /= 2
print("第十次反弹的高度:",H)
print("共走过的路程:",S)
