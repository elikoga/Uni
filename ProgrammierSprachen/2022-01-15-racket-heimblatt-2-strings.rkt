;; Die ersten drei Zeilen dieser Datei wurden von DrRacket eingefügt. Sie enthalten Metadaten
;; über die Sprachebene dieser Datei in einer Form, die DrRacket verarbeiten kann.
#reader(lib "beginner-reader.rkt" "deinprogramm" "sdp")((modname 2022-01-15-racket-heimblatt-2-strings) (read-case-sensitive #f) (teachpacks ((lib "image.rkt" "teachpack" "deinprogramm" "sdp"))) (deinprogramm-settings #(#f write repeating-decimal #f #t none explicit #f ((lib "image.rkt" "teachpack" "deinprogramm" "sdp")))))
(define language "your-worst-nightmare")

(define-record empty-list
  make-empty-list
  empty?)

(define-record cons-list-of-strings
  make-cons-list-of-strings
  cons-list-of-strings?
  (string-list-first string)
  (string-list-rest list-of-strings))

(define list-of-strings
  (signature
   (mixed empty-list
          cons-list-of-strings)))

(: list-without-last (list-of-strings -> list-of-strings))

(define list-without-last
  (lambda (list)
    (cond
      ((empty? (string-list-rest list)) (make-empty-list))
      (else (make-cons-list-of-strings (string-list-first list) (list-without-last (string-list-rest list)))))))

(: list-last (list-of-strings -> string))

(define list-last
  (lambda (list)
    (cond
      ((empty? (string-list-rest list)) (string-list-first list))
      (else (list-last (string-list-rest list))))))

(: concat-list (list-of-strings -> string))

(define concat-list
  (lambda (list)
    (cond
      ((empty? list) "")
      (else (string-append (string-list-first list) (concat-list (string-list-rest list)))))))

(check-expect (concat-list (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-cons-list-of-strings "c" (make-empty-list))))) "abc")

(: list-append (list-of-strings string -> list-of-strings))

(define list-append
  (lambda (list1 str)
    (cond
      ((empty? list1) (make-cons-list-of-strings str (make-empty-list)))
      (else (make-cons-list-of-strings (string-list-first list1) (list-append (string-list-rest list1) str))))))

(check-expect (list-append (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-empty-list))) "c") (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-cons-list-of-strings "c" (make-empty-list)))))

; normalize string-list by making all upper case letters lower case

(: string-to-lower-case (string -> string))

(define string-to-lower-case
  (lambda (str)
    (cond
      ((string=? str "A") "a")
      ((string=? str "E") "e")
      ((string=? str "B") "b")
      ((string=? str "G") "g")
      ((string=? str "C") "c")
      ((string=? str "D") "d")
      ((string=? str "F") "f")
      ((string=? str "H") "h")
      ((string=? str "I") "i")
      ((string=? str "J") "j")
      ((string=? str "K") "k")
      ((string=? str "L") "l")
      ((string=? str "M") "m")
      ((string=? str "N") "n")
      ((string=? str "O") "o")
      ((string=? str "P") "p")
      ((string=? str "Q") "q")
      ((string=? str "R") "r")
      ((string=? str "S") "s")
      ((string=? str "T") "t")
      ((string=? str "U") "u")
      ((string=? str "V") "v")
      ((string=? str "W") "w")
      ((string=? str "X") "x")
      ((string=? str "Y") "y")
      ((string=? str "Z") "z")
      (else str))))

(check-expect (string-to-lower-case "A") "a")
(check-expect (string-to-lower-case "B") "b")

(: normalize-string-list (list-of-strings -> list-of-strings))

(define normalize-string-list
  (lambda (list)
    (cond
      ((empty? list) (make-empty-list))
      (else (make-cons-list-of-strings (string-to-lower-case (string-list-first list)) (normalize-string-list (string-list-rest list)))))))

(check-expect (normalize-string-list (make-cons-list-of-strings "A" (make-cons-list-of-strings "B" (make-empty-list)))) (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-empty-list))))

(: first-char-after-prefix (list-of-strings string -> string))

(define first-char-after-prefix
  (lambda (prefix str)
    (cond
      ((string>=? str (string-append (concat-list prefix) "z")) "z")
      ((string>=? str (string-append (concat-list prefix) "y")) "y")
      ((string>=? str (string-append (concat-list prefix) "x")) "x")
      ((string>=? str (string-append (concat-list prefix) "w")) "w")
      ((string>=? str (string-append (concat-list prefix) "v")) "v")
      ((string>=? str (string-append (concat-list prefix) "u")) "u")
      ((string>=? str (string-append (concat-list prefix) "t")) "t")
      ((string>=? str (string-append (concat-list prefix) "s")) "s")
      ((string>=? str (string-append (concat-list prefix) "r")) "r")
      ((string>=? str (string-append (concat-list prefix) "q")) "q")
      ((string>=? str (string-append (concat-list prefix) "p")) "p")
      ((string>=? str (string-append (concat-list prefix) "o")) "o")
      ((string>=? str (string-append (concat-list prefix) "n")) "n")
      ((string>=? str (string-append (concat-list prefix) "m")) "m")
      ((string>=? str (string-append (concat-list prefix) "l")) "l")
      ((string>=? str (string-append (concat-list prefix) "k")) "k")
      ((string>=? str (string-append (concat-list prefix) "j")) "j")
      ((string>=? str (string-append (concat-list prefix) "i")) "i")
      ((string>=? str (string-append (concat-list prefix) "h")) "h")
      ((string>=? str (string-append (concat-list prefix) "g")) "g")
      ((string>=? str (string-append (concat-list prefix) "f")) "f")
      ((string>=? str (string-append (concat-list prefix) "e")) "e")
      ((string>=? str (string-append (concat-list prefix) "d")) "d")
      ((string>=? str (string-append (concat-list prefix) "c")) "c")
      ((string>=? str (string-append (concat-list prefix) "b")) "b")
      ((string>=? str (string-append (concat-list prefix) "a")) "a")
      ((string>=? str (string-append (concat-list prefix) "Z")) "Z")
      ((string>=? str (string-append (concat-list prefix) "Y")) "Y")
      ((string>=? str (string-append (concat-list prefix) "X")) "X")
      ((string>=? str (string-append (concat-list prefix) "W")) "W")
      ((string>=? str (string-append (concat-list prefix) "V")) "V")
      ((string>=? str (string-append (concat-list prefix) "U")) "U")
      ((string>=? str (string-append (concat-list prefix) "T")) "T")
      ((string>=? str (string-append (concat-list prefix) "S")) "S")
      ((string>=? str (string-append (concat-list prefix) "R")) "R")
      ((string>=? str (string-append (concat-list prefix) "Q")) "Q")
      ((string>=? str (string-append (concat-list prefix) "P")) "P")
      ((string>=? str (string-append (concat-list prefix) "O")) "O")
      ((string>=? str (string-append (concat-list prefix) "N")) "N")
      ((string>=? str (string-append (concat-list prefix) "M")) "M")
      ((string>=? str (string-append (concat-list prefix) "L")) "L")
      ((string>=? str (string-append (concat-list prefix) "K")) "K")
      ((string>=? str (string-append (concat-list prefix) "J")) "J")
      ((string>=? str (string-append (concat-list prefix) "I")) "I")
      ((string>=? str (string-append (concat-list prefix) "H")) "H")
      ((string>=? str (string-append (concat-list prefix) "G")) "G")
      ((string>=? str (string-append (concat-list prefix) "F")) "F")
      ((string>=? str (string-append (concat-list prefix) "E")) "E")
      ((string>=? str (string-append (concat-list prefix) "D")) "D")
      ((string>=? str (string-append (concat-list prefix) "C")) "C")
      ((string>=? str (string-append (concat-list prefix) "B")) "B")
      ((string>=? str (string-append (concat-list prefix) "A")) "A"))))

(check-expect (first-char-after-prefix (make-cons-list-of-strings "n" (make-cons-list-of-strings "c" (make-empty-list))) "ncg") "g")

(check-expect (first-char-after-prefix (make-cons-list-of-strings "n" (make-cons-list-of-strings "c" (make-empty-list))) "ncgO") "g")

(: split-string-helper (list-of-strings string -> list-of-strings))

(define split-string-helper
  (lambda (prefix str)
    (cond
      (; if we have determined all characters, the concatenation of the prefix is the str
       (string=? str (concat-list prefix))
       prefix)
      (else ; determine the next character and recurse
       (split-string-helper (list-append prefix (first-char-after-prefix prefix str)) str)))))

(check-expect (split-string-helper (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-empty-list))) "abc") (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-cons-list-of-strings "c" (make-empty-list)))))

(: split-string (string -> list-of-strings))

(define split-string
  (lambda (str)
    (split-string-helper (make-empty-list) str)))

(check-expect (split-string "abc") (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-cons-list-of-strings "c" (make-empty-list)))))


; now let's test this

(check-expect
 (split-string "abcd")
 (make-cons-list-of-strings "a"
                            (make-cons-list-of-strings "b"
                                                       (make-cons-list-of-strings "c"
                                                                                  (make-cons-list-of-strings "d"
                                                                                                             (make-empty-list))))))

(: palindrome-list? (list-of-strings -> boolean))

(define palindrome-list?
  (lambda (list)
    (cond
      ((empty? list) #t)
      ((empty? (string-list-rest list)) #t)
      (else (and
             (string=? (string-list-first list) (list-last list))
             (palindrome-list? (list-without-last (string-list-rest list))))))))

(: palindrome? (string -> boolean))

(define palindrome?
  (lambda (str); convert to list then check
    (palindrome-list? (normalize-string-list (split-string str)))))

(check-expect
 (palindrome? "a")
 #t)
(check-expect
 (palindrome? "ab")
 #f)
(check-expect
 (palindrome? "aba")
 #t)
(check-expect
 (palindrome? "abab")
 #f)
(check-expect
 (palindrome? "ababa")
 #t)
(check-expect
 (palindrome? "ababab")
 #f)
(check-expect
 (palindrome? "aBbA")
 #t)
(check-expect
 (palindrome? "aBbAb")
 #f)

