# Aufgabe 39
1. $\begin{pmatrix}1&n\\0&1\end{pmatrix}\begin{pmatrix}1&m\\0&1\end{pmatrix}=\begin{pmatrix}1&m+n\\0&1\end{pmatrix}$
2. $\begin{pmatrix}2&1\\0&2\end{pmatrix}^{10}=\begin{pmatrix}1024&5120\\0&1024\end{pmatrix}$
3. $\begin{pmatrix}3&-4&5\\2&-3&1\\3&-5&-1\end{pmatrix}\begin{pmatrix}2&29\\2&18\\0&-3\end{pmatrix}=\begin{pmatrix}-2&0\\-2&1\\-4&0\end{pmatrix}$
4. $\begin{pmatrix}1&5&3\\2&-3&1\end{pmatrix}\begin{pmatrix}2&-3&5\\-1&4&-2\\3&-1&1\end{pmatrix}=\begin{pmatrix}6&14&-2\\10&-19&17\end{pmatrix}$
5. $\begin{pmatrix}1&-1&3\\-1&1&-3\\2&-2&6\end{pmatrix}\begin{pmatrix}1&5&2\\0&3&-1\\2&1&-1\end{pmatrix}=\begin{pmatrix}7&5&0\\-7&-5&0\\14&10&0\end{pmatrix}$
6. $\begin{pmatrix}1&2&0&0\\2&1&0&0\\0&0&1&3\\0&0&3&1\end{pmatrix}\begin{pmatrix}1&1&0&0\\1&1&0&0\\0&0&1&-1\\0&0&-1&1\end{pmatrix}=\begin{pmatrix}3&3&0&0\\3&3&0&0\\0&0&-2&2\\0&0&2&-2\end{pmatrix}$

# Aufgabe 40
1. $\begin{pmatrix}3&0&2&0\\0&1&2&1\\2&3&0&0\end{pmatrix}\cdot\begin{pmatrix}1&-2&2\\2&-1&1\\-1&1&-2\\2&2&-1\end{pmatrix}+\begin{pmatrix}-2&0&-3\\0&6&-3\\5&-2&8\end{pmatrix}\\
=\begin{pmatrix}1&-4&2\\2&3&-4\\8&-7&7\end{pmatrix}+\begin{pmatrix}-2&0&-3\\0&6&-3\\5&-2&8\end{pmatrix}\\
=\begin{pmatrix}-1&-4&-1\\2&9&-7\\13&-9&15\end{pmatrix}$
2. $\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}^2=\begin{pmatrix}4&0&0&0\\0&4&0&0\\0&0&4&0\\0&0&0&4\end{pmatrix}$

# Aufgabe 42
## 1)
$V,W\in Mat_{2\times 2}(\R)$

$f(V+W)=A(V+W)+(V+W)B=AV+AW+VB+WB=AV+VB+AW+WB=f(V)+f(W)$

$f(\lambda V)=A(\lambda V)+(\lambda V)B=\lambda(AV+VB)=\lambda f(V)$

$\implies f$ ist linear

## 2)
$f(E_{11})=\begin{pmatrix}1&-1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}1&0\\0&0\end{pmatrix}\begin{pmatrix}0&1\\-1&1\end{pmatrix}=\begin{pmatrix}1&0\\1&0\end{pmatrix}+\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}1&1\\1&0\end{pmatrix}$

$f(E_{12})=\begin{pmatrix}1&-1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}+\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&1\\-1&1\end{pmatrix}=\begin{pmatrix}0&1\\0&1\end{pmatrix}+\begin{pmatrix}-1&1\\0&0\end{pmatrix}=\begin{pmatrix}-1&2\\0&1\end{pmatrix}$

$f(E_{21})=\begin{pmatrix}1&-1\\1&0\end{pmatrix}\begin{pmatrix}0&0\\1&0\end{pmatrix}+\begin{pmatrix}0&0\\1&0\end{pmatrix}\begin{pmatrix}0&1\\-1&1\end{pmatrix}=\begin{pmatrix}-1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&1\end{pmatrix}=\begin{pmatrix}-1&0\\0&1\end{pmatrix}$

$f(E_{22})=\begin{pmatrix}1&-1\\1&0\end{pmatrix}\begin{pmatrix}0&0\\0&1\end{pmatrix}+\begin{pmatrix}0&0\\0&1\end{pmatrix}\begin{pmatrix}0&1\\-1&1\end{pmatrix}=\begin{pmatrix}0&-1\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\-1&1\end{pmatrix}=\begin{pmatrix}0&-1\\-1&1\end{pmatrix}$

$[f]^B_B=\begin{pmatrix}1&-1&-1&0\\1&2&0&-1\\1&0&0&-1\\0&1&1&1\end{pmatrix}$

## 3)
$X\in  Mat_{2\times 2}(\R)$
$f(X)=0\iff AX+XB=0\iff \begin{pmatrix}x_1-x_3&x_2-x_4\\x_1&x_2\end{pmatrix}+\begin{pmatrix}-x_2&x_1+x_2\\-x_4&x_3+x_4\end{pmatrix}=0\iff\begin{pmatrix}x_1-x_2-x_3&x_1+2x_2+x_4\\x_1-x_4&x_2+x_3+x_4\end{pmatrix}=0$

$\implies\begin{cases}x_1-x_2-x_3=0\\x_1+2x_2+x_4=0\\x_1-x_4=0\\x_2+x_3+x_4=0\end{cases}$

$\implies\begin{pmatrix}1&-1&-1&0\\1&2&0&1\\1&0&0&-1\\0&1&1&1\end{pmatrix}$
$\overset{II-I,III-I}\leadsto\begin{pmatrix}1&-1&-1&0\\0&3&1&1\\0&1&1&-1\\0&1&1&1\end{pmatrix}$
$\overset{II-3IV,III-IV,I+IV}\leadsto\begin{pmatrix}1&0&0&1\\0&0&-2&-2\\0&0&0&-2\\0&1&1&1\end{pmatrix}$
$\overset{II\cdot(-\frac12),III\cdot(-\frac12)}\leadsto\begin{pmatrix}1&0&0&1\\0&0&1&1\\0&0&0&1\\0&1&1&1\end{pmatrix}$
$\overset{I-III,II-III,IV-III}\leadsto\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&0&0&1\\0&1&1&0\end{pmatrix}$
$\overset{IV-II}\leadsto\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&0&0&1\\0&1&0&0\end{pmatrix}$
$\overset{II\leftrightarrow IV,III\leftrightarrow IV}\leadsto\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}$

$\implies Ker(f)=\{\begin{pmatrix}0&0\\0&0\end{pmatrix}\}$
$\implies(\begin{pmatrix}0&0\\0&0\end{pmatrix})$ ist Basis von $Ker(f)$

---

$Im(f)=\langle f(E_{11}),f(E_{12}),f(E_{21}),f(E_{22})\rangle_\R$

$f(E_{11}),f(E_{12}),f(E_{21}),f(E_{22})$ sind linear abhängig

$\implies (\begin{pmatrix}1&1\\1&0\end{pmatrix},\begin{pmatrix}-1&2\\0&1\end{pmatrix},\begin{pmatrix}-1&0\\0&1\end{pmatrix})$ ist eine Basis von $Im(f)$

# Aufgabe 43
$p,q\in K[t]_{<n}$

$f(p+q)=(p+q)(t+1)-(p+q)(t)=p(t+1)+q(t+1)-p(t)-q(t)\\=p(t+1)-p(t)+q(t+1)-q(t)=f(p)+f(q)$

$f(\lambda p)=(\lambda p)(t+1)-(\lambda p)(t)=\lambda p(t+1)-\lambda p(t)=\lambda (p(t+1)-p(t))=\lambda f(p)$

$\implies f$ ist linear

---

- $f(1)=0$
- $f(t)=1$
- $f(t^2)=(t+1)^2-t^2=t^2+2t+1-t^2=2t+1$
- $f(t^3)=(t+1)^3-t^3=t^3+3t^2+3t+1-t^3=3t^2+3t+1$
- ...
- $f(t^i)=\binom i{i-1}t^{i-1}+...+\binom ijt^j+...+\binom i2t^2+\binom i1t+1$
- ...
- $f(t^{n-1})=\binom{n-1}{n-2}t^{n-2}+...+\binom{n-1}jt^j+...+\binom{n-1}2t^2+\binom{n-1}1t+1$

$\implies [f]=\begin{pmatrix}0&\binom 10&\binom20&\binom30&...&\binom i0&...&\binom{n-1}0\\0&0&\binom21&\binom31&...&\binom i1&...&\binom{n-1}1\\0&0&0&\binom 32&...&\binom i2&...&\binom{n-1}2\\\vdots\\0&0&0&0&...&\binom{i}{i-1}&...&\binom{n-1}{i-1}\\\vdots\\0&0&0&0&...&0&...&0\end{pmatrix}$