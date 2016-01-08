from ssfsm import DFA_Machine

l = DFA_Machine('X')
l.X['a'] = l.W
l.X['b'] = l.Z
l.Y['a'] = l.Z
l.Y['b'] = l.X
l.Z['ab'] = l.Z
l.V['a'] = l.Y
l.V['b'] = l.Z
l.W['a'] = l.Z
l.W['b'] = l.V
l.V = True
l.X = True

#print(l().dot)

m = l().get_minimized()
print(m().dot)
