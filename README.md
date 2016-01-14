# TI TUTORIUM

## Reguläre Sprachen

Installation graphenbibliothek:

* `git clone https://github.com/maweki/ssfsm.git`

* branch "nfa" auschecken

* im Projektordner `pip install --user .`

* Graphen zu pdf: `python script.py | dot -Tpdf > foo.pdf`

* Beispiele im Ordner 1


Beachte:

* kreuzprodukt von Automaten (https://github.com/maweki/ssfsm/blob/nfa/ssfsm/dfa.py#L174)
* Automatenverkettung (https://github.com/maweki/ssfsm/blob/nfa/ssfsm/dfa.py#L126)
* Pumping lemma Beispiel (https://github.com/maweki/ssfsm/blob/nfa/ssfsm/dfa.py#L422)
* Äquivalenzklassen durch Nerode relation (https://github.com/maweki/ssfsm/blob/nfa/ssfsm/dfa.py#L200)
* Reguläre Sprache Check (https://github.com/maweki/ssfsm/blob/nfa/ssfsm/dfa.py#L442)

Mögliche Fragestellungen:

* Ist Sprache allg. abgeschlossen unter [...]? -> Ja (mit allg. Konstruktion)
* Ist spezielle Sprache regulär? -> Nein (PL), Ja (Automat)
* Wie geht minimierung? -> Äquivalenzklassen konstruieren via Nerode
* Defn. Nerode-Relation
* Zu jedem NFA gehört DFA. -> Konstruktion

## Kontextfreie Sprachen

Benutzung siehe Beispiele

Beachte:

* T/NT-Zugehörigkeit (https://github.com/maweki/ti-tutorium16/blob/master/2/cfg.py#L36-L39)
* Abschlüsse und Nebenbedingungen (https://github.com/maweki/ti-tutorium16/blob/master/2/cfg.py#L41-L59)
* Pumping Lemma (https://github.com/maweki/ti-tutorium16/blob/master/2/cfg.py#L100)
* Konstruktion Chomsky-Normalform (beachte Terminationsargumente für Algorithmus) (https://github.com/maweki/ti-tutorium16/blob/master/2/cfg.py#L110)
* Lsg. Wortproblem (beachte Terminationsargument für Algorithmus) (https://github.com/maweki/ti-tutorium16/blob/master/2/cfg.py#L146)


Fragestellungen:

* Dfn Chomsky-Normalform, Erkläre Algorithmus zum Erstellen, Erkläre Lsg. Wortproblem (CYK) mit Hilfe von Chomsky-Normalform
* Überführe Beispiel CFG in CNF (Erkläre dabei Algorithmus), Löse Wortproblem am Beispiel
* Gegebene Sprache(n). Kontextfrei? -> Ja (CFG aufstellen). Nein (PL)
* Abschluss unter ...? -> Ja (Konstruktion)
* Gegebene Kontextfreie Sprachen, Schnitt auch Kontextfrei? -> Nein (PL)

Fragen:

* maweki bei gmail
* mwenzel bei imn
