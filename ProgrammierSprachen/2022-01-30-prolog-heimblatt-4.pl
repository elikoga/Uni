% Vorname Name Matrikelnummer User Vorlesungen Professor/in
% Alice J ̈ackel 9523343 ajaeckel Einf ̈uhrung in Geschichte
% Philosophie
% Rogge
% Oestrovsky
% Pius H ̈olzenbeck 9523377 phoelzer Philosophie Oestrovsky
% Adina Walter 9523418 adwalter
% Einf ̈uhrung in Geschichte
% Alte Sprachen
% Latein
% Rogge
% Eckbauer
% Finke
% Kathi Meister 8533463 kmeister Mathematik
% Englisch
% Benthin
% Finke
% Valeska Warmer 9523888 vwarmer Mathematik
% Kunstgeschichte
% Benthin
% Eckbauer
% S ̈onke R ̈omer 9523574 sroemer
% Einf ̈uhrung in Geschichte
% Philosophie
% Latein
% Rogge
% Oestrovsky
% Finke
% Leonard Koch 8925543 leokoch
% Mathematik
% Alte Sprachen
% Latein
% Benthin
% Eckbauer
% Finke

istStudi('Alice', 'Jäckel').
istStudi('Pius', 'Hölzenbeck').
istStudi('Adina', 'Walter').
istStudi('Kathi', 'Meister').
istStudi('Valeska', 'Warmer').
istStudi('Sönke', 'Römer').
istStudi('Leonard', 'Koch').

hatMatrikelnummer('Alice', 'Jäckel', 9523343).
hatMatrikelnummer('Pius', 'Hölzenbeck', 9523377).
hatMatrikelnummer('Adina', 'Walter', 9523418).
hatMatrikelnummer('Kathi', 'Meister', 8533463).
hatMatrikelnummer('Valeska', 'Warmer', 9523888).
hatMatrikelnummer('Sönke', 'Römer', 9523574).
hatMatrikelnummer('Leonard', 'Koch', 8925543).

userZurMatrikelnummer(ajaekel, 9523343).
userZurMatrikelnummer(phoelzer, 9523377).
userZurMatrikelnummer(adwalter, 9523418).
userZurMatrikelnummer(kmeister, 8533463).
userZurMatrikelnummer(vwarmer, 9523888).
userZurMatrikelnummer(sroemer, 9523574).
userZurMatrikelnummer(leokoch, 8925543).

haeltVorlesung('Einführung in Geschichte', 'Rogge').
haeltVorlesung('Philosophie', 'Oestrovsky').
haeltVorlesung('Alte Sprachen', 'Eckbauer').
haeltVorlesung('Latein', 'Finke').
haeltVorlesung('Mathematik', 'Benthin').
haeltVorlesung('Englisch', 'Finke').
haeltVorlesung('Kunstgeschichte', 'Eckbauer').

hoertVorlesung(ajaekel, 'Einführung in Geschichte').
hoertVorlesung(ajaekel, 'Philosophie').
hoertVorlesung(phoelzer, 'Philosophie').
hoertVorlesung(adwalter, 'Einführung in Geschichte').
hoertVorlesung(adwalter, 'Alte Sprachen').
hoertVorlesung(adwalter, 'Latein').
hoertVorlesung(kmeister, 'Mathematik').
hoertVorlesung(kmeister, 'Englisch').
hoertVorlesung(vwarmer, 'Mathematik').
hoertVorlesung(vwarmer, 'Kunstgeschichte').
hoertVorlesung(sroemer, 'Einführung in Geschichte').
hoertVorlesung(sroemer, 'Philosophie').
hoertVorlesung(sroemer, 'Latein').
hoertVorlesung(leokoch, 'Mathematik').
hoertVorlesung(leokoch, 'Alte Sprachen').
hoertVorlesung(leokoch, 'Latein').

%%%

hoert(Vorlesung, Vorname, Nachname) :-
    istStudi(Vorname, Nachname),
    hatMatrikelnummer(Vorname, Nachname, Matrikelnummer),
    userZurMatrikelnummer(User, Matrikelnummer),
    hoertVorlesung(User, Vorlesung).

schreibtPruefung(Vorlesung, User) :-
    userZurMatrikelnummer(User, Matrikelnummer),
    Matrikelnummer >= 9000000,
    hoertVorlesung(User, Vorlesung).

wasHoerenDieStudentenNoch(Professor, Vorlesung) :-
    haeltVorlesung(EineVorlesung, Professor),
    hoertVorlesung(User, EineVorlesung),
    hoertVorlesung(User, Vorlesung),
    \+ haeltVorlesung(Vorlesung, Professor).

%%% Übung 2 Listen

istInListe(Liste, Elem) :-
    Liste = [Elem | _].

istInListe(Liste, Elem) :-
    Liste = [_ | Rest],
    istInListe(Rest, Elem).

istLetztesElement(Liste, Elem) :-
    Liste = [Elem].

istLetztesElement(Liste, Elem) :-
    Liste = [_ | Rest],
    istLetztesElement(Rest, Elem).

gibAusLetztesElement(Liste) :-
    istLetztesElement(Liste, Elem),
    write(Elem).

laengeListe(Liste, Laenge) :-
    Liste = [] -> Laenge is 0;
    Liste = [_ | Rest],
    laengeListe(Rest, LaengeRest),
    Laenge is LaengeRest + 1.

konkatenationListe(Liste1, Liste2, Liste3) :-
    Liste1 = [],
    Liste2 = Liste3.

konkatenationListe(Liste1, Liste2, Liste3) :-
    Liste1 = [Elem | Rest],
    konkatenationListe(Rest, Liste2, Rest2),
    Liste3 = [Elem | Rest2].

% Übung 3

fibonacci(Index, Fibonacci) :-
    Index = 0 -> Fibonacci is 0;
    Index = 1 -> Fibonacci is 1;
    Index > 1,
    Index1 is Index - 1,
    Index2 is Index - 2,
    fibonacci(Index1, Fibonacci1),
    fibonacci(Index2, Fibonacci2),
    Fibonacci is Fibonacci1 + Fibonacci2.

hanoi(0, _, _, _).

hanoi(Anzahl, Start, Ziel, Hilf) :-
    Anzahl > 0,
    Anzahl1 is Anzahl - 1,
    hanoi(Anzahl1, Start, Hilf, Ziel),
    write(Start),
    write(' -> '),
    write(Ziel),
    nl,
    hanoi(Anzahl1, Hilf, Ziel, Start).

% Aufruf mit bspw. ?- hanoi(4, 'A', 'B', 'C').

% Übung 4

% Jemand hat geklaut, alle streiten es ab.

% Milan sagt, dass Yasmin lügt.

% Yasmin sagt, dass Samuel lügt.

% Samuel sagt, dass Milan und Yasmin lügen


% sagtWahrheit(milan) :- lügt(yasmin).
% sagtWahrheit(yasmin) :- lügt(samuel).

% sagtWahrheit(samuel) :- lügt(milan), lügt(yasmin).

% lügt(milan) :- sagtWahrheit(yasmin).
% lügt(yasmin) :- sagtWahrheit(samuel).

% lügt(samuel) :- sagtWahrheit(milan).
% lügt(samuel) :- sagtWahrheit(yasmin).

% lügt(samuel) :- sagtWahrheit(milan), sagtWahrheit(yasmin).
% lügt(samuel) :- lügt(milan), sagtWahrheit(yasmin).
% lügt(samuel) :- sagtWahrheit(milan), lügt(yasmin).



sagtWahrheitWennLügt(milan, yasmin).
sagtWahrheitWennLügt(yasmin, samuel).

lügtWennSagtWahrheit(milan, yasmin).
lügtWennSagtWahrheit(yasmin, samuel).
lügtWennSagtWahrheit(samuel, milan).
lügtWennSagtWahrheit(samuel, yasmin).


werLügt(X) :-
    lügtWennSagtWahrheit(X, Y),
    sagtWahrheitWennLügt(Y, Z),
    lügtWennSagtWahrheit(Z, Y).
% Y sagt die Wahrheit.
