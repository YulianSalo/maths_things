import math

def y(x):
    '''Write here any function that you need.
    math.cos(pow(x,3)) was my funtion
    '''
    return math.cos(pow(x,3))



def lagrange(power_pol, point, l_range, r_range):
    ''' This method calculate polynomial for one point.
    In order to run it properly we need to run it in the loop iterating through each point'''

    S = 0.0

    step = abs((r_range - l_range)/power_pol)

    for i in range(power_pol):
        B_given[i] = l_range+ i * step

    for i in range(power_pol):

        P1 = 1.0
        P2 = 1.0

        for k in range (power_pol):

            if i != k :
                P1 = P1*(point - B_given[k])
                P2 = P2*(B_given[i] - B_given[k])

        S = S + y(B_given[i]) * P1 / P2

    return S

tested_length = 5

power_pol = int(input("Polymomial power: "))
l_range= float(input("Left range: "))
r_range = float(input("Right range: "))

A_tested = [[0] * tested_length for i in range(tested_length)]
B_given = [[0] * power_pol for i in range(power_pol)]

x_true = [[0] * tested_length for i in range(tested_length)]
x_approx = [[0] * tested_length for i in range(tested_length)]

for i in range(tested_length):
    A_tested[i] = float(input("Tested point {}: ".format(i+1)))
    x_true[i] = y(A_tested[i])

for i in range(tested_length):
    x_approx[i] = lagrange(power_pol, A_tested[i], l_range, r_range)

print("True result: ", x_true)
print("Approx result: ", x_approx)
