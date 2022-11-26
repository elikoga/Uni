%% Based on LaTeX Class for exercise sheets from Sascha Brauer
%% Adapted to group submissions: 18-10-2022

%% Document Baseclass and encoding
\LoadClass[12pt, a4paper]{scrartcl}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern}
%%

%% Package Options
\newif\ifanswer\answerfalse
\newif\ifenglish\englishfalse

\DeclareOption{answers}{\answertrue}
\DeclareOption{english}{\englishtrue}

\ProcessOptions
%%

%% Language Formatting
\ifenglish
\RequirePackage[english]{babel}
\else
\RequirePackage[ngerman]{babel}
\fi
%%

%% General Layout
\RequirePackage[margin=2.5cm]{geometry}
\RequirePackage{hyperref}

\RequirePackage[footsepline]{scrlayer-scrpage}
\pagestyle{scrheadings}

\clearpairofpagestyles
\makeatletter
\cfoot{\normalfont \ifenglish Page \else Seite \fi\pagemark~\ifenglish of \else von \fi\the\exercise@seiten}
\makeatother

\parindent = 0em
%%

%% Math
\RequirePackage{amsmath,amsfonts,amssymb,amsthm,mathtools}

\makeatletter
\newtheoremstyle{thmstyle}
  {3pt}{3pt}{\itshape}{}{\bfseries}{}{.5em}
  {\thmname{#1}\thmnumber{ #2}\thmnote{ \textmd{(#3)}}}
\theoremstyle{thmstyle}
\makeatother

\newcounter{ex}
\setcounter{ex}{0}
\newtheorem{definition}{Definition}[ex]
\newtheorem{lemma}[definition]{Lemma}
\newtheorem{problem}[definition]{Problem}
\ifenglish
\newtheorem{theorem}[definition]{Theorem}
\newtheorem{example}[definition]{Example}
\newtheorem{claim}[definition]{Claim}
\newtheorem{observation}[definition]{Observation}
\else
\newtheorem{theorem}[definition]{Satz}
\newtheorem{example}[definition]{Beispiel}
\newtheorem{claim}[definition]{Behauptung}
\newtheorem{observation}[definition]{Beobachtung}
\fi

%% Graphics
\RequirePackage{graphicx}
\DeclareGraphicsExtensions{.pdf,.ai}
\graphicspath{{../figures/converted/}{../figures/others/}{../figures/ai-version-cs/}}
\DeclareGraphicsRule{.ai}{pdf}{*}{}% Handle .ai files as .pdf files.
\RequirePackage{tikz}
\usetikzlibrary{arrows,automata,positioning,decorations.markings,shadows}
%%

%% Exercise specifics
\newif\ifishomework\ishomeworktrue
\newif\ifisinclass\isinclassfalse
\newif\ifnotomitdates\notomitdatestrue
\newif\ifnotomitsummary\notomitsummarytrue
\newif\ifnotomitlogo\notomitlogotrue
\newcommand{\homework}{\ishomeworktrue \isinclassfalse}
\newcommand{\inclass}{\ishomeworkfalse \isinclasstrue}
\newcommand{\generic}{\ishomeworktrue \isinclasstrue}
\newcommand{\omitdates}{\notomitdatesfalse}
\newcommand{\omitsummary}{\notomitsummaryfalse}
\newcommand{\omitlogo}{\notomitlogofalse}

\RequirePackage{framed}
\makeatletter
\renewenvironment{oframed}{
  \def\FrameCommand{\hskip\@totalleftmargin\OpenFBox\FrameRule\FrameRule}%
  \def\FirstFrameCommand{\OpenFBox\FrameRule\z@}%
  \def\MidFrameCommand{\OpenFBox\z@\z@}%
  \def\LastFrameCommand{\OpenFBox\z@\FrameRule}%
  \MakeFramed {\advance\hsize-\width \@totalleftmargin\z@ \linewidth\hsize
   \@setminipage \FrameRestore}%
  }{\par\unskip\endMakeFramed}

\newcount\exercise@aufgaben
\newcount\exercise@aufgaben@pre
\newcount\exercise@punkte
\newcount\exercise@punkte@pre
\newcount\exercise@seiten
\newenvironment{exercise}[2][]
{
	\global\advance\exercise@aufgaben by 1
	\refstepcounter{ex}
	\par
	\vspace{20pt}
	\textbf{\ifenglish Exercise \else Aufgabe \fi\theex}
	\ifx\\#2\else (#2)\fi
	\ifx\\#1\else\global\advance\exercise@punkte by #1 \hfill(#1~\ifenglish \ifnum#1=1 Point\else Points\fi\else \ifnum#1=1 Punkt\else Punkte\fi\fi)\fi

}{}

\newcommand{\answer}[1]
{
	\ifanswer
	\begin{oframed}
		\textbf{\ifenglish Solution: \else Lösung: \fi} #1
	\end{oframed}
	\fi
}

\newcommand{\exercisetlaux}{}
\newcommand{\exercisetl}[1]{\renewcommand{\exercisetlaux}{#1}}
\newcommand{\exercisedateaux}{\today}
\newcommand{\exercisedate}[1]{\renewcommand{\exercisedateaux}{#1}}
\newcommand{\exercisegroupaux}{}
\newcommand{\exercisegroup}[2]{\renewcommand{\exercisegroupaux}{Gruppe #1:\\ #2}}
\newcommand{\exerciseheader}
{
\begin{minipage}[t][][b]{.37\textwidth}
	{\small \exercisetlaux}
\end{minipage}
\ifnotomitlogo
\hfill
\begin{minipage}[t][][b]{.2\textwidth}
\begin{center}\includegraphics[width=2.5cm]{./figures/cuk_logo_2019.pdf}\end{center}
\end{minipage}
\fi
\hfill
\fbox{\begin{minipage}[t][][b]{.37\textwidth}
{\small \exercisegroupaux}
\end{minipage}}
}
\newcommand{\exerciselectureaux}{}
\newcommand{\exerciselecture}[1]{\renewcommand{\exerciselectureaux}{#1}}
\newcommand{\exercisenumberaux}{}
\newcommand{\exercisenumber}[1]{\renewcommand{\exercisenumberaux}{#1}}
\newcommand{\exercisehandinaux}{}
\newcommand{\exercisehandin}[1]{\renewcommand{\exercisehandinaux}{#1}}
\newcommand{\exerciseinclassaux}{}
\newcommand{\exerciseinclass}[1]{\renewcommand{\exerciseinclassaux}{#1}}
\newcommand{\exercisetitle}
{
\begin{center}
	\textbf{\large\exerciselectureaux}
	\medskip

	\textbf{\ifishomework \ifisinclass \ifenglish Exercise \else Übungszettel \fi \else \ifenglish Homework \else Heimübung \fi \fi \else \ifenglish In Class Exercise \else Präsenzübung \fi \fi \exercisenumberaux}

	\ifnotomitdates
	\ifisinclass \textbf{\exerciseinclassaux}\fi

	\ifishomework\textbf{\ifenglish Hand In: \else Abgabe: \fi \exercisehandinaux}\fi
	\fi

	\ifnotomitsummary
	\ifenglish
	(This exercise sheet contains \the\exercise@aufgaben@pre~\ifnum\the\exercise@aufgaben@pre=1 exercise\else exercises\fi
	\ifishomework \ with a total of \the\exercise@punkte@pre~\ifnum\the\exercise@punkte@pre=1 point\else points\fi \fi)
	\else
	(Dieser Übungszettel besteht aus \the\exercise@aufgaben@pre~\ifnum\the\exercise@aufgaben@pre=1 Aufgabe\else Aufgaben\fi
	\ifishomework \ mit insgesamt \the\exercise@punkte@pre~\ifnum\the\exercise@punkte@pre=1 Punkt\else Punkten\fi \fi)
	\fi
	\fi
\end{center}
}

\AtBeginDocument{
	\exercise@aufgaben@pre = \exercise@aufgaben\relax
	\exercise@aufgaben = 0
	\exercise@punkte@pre = \exercise@punkte\relax
	\exercise@punkte = 0
}

\AtEndDocument{
	\if@filesw
		\immediate\write\@auxout{\string\global\string\exercise@aufgaben = \the\exercise@aufgaben}
		\immediate\write\@auxout{\string\global\string\exercise@punkte = \the\exercise@punkte}
		\immediate\write\@auxout{\string\global\string\exercise@seiten = \thepage}
	\fi
}
\makeatother
%%
