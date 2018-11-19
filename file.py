import random
import matplotlib.pyplot as plt

def errors(n, n_range):

    y_axis=[]
    lst_first=[]
    lst_get = 0.0
    lst_way = []
    S=0
    count2 = []
    tmp_count= 0

    incr = -1.0
    incr = round(incr, 2)

    for i in range(n):

        for j in range(3):

            lst_way.append(random.uniform(-1, 1))

        lst_get = lst_way[1]
        lst_get = round(lst_get,6)
        lst_way = []
        print(lst_get)
        lst_first.append(lst_get)

    print(lst_first)

    '''for i in range(n):
        lst.append(random.uniform(-1, 1))
    print(len(lst))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")'''
    lst = lst_first
    lst.sort()

    for i in range(n_range):

        for j in range(len(lst)):

            if lst[j]<incr and lst[j]>incr-0.1:
                tmp_count+=1
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

    for i in range(len(count2)):
        S+=count2[i]

    print(S)

    x = lst
    y = y_axis
    plt.plot(x,y)
    plt.show()

#####################################################################################

n = int(input("n:"))
n_range = int(input("n_range:"))
errors(n, n_range)

