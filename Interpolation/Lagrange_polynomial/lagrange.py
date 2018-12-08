
def lagrange(power_pol, point, l_range, r_range):
    S = 0.0
    print(point)
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
