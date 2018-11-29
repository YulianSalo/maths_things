import numpy as np

def cholesky(a, t, n):

   b = [[0] * n for i in range(n)]
   c = [[0] * n for i in range(n)]
   y = [n for n in range(n)]
   x = [n for n in range(n)]

   for i in range(n):

      for j in range(n):

         if j ==0:
            b[i][0] = a[i][0]

         if i>=j:
            b[i][j] = a[i][j]

            for k in range(j):
               b[i][j] -= b[i][k] * c[k][j]

      for j in range(n):

         if i == 0:
            c[0][j] = a[0][j] / b[0][0]

         if i<=j:
            c[i][j] = a[i][j]

            for k in range(i):
               c[i][j] -= b[i][k] * c[k][j]

            c[i][j] /= b[i][i]


   print("C:", np.matrix(c))
   print("B:", np.matrix(b))

   y = t

   for i in range( n):

      temp = y[0]
      part1 = 0.0

      for j in range(0,i):
         y[i] =t[i]- b[i][j]*y[j]


      y[i] =y[i]/b[i][i]

   print("Y: ", y)

   x=y

   for i in range(n, -1, -1):

      for j in range(i+1, n):
         x[i] -= c[i][j]*x[j]



   print("X:", x)

   ########################################################################################

n=4
a = [[0] * n for i in range(n)]
t = [n for n in range(n)]
a = [[-11, -6, 3,-1], [4, 14, 2, 1], [-1, -3, -12, -1], [-4, -1, 1, 15]]
t = [-2, 4, -2, 1]

#n = int(input("N:"))
'''for i in range(n):
   for j in range (n):
      a[i][j]=float(input("A:"))
print("A:", np.matrix(a))


for j in range(n):
   y[j] = float((input("T: ")))
print("B:", t)'''

cholesky(a, t, n)


















