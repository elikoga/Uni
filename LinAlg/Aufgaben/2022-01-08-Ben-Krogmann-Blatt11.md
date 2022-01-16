# Aufgabe 62
- $3x^2+2x+1\mapsto x^2+2x+3$
- $x^2+3x+2\mapsto2x^2+3x+1$
- $2x^2+x+3\mapsto3x^2+x+2$

---

## 1)
$\begin{cases}a3x^2+bx^2+c2x^2=x^2\\a2x+b3x+cx=2x\\a+2b+3c=3\end{cases}$

$\begin{pmatrix}3x^2&x^2&2x^2&|&x^2\\2x&3x&x&|&2x\\1&2&3&|&3\end{pmatrix}$
$\overset{I\cdot\frac1{x^2},II\cdot\frac1x}\leadsto\begin{pmatrix}3&1&2&|&1\\2&3&1&|&2\\1&2&3&|&3\end{pmatrix}$
$\overset{I-3III,II-2III}\leadsto\begin{pmatrix}0&-5&-7&|&-8\\0&-1&-5&|&-4\\1&2&3&|&3\end{pmatrix}$
$\overset{I-5II,III+2II}\leadsto\begin{pmatrix}0&0&18&|&12\\0&-1&-5&|&-4\\1&0&-7&|&-5\end{pmatrix}$
$\overset{I\cdot\frac1{18},II\cdot(-1)}\leadsto\begin{pmatrix}0&0&1&|&\frac23\\0&1&5&|&4\\1&0&-7&|&-5\end{pmatrix}$
$\overset{II-5I,III+7I}\leadsto\begin{pmatrix}0&0&1&|&\frac23\\0&1&0&|&\frac23\\1&0&0&|&-\frac13\end{pmatrix}$

Test
$-\frac13(3x^2+2x+1)+\frac23(x^2+3x+2)+\frac23(2x^2+x+3)=(-x^2-\frac23x-\frac13)+(\frac23x^2+2x+\frac43)+(\frac43x^2+\frac23x+2)=x^2+2x+3$

## 2)
$\begin{pmatrix}3&1&2&|&2\\2&3&1&|&3\\1&2&3&|&1\end{pmatrix}$
$\overset{I-3III,II-2III}\leadsto\begin{pmatrix}0&-5&-7&|&-1\\0&-1&-5&|&1\\1&2&3&|&1\end{pmatrix}$
$\overset{I-5II,III+2II}\leadsto\begin{pmatrix}0&0&18&|&-6\\0&-1&-5&|&1\\1&0&-7&|&3\end{pmatrix}$
$\overset{I\cdot\frac1{18},II\cdot(-1)}\leadsto\begin{pmatrix}0&0&1&|&-\frac13\\0&1&5&|&-1\\1&0&-7&|&3\end{pmatrix}$
$\overset{II-5I,III+7I}\leadsto\begin{pmatrix}0&0&1&|&-\frac13\\0&1&0&|&\frac23\\1&0&0&|&\frac23\end{pmatrix}$

Test
$\frac23(3x^2+2x+1)+\frac23(x^2+3x+2)-\frac13(2x^2+x+3)=(2x^2+
\frac43x+\frac23)+(\frac23x^2+2x+\frac43)+(-\frac23x^2-\frac13x-1)=2x^2+3x+1$

## 3)
$\begin{pmatrix}3&1&2&|&3\\2&3&1&|&1\\1&2&3&|&2\end{pmatrix}$
$\overset{I-3III,II-2III}\leadsto\begin{pmatrix}0&-5&-7&|&-3\\0&-1&-5&|&-3\\1&2&3&|&2\end{pmatrix}$
$\overset{I-5II,III+2II}\leadsto\begin{pmatrix}0&0&18&|&12\\0&-1&-5&|&-3\\1&0&-7&|&-4\end{pmatrix}$
$\overset{I\cdot\frac1{18},II\cdot(-1)}\leadsto\begin{pmatrix}0&0&1&|&\frac23\\0&1&5&|&3\\1&0&-7&|&-4\end{pmatrix}$
$\overset{II-5I,III+7I}\leadsto\begin{pmatrix}0&0&1&|&\frac23\\0&1&0&|&-\frac13\\1&0&0&|&\frac23\end{pmatrix}$

Test
$\frac23(3x^2+2x+1)-\frac13(x^2+3x+2)+\frac23(2x^2+x+3)=(2x^2+\frac43x+\frac23)+(-\frac13x^2-x-\frac23)+(\frac43x^2+\frac23x+2)=3x^2+x+2$


---

dunno ob es auch einfacher geht

$[f]^C_C=\begin{pmatrix}-\frac13&\frac23&\frac23\\\frac23&\frac23&-\frac13\\\frac23&-\frac13&\frac23\end{pmatrix}$

# Aufgabe 64
1. $\sigma\tau=\begin{pmatrix}1&2&3&4&5&6&7\\3&5&2&1&6&7&4\end{pmatrix}$
2. $\tau\sigma=\begin{pmatrix}1&2&3&4&5&6&7\\7&1&2&3&6&4&5\end{pmatrix}$
3. $\sigma^{-1}=\begin{pmatrix}1&2&3&4&5&6&7\\2&3&4&6&7&5&1\end{pmatrix}$
4. $\tau^{-1}=\begin{pmatrix}1&2&3&4&5&6&7\\7&6&5&2&1&3&4\end{pmatrix}$
5. $sgn(\sigma)=(-1)^{t(\sigma)}$
   1. $t(\sigma)=|\{1\leq i<j\leq n|\sigma(i)>\sigma(j)\}|$
   2. $=|\{(1,5),(1,6),(1,7),(2,3),(2,4),(2,5),\\(2,6),(2,7),(3,4),(3,5),(3,6),(3,7),\\(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)\}|$
   3. $=18$
   4. $\implies sgn(\sigma)=(-1)^{18}=1$
6. $sgn(\tau)=(-1)^{t(\tau)}$
   1. $t(\tau)=|\{1\leq i<j\leq n|\tau(i)>\tau(j)\}|$
   2. $=|\{(1,2),(1,5),(1,6),(1,7),(2,5),(2,6),\\(2,7),(3,5),(3,6),(3,7),(4,5),(4,6)\\,(4,7),(5,6),(5,7),(6,7)\}|$
   3. $=16$
   4. $\implies sgn(\tau)=(-1)^{16}=1$

# Aufgabe 65
$\sigma=\begin{pmatrix}1&2&3&4&5\\2&3&5&1&4\end{pmatrix}$

ist es echt so einfach?

# Aufgabe 66
## 1)
- falls $i=3,k=8$
  - $t(\sigma)=5$
- falls $i=8,k=3$
  - $t(\sigma)=8$

$\implies i=8,k=3$

## 2)
- falls $i=3,k=6$
  - $t(\tau)=3$
- falls $i=6,k=3$
  - $t(\tau)=6$

$\implies i=3,k=6$