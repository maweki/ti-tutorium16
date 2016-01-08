from ssfsm import DFA_Machine

l = DFA_Machine('A')
l.A[0] = l.A
l.A[1] = l.B
l.B[0] = l.C
l.B[1] = l.D
l.C[0] = l.C
l.C[1] = l.E
l.D[0] = l.C
l.D[1] = l.D
l.E[0] = l.E
l.E[1] = l.E
l.A = True
l.C = True
l.E = True
print(l().dot)

m = l().get_minimized()
#print(m().dot)
