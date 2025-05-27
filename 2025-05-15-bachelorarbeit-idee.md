Bachelorarbeit Idee: Nix Expression Generation using LLMs

Evaluation von vortrainierten Language Modellen zur Generierung von Nix-Ausdrücken

Potentiell Training/Fine-Tuning von einem Modell zur Generierung von Nix-Ausdrücken

## Hintergrund

- Eelco Dolstra, Merijn de Jonge, and Eelco Visser – Utrecht University, "Nix: A Safe and Policy-Free System for Software Deployment"
  - Describes the Nix package manager and its purely functional deployment model.
  - Cited 148 times
- Eelco Dolstra, PhD Thesis, "The Purely Functional Software Deployment Model"
  - Describes Nix, Nixpkgs and NixOS (in the works)
  - Cited 104 times
- Nix is a purely functional package manager that allows for reproducible builds and deployments.
- Nix expressions are used to define packages and their dependencies in a declarative manner.
- The nixpkgs repository contains a large collection of Nix expressions for various software packages.
- One could use the nixpkgs repository as a dataset for training and evaluating models for Nix expression generation.

## Ansatz

- Collect a dataset of Nix expressions from the nixpkgs repository.
- Extract structured features from the source repositories, such as package metadata, dependencies, and build instructions
- Evaluate pretrained models using in-context learning to generate Nix expressions based on the extracted features.
- Explore fine-tuning or training approaches to improve the quality of generated Nix expressions.

---

Deutsch:

# Bachelorarbeit Idee: Nix Expression Generation using LLMs

Evaluation von vortrainierten Language Modellen zur Generierung von Nix-Ausdrücken

Potentiell Training/Fine-Tuning von einem Modell zur Generierung von Nix-Ausdrücken

## Hintergrund

- Eelco Dolstra, Merijn de Jonge, and Eelco Visser – Utrecht University, "Nix: A Safe and Policy-Free System for Software Deployment"
  - Beschreibt den Nix Paketmanager und sein rein funktionales Deployment-Modell.
  - 148 Zitationen
- Eelco Dolstra, PhD Thesis, "The Purely Functional Software Deployment Model"
  - Beschreibt Nix, Nixpkgs und NixOS
  - 104 Zitationen
- Nix ist ein rein funktionaler Paketmanager, der reproduzierbare Builds und Deployments ermöglicht.
- Nix-Ausdrücke werden verwendet, um Pakete, deren Abhängigkeiten und Build-Anweisungen deklarativ zu definieren.
- Das nixpkgs Repository enthält eine große Sammlung von Nix-Ausdrücken für verschiedene Softwarepakete
- Man kann das nixpkgs Repository als Datensatz für das Training und die Evaluation von Modellen zur Generierung von Nix-Ausdrücken verwenden.

## Ansatz

- Sammeln eines Datensatzes von Nix-Ausdrücken aus dem nixpkgs Repository.
- Extrahieren von strukturierten Merkmalen aus den Quell-Repositories, wie z.B. Paket-Metadaten, Abhängigkeiten und Build-Anweisungen.
- Evaluieren von vortrainierten Modellen mittels In-Context Learning zur Generierung von Nix-Ausdrücken basierend auf den extrahierten Merkmalen.
- (potentiell, falls vom Außmaß möglich): Erforschen von Fine-Tuning oder Trainings-Ansätzen zur Verbesserung der Qualität der generierten Nix-Ausdrücke.

---

# Mögliche Betreuer

Software Engineering:

- Bodden
- Stefan Sauer
- SICP
  - Postdocs:
    - Simon Oberthür
    - Gunnar Schomaker
    - Dennis Wolters

AI/ML:

- Data Science FG bei Ngonga
  - FG Anfragen, wer in Frage kommt
- Heindorf

---

