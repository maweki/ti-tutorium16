from ssfsm import DFA_Machine

# Akzeptiert nur gerade Binärzahlen

even = DFA_Machine('a')
even.a[0] = even.b
even.b[0] = even.b
even.a[1] = even.a
even.b[1] = even.a
even.b = True

print(even().dot)

odd_length = DFA_Machine('e')
odd_length.e[(0,1)] = odd_length.o
odd_length.o[(0,1)] = odd_length.e
odd_length.o = True

#print(odd_length().dot)

#print((even + odd_length)().dot)
#print((even & odd_length)().get_minimized()().dot)
