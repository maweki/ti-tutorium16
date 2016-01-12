from collections import namedtuple
from itertools import chain
from string import ascii_uppercase

ntnames = {}

T = namedtuple('T', 'symbol')
class NT(object):
    def __repr__(self):
        if not self in ntnames:
            ntnames[self] = ascii_uppercase[len(ntnames)]
        return ntnames[self]
#NT = namedtuple('NT', ())

class CFG(object):
    def __init__(self, start, rules):
        self.__terminals = set(s for s in chain.from_iterable((r for l, r in rules)) if isinstance(s, T))
        self.__nonterminals = set(l for l, r in rules)
        self.__rules = set(rules)
        self.__start = start
        assert(isinstance(start, NT))
        for nt in self.__nonterminals:
            assert(isinstance(nt, NT))

    def __or__(self, other):
        assert(not (self.__nonterminals & other.__nonterminals)) # Grammars should not share Nonterminals
        start = NT()
        rules = self.__rules | other.__rules | set([(start, (self.__start,)), (start, (other.__start,))])
        return CFG(start, rules)

    def __add__(self, other):
        assert(not (self.__nonterminals & other.__nonterminals)) # Grammars should not share Nonterminals
        start = NT()
        rules = self.__rules | other.__rules | set([(start, (self.__start, other.__start))])
        return CFG(start, rules)

    def kleene(self):
        start = NT()
        rules = self.__rules | set([(start, (self.__start, start)), (start, (self.__start,))])
        return CFG(start, rules)

    def __repr__(self):
        return repr(((self.__start), self.__rules))

    def chomsky_normal_form(self):
        # Rules are either NT -> (NT, NT)
        # or NT -> (T,)
        t_repl = {t.symbol: NT() for t in self.__terminals}
        old_rules = set(self.__rules)
        new_rules = set((nt,(T(ts),)) for ts, nt in t_repl.items())

        types = lambda i: tuple(map(type, i))

        while old_rules:
            l, r = old_rules.pop()
            if types(r) == (T,) or types(r) == (NT, NT):
                # rules are good
                new_rules.add((l, r))
                continue
            if types(r) == (NT,):
                # reduce transitively
                for l2, r2 in chain(set(old_rules), new_rules):
                    if l2 == r[0]:
                        old_rules.add((l, r2))
                continue
            if any(type(e) is T for e in r):
                rn = tuple((t_repl[e.symbol] if type(e) is T else e) for e in r)
                old_rules.add((l, rn))
                continue
            if len(r) > 2:
                ln = NT()
                new_rules.add((l, (r[0], ln)))
                old_rules.add((ln, (r[1:])))
        return CFG(self.__start, new_rules)

    def accepts(self, word, verbose=False):
        from itertools import product
        p = tuple(set(nt for nt, r in self.__rules if len(r) == 1 and type(r[0]) is T and r[0].symbol == w) for w in word)
        deconstructions = set(product(*p))
        while deconstructions:
            if verbose:
                print(deconstructions)
            d = deconstructions.pop()
            if d == (self.__start,):
                return True
            for i in range(len(d)-1):
                pair = d[i:i+2]
                for l, r in self.__rules:
                    if pair == r:
                        deconstructions.add(d[:i] + (l,) + d[i+2:])
        return False
