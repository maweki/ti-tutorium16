from collections import namedtuple
from itertools import chain
from string import ascii_uppercase


T = namedtuple('T', 'symbol')
class NT(object):
    __ntnames = {}
    def __repr__(self):
        if not self in self.__ntnames:
            self.__ntnames[self] = ascii_uppercase[len(self.__ntnames)]
        return self.__ntnames[self]

class CFG(object):

    @property
    def terminals(self):
        return set(s for s in chain.from_iterable((r for l, r in self.__rules)) if isinstance(s, T))

    @property
    def nonterminals(self):
        return set(l for l, r in self.__rules)

    @property
    def rules(self):
        return set(self.__rules)

    @property
    def start(self):
        return self.__start

    def __init__(self, start, rules):
        self.__rules = set(rules)
        self.__start = start
        assert(isinstance(start, NT))
        for l, r in self.rules:
            assert(isinstance(l, NT))
            for r_ in r:
                assert(isinstance(r_, NT) or isinstance(r_, T))

    def __or__(self, other):
        # Old rules and A -> A', A -> A''
        assert(not (self.nonterminals & other.nonterminals)) # Grammars should not share Nonterminals
        new_start = NT()
        rules = self.rules | other.rules | set([(new_start, (self.start,)), (new_start, (other.start,))])
        return CFG(new_start, rules)

    def __add__(self, other):
        # Old rules and A -> A'A'
        assert(self is other or not (self.nonterminals & other.nonterminals)) # Grammars should not share Nonterminals (doesn't if its the same grammar)
        new_start = NT()
        rules = self.rules | other.rules | set([(new_start, (self.start, other.start))])
        return CFG(new_start, rules)

    def kleene(self):
        # actually not kleene start closure because no A -> eps rule.
        start = NT()
        rules = self.rules | set([(start, (self.start, start)), (start, (self.start,))])
        return CFG(start, rules)

    def __repr__(self):
        return repr(((self.start), self.rules))

    def produce_word(self, symbol=None):
        return next(iter(self.produce_words(symbol)))

    def produce_words(self, symbol=None):
        symbol = symbol or self.start
        from collections import deque
        assert(symbol in self.nonterminals)
        queue = deque([(symbol,)])
        while queue:
            # queue size always increases
            # we pop the smallest (shortest derivation) words from the left and
            # add longer derivations to the right so we eventually generate all words
            w = queue.popleft()
            if all(type(s) is T for s in w):
                yield tuple(s.symbol for s in w)
                continue
            idx, nt = next(iter((pos, s) for pos, s in enumerate(w) if type(s) is NT))
            for l, r in self.rules:
                if l == nt:
                    queue.append(w[:idx] + tuple(r) + w[idx+1:])


    def get_reachable(self, symbol):
        def get_reachable_rec(symbol, seen):
            if symbol in seen:
                return set()
            else:
                result = set()
                matching_rules_rhs = (r for l, r in self.rules if l == symbol)
                for r in matching_rules_rhs:
                    for s in r:
                        if type(s) is NT:
                            result |= set([s]) | get_reachable_rec(s, seen | set([symbol]))
                return result
        return get_reachable_rec(symbol, set())

    def get_pumping_lemma(self):
        is_proper_subsequence = lambda s, l: any(l[d:len(s) + d] == s for d in range(len(l) - len(s)))
        looping_state = next(iter(s for s in self.nonterminals if s in self.get_reachable(s)))
        w = self.produce_word(looping_state)
        vwx = next(iter(vwx for vwx in self.produce_words(looping_state) if is_proper_subsequence(w, vwx)))
        v_, w_, x_ = ''.join(vwx).partition(''.join(w))
        uvwxy = next(iter(uvwxy for uvwxy in self.produce_words(self.start) if is_proper_subsequence(vwx, uvwxy)))
        u_, vwx_, y_ = ''.join(uvwxy).partition(''.join(vwx))
        return (u_, v_, w_, x_, y_)

    def chomsky_normal_form(self):
        # Rules are either NT -> (NT, NT)
        # or NT -> (T,)
        t_repl = {t.symbol: NT() for t in self.terminals}
        old_rules = set(self.rules)
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
                # the length of some A -> B -> C chain always decreases (some B -> C is removed)
                # and we don't add A -> A so we don't add infinitely many new rules
                for l2, r2 in chain(set(old_rules), new_rules):
                    if l2 == r[0] and r2 != (l,):
                        old_rules.add((l, r2))
                continue
            if any(type(e) is T for e in r):
                # Replace any T with the corresponding NT
                rn = tuple((t_repl[e.symbol] if type(e) is T else e) for e in r)
                old_rules.add((l, rn))
                continue
            if len(r) > 2:
                # reduce rule sizes A -> BCD => A -> BB', B' -> CD
                # All added rules get smaller
                ln = NT()
                new_rules.add((l, (r[0], ln)))
                old_rules.add((ln, (r[1:])))
        return CFG(self.start, new_rules)

    def accepts(self, word, verbose=False):
        from itertools import product
        p = tuple(set(nt for nt, r in self.rules if len(r) == 1 and type(r[0]) is T and r[0].symbol == w) for w in word)
        deconstructions = set(product(*p))
        while deconstructions:
            # termination argument:
            # we may add many deconstructions but they are all shorter than the last because we are in Chomsky Normal Form
            # Rulesets A -> B, B -> A (not Chomsky Normal Form) lead to infinite loop
            if verbose:
                print(deconstructions)
            d = deconstructions.pop()
            if d == (self.start,):
                return True
            for i in range(len(d)-1):
                pair = d[i:i+2]
                for l, r in self.rules:
                    if pair == r:
                        deconstructions.add(d[:i] + (l,) + d[i+2:])
        return False
