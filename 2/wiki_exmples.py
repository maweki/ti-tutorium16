from cfg import T, NT, CFG

# examples from https://en.wikipedia.org/wiki/Context-free_grammar#Examples

# Well-formed parentheses
S = NT()
o = T('(')
c = T(')')
wfp = CFG(S,[
    (S, (S, S)),
    (S, (o, S, c)),
    (S, (o, c))
])

# Well-formed nested parentheses and square brackets
O = T('[')
C = T(']')
wfnpasb = CFG(S,[
    (S, (S, S)),
    (S, (o, c)),
    (S, (o, S, c)),
    (S, (O, C)),
    (S, (O, S, C)),
])

# A regular grammar
a = T('a')
b = T('b')
arg = CFG(S,[
    (S, (a,)),
    (S, (a, S)),
    (S, (b, S)),
])

# Matching pairs
mp = CFG(S,[
    (S, (a, S, b)),
    (S, (a, b)),
])

# Algebraic expressions
x, y, z = T('x'), T('y'), T('z')
plus, minus, multi, div = T('+'), T('-'), T('*'), T('/')
ae = CFG(S, [
    (S, (x,)),
    (S, (y,)),
    (S, (z,)),
    (S, (S, plus, S)),
    (S, (S, minus, S)),
    (S, (S, multi, S)),
    (S, (S, div, S)),
    (S, (o, S, c)),
])

# Further examples
U, V, T = NT(), NT(), NT()
fe1 = CFG(S, [
    (S, (U,)),
    (S, (V,)),
    (U, (T, a, U)),
    (U, (T, a, T)),
    (U, (U, a, T)),
    (V, (T, a, V)),
    (V, (T, a, T)),
    (V, (V, a, T)),
    (T, (a, T, b, T)),
    (T, (b, T, a, T)),
    (T, (a, b, T)),
    (T, (b, a, T)),
    (T, (a, T, b)),
    (T, (b, T, a)),
    (T, (a, b)),
    (T, (b, a)),
])

A = NT()
fe2 = CFG(S, [
    (S, (b, S, b, b)),
    (S, (A,)),
    (A, (a, A)),
    (A, (a))
])
