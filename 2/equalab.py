from cfg import T, NT, CFG

Z = NT()
P = NT()
M = NT()
a = T('a')
b = T('b')

g = CFG(Z, [
    (Z, (a, P)),
    (Z, (b, M)),
    (P, (b,)),
    (P, (a,P,P)),
    (M, (a,)),
    (M, (b,M,M))
]).kleene()
g_ = g.chomsky_normal_form()
print(g_.accepts('baabbbaaabba'))
print(g_.accepts('baabbaaabba'))
