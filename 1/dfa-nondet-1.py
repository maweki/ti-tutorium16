from ssfsm import NFA_Machine

#  {01}*1{01}^n für n = 2

A = NFA_Machine('a')
A.a[0] += A.a
A.a[1] += A.a
A.a[1] += A.b
A.b[0] += A.c
A.b[1] += A.c
A.c[0] += A.d
A.c[1] += A.d
A.d = True
#print(A().dot)

det = A().dfa()
print(det().dot)
