# TI TUTORIUM

## Reguläre Sprachen

Installation graphenbibliothek:

* `git clone https://github.com/maweki/ssfsm.git`

* branch "nfa" auschecken

* im Projektordner `pip install --user .`

* Graphen zu pdf: `python3 script.py | dot -Tpdf > foo.pdf`

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


## P/NP

Reduktionsideen:

Überlege Korrektheit (es kommen keine falschen Lösungen dazu), Vollständigkeit (es kommen keine korrekten Lösungen weg), <- Zusammen Erfüllbarkeitsäquivalent, Komplexität/Kosten

* SAT->3SAT
  * kurze Klauseln mit doppelten Literalen auffüllen
  * lange klauseln verketten (ähnlich Chomsky-Normalform) ABCD -> (AB1, ~1CD)
* DHC->HC
  * Jeder Knoten zu 3 Knoten (Eingang, Ausgang, Mitte)
  * Mitte kann nur Über Eingang -> Mitte -> Ausgang oder Ausgang -> Mitte -> Eingang erreicht werden
  * Nur Ausgänge mit Eingängen verbinden, damit immer Eingang -> Mitte -> Ausgang -> Eingang -> Mitte -> Ausgang usw...
* 3SAT->IS
  * Gesucht IS größe n für n Klauseln
  * Für jedes Literal in jeder Klausel einen Knoten
  * Nur ein erfüllendes Literal in jeder Klausel -> Alle Literale einer Klausel verbinden
  * Keine widersprüchlichen Literate in Lösung -> Alle Literale mit ihren Negationen verbinden
* HC->TSP
  * Alle Strecken bekommen kosten 1
  * Rundreise länge n gesucht für n Knoten (wenn ja, dann HC)
* SAT3->DHC
  * Ein knoten für jede Variable
  * 6-Knoten "Gadget" für jede 3-Klausel kann vollständig erfüllt (besucht) werden durch 1, 2 oder 3 eingehende erfüll-Kante
  * Yeah/Ney-Kante aus Variable in erfüllendes Literal aus Klausel 1, dann Klausel 2 usw., dann Eingang nächste Variable

Fragestellungen:

* Was bedeutet Problem in P/NP?
* p1 <=p p2. Wie ist Klassenzugehörigkeit von p1, p2? Welcher Zusammenhang besteht?
* Zeige Reduktion (SAT->SAT3/DHC->HC/3SAT->Clique/3SAT->IS/HC->TSP/SAT3->DHC), begründe Korrektheit, gehe auf Kosten/Zeit/Komplexität der Reduktion ein
* Erkläre "NP-Vollständig"/"NP-Schwer"/"NP"/"P" mit (det/ndet) Turing-Maschinen als Algorithmenmodell

# Entscheidbarkeit

* Entscheidbar/Rekursiv
  * akzeptiert immer in endl. Zeit
  * lehnt immer in endl. Zeit ab
  * abgeschlossen unter Komplement
* Semi-Entscheidbar/(Rekursiv) Aufzählbar
  * akzeptiert immer in endl. Zeit
  * hält bei Ablehnung nicht immer
  * Komplement unentscheidbar (wenn Komplement auch Semi-Entscheidbar, dann beide in Wirklichkeit entscheidbar)
* Unentscheidbar
  * hält bei akzeptierten Wörtern nicht immer
* Diagonalsprache
  * Universelle Turing-Maschine M existiert und wird mit Zeichenkette w als M_w kodiert
  * D = {w | M_w akzeptiert w nicht} (mit w kodierte Turing-Maschine bekommt w als Eingabe und akzpetiert w nicht)

Fragestellungen:

* L oder ~L unentscheidbar. L oder ~L Semi-Entscheidbar?
* Ist Diagonalsprache Semi-Entscheidbar?
* Reduktion P1 < P2: Verhalten (Semi/Un)entscheidbarkeit

Viel Erfolg!

Fragen:

* maweki bei gmail
* mwenzel bei imn
