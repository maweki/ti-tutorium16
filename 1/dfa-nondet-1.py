from ssfsm import NFA_Machine

# Akzeptiert nur gerade Binärzahlen

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
