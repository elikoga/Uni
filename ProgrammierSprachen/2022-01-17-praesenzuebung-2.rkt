;; Die ersten drei Zeilen dieser Datei wurden von DrRacket eingefügt. Sie enthalten Metadaten
;; über die Sprachebene dieser Datei in einer Form, die DrRacket verarbeiten kann.
#reader(lib "beginner-reader.rkt" "deinprogramm" "sdp")((modname 2022-01-17-praesenzuebung-2) (read-case-sensitive #f) (teachpacks ((lib "image.rkt" "teachpack" "deinprogramm" "sdp"))) (deinprogramm-settings #(#f write repeating-decimal #f #t none explicit #f ((lib "image.rkt" "teachpack" "deinprogramm" "sdp")))))
(define language "your-worst-nightmare")

; calculate fahrenheit from celcius
; 0c = 32f
; 1c = 32 + (9/5)f

(: celcius-to-fahrenheit (real -> real))

(define celcius-to-fahrenheit
  (lambda (celcius)
    (+ 32 (* celcius 9/5))))

(check-expect (celcius-to-fahrenheit 0) 32)
(check-expect (celcius-to-fahrenheit 1) (+ 32 (/ 9 5)))

(: fahrenheit-celcius-convert (string real -> real))

(check-expect (fahrenheit-celcius-convert "C" 0) 32)
(check-expect (fahrenheit-celcius-convert "C" 1) (+ 32 (/ 9 5)))
(check-expect (fahrenheit-celcius-convert "F" 32) 0)
(check-expect (fahrenheit-celcius-convert "F" (+ 32 (/ 9 5))) 1)

(define fahrenheit-celcius-convert
  (lambda (unit input)
    (cond ((string=? unit "C") (celcius-to-fahrenheit input))
          ((string=? unit "F") 
            (/ (- input 32) 9/5)))))

; Aufgabe 2
; a)
; (: + (number number -> number))
; b)
; (: fuck-you ((natural -> integer) natural natural -> integer))

; Aufgabe 3
(define-record empty-list
  make-empty-list
  empty?)

(define-record cons-list-of-numbers
  cons
  cons?
  (first number)
  (rest list-of-numbers))

(define list-of-numbers
  (signature
   (mixed empty-list
          cons-list-of-numbers)))

(: sum-list (list-of-numbers -> number))

(define sum-list
  (lambda (list)
    (cond
      ((empty? list) 0)
      (else (+ (first list) (sum-list (rest list)))))))

(check-expect (sum-list (make-empty-list)) 0)
(check-expect (sum-list (cons 1 (make-empty-list))) 1)
(check-expect (sum-list (cons 1 (cons 2 (make-empty-list)))) 3)

(: length-list (list-of-numbers -> number))

(define length-list
  (lambda (list)
    (cond
      ((empty? list) 0)
      (else (+ 1 (length-list (rest list)))))))

(: average-list (list-of-numbers -> number))

(define average-list
  (lambda (list)
    (/ (sum-list list) (length-list list))))

; (check-expect (average-list (make-empty-list)) 0)
; undefined should be undefined
(check-expect (average-list (cons 1 (make-empty-list))) 1)
(check-expect (average-list (cons 1 (cons 2 (make-empty-list)))) 1.5)

;Schreiben Sie eine Funktion, die die Standardabweichung berechnet.
; σ : Standardabweichung
; x_i : Zufallswerte
; μ : Mittelwert
; N : Größe

(: standard-deviation (list-of-numbers -> number))

(define standard-deviation
  (lambda (list)
    (sqrt
        (/
            (sum-list
                (map
                    (lambda (x)
                        (* 
                            (- x (average-list list)) 
                            (- x (average-list list))))
                    list))
            (length-list list)))))

(: map ((number -> number) list-of-numbers -> list-of-numbers))

(define map
    (lambda (func list)
        (cond
            ((empty? list) (make-empty-list))
            (else (cons (func (first list)) (map func (rest list)))))))

; (check-expect (standard-deviation (make-empty-list)) 0)
(check-expect (standard-deviation (cons 1 (make-empty-list))) 0)
(check-expect (standard-deviation (cons 1 (cons 2 (make-empty-list)))) 0.5)
(check-expect (standard-deviation (cons 3 (cons 2 (make-empty-list)))) 0.5)

; Ubung 4.
; Implementieren Sie eine Funktion, die
; a) ein neues Element vorne an eine Liste anfügt.
; b) die ersten 3 Werte einer Liste ausgibt.
; c) die eine ganze Zahl als Nutzereingabe (zur Laufzeit) entgegennimmt und deren Quadrat ausgibt.
; d) ein neues Element an die richtige Stelle einer sortierten Liste einfügt und diese ausgibt.

(: prepend (number list-of-numbers -> list-of-numbers))

(define prepend
  (lambda (number list)
    (cons number list)))

(: head-3 (list-of-numbers -> list-of-numbers))

(: head-n (number list-of-numbers -> list-of-numbers))

(define head-3
  (lambda (list)
    (head-n 3 list)))

(define head-n
  (lambda (n list)
    (cond
      ((empty? list) (make-empty-list))
      ((= n 0) (make-empty-list))
      (else (cons (first list) (head-n (- n 1) (rest list)))))))

(check-expect (head-3 (make-empty-list)) (make-empty-list))
(check-expect (head-3 (cons 1 (make-empty-list))) (cons 1 (make-empty-list)))
(check-expect (head-3 (cons 1 (cons 2 (make-empty-list)))) (cons 1 (cons 2 (make-empty-list))))
(check-expect (head-3 (cons 1 (cons 2 (cons 3 (make-empty-list))))) (cons 1 (cons 2 (cons 3 (make-empty-list)))))
(check-expect (head-3 (cons 1 (cons 2 (cons 3 (cons 4 (make-empty-list)))))) (cons 1 (cons 2 (cons 3 (make-empty-list)))))

(: square-custom (number -> number))

(define square-custom
  (lambda (x)
    (* x x)))

; read : (-> any)

(: square-interactive (-> number))

(define square-interactive
  (lambda ()
    (square-custom (read))))


(: insert-sorted (number list-of-numbers -> list-of-numbers))

(define insert-sorted
  (lambda (number list)
    (cond
      ((empty? list) (cons number (make-empty-list)))
      ((< number (first list)) (cons number list))
      (else (cons (first list) (insert-sorted number (rest list)))))))

(check-expect (insert-sorted 1 (make-empty-list)) (cons 1 (make-empty-list)))
(check-expect (insert-sorted 1 (cons 2 (make-empty-list))) (cons 1 (cons 2 (make-empty-list))))
(check-expect (insert-sorted 1 (cons 2 (cons 3 (make-empty-list)))) (cons 1 (cons 2 (cons 3 (make-empty-list)))))
(check-expect (insert-sorted 2 (cons 1 (cons 3 (make-empty-list)))) (cons 1 (cons 2 (cons 3 (make-empty-list)))))

; Übung 5.
; Schreiben Sie eine endrekursive Funktion, die die Fakult ̈at einer gegebenen ganzen Zahl berechnet.

(: factorial (natural -> natural))

(define factorial
  (lambda (n)
    (cond
      ((= n 0) 1)
      (else (* n (factorial (- n 1)))))))

; Ubung 6.
; Stellen Sie Schritt für Schritt den Zustand, also Namensraum, Stack und Heap, des folgenden Python-
; programms dar.
; 1| a = 0
; 2| b = 1
; 3| n = 3
; 4| def fibonacciAndIncr(a, b, n, c):
; 5|     c += 1
; 6|     if (n == 0):
; 7|         return (a, c)
; 8|     return fibonacciAndIncr(b, a + b, n - 1, c)
; 9| result = fibonacciAndIncr(a, b, n, 2)

; ---

; Ubung 7.
; Arithmetik
; Sie sollen einen Taschenrechner implementieren, der eine Liste im Format (Num Op Num Op ... Op Num)
; erh ̈alt und das Ergebnis berechnet. Num ist eine natürliche Zahl und Op ist ein Operator aus der Menge
; {+, -, ∗, /}. Die Idee besteht darin die Arithmetik rekursiv auszuführen, indem wir das erste Element
; und den ersten Operator in der Liste lesen und diese auf die Restliste anwenden. Ein Aufruf (calc (Num1
; Op1 Num2 Op2 ...)) f ̈uhrt damit zur Auswertung (Op1 Num1 (Op2 Num2 (Op3 Num3) ... )).
; a) ̈Ubernehmen Sie die Listendefinition aus der Vorlesung. In der jetzigen Version kann diese jedoch
; nur Werte des Typs number enthalten. Verändern Sie die Definition dahingehend, dass auch Werte
; vom Typ string in der Liste enthalten sein k ̈onnen.
; 
; b) Sie sollen nun einen Rahmen für die Funktion bauen, in dem wir entscheiden, ob wir als nächstes
; eine Addition, eine Subtraktion, eine Multiplikation oder eine Division durchführen m ̈ussen oder
; ob das n ̈achste Element bereits das letzte Element der Liste ist. Implementieren Sie einen Funkti-
; onsrahmen für die Funktion calc. Verwenden Sie eine Fallunterscheidung.
;
; c) Implementieren Sie nun die arithmetischen Funktionen des Taschenrechners und geben Sie im
; else Fall eine Fehlermeldung aus.
;
; d) Schreiben Sie check-expects f ̈ur die arithmetischen Ausdrücke 4 - 5 + 3 und 5 * 3 + 6
; und setzen Sie Klammern in den Ausdrücken um zu verdeutlichen wie diese ausgewertet werden.
;
; e) Korrigieren Sie mögliches Fehlverhalten.e

; a)

; (define-record empty-list
;   make-empty-list
;   empty?)

(define-record cons-list-of-numbers-and-strings
    cons-n
    cons-n?
    (first-n (mixed number string))
    (rest-n list-of-numbers-and-strings))

(define list-of-numbers-and-strings
  (signature (mixed
              empty-list
              cons-list-of-numbers-and-strings)))

; b) c)

(: calc (list-of-numbers-and-strings -> number))

(define calc
    (lambda (list)
      (cond
        ((empty? list) (violation "calc: empty list"))
        ((cons-n? list) (cond
            (; if the tail is empty, last number just return that
                (empty? (rest-n list))
                (first-n list))
            (; case +
                (string=? (first-n (rest-n list)) "+")
                (+ (first-n list) (calc (rest-n (rest-n list)))))
            (; case -
                (string=? (first-n (rest-n list)) "-")
                (- (first-n list) (calc (rest-n (rest-n list)))))
            (; case *
                (string=? (first-n (rest-n list)) "*")
                (* (first-n list) (calc (rest-n (rest-n list)))))
            (; case /
                (string=? (first-n (rest-n list)) "/")
                (/ (first-n list) (calc (rest-n (rest-n list)))))
            (else (violation "calc: invalid operator")))))))

; d)

; 4 - 5 + 3 und 5 * 3 + 6

; umgeformt

; ((4 - 5) + 3) und ((5 * 3) + 6)

; (+ (- 4 5) 3) und (+ (* 5 3) 6)

; (3 + (4 - 5)) und (6 + (5 * 3))

(check-expect (calc (cons-n 3 (cons-n "+" (cons-n 4 (cons-n "-" ( cons-n 5 (make-empty-list))))))) (+ (- 4 5) 3))
(check-expect (calc (cons-n 6 (cons-n "+" (cons-n 5 (cons-n "*" ( cons-n 3 (make-empty-list))))))) (+ (* 5 3) 6))
