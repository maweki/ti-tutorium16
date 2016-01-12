from cfg import T, NT, CFG

S = NT()
a = T('a')
b = T('b')
g = CFG(S, [(S, (a,S,b)), (S, (a,b))])
print(g)
g_ = g.chomsky_normal_form()
print(g_)
print(g_.accepts('abaabab', True))
print(g_.accepts('aaabbb', True))


S = NT()
a = T('a')
b = T('b')
gr = CFG(S, [(S, (b,S,a)), (S, (b,a))])

gc = g | gr
gc_ = gc.chomsky_normal_form()
print(gc_.accepts('aabb', True))
print(gc_.accepts('bbaa', True))

gp = g + gr
gp_ = gp.chomsky_normal_form()
print(gp_.accepts('aaabbbbbaa', True))
print(gp_.accepts('aaabbaabbbaa'))

gk = g.kleene()
gk_ = gk.chomsky_normal_form()
print(gk_)
print(gk_.accepts('ababaaabbbaabb'))
