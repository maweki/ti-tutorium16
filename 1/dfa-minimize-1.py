from ssfsm import DFA_Machine

l = DFA_Machine('A')
l.A[0] = l.H
l.A[1] = l.B
l.B[0] = l.H
l.B[1] = l.A
l.C[0] = l.E
l.C[1] = l.F
l.D[0] = l.E
l.D[1] = l.F
l.E[0] = l.F
l.E[1] = l.G
l.F[(0,1)] = l.F
l.G[0] = l.G
l.G[1] = l.F
l.H[(0,1)] = l.C
l.F = True
l.G = True
print(l().dot)

m = l().get_minimized()
#print(m().dot)
