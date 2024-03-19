#Goldbach difference pair is printed and graphed, Used for my new take on solving the goldbach conjecture
import numpy as np
import matplotlib.pyplot as plt
def isprime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
def gbpair(b):

    bi = int(b)
    half = int(bi / 2)
    for i in range(half,0,-1):
        if isprime(i):
            j = bi-i
            if isprime(j):return j
lim= input("till what to list:" )
limint =int(lim)
count = int(input("What count start at "))
index = int(input("what indexing would you like"))




#to print graph with count and dif

x = np.array([])
y = np.array([])
while count<=limint:
    upper = gbpair(count)
    upperint = int(upper)
    lower = count-upperint
    arr = [lower,upper]
    #print(arr,end=' ')
    #print(upper-lower,end = ' ')
    print(count)
    x = np.append(x,count)
    y = np.append(y,upperint-lower)
    #print(x,end=' ')
    #print(y)
    count+=index

print(y)

plt.plot(x,y)
plt.show()
'''

#to print pair dif and count below
while count<=limint:
    upper = gbpair(count)
    upperint = int(upper)
    lower = count-upperint
    arr = [lower,upper]
    print(arr,end=' ')
    print(upper-lower,end = ' ')
    print(count)
x = np.array([])
y = np.array([])
numofz =0
while count<=limint:
    upper = gbpair(count)
    upperint = int(upper)
    lower = count - upperint
    dif = upperint-lower
    count+=index

    if dif==0:
        numofz+=1
        x=np.append(x,count)
        y = np.append(y,numofz)

print(np.shape(x))

plt.scatter(x,y)
plt.show()

'''

x = np.array([])
y = np.array([])
while count<=limint:
    if count ==4: prev =0

    upper = gbpair(count)
    upperint = int(upper)
    lower = count-upperint
    #arr = [lower,upper]
    #print(arr,end=' ')
    #print(upper-lower,end = ' ')
    #print(count)
    dif = upperint - lower
    cum = dif - prev
    x = np.append(x,count)

    y = np.append(y,dif)
    #print(x,end=' ')
    #print(y)
    if count != 4:
        prev = dif
    count+=index

print(y)

plt.plot(x,y)
plt.show()




















