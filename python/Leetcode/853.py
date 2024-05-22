""" car fleet problem """
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

pairs = [[p,s] for p,s in zip(position, speed)]


newparsort = sorted(pairs)[::-1]
print(newparsort)

stackval = []
for p,s in sorted(pairs)[::-1]:
    speedval = (target - p) / s
    stackval.append(speedval)

    if len(stackval) >=2 and stackval[-1] <= stackval[-2]:
        stackval.pop()    

print(len(stackval))
