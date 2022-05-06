;; Die ersten drei Zeilen dieser Datei wurden von DrRacket eingefügt. Sie enthalten Metadaten
;; über die Sprachebene dieser Datei in einer Form, die DrRacket verarbeiten kann.
#reader(lib "vanilla-reader.rkt" "deinprogramm" "sdp")((modname 2022-01-23-racket-heimblatt-3) (read-case-sensitive #f) (teachpacks ()) (deinprogramm-settings #(#f write repeating-decimal #f #t none explicit #f ())))
(define language "sdpanfänger")

; ASCII-Art
; Implementieren Sie je eine Funktion, die die in Abbildung 1, Abbildung 2 und Abbildung 3 gezeig-
; ten pattern auf die Kommandozeile drucken. (Benutzen Sie dazu Rekursion und Fallunterscheidungen.)

; ##########
; ##########
; ##########
; ##########
; ##########
; ##########
; ##########
; ##########
; ##########
; ##########
; Abbildung 1: Pattern A
; ##########
; #        #
; #        #
; #        #
; #        #
; #        #
; #        #
; #        #
; #        #
; ##########
; Abbildung 2: Pattern B
; ##########
; ##       #
; # #      #
; #  #     #
; #   #    #
; #    #   #
; #     #  #
; #      # #
; #       ##
; ##########
; Abbildung 3: Pattern C

; write-string : (string -> unspecific)
; write-newline : (-> unspecific)


(: pattern-a-n-m (natural natural -> string))

(define pattern-a-n-m
  (lambda (n m)
    (cond ((= n 0) "")
          ((= m 1) (string-append "#" (pattern-a-n-m (- n 1) 1)))
          (else (string-append (pattern-a-n-m n 1) "\n"
                               (pattern-a-n-m n (- m 1)))))))

(: pattern-a-n (natural -> string))

(define pattern-a-n
  (lambda (n) (string-append (pattern-a-n-m n n) "\n")))


(define pattern-a (lambda () (write-string (pattern-a-n 10))))

(write-string "Pattern A:\n")
(pattern-a)

(: repeat-n (natural string -> string))




(define pattern-b (lambda () (write-string (pattern-b-n 10))))

(: pattern-b-n (natural -> string))

(define pattern-b-n
  (lambda (n) (pattern-b-from-n 1 10)))

(define repeat-n
  (lambda (n s)
    (cond ((= n 0) "")
          (else (string-append (repeat-n (- n 1) s) s)))))

(: pattern-b-from-n (natural natural -> string))

(define pattern-b-from-n
  (lambda (from n)
    (cond ((= from 1) (string-append (repeat-n n "#") "\n" (pattern-b-from-n (+ from 1) n)))
          ((= from n) (string-append (repeat-n n "#") "\n"))
          (else (string-append "#" (repeat-n (- n 2) " ") "#\n"
                                (pattern-b-from-n (+ from 1) n))))))

(write-string "Pattern B:\n")
(pattern-b)


(define pattern-c (lambda () (write-string (pattern-c-n 10))))

(: pattern-c-n (natural -> string))

(define pattern-c-n (lambda (n) (pattern-c-from-n 1 n)))

(: pattern-c-from-n (natural natural -> string))

(define pattern-c-from-n
  (lambda (from n)
    (cond ((= from 1) (string-append (repeat-n n "#") "\n" (pattern-c-from-n (+ from 1) n)))
          ((= from n) (string-append (repeat-n n "#") "\n"))
          (else (string-append "#" (repeat-n (- from 2) " ") "#" (repeat-n (- (- n 2) (+ (- from 2) 1)) " ") "#\n"
                                (pattern-c-from-n (+ from 1) n))))))

(write-string "Pattern C:\n")
(pattern-c)

; Übung 2

; binomial
(: binomial (natural natural -> natural))

(define binomial
  (lambda (n k)
    (cond ((= k 0) 1)
          ((= k n) 1)
          (else (+ (binomial (- n 1) k) (binomial (- n 1) (- k 1)))))))

; pascal triangle
(: pascal-triangle (natural -> string))
(: pascal-row (natural -> string))
(: pascal-row-helper (natural natural -> string))

(define pascal-triangle 
  (lambda (n)
    (cond ((= n 0) (pascal-row 0))
          (else (string-append (pascal-triangle (- n 1)) "\n" (pascal-row n))))))

(define pascal-row-helper ; n = row, k = columns to print left
  (lambda (n k)
    (cond ((= k 0) (number->string (binomial n k)))
          (else 
            (string-append 
              (pascal-row-helper n (- k 1))
              " "
              (number->string (binomial n k)))))))

(define pascal-row (lambda (n)
  (pascal-row-helper n n)))

; (write-string (pascal-triangle 10))

; read : (-> any)

; read number then print pascal triangle
(define read-pascal-triangle (lambda ()
  (write-string (string-append (pascal-triangle (read)) "\n"))))

(read-pascal-triangle)

; Übung 3

; random : (natural -> natural)

(: integrate ((real -> real) natural real real -> real))
; takes function to integrate, number of samples, lower bound, upper bound

(: random-real (real real -> real))

; use random natural smaller than 1000000000

(: random-precision natural)

(define random-precision 1000000000)

(define random-real
  (lambda (lower upper)
    (+
      lower
      (*
        (- upper lower)
        (/
          (random random-precision)
          random-precision)))))

(define integrate
  (lambda (f n a b)
    (cond
      ((= n 1) (f (random-real a b)))
      (else 
        (/
          (+ 
            (* (integrate f (- n 1) a b) (- n 1))
            (f (random-real a b)))
          n)))))

; integral from 0 to 1 of \frac{4}{1+x^2}

(write-string 
  (number->string
    (exact->inexact
      (integrate 
        (lambda (x) 
          (/ 4 (+ 1 (* x x)))) 
          50
          0
          1))))
