```kroki-graphviz
digraph G {
  0 -> 8 [label="l"]
  0 -> 1 [label="r"]
  0 [label="(8, -6)\n8"]
  1 -> 2 [label="l"]
  1 [label="(9, -1)\n11"]
  2 -> 5 [label="l"]
  2 -> 3 [label="r"]
  2 [label="(10, 4)\n10"]
  3 -> 4 [label="l"]
  3 [label="(11, 7)\n11"]
  4 [label="\n11"]
  5 -> 7 [label="l"]
  5 -> 6 [label="r"]
  5 [label="\n9"]
  6 [label="\n10"]
  7 [label="\n9"]
  8 -> 16 [label="l"]
  8 -> 9 [label="r"]
  8 [label="(3, -5)\n4"]
  9 -> 13 [label="l"]
  9 -> 10 [label="r"]
  9 [label="(6, 3)\n6"]
  10 -> 12 [label="l"]
  10 -> 11 [label="r"]
  10 [label="(7, 4)\n7"]
  11 [label="\n8"]
  12 [label="\n7"]
  13 -> 15 [label="l"]
  13 -> 14 [label="r"]
  13 [label="(5, 11)\n5"]
  14 [label="\n6"]
  15 [label="\n5"]
  16 -> 20 [label="l"]
  16 -> 17 [label="r"]
  16 [label="(1, 1)\n2"]
  17 -> 19 [label="l"]
  17 -> 18 [label="r"]
  17 [label="(4, 9)\n3"]
  18 [label="\n4"]
  19 [label="\n3"]
  20 -> 22 [label="l"]
  20 -> 21 [label="r"]
  20 [label="(2, 8)\n1"]
  21 [label="\n2"]
  22 [label="\n1"]
}
```

```kroki-graphviz
digraph G {
  0 -> 8 [label="l", color=red]
  0 -> 1 [label="r"]
  0 [label="(8, -6)\n8", color=red]
  1 -> 2 [label="l"]
  1 [label="(9, -1)\n11"]
  2 -> 5 [label="l"]
  2 -> 3 [label="r"]
  2 [label="(10, 4)\n10"]
  3 -> 4 [label="l"]
  3 [label="(11, 7)\n11"]
  4 [label="\n11"]
  5 -> 7 [label="l"]
  5 -> 6 [label="r"]
  5 [label="\n9"]
  6 [label="\n10"]
  7 [label="\n9"]
  8 -> 16 [label="l", color=red]
  8 -> 9 [label="r", color=red]
  8 [label="(3, -5)\n4", color=red]
  9 -> 13 [label="l"]
  9 -> 10 [label="r", color=red]
  9 [label="(6, 3)\n6", color=red]
  10 -> 12 [label="l"]
  10 -> 11 [label="r"]
  10 [label="(7, 4)\n7", color=red]
  11 [label="\n8"]
  12 [label="\n7"]
  13 -> 15 [label="l"]
  13 -> 14 [label="r"]
  13 [label="(5, 11)\n5"]
  14 [label="\n6"]
  15 [label="\n5"]
  16 -> 20 [label="l"]
  16 -> 17 [label="r", color=red]
  16 [label="(1, 1)\n2", color=red]
  17 -> 19 [label="l"]
  17 -> 18 [label="r"]
  17 [label="(4, 9)\n3", color=red]
  18 [label="\n4"]
  19 [label="\n3"]
  20 -> 22 [label="l"]
  20 -> 21 [label="r"]
  20 [label="(2, 8)\n1"]
  21 [label="\n2"]
  22 [label="\n1"]
}
```

Output: [(3, -5), (6, 3), (4, 9)]

```latex
\subsection*{Aufgabe 12}

\subsubsection*{a)}

% \includegraphics{diag1.png}
% \includegraphics{diag2.png}

\begin{center}
% I just want to embed the images here
\includegraphics[width=0.4\textwidth]{diag1.png}
\includegraphics[width=0.4\textwidth]{diag2.png}

\end{center}
```