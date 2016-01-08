from ssfsm import DFA_Machine


D1 = DFA_Machine('A')
D1.A[0] = D1.B
D1.A[1] = D1.A
D1.B[0] = D1.A
D1.B[1] = D1.B
D1.A = True

D2 = DFA_Machine('C')
D2.C[0] = D2.C
D2.C[1] = D2.D
D2.D[0] = D2.D
D2.D[1] = D2.C
D2.D = True

D3 = DFA_Machine('E')
D3.E[0] = D3.E
D3.E[1] = D3.F
D3.F[0] = D3.G
D3.F[1] = D3.F
D3.G[(0,1)] = D3.G
D3.E = True
D3.F = True

D4 = DFA_Machine('H')
D4.H[0] = D4.I
D4.H[1] = D4.H
D4.I[0] = D4.I
D4.I[1] = D4.J
D4.J[(0,1)] = D4.J
D4.H = True
D4.I = True

D5 = DFA_Machine('K')
D5.K[0] = D5.L
D5.K[1] = D5.M
D5.L[0] = D5.M
D5.L[1] = D5.K
D5.M[(0,1)] = D5.M
D5.K = True

D6 = DFA_Machine('N')
D6.N[0] = D6.O
D6.N[1] = D6.P
D6.O[0] = D6.P
D6.O[1] = D6.N
D6.P[(0,1)] = D6.P
D6.O = True

#print(D1().dot)
#print(D2().dot)
#print(D3().dot)
#print(D4().dot)

#print((D1 & D2)().dot)
#print((D1 | D2)().dot)
#print((D3 & D4)().dot)
#print((D3 | D4)().dot)

# D1 - D2 == D1 & ~D2


#print((D2 + D2)().dot)
