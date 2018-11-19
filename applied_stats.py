import random
import matplotlib.pyplot as plt

def errors(n, n_range):
    lst_plus = []
    lst_minus = []
    y_axis=[]

    count = 0
    count2 = []
    tmp_count= 0

    lst_range = list(range(-10,10))
    for i in range ( n_range):
        lst_range[i] /=10

    incr = -1.0
    incr = round(incr, 2)

    for i in range(n):
        lst_minus.append(random.uniform(-0.9999, 0))
        lst_plus.append(random.uniform(0, 0.9999))
        lst_minus[i] = round(lst_minus[i], 6)
        lst_plus[i] = round(lst_plus[i], 6)
        count += 1

    lst = lst_minus + lst_plus

    print(len(lst))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    lst.sort()

    for i in range(n_range):
        for j in range(len(lst)):
            if lst[j]<incr and lst[j]>incr-0.1:
                tmp_count+=1
                #print(tmp_count)
                #count2.append(tmp_count)
                print(incr, tmp_count, lst[j])
        count2.append(tmp_count)
        for k in range(tmp_count):
            y_axis.append(tmp_count)
        tmp_count=0
        incr+=0.1


    for j in range(len(lst)):
        if lst[j]>incr-0.1 and lst[j]<1:
            tmp_count+=1
            print(incr, tmp_count, lst[j])

    count2.append(tmp_count)
    for k in range(tmp_count):
        y_axis.append(tmp_count)
    incr+=0.1

    print(count2)

    x = lst
    y = y_axis
    plt.plot(x,y)
    plt.show()

#####################################################################################

n = int(input("n:"))
n= n//2

n_range = int(input("n_range:"))
errors(n, n_range)

