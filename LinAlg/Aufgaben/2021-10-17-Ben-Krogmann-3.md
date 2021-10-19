# Aufgabe 1
Nur $A\vec c$ liefert ein Ergebnis, da die anderen beiden Vektoren zu wenige Elemente haben, um ein Multiplikation ausführen zu können.

$A\vec c=\begin{pmatrix}1&-2&3&5\\-2&1&0&7\\0&2&4&-1\end{pmatrix}\begin{pmatrix}1\\2\\-1\\3\end{pmatrix}=\begin{pmatrix}1-4-3+15\\-2+2+0+21\\0+4-4-3\end{pmatrix}=\begin{pmatrix}9\\21\\-3\end{pmatrix}$

# Aufgabe 2
$\forall a\in Mat_{m\times n}(\mathbb R),\vec x\in\mathbb R^n,\lambda\in\mathbb R:A(\lambda\vec x)=\lambda(A\vec x)$

$\begin{aligned}
    &A(\lambda\vec x)\\
    =&A\begin{pmatrix}\lambda x_1\\...\\\lambda x_n\end{pmatrix}\\
    =&\begin{pmatrix}a_{11}&...&a_{1n}\\...\\a_{m1}&...&a_{mn}\end{pmatrix}\begin{pmatrix}\lambda x_1\\...\\\lambda x_n\end{pmatrix}\\
    =&\begin{pmatrix}a_{11}(\lambda x_1)&+...+&a_{1n}(\lambda x_n)\\...\\a_{m1}(\lambda x_1)&+...+&a_{mn}(\lambda x_n)\end{pmatrix}\\
    =&\begin{pmatrix}(a_{11}x_1)\lambda&+...+&(a_{1n}x_n)\lambda\\...\\(a_{m1}x_1)\lambda&+...+&(a_{mn}x_n)\lambda\end{pmatrix}\\
    =&\lambda\begin{pmatrix}a_{11}x_1&+...+&a_{1n}x_n\\...\\a_{m1}x_1&+...+&a_{mn}x_n\end{pmatrix}\\
    =&\lambda(A\vec x)
\end{aligned}$

# Aufgabe 3
## 1)
$\begin{aligned}
    &\begin{pmatrix}1&-2&3&-4&|&4\\0&1&-1&1&|&-3\\1&3&0&-3&|&1\\0&-7&3&1&|&-3\end{pmatrix}\\
    \overset{III-I,IV+7II}\iff&\begin{pmatrix}1&-2&3&-4&|&4\\0&1&-1&1&|&-3\\0&5&-3&1&|&-3\\0&0&-4&8&|&18\end{pmatrix}\\
    \overset{III-5II}\iff&\begin{pmatrix}1&-2&3&-4&|&4\\0&1&-1&1&|&-3\\0&0&2&-4&|&12\\0&0&-4&8&|&18\end{pmatrix}\\
    \overset{IV+2III}\iff&\begin{pmatrix}1&-2&3&-4&|&4\\0&1&-1&1&|&-3\\0&0&2&-4&|&12\\0&0&0&0&|&42\end{pmatrix}
\end{aligned}$

Da $0x_1+0x_2+0x_3+0x_4=0\not=42$, hat dieses System keine Lösung.

## 2)
$\begin{aligned}
    &\begin{pmatrix}1&-2&1&1&|&1\\1&-2&1&-1&|&-1\\1&-2&1&5&|&5\end{pmatrix}\\
    \overset{II-I,III-I}\iff&\begin{pmatrix}1&-2&1&1&|&1\\0&0&0&-2&|&-2\\0&0&0&4&|&4\end{pmatrix}\\
    \overset{II\cdot(-\frac12)}\iff&\begin{pmatrix}1&-2&1&1&|&1\\0&0&0&1&|&1\\0&0&0&4&|&4\end{pmatrix}\\
    \overset{I-II,III-4II}\iff&\begin{pmatrix}1&-2&1&0&|&0\\0&0&0&1&|&1\\0&0&0&0&|&0\end{pmatrix}
\end{aligned}$

$\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}=\begin{pmatrix}2x_2-x_3\\\frac12x_1+\frac12x_3\\-x_1+2x_2\\1\end{pmatrix}=\begin{pmatrix}0\\0\\0\\1\end{pmatrix}+x_1\begin{pmatrix}0\\\frac12\\-1\\0\end{pmatrix}+x_2\begin{pmatrix}2\\0\\2\\0\end{pmatrix}+x_3\begin{pmatrix}-1\\\frac12\\0\\0\end{pmatrix}$

$Lös(2)=\begin{pmatrix}0\\0\\0\\1\end{pmatrix}+\alpha\begin{pmatrix}0\\\frac12\\-1\\0\end{pmatrix}+\beta\begin{pmatrix}2\\0\\2\\0\end{pmatrix}+\gamma\begin{pmatrix}-1\\\frac12\\0\\0\end{pmatrix}$ mit $\alpha,\beta,\gamma\in\mathbb R$

### Test
$\alpha=0,\beta=0,\gamma=0$

$\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}=\begin{pmatrix}0\\0\\0\\1\end{pmatrix}\implies\begin{cases}0+0+0+1=1\\0+0+0-1=-1\\0+0+0+5=5\end{cases}$

## 3)
$\begin{aligned}
    &\begin{pmatrix}1&3&5&7&|&12\\3&5&7&1&|&0\\5&7&1&3&|&4\\7&1&3&5&|&16\end{pmatrix}\\
    \overset{II-3I,III-5I,IV-7I}\iff&\begin{pmatrix}1&3&5&7&|&12\\0&-4&-8&-20&|&-36\\0&-8&-24&-32&|&-56\\0&-20&-32&-44&|&-68\end{pmatrix}\\
    \overset{II\cdot(-\frac14),III\cdot(-\frac18),IV\cdot(-\frac14)}\iff&\begin{pmatrix}1&3&5&7&|&12\\0&1&2&5&|&9\\0&1&3&4&|&7\\0&5&8&11&|&17\end{pmatrix}\\
    \overset{III-II,IV-5II}\iff&\begin{pmatrix}1&3&5&7&|&12\\0&1&2&5&|&9\\0&0&1&-1&|&-2\\0&0&-7&-9&|&-18\end{pmatrix}\\
    \overset{IV+7III}\iff&\begin{pmatrix}1&3&5&7&|&12\\0&1&2&5&|&9\\0&0&1&-1&|&-2\\0&0&0&-16&|&-32\end{pmatrix}\\
    \overset{IV\cdot(-\frac1{16})}\iff&\begin{pmatrix}1&3&5&7&|&12\\0&1&2&5&|&9\\0&0&1&-1&|&-2\\0&0&0&1&|&2\end{pmatrix}\\
    \overset{I-7IV,II-5IV,III+IV}\iff&\begin{pmatrix}1&3&5&0&|&-2\\0&1&2&0&|&-1\\0&0&1&0&|&0\\0&0&0&1&|&2\end{pmatrix}\\
    \overset{I-5III,II-2III}\iff&\begin{pmatrix}1&3&0&0&|&-2\\0&1&0&0&|&-1\\0&0&1&0&|&0\\0&0&0&1&|&2\end{pmatrix}\\
    \overset{I-3II}\iff&\begin{pmatrix}1&0&0&0&|&1\\0&1&0&0&|&-1\\0&0&1&0&|&0\\0&0&0&1&|&2\end{pmatrix}&
\end{aligned}$

$\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}=\begin{pmatrix}1\\-1\\0\\2\end{pmatrix}$

### Test
$\begin{cases}1-3+0+14=12\\3-5+0+2=0\\5-7+0+6=4\\7-1+0+10=16\end{cases}$

## 4)
$\begin{aligned}
    &\begin{pmatrix}-6&8&-5&-1&|&9\\-2&4&7&3&|&1\\-3&5&4&2&|&3\\-3&7&17&7&|&\lambda\end{pmatrix}\\
    \overset{II\cdot(-3),III\cdot(-2),IV\cdot(-2)}\iff&\begin{pmatrix}-6&8&-5&-1&|&9\\6&-12&-21&-9&|&-3\\6&-10&-8&-4&|&-6\\6&-14&-34&-14&|&-2\lambda\end{pmatrix}\\
    \overset{II+I,III+I,IV+I}\iff&\begin{pmatrix}-6&8&-5&-1&|&9\\0&-4&-26&-10&|&6\\0&-2&-13&-5&|&3\\0&-6&-39&-15&|&-2\lambda+9\end{pmatrix}\\
    \overset{II\leftrightarrow III}\iff&\begin{pmatrix}-6&8&-5&-1&|&9\\0&-2&-13&-5&|&3\\0&-4&-26&-10&|&6\\0&-6&-39&-15&|&-2\lambda+9\end{pmatrix}\\
    \overset{III-2II,IV-3II}\iff&\begin{pmatrix}-6&8&-5&-1&|&9\\0&-2&-13&-5&|&3\\0&0&0&0&|&0\\0&0&0&0&|&-2\lambda\end{pmatrix}\\
    \overset{I\cdot(-\frac16),II\cdot(-\frac12)}\iff&\begin{pmatrix}1&-\frac86&\frac56&\frac16&|&-\frac96\\0&1&\frac{13}2&\frac52&|&-\frac32\\0&0&0&0&|&-2\lambda\end{pmatrix}\\
    \overset{I+\frac43II}\iff&\begin{pmatrix}1&0&\frac{57}6&\frac{21}6&|&-\frac{21}6\\0&1&\frac{13}2&\frac52&|&-\frac32\\0&0&0&0&|&-2\lambda\end{pmatrix}
\end{aligned}$


$\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}=\begin{pmatrix}-\frac72-\frac{19}2x_3-\frac72x_4\\-\frac32-\frac{13}2x_3-\frac52x_4\\x_3\\x_4\end{pmatrix}=\begin{pmatrix}-\frac72\\-\frac32\\0\\0\end{pmatrix}+x_3\begin{pmatrix}-\frac{19}2\\-\frac{13}2\\1\\0\end{pmatrix}+x_4\begin{pmatrix}-\frac72\\-\frac52\\0\\1\end{pmatrix}$

Für $0=-2\lambda\implies\lambda=0$ hat das System die Lösung:

$\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}=\begin{pmatrix}-\frac72\\-\frac32\\0\\0\end{pmatrix}+\alpha\begin{pmatrix}-\frac{19}2\\-\frac{13}2\\1\\0\end{pmatrix}+\beta\begin{pmatrix}-\frac72\\-\frac52\\0\\1\end{pmatrix}$ mit $\alpha,\beta\in\mathbb R$

Für $\lambda\not=0$ hat das System keine Lösung.#

# Aufgabe 4
$f(x)=ax^3+bx^2+cx+d$

$\begin{aligned}
    &\begin{cases}a(-1)^3+b(-1)^2+c(-1)+d=0\\a0^3+b0^2+c0+d=1\\a1^3+b1^2+c1+d=2\\a2^3+b2^2+c2+d=4\end{cases}\\
    \iff&\begin{cases}-a+b-c+d=0\\d=1\\a+b+c+d=2\\8a+4b+2c+d=4\end{cases}\\
    \overset{I-II,III-II,IV-II}\iff&\begin{cases}-a+b-c=-1\\a+b+c=1\\8a+4b+2c=3\\d=1\end{cases}\\
    \overset{II+I,III+8I}\iff&\begin{cases}-a+b-c=-1\\2b=0\\12b-6c=-5\\d=1\end{cases}\\
    \overset{I\cdot(-1),II\cdot\frac12}\iff&\begin{cases}a-b+c=1\\b=0\\12b-6c=-5\\d=1\end{cases}\\
    \overset{III-12II,I+II}\iff&\begin{cases}a+c=1\\b=0\\-6c=-5\\d=1\end{cases}\\
    \overset{III\cdot(-\frac16)}\iff&\begin{cases}a+c=1\\b=0\\c=\frac56\\d=1\end{cases}\\
    \overset{I-III}\iff&\begin{cases}a=\frac16\\b=0\\c=\frac56\\d=1\end{cases}
\end{aligned}$

$\implies f(x)=\frac16x^3+\frac56x+1$

# Aufgabe 5


# Aufgabe 6
$A\vec a=\begin{pmatrix}1&+2&+3&+4&+...&+n\\0&+2&+3&+4&+...&+n\\0&+0&+3&+4&+...&+n\\0&+0&+0&+4&+...&+n\\...\\0&+0&+0&+0&+...&+n\end{pmatrix}=\begin{pmatrix}\sum_{k=1}^nk\\\sum_{k=2}^nk\\\sum_{k=3}^nk\\\sum_{k=4}^nk\\...\\\sum_{k=1}^nk\end{pmatrix}$

$A\vec b=\begin{pmatrix}1&+2^3&+3^3&+4^3&+...&+n^3\\0&+2^3&+3^3&+4^3&+...&+n^3\\0&+0&+3^3&+4^3&+...&+n^3\\0&+0&+0&+4^3&+...&+n^3\\...\\0&+0&+0&+0&+...&+n^3\end{pmatrix}=\begin{pmatrix}\sum_{k=1}^nk^3\\\sum_{k=2}^nk^3\\\sum_{k=3}^nk^3\\\sum_{k=4}^nk^3\\...\\\sum_{k=1}^nk^3\end{pmatrix}$