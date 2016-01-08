from ssfsm import DFA_Machine

l = DFA_Machine(0)
l[0]['a'] = l[1]
l[0]['b'] = l[2]
l[1]['a'] = l[1]
l[1]['b'] = l[3]
l[2]['a'] = l[1]
l[2]['b'] = l[2]
l[3]['a'] = l[1]
l[3]['b'] = l[4]
l[4]['a'] = l[1]
l[4]['b'] = l[2]
l[4] = True

print(l().dot)

m = l().get_minimized()
#print(m().dot)
