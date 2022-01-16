;; Die ersten drei Zeilen dieser Datei wurden von DrRacket eingefügt. Sie enthalten Metadaten
;; über die Sprachebene dieser Datei in einer Form, die DrRacket verarbeiten kann.
#reader(lib "beginner-reader.rkt" "deinprogramm" "sdp")((modname 2022-01-15-racket-heimblatt-2) (read-case-sensitive #f) (teachpacks ((lib "image.rkt" "teachpack" "deinprogramm" "sdp"))) (deinprogramm-settings #(#f write repeating-decimal #f #t none explicit #f ((lib "image.rkt" "teachpack" "deinprogramm" "sdp")))))
(define pi (* 2 (acos 0)))

; calculate the circumference of a circle from the radius

(: circle-circumference (real -> real))

(define circle-circumference
  (lambda (r)
    (* 2 pi r)))

(check-expect (circle-circumference 0) 0)
(check-within (circle-circumference 1/2) pi 0.0001)

(: circle-area (real -> real))

(define circle-area
  (lambda (r)
    (* pi r r)))

(check-expect (circle-area 0) 0)
(check-within (circle-area 1) pi 0.0001)

(: sphere-volume (real -> real))

(define sphere-volume
  (lambda (r)
    (* 4/3 pi r r r)))

(check-expect (sphere-volume 0) 0)
(check-within (sphere-volume 1) (* 4/3 pi) 0.0001)

(define-record cartesian
  make-cartesian
  (cartesian-x real)
  (cartesian-y real))

(: cartesian-from-polar (real real -> cartesian))

(define cartesian-from-polar
  (lambda (r phi)
    (make-cartesian
     (* r (cos phi))
     (* r (sin phi)))))

(check-expect (cartesian-from-polar 0 3234) (make-cartesian 0 0))

(: leap-year? (integer -> boolean))

(define leap-year?
  (lambda (year)
    (cond
      ((not (= 0 (modulo year 4))) #f)
      ((not (= 0 (modulo year 100))) #t)
      ((= 0 (modulo year 400)) #t)
      (else #f))))

(check-expect (leap-year? 0) #t)
(check-expect (leap-year? 1) #f)
(check-expect (leap-year? 100) #f)
(check-expect (leap-year? 400) #t)

(define-record real-3
  make-real-3
  (real-3-x real)
  (real-3-y real)
  (real-3-z real))

(: real-3-length (real-3 -> real))

(define real-3-length
  (lambda (vec)
      (sqrt
       (+
        (* (real-3-x vec) (real-3-x vec))
        (* (real-3-y vec) (real-3-y vec))
        (* (real-3-z vec) (real-3-z vec))))))

(check-expect (real-3-length (make-real-3 3 4 0)) 5)

(: real-3-subtract (real-3 real-3 -> real-3))

(define real-3-subtract
  (lambda (vec1 vec2)
    (make-real-3
     (- (real-3-x vec1) (real-3-x vec2))
     (- (real-3-y vec1) (real-3-y vec2))
     (- (real-3-z vec1) (real-3-z vec2)))))

(: real-3-distance (real-3 real-3 -> real))

(define real-3-distance
  (lambda (vec1 vec2)
    (real-3-length
     (real-3-subtract vec1 vec2))))

(check-expect (real-3-distance (make-real-3 0 3 0) (make-real-3 4 0 0)) 5)

(define real-3-cross-product
  (lambda (vec1 vec2)
    (make-real-3
     (- (* (real-3-y vec1) (real-3-z vec2))
        (* (real-3-z vec1) (real-3-y vec2)))
     (- (* (real-3-z vec1) (real-3-x vec2))
        (* (real-3-x vec1) (real-3-z vec2)))
     (- (* (real-3-x vec1) (real-3-y vec2))
        (* (real-3-y vec1) (real-3-x vec2))))))


(check-expect
 (real-3-cross-product (make-real-3 1 2 3) (make-real-3 4 5 6))
 (make-real-3 -3 6 -3))

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

(define-record cons-list-of-strings
  make-cons-list-of-strings
  const-list-of-strings?
    (string-list-first string)
    (string-list-rest list-of-strings))

(define list-of-strings
  (signature
   (mixed empty-list
          cons-list-of-strings)))

; string-append exists

(: concat-list (list-of-strings -> string))

(define concat-list
  (lambda (list)
    (cond
      ((empty? list) "")
      (else (string-append (string-list-first list) (concat-list (string-list-rest list)))))))

(check-expect (concat-list (make-empty-list)) "")
(check-expect (concat-list (make-cons-list-of-strings "a" (make-empty-list))) "a")
(check-expect 
    (concat-list 
        (make-cons-list-of-strings "a" (make-cons-list-of-strings "b" (make-empty-list)))) 
    "ab")

; check wether string is in list with string=?

(: string-in-list? (string list-of-strings -> boolean))

(define string-in-list?
  (lambda (str list)
    (cond
      ((empty? list) #f)
      (else (or (string=? str (string-list-first list))
                (string-in-list? str (string-list-rest list)))))))

(check-expect (string-in-list? "a" (make-cons-list-of-strings "a" (make-empty-list))) #t)
(check-expect (string-in-list? "b" (make-cons-list-of-strings "a" (make-empty-list))) #f)

; greatest common divisor

(: ggt (integer integer -> integer))

(define ggt
  (lambda (a b)
    (cond
      ((= a b) a)
      ((> a b) (ggt (- a b) b))
      (else (ggt a (- b a))))))

(check-expect (ggt 4 2) 2)
(check-expect (ggt 2 4) 2)
(check-expect (ggt 6 3) 3)
(check-expect (ggt 3 6) 3)
(check-expect (ggt 23 4) 1)
(check-expect (ggt 82 4) 2)
