# Aufgabe 26
Die Regeln zur Vektoraddition bleiben gleich, da die Vektoraddition nicht geändert wurde.

$\lambda=a+bi,\mu=c+di$

$(\lambda\cdot\mu)\circ\vec v=((ac-bd)+i(ad+bc))\circ\vec v=((ac-bd)-i(ad+bc))\cdot\vec v=(a-bi)(c-di)\vec v=\overline\lambda\cdot\overline\mu\cdot\vec v=\overline\lambda\cdot(\mu\circ \vec v)=\lambda\circ(\mu\circ\vec v)$

$(1+0i)\circ\vec v=(1-0i)\cdot\vec v=1\cdot\vec v=\vec v$

$(\lambda+\mu)\circ\vec v=((a+c)+i(b+d))\circ\vec v=((a+c)-i(b+d))\cdot\vec v=((a-bi)+(c-di))\cdot\vec v=(\overline\lambda+\overline\mu)\vec v=\overline\lambda\cdot\vec v+\overline\mu\cdot\vec v=(\lambda\circ\vec v)+(\mu\circ\vec v)$

$\lambda\circ(\vec v+\vec u)=\overline\lambda\cdot(\vec v+\vec u)=\overline\lambda\cdot\vec v+\overline\lambda\cdot\vec u=(\lambda\circ\vec v)+(\lambda\circ\vec u)$

$\implies(V,\circ,+)$ ist ein $\Complex$-VR

# Aufgabe 27
$\vec v_2\in \langle\vec v_1,\vec v_3\rangle_\mathbb Q$
$\implies\exists\lambda_1,\lambda_2\in\mathbb Q:\vec v_2=\lambda_1\cdot\vec v_1+\lambda_2\vec v_3$

$\begin{pmatrix}3&-1&|&1\\1&1&|&5\\-7&3&|&0\\4&0&|&6\end{pmatrix}$
$\overset{I-3II,III+7II,IV-4III}\rightsquigarrow\begin{pmatrix}0&-4&|&-14\\1&1&|&5\\0&10&|&35\\0&-4&|&-14\end{pmatrix}$
$\rightsquigarrow\begin{pmatrix}0&1&|&\frac72\\1&1&|&5\\0&1&|&\frac72\\0&1&|&\frac72\end{pmatrix}$

$\rightsquigarrow\begin{pmatrix}0&1&|&\frac72\\1&0&|&\frac32\end{pmatrix}$

$\begin{pmatrix}\lambda_1\\\lambda_2\end{pmatrix}=\begin{pmatrix}\frac32\\\frac72\end{pmatrix}$

Test
$\frac32\begin{pmatrix}3\\1\\-7\\4\end{pmatrix}+\frac72\begin{pmatrix}-1\\1\\3\\0\end{pmatrix}=\begin{pmatrix}\frac92-\frac72\\\frac32+\frac72\\-\frac{21}{2}+\frac{21}2\\\frac{12}2+0\end{pmatrix}=\begin{pmatrix}1\\5\\0\\6\end{pmatrix}=\vec v_2$

# Aufgabe 28
## 1)
$\begin{pmatrix}1&2&3\\2&5&7\\3&7&10\end{pmatrix}$

$\overset{II-2I,III-3I}\rightsquigarrow\begin{pmatrix}1&2&3\\0&1&1\\0&1&1\end{pmatrix}$

$\overset{III-II,I-2II}\rightsquigarrow\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}$

$\implies\begin{pmatrix}\lambda_1\\\lambda_2\\\lambda_3\end{pmatrix}=\begin{pmatrix}-\lambda_3\\-\lambda_3\\\lambda_3\end{pmatrix}=\lambda_3\begin{pmatrix}-1\\-1\\1\end{pmatrix}$

$\implies$ linear abhängig

## 2)
$\begin{pmatrix}1&2&3\\2&5&7\\3&7&11\end{pmatrix}$

$\overset{II-2I,III-3I}\rightsquigarrow\begin{pmatrix}1&2&3\\0&1&1\\0&1&2\end{pmatrix}$

$\overset{III-II,I-2II}\rightsquigarrow\begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}$

$\overset{II-III,I-III}\rightsquigarrow\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}$

$\implies\begin{pmatrix}\lambda_1\\\lambda_2\\\lambda_3\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}$

$\implies$ linear unabhängig

# Aufgabe 29
Wenn zwei Vektoren in allen Untermengen sind, dann muss auch ihre Summe in allen Untermengen sein

Wenn ein Vektor in allen Untermengen ist, dann müssen auch alle Vektoren, die durch einen Skalar erzeugt werden köönnen, in allen Untermengen sein

# Aufgabe 30
