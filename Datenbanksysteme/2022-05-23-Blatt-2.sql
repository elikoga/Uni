-- Verlies (V):
-- VerID (VID) : Integer Primärschlüssel
-- Ort (O) : Text
-- SchatzNiveau (SN) : Integer (kann nur Werte zwischen 1 und 100 annehmen)
-- NachesteEbene (NE) : Integer Fremdschlüssel auf Spalte VerID der Tabelle Verlies
--  Held (H):
-- HeldID (HID) : Integer Primärschlüssel
-- Name (N) : Text Eindeutig
-- WaffenStaerke (WS) : Integer
-- WillPluendern (WP) : Integer Fremdschlüssel auf Spalte VerID der Tabelle Verlies
-- StarkGegen (SG) : Integer Fremdschlüssel auf Spalte BesID der Tabelle Be-
-- schuetzer
-- 1
--  Beschuetzer (B):
-- BesID (BID) : Integer Primärschlüssel
-- Name (N) : Text Eindeutig
-- VertStaerke (VS) : Integer
-- Beschuetzt (BS) : Integer Fremdschlüssel auf Spalte VerID der Tabelle Verlies
DROP TABLE IF EXISTS V;
DROP TABLE IF EXISTS Verlies;
DROP TABLE IF EXISTS H;
DROP TABLE IF EXISTS Held;
DROP TABLE IF EXISTS B;
DROP TABLE IF EXISTS Beschuetzer;

CREATE TABLE IF NOT EXISTS Verlies (
  VerID INTEGER PRIMARY KEY,
  Ort TEXT,
  SchatzNiveau INTEGER,
  NachesteEbene INTEGER,
  FOREIGN KEY (NachesteEbene) REFERENCES Verlies(VerID)
);

CREATE TABLE IF NOT EXISTS V (
  VID INTEGER PRIMARY KEY,
  O TEXT,
  SN INTEGER,
  NE INTEGER,
  FOREIGN KEY (NE) REFERENCES V (VID)
);

CREATE TABLE IF NOT EXISTS Held (
  HeldID INTEGER PRIMARY KEY,
  Name TEXT,
  WaffenStaerke INTEGER,
  WillPluendern INTEGER,
  StarkGegen INTEGER,
  FOREIGN KEY (WillPluendern) REFERENCES Verlies(VerID),
  FOREIGN KEY (StarkGegen) REFERENCES Beschuetzer(BesID)
);

CREATE TABLE IF NOT EXISTS H (
  HID INTEGER PRIMARY KEY,
  N TEXT,
  WS INTEGER,
  WP INTEGER,
  SG INTEGER,
  FOREIGN KEY (WP) REFERENCES V (VID),
  FOREIGN KEY (SG) REFERENCES B (BID)
);

CREATE TABLE IF NOT EXISTS Beschuetzer (
  BesID INTEGER PRIMARY KEY,
  Name TEXT,
  VertStaerke INTEGER,
  Beschuetzt INTEGER,
  FOREIGN KEY (Beschuetzt) REFERENCES Verlies(VerID)
);

CREATE TABLE IF NOT EXISTS B (
  BID INTEGER PRIMARY KEY,
  N TEXT,
  VS INTEGER,
  BS INTEGER,
  FOREIGN KEY (BS) REFERENCES V (VID)
);

-- Verlies (V):
-- VerID NaechsteEbene Ort SchatzNiveau
-- (VID) (NE) (O) (SN)
-- 1 3 Fort Knox 33
-- 2 - Alcatraz 97
-- 3 - Fort Knox 98
-- 4 6 New Gate 22
-- 5 2 Alcatraz 99
-- 6 - Maze Prison 96

INSERT INTO V(VID, NE, O, SN) VALUES (1, 3, 'Fort Knox', 33);
INSERT INTO V(VID, NE, O, SN) VALUES (2, NULL, 'Alcatraz', 97);
INSERT INTO V(VID, NE, O, SN) VALUES (3, NULL, 'Fort Knox', 98);
INSERT INTO V(VID, NE, O, SN) VALUES (4, 6, 'New Gate', 22);
INSERT INTO V(VID, NE, O, SN) VALUES (5, 2, 'Alcatraz', 99);
INSERT INTO V(VID, NE, O, SN) VALUES (6, NULL, 'Maze Prison', 96);

INSERT INTO Verlies(VerID, NachesteEbene, Ort, SchatzNiveau) VALUES (1, 3, 'Fort Knox', 33);
INSERT INTO Verlies(VerID, NachesteEbene, Ort, SchatzNiveau) VALUES (2, NULL, 'Alcatraz', 97);
INSERT INTO Verlies(VerID, NachesteEbene, Ort, SchatzNiveau) VALUES (3, NULL, 'Fort Knox', 98);
INSERT INTO Verlies(VerID, NachesteEbene, Ort, SchatzNiveau) VALUES (4, 6, 'New Gate', 22);
INSERT INTO Verlies(VerID, NachesteEbene, Ort, SchatzNiveau) VALUES (5, 2, 'Alcatraz', 99);
INSERT INTO Verlies(VerID, NachesteEbene, Ort, SchatzNiveau) VALUES (6, NULL, 'Maze Prison', 96);


-- Held (H):
-- HeldID WillPluendern StarkGegen Name WaffenStaerke
-- (HID) (WP) (SG) (N) (WS)
-- 11 2 21 Merlin 55
-- 12 6 21 Arthur 11
-- 13 5 23 Percy 44
-- 14 3 21 Peter 33

INSERT INTO H(HID, WP, SG, N, WS) VALUES (11, 2, 21, 'Merlin', 55);
INSERT INTO H(HID, WP, SG, N, WS) VALUES (12, 6, 21, 'Arthur', 11);
INSERT INTO H(HID, WP, SG, N, WS) VALUES (13, 5, 23, 'Percy', 44);
INSERT INTO H(HID, WP, SG, N, WS) VALUES (14, 3, 21, 'Peter', 33);

INSERT INTO Held(HeldID, WillPluendern, StarkGegen, Name, WaffenStaerke) VALUES (11, 2, 21, 'Merlin', 55);
INSERT INTO Held(HeldID, WillPluendern, StarkGegen, Name, WaffenStaerke) VALUES (12, 6, 21, 'Arthur', 11);
INSERT INTO Held(HeldID, WillPluendern, StarkGegen, Name, WaffenStaerke) VALUES (13, 5, 23, 'Percy', 44);
INSERT INTO Held(HeldID, WillPluendern, StarkGegen, Name, WaffenStaerke) VALUES (14, 3, 21, 'Peter', 33);

-- Beschuetzer (B):
-- BesID Beschuetzt Name VertStaerke
-- (BID) (BS) (N) (VS)
-- 21 2 Juana 44
-- 22 2 Minnie 22
-- 23 5 Felicitas 33
-- 24 6 Catherine 11

INSERT INTO B(BID, BS, N, VS) VALUES (21, 2, 'Juana', 44);
INSERT INTO B(BID, BS, N, VS) VALUES (22, 2, 'Minnie', 22);
INSERT INTO B(BID, BS, N, VS) VALUES (23, 5, 'Felicitas', 33);
INSERT INTO B(BID, BS, N, VS) VALUES (24, 6, 'Catherine', 11);

INSERT INTO Beschuetzer(BesID, Beschuetzt, Name, VertStaerke) VALUES (21, 2, 'Juana', 44);
INSERT INTO Beschuetzer(BesID, Beschuetzt, Name, VertStaerke) VALUES (22, 2, 'Minnie', 22);
INSERT INTO Beschuetzer(BesID, Beschuetzt, Name, VertStaerke) VALUES (23, 5, 'Felicitas', 33);
INSERT INTO Beschuetzer(BesID, Beschuetzt, Name, VertStaerke) VALUES (24, 6, 'Catherine', 11);


