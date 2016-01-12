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

pl = g.get_pumping_lemma()
print(pl)
u,v,w,x,y = pl
for i in range(20):
    print("%s%s%s%s%s" % (u, v*i, w, x*i, y))
