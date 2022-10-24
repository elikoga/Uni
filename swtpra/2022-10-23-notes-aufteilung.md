# 2022-10-23 SWTPRA Komponentenaufteilung

Vorab: Für Gantt relevant: [##Arbeits-Chunks](#arbeits-chunks)

## Big Picture

- 4 Finale Anwendungen
  - Server
  - Engine-Teilnehmer
  - Android-Teilnehmer
  - PC-Beobachter

Daraus geht ein Kern von Komponenten hervor, die für alle oder ein Subset der Anwendungen benötigt werden.

- Spielmodell (state)
  - Spiellogik
- Kommunikation
  - Client -> Server

---

Für die einzelnen Anwendungen müssen wir noch weitere Komponenten definieren.

## Server

Für den Server beinhalten alle Komponenten: GUI, Netzwerk-Nachrichten und Business-Logik.

Komponenten die ich herausgelesen habe:

- Spielkonfigurations-Management
  - Konfigurationen erstellen
  - Konfigurationen bearbeiten
  - Konfigurationen speichern
- Spielmanagement
  - Spiel nach Konfiguration starten
    - Nutzer-Auswahl
  - Laufende Spiele verwalten
    - Spiele auflisten
    - Spiel pausieren
    - Spiel beenden
- Tourniermanagement
  - Spiel-Planen
  - Rangfolge anzeigen
  - Abgelaufene Spiele anzeigen
  - Tournier-Lobby

Geteilte Komponenten:

- Spielmodell (state)
  - Spiellogik

## Engine-Teilnehmer

Der Engine Teilehmer besteht aus einem Suchalgoritmus über den Spielbaum.

Komponenten die ich herausgelesen habe:

- Suchalgoritmus
  - Für uns am viel-versprechendsten: Minimax mit Alpha-Beta-Pruning und iterativer Tiefensuche

Geteilte Komponenten:

- Spielmodell (state)
  - Spiellogik
- Kommunikation
  - Client -> Server

<!-- ## Android-Teilnehmer

Der Android-Teilnehmer beinhaltet für alle Komponenten: GUI, Netzwerk-Nachrichten und Business-Logik.

Komponenten die ich herausgelesen habe:

- Spielauflistung
- Spielbeitritt
- Spielteilnahme
  - Als Beobachter
  - Oder als Spieler

Geteilte Komponenten:

- Spielmodell (state)
  - Spiellogik
- Kommunikation
  - Client -> Server -->

## PC-Beobachter

Der PC-Beobachter beinhaltet für alle Komponenten: GUI, Netzwerk-Nachrichten und Business-Logik.

- Spielauflistung
- Spielbeitritt
- Spielteilnahme
  - Als Beobachter

Geteilte Komponenten:

- Spielmodell (state)
- Kommunikation
  - Client -> Server

Man bemerke, dass der PC-Beobachter die Spiellogik nicht benötigt, da er nur die Spielzüge anzeigt.

---

## Zusätzlice Arbeitsschritte

- DevOps-Dokument
- Aufbau erworbener Android-Beobachter -> Android-Teilnehmer

## Zeitliche Anordnung

Parallele Entwicklung von Spielmodell, Spiel-Server und Engine-Teilnehmer (wenn auch mit unvollständigen Spiel-Algorithmen).

Arbeitsteil 1:

- Spielmodell
- Rudimentärer (Prä-Kommitee) Client <-> Server Kommunikation

Arbeitsteil 2:

- Spiel-Server (minimal, nur soweit man den PC-Beobachter, Engine-Teilnehmer testen kann)
- Rudimentärer Engine-Teilnehmer (random moves, als Server Test)

Arbeitsteil 3:

- PC-Beobachter (mit GUI)
- Server-GUI (niedrige Priorität)

---

## Sprint-Planung

- 2-Wöchige Sprints
  - 2022-10-28 - 2022-11-11
    - Spielmodell
    - Rudimentärer (Prä-Kommitee) Client <-> Server Kommunikation
    - Product Backlog
  - 2022-11-11 - 2022-11-25
    - Spiel-Server (minimal, nur soweit man den PC-Beobachter, Engine-Teilnehmer testen kann)
    - Rudimentärer Engine-Teilnehmer (random moves, als Server Test)
    - PC-Beobachter (mit GUI)
    - Abgabe
      - Product Backlog
        - 2022-11-14
        - Issues auf GitLab
      - QA Dokument
        - 2022-11-14
      - Interface-Dokument (Protokoll-Dokument)
        - 2022-11-21
        - Protokoll-Kommitee ist eigentlich dafür zuständig
  - 2022-11-25 - 2022-12-09
    - PC-Beobachter (mit GUI)
    - Abgabe
      - DevOps Dokument
        - 2022-12-09
      - Implementierung - Messeversion
        - 2022-12-09
  - 2022-12-09 - 2022-12-23
    - Anfang Erworbenen Android-Beobachter -> Android-Teilnehmer
    - Server-Features
      - Server-Gui
      - Tournament
      - Konfiguration
    - Außerordentliches Meeting in der Woche 2022-12-19 - 2022-12-23
      - Entscheidung wann ist noch offen
  - 2022-12-23 - 2023-01-06
    - Alles auf Arbeitslevel: "Best-Effort"
    - Android-Teilnehmer
    - Server-Features
      - Server-Gui
      - Tournament
      - Konfiguration
    - Engine-Algorithmus
    - !! Ferien
  - 2022-01-06 - 2022-01-20
    - Finalisierung aller Komponenten
      - Android-Teilnehmer
      - Server-Features
        - Server-Gui
        - Tournament
        - Konfiguration
      - Engine-Algorithmus
    - Abarbeitung des Übrigen Backlogs
  - 2022-01-20 - 2022-01-27
    - !! Halber Sprint
    - Keine Arbeitslast, nur Maintenance
    - Vorbereitung Abschlusspräsentation
    - Abgabe
      - Endabgabe
        - 2022-01-27
      - Abgabe der Turnierversion
        - 2022-01-27
  - 2022-01-27 - 2022-02-03
    - !! Halber Sprint
    - Persönliche Vorbereitung auf Abschlusspräsentation

---

## Arbeits-Chunks

- Spielmodell
  - ab 2022-10-28
  - bis 2022-11-11
  - Zeitaufwand: 2 = 84h
- Rudimentärer (Prä-Kommitee) Client <-> Server Kommunikation
  - ab 2022-10-28
  - bis 2022-11-11
  - Zeitaufwand: 2 = 84h
- Spiel-Server (minimal, nur soweit man den PC-Beobachter, Engine-Teilnehmer testen kann)
  - ab 2022-11-11
  - bis 2022-11-25
  - Finish-to-Finish abhängig von Spielmodell, Rudimentärer (Prä-Kommitee) Client <-> Server Kommunikation
  - Zeitaufwand: 3 = 126h
- Rudimentärer Engine-Teilnehmer (random moves, als Server Test)
  - ab 2022-11-11
  - bis 2022-11-25
  - Finish-to-Finish abhängig von Spielmodell, Rudimentärer (Prä-Kommitee) Client <-> Server Kommunikation
  - Zeitaufwand: 1 = 42h
- Product Backlog
  - ab 2022-10-28
  - bis 2022-11-14
  - Zeitaufwand: 3 = 126h
- QA Dokument
  - ab 2022-10-28
  - bis 2022-11-14
  - Zeitaufwand: 3 = 126h
- Interface-Dokument (Protokoll-Dokument)
  - ab 2022-10-28
  - bis 2022-11-21
  - Zeitaufwand: 5 = 210h
- Implementierung - Messeversion
  - ab 2022-11-11
  - bis 2022-12-09
  - DevOps Dokument
  - PC-Beobachter (mit GUI)
  - Finish-To-Finish abhängig von Spielmodell, Spiel-Server (minimal)
  - Zeitaufwand: 7 = 294h
- Server-Features
  - ab 2022-12-09
  - bis 2022-01-20
  - Server-Gui
  - Tournament
  - Konfiguration
  - Start-to-Finish abhängig von Spiel-Server (minimal)
  - Zeitaufwand: 7 = 294h
- Android-Beobachter -> Android-Teilnehmer
  - ab 2022-12-09
  - bis 2022-01-20
  - Start-to-Finish abhängig von Implementierung - Messeversion
  - Zeitaufwand: 6 = 252h
- Engine-Algorithmus
  - ab 2022-12-23
  - bis 2022-01-20
  - Start-to-Finish abhängig von Rudimentärer Engine-Teilnehmer
  - Zeitaufwand: 5 = 210h
- Endabgabe
  - ab 2022-01-06
  - bis 2022-01-27
  - Präsentation
  - Implementierung (Abgabe-Vorbereitung)
  - Test-Report (Abgabe-Vorbereitung)
  - Finish-to-Finish abhängig von Server-GUI, Server-Features, Android-Beobachter -> Android-Teilnehmer, Engine-Algorithmus
  - Zeitaufwand: 4 = 168h

Wir haben 7.5 Äquivalente Sprints, also 15 Wochen (Ferien ist 1/2 Sprint).
Es sind 240h workload für das Modul geplant.
Für die Auftakte gehen 6 Stunden drauf. Für die Messe 4 Stunden. Für die Abschlusspräsentation 4 Stunden. Und 10 Stunden für die Klausur + Vorbereitung.

Es bleiben 216 Stunden für die Entwicklung.

216 Stunden / 15 Wochen = 14.4 Stunden pro Woche.

Pro Woche gehen 2 Stunden drauf für die Meetings.

Das sind 12.4 Stunden pro Woche für die Entwicklung.

Das heißt, über 11 Leute haben wir insgesamt 136.4 Stunden pro Woche oder auch insgesamt 2046 Stunden für das Gesamte Projekt zu verteilen.

Wir haben insgesamt 48 Zeitunits und 2046 Stunden/48 Zeitunits ~ 42.6 Stunden pro Zeitunit, also 42 Stunden pro Zeitunit.

## Infos zum Erklärenden Text zum Projektplan

- Alle Software-Arbeitsschritte beinhalten die Implementation von Tests und Dokumentation
- Mit "Spielmodell" ist die Softwarekomponente gemeint, die
  - Die Abstrakte Datenstruktur des Spiels beinhaltet und zur verfügung stellt
  - Die Spiellogik implementiert
