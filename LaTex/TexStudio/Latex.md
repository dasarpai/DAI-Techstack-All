<link rel="stylesheet" href="../style.css">

## Problems when we concert latext 2 column documnt to pdf file
After that we convert that to docx file in google doc then has following problems.
- Tables get converted to images some into table, some into normal text.
- Some images imported with low resolution and some not improted at all.
- font size changes for different text.
- Because of different page height pager header come in between.
- landscape table not converted correctly. All text wipeout.

But if you this pdf file in office libre then everything is perfectly editable and open in doc file.
Here every line has become one text box and limited editing is possible.

# Overleaf

https://www.overleaf.com/learn/latex/Sections_and_chapters

# 27-08-20 10:27
### LaTex, OverLeaf Notes
Learned what is LaTex, different software for LaTex. I installed LexMaker, JabReb 5.0, basic-miktex-20.6.29-x64
Setup Overleaf account and learned how LaTex work. Explored various features of LaTex
Trying to convert my SDSHL interim report into LaTex. Tried Overleaf and LexMaker. But lots of issues.

Solved puzzles
- How to put footnote
- How to use url
- How to put biblography table
- How to put TOC
- How to create header (Section/ Subsection/ Subsection)
- How to create order and unorder item list
- How to put page number
- What is preemble
- How to put chapters
- How to put Header without number & with number
- How to structure document in main document
- What is the role of importing different packages
- Devnagari font problem in LaTex

### Devnagari Fonts in Latex
```
Hindi (Devanagari script)
Aksharyogini2
Annapurna SIL
BABEL Unicode
Chandas
FreeSans
FreeSerif
Gargi
Lohit Devanagari
Nakula
Noto Sans Devanagari
Noto Serif Devanagari
Sahadeva
Samanata
Samyak Devanagari
Sarai
Shobhika
```

# 11-Jun-22
```
glossary 
reference 
acronym 
footnote 
```

### Preamble
- Everyting before \begin{document} is called preamble.
- In the preamble you define the type of document you are writing, the language you are writing in, the packages you would like to use (more on this later) and several other elements. 
- \documentclass[12pt, letterpaper|a4paper|legalpaper]{article}
- \usepackage[utf8]{inputenc}
- \title {}
- \author {}
- \thank{}
- \date{}
- \author{Hubert Farnsworth \thanks{funded by the Overleaf team}}
- \usepackage{graphicx}
- \graphicspath{ {images/} }

### Document
##### Common Text
- \begin{document}
- \maketitle
- We have now added a title, author and date to our first \LaTeX{} document!
- % This line here is a comment. It will not be printed in the document. - COMMENT
- Some of the \textbf{greatest} %boldface
- discoveries in \underline{science} %underline
- were made by \textbf{\textit{accident}}. %italics
- \emph{discoveries} %Empahsis. Behvarious is reverse than what is surrounding text.

- \includegraphics{universe}
- \end{document}

### Adding Figure
```
\begin{figure}[h]
    \centering
    \includegraphics[width=0.25\textwidth]{mesh}
    \caption{a nice plot}
    \label{fig:mesh1}
\end{figure}
As you can see in the figure \ref{fig:mesh1}, the function grows near 0. Also, in the page \pageref{fig:mesh1} is the same example.

##### List 
\begin{itemize}
  \item The individual entries are indicated with a black dot, a so-called bullet.
  \item The text in the entries may be of any length.
\end{itemize}

\begin{enumerate}
  \item This is the first entry in our list
  \item The list numbers increase with each entry we add
\end{enumerate}
```

#### Mathematics 
- In physics, the mass-energy equivalence is stated by the equation $E=mc^2$, discovered in 1905 by Albert Einstein.

#### Abstract 
```
\begin{document}

\begin{abstract}
This is a simple paragraph at the beginning of the 
document. A brief introduction about the main subject.
\end{abstract}
\end{document}
```

### Table - https://www.overleaf.com/learn/latex/Tables
```
\begin{center}
\begin{tabular}{||c c c c||} 
 \hline
 Col1 & Col2 & Col2 & Col3 \\ [0.5ex] 
 \hline\hline
 1 & 6 & 87837 & 787 \\ 
 \hline
 2 & 7 & 78 & 5415 \\
 \hline
 3 & 545 & 778 & 7507 \\
 \hline
 4 & 545 & 18744 & 7560 \\
 \hline
 5 & 88 & 788 & 6344 \\ [1ex] 
 \hline
\end{tabular}
\end{center}
```

#### Table 
```
\documentclass{article}
\usepackage{tabularx}
\begin{document}
\begin{tabularx}{0.8\textwidth} { 
  | >{\raggedright\arraybackslash}X 
  | >{\centering\arraybackslash}X 
  | >{\raggedleft\arraybackslash}X | }
 \hline
 item 11 & item 12 & item 13 \\
 \hline
 item 21  & item 22  & item 23  \\
\hline
\end{tabularx}
\end{document}
```


## env 
- begin{}, end{} - These all are EVN
- abstract, align, align*, array, center, document, enumurate, equation, equation*,example, figure, frame, gather, gather*, it, itemize, list, multiline, multiline*, quoe, spilit, table, tabular, thebibliography, verbatim, 

## cmd1
\item[] , \section{}, \textbf{}, ]cit{}, \label{}, \textit{}, icludegraphics[]{}, \documentclass[]{}, \documentclass{}, \fram{}{}, \subsetion{}, \hline , \caption{}, \centering, \vspace{}, \title{}, \author[]{}, \author{}, \maketitle , \textwidth , \newcommand{}[]{}, \renewcommand{}{}, \date{}, \emp{}, \textsc{} , \multicolumn{}{}{}, \input{}, \mathbf{}, \chapter{}, \subsection{}, bibitem[]{}, \bibitem{}, \text{}, \setlength{}{}, \mathcal{}, mathrm{}, boldsymbol , include{}, \address{}, \paragraph{}, \texttt{}, \color{}, \bibliography{}, \hat{}, \footnote{}, \newtheorem{}{}, \sqrt{} , \newcounter{somecounter}, \setcounter{somecounter}{9}, \alph{}, Alph{}, \arabic, fnsymbol, newcounter, roman{}, Roman{}, 

## cmd2
\alpha , \in , \right , \left , \sum , \par , \lambda, \newpage, \theta, \hspace, \beta, \times 
\mu, \linewidth, \delta, \sigma , \pi , \small , \LaTex, \cdot , \Delta, \tau, \hfill, \lef , \footnotesize \large \Large, \epsilon, rho , omega , gamma , clearpage, infty, phi , partial, quad, iota , vartheta, rarrho , varsigma, varpi , Upsilon 
\item 

## cross-reference 
\ref {}

## pkg
usepackage{} -
adjustbox, algorithm, algorithm2e, algorithmic, algpsedocde, aliascnt, amsfonts, amsmath, amssymb, amsthm, appendix, array, authblk, babel, biblatex, blindtext, bm, booktabs, calc, caption, changepage, cite, collection, color, colortbl, comment, csquotes, dcolumn, enumerate, enumitem, epsifig, epstopdf, etoolbox, fancyhdr, float, fontenc, fontspec, framed, fullpage, gensymb, geometry, graphics, graphicx, halvet, hyperref, ifpdf, ifthen, indentfirst, inputenc, lastpage, latexsym, layaureo, lineno, lipsum, listings, lmodern, longtabl, madeidx, marvosym, mathptmx, mathrsfs, mathtools,microtype, moderncvcompatibility, doerncvstyleclassic, multicol, multirow, natbib, parskip, pdfpages, pdfplots, pifont, placeins, ragged2e, rotating, setspace, siunitx, soul, subcaption, subfig, subfigure, superfigure, supertabular, tabularx, textcomp, textpos, tikz, times, titlesec, tocbibind, todonotes, tweaklist, url, verbatim, wrapfig, xcolor, xltxtra, xparse, space, xunicode, 

## Overleaf Project 
```
Blank Project 
Example Project 
Upload Project 
Import from GitHub 
Academic Journal 
Book 
Formal Letter 
Homework Assignment 
Poster 
Presentation 
Project / Lab Report 
Resume / CV
Thesis 
View All 

Overleaf guides
Creating a document in Overleaf
Uploading a project
Copying a project
Creating a project from a template
Using the Overleaf project menu
Including images in Overleaf
Exporting your work from Overleaf
Working offline in Overleaf
Using Track Changes in Overleaf
Using bibliographies in Overleaf
Sharing your work with others
Using the History feature
Debugging Compilation timeout errors
How-to guides
Guide to Overleaf’s premium features

LaTeX Basics
Creating your first LaTeX document
Choosing a LaTeX Compiler
Paragraphs and new lines
Bold, italics and underlining
Lists
Errors

Mathematics
Mathematical expressions
Subscripts and superscripts
Brackets and Parentheses
Matrices
Fractions and Binomials
Aligning equations
Operators
Spacing in math mode
Integrals, sums and limits
Display style in math mode
List of Greek letters and math symbols
Mathematical fonts
Using the Symbol Palette in Overleaf

Figures and tables
Inserting Images
Tables
Positioning Images and Tables
Lists of Tables and Figures
Drawing Diagrams Directly in LaTeX
TikZ package

References and Citations
Bibliography management with bibtex
Bibliography management with natbib
Bibliography management with biblatex
Bibtex bibliography styles
Natbib bibliography styles
Natbib citation styles
Biblatex bibliography styles
Biblatex citation styles

Document structure
Sections and chapters
Table of contents
Cross referencing sections, equations and floats
Indices
Glossaries
Nomenclatures
Management in a large project
Multi-file LaTeX projects
Hyperlinks

Formatting
Lengths in LATEX
Headers and footers
Page numbering
Paragraph formatting
Line breaks and blank spaces
Text alignment
Page size and margins
Single sided and double sided documents
Multiple columns
Counters
Code listing
Code Highlighting with minted
Using colours in LaTeX
Footnotes
Margin notes

Fonts
Font sizes, families, and styles
Font typefaces
Supporting modern fonts with XƎLATEX

Presentations
Beamer
Powerdot
Posters

Commands
Commands
Environments

Field specific
Theorems and proofs
Chemistry formulae
Feynman diagrams
Molecular orbital diagrams
Chess notation
Knitting patterns
CircuiTikz package
Pgfplots package
Typesetting exams in LaTeX
Knitr
Attribute Value Matrices

Class files
Understanding packages and class files
List of packages and class files
Writing your own package
Writing your own class

Advanced TeX/LaTeX
In-depth technical articles on TeX/LaTeX

\verb!\frac{1}{2}! %verbatim

Comments %

\emph{mainly}

  
\begin{itemize}
\item Tea
\item Milk
\item Biscuits
\end{itemize}


\begin{enumerate}
\item Tea
\item Milk
\item Biscuits
\end{enumerate}

\begin{figure}
\includegraphics{gerbil}
\end{figure}

\begin{equation}
\alpha + \beta + 1
\end{equation}

\documentclass{article}
\begin{document}
Hello World! % your content goes here...
\end{document}

Type your text between \begin{document} and \end{document}.


Some common characters have special meanings in LATEX are as below. Therefor use \ along with these characters if you want them in text.
% percent sign
# hash (pound / sharp) sign
& ampersand
$ dollar sign
\$\%\&\#!


Use curly braces { } to group superscripts and subscripts.
$F_n = F_{n-1} + F^{n-2}$ % ok!

There are commands for Greek letters and common notation.
$\mu = A e^{Q/RT}$
$\Omega = \sum_{k=1}^{n} \omega_k$

\begin{equation}
x = \frac{-b \pm \sqrt{b^2 - 4ac}}
{2a}
\end{equation}
where $a$, $b$ and $c$ are \ldots

- Packages are libraries of extra commands and environments.
There are thousands of freely available packages.
- We have to load each of the packages we want to use with a
\usepackage command in the preamble.

\documentclass{article}
\usepackage{amsmath} % preamble
\begin{document}
% now we can use commands from amsmath here...
\end{document}


Use equation* (“equation-star”) for unnumbered equations.
\begin{equation*}
\Omega = \sum_{k=1}^{n} \omega_k
\end{equation*}


\begin{equation*} % bad!
min_{x,y} (1-x)^2 + 100(y-x^2)^2
\end{equation*}

\begin{equation*} % good!
\min_{x,y}{(1-x)^2 + 100(y-x^2)^2}
\end{equation*}


You can use \operatorname for others.
\begin{equation*}
\beta_i =
\frac{\operatorname{Cov}(R_i, R_m)}
{\operatorname{Var}(R_m)}
\end{equation*}

Align a sequence of equations at the equals sign
with the align* environment.
\begin{align*}
(x+1)^3 &= (x+1)(x+1)(x+1) \\
&= (x+1)(x^2 + 2x + 1) \\
&= x^3 + 3x^2 + 3x + 1
\end{align*}

A double backslash \ \ starts a new line.
\infty

Let \( \mathcal{T} \) be a topological space, a basis is defined as
\[
 \mathcal{B} = \{B_{\alpha} \in \mathcal{T}\, |\,  U = \bigcup B_{\alpha} \forall U \in \mathcal{T} \}
\]

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\begin{align*}
RQSZ \\
\mathcal{RQSZ} \\
\mathfrak{RQSZ} \\
\mathbb{RQSZ}
\end{align*}
\end{document}
```



### Mathematical fonts 
```
\begin{align*}
3x^2 \in R \subset Q \\
\mathnormal{3x^2 \in R \subset Q} \\
\mathrm{3x^2 \in R \subset Q} \\
\mathit{3x^2 \in R \subset Q} \\
\mathbf{3x^2 \in R \subset Q} \\
\mathsf{3x^2 \in R \subset Q} \\
\mathtt{3x^2 \in R \subset Q}
\end{align*}

\[ \int\limits_0^1 x^2 + y^2 \ dx \]

\[ \int_0^1 x^2 + y^2 \ dx \]

\[ x^{2 \alpha} - 1 = y_{ij} + y_{ij}  \]

\[ (a^n)^{r+s} = a^{nr+ns}  \]

\[ \sum_{i=1}^{\infty} \frac{1}{n^s} 
= \prod_p \frac{1}{1 - p^{-s}} \]


\cup_{i=1}^n
\cap_{i=1}^n
\oint_{i=1}^n
\coprod_{i=1}^n

\begin{multline*}
p(x) = 3x^6 + 14x^5y + 590x^4y^2 + 19x^3y^3\\ 
- 12x^2y^4 - 12xy^5 + 2y^6 - a^3b^3
\end{multline*}


\documentclass{article}
\usepackage{amsmath}
\begin{document}
Spaces in mathematical mode.
```

### Spaces
```
\begin{align*}
f(x) &= x^2\! +3x\! +2 \\
f(x) &= x^2+3x+2 \\
f(x) &= x^2\, +3x\, +2 \\
f(x) &= x^2\: +3x\: +2 \\
f(x) &= x^2\; +3x\; +2 \\
f(x) &= x^2\ +3x\ +2 \\
f(x) &= x^2\quad +3x\quad +2 \\
f(x) &= x^2\qquad +3x\qquad +2
\end{align*}
\end{document}
```

### LATEX code	Description
```
\quad	space equal to the current font size (= 18 mu)
\,	3/18 of \quad (= 3 mu)
\:	4/18 of \quad (= 4 mu)
\;	5/18 of \quad (= 5 mu)
\!	-3/18 of \quad (= -3 mu)
\ (space after backslash!)	equivalent of space in normal text
\qquad	twice of \quad (= 36 mu)
```

### Lists_of_tables_and_figures
```
\documentclass{article}
\usepackage{graphicx}
\graphicspath{ {figures/} }
\usepackage{array}

\begin{document}

\thispagestyle{empty}
\listoffigures
\listoftables
\newpage
\pagenumbering{arabic}

Lorem ipsum dolor sit amet, consectetuer adipiscing 
elit.  Etiam lobortisfacilisis...
\end{document}

\renewcommand{\listfigurename}{List of plots}
\renewcommand{\listtablename}{Tables}

\thispagestyle{empty}
\listoffigures
\listoftables
\clearpage
```

### Sections_and_chapters
```
-1	\part{part}
0	\chapter{chapter}
1	\section{section}
2	\subsection{subsection}
3	\subsubsection{subsubsection}
4	\paragraph{paragraph}
5	\subparagraph{subparagraph}

\documentclass{article} % \documentclass{report}
\title{Sections and Chapters}
\author{Overleaf}
\date{\today}

\begin{document} 
\maketitle %Contents
\tableofcontents

\newcommand\shortlorem{Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.}

\section{Introduction}
This is the first section (numbered).

\shortlorem
\addcontentsline{toc}{section}{Unnumbered Section}
\section*{Unnumbered Section}
An unnumbered section

\shortlorem

\section{Second section}
The second numbered section.

\shortlorem
\end{document}

\chapter{An Introduction to Lua\TeX}
Chapter 1
An Introduction to LuaTEX

\section{What is it—and what makes it so different?}
\subsection{Explaining Lua\TeX: Where to start?}

\part{History of Lua\TeX}
Part I
History of LuaTEX

```

### Useful Packages 
```
\usepackage[version=4]{mhchem} %this is good for chemical reactions
\usepackage{amsmath} %maths package
\usepackage{amssymb} %symbol package
\usepackage{textcomp,gensymb} %more symbols (eg \degree)
\usepackage{multirow} %for tables
\usepackage{longtable} %for long tables
\usepackage{booktabs} %more tables
\usepackage{pdfpages} %allows PDFs to be included in document (good if you want to include a pdf in an appendix eg)
\usepackage{colortbl} %good for colouring in cells on a table
\usepackage{rotating} %allows you to rotate graphics
\usepackage[table]{xcolor} %more colouring of tables
\definecolor{Gray}{gray}{0.9} %this defines a colour to be used and gives it a name. This is a colour called 'Gray' it is 'gray' with transparency 0.9

“अमी मोंजुलिका. अमी राजा को जरूर मारबो !},
अरे वा! इनको इस महान कार्य के लिऐ तो कम से पद्मश्री award मिलना ही चाहिऐ.

Test, you can remove this. figure \ref{fig:evolution_of_hinglish}
```

### Problems
1. Hindi joint char priting.
2. Different fonts.
3. Chapter Title in Devnangari.
4. Emoji printing.

### Babel Package
- The Babel package presented in the introduction allows to use special characters and also translates some elements within the document.
- You can activate the babel package by adding the next command to the preamble:
- \usepackage[language]{babel}
- https://texdoc.org/serve/babel/0 - babel pkg documentation.

### Babel: Localization and internationalization
- Unicode
- TEX
- pdfTEX
- LuaTEX
- XeTEX

\begin{otherlanguage}{english}

\end{otherlanguage}

Devanagari In luatex and the the default renderer many fonts work, but some others do not, the main issue being the ‘ra’. You may need to set explicitly the script to either deva or dev2, eg: \newfontscript{Devanagari}{deva}

- https://mirror.kku.ac.th/CTAN/macros/luatex/latex/emoji/emoji-doc.pdf
- https://mirror.kku.ac.th/CTAN/
- book: https://www.dickimaw-books.com/latex/novices/novices-report.pdf
- https://www.dickimaw-books.com/latex/novices/


### TeX Installation on Local Machine
- https://miktex.org/download
- https://www.texstudio.org/
- http://www.uofclinguistics.org/
- https://www.luatex.org/download.html
- https://ctan.org/pkg
- TeXworks - lowering the entry barrier to the TeX world https://tug.org/texworks/
- Package fontspec Error: The font "LibertinusSerif" cannot be found. [Ligatures=Common, Scale=1.0]{Libertinus Serif}

```
\babelprovide[import]{hindi}
\babelfont[hindi]{rm}
{Shobhika}

\babelfont{rm}

[Ligatures=Common, Scale=1.0]{Libertinus Serif}

\babelfont{sf}
[Ligatures=Common]{Libertinus Sans}
\babelfont{tt}
{Libertinus Mono}
\newfontscript{Devanagari}{deva}

\usepackage{fontspec}

Package fontspec Error: The font "AdobeDevanagari" cannot be found. ...indifont{Adobe Devanagari}[Script=Devanagari]
Package fontspec Error: The font "AdobeDevanagari" cannot be found. ...indifont{Adobe Devanagari}[Script=Devanagari]
Font \TU/AdobeDevanagari(0)/m/n/10=AdobeDevanagari:mode=harf;language=dflt; at 10pt not loadable: metric data not found or bad. ...hindi{यह है देवनागरी}

Font "AdobeDevanagari" does not contain requested(fontspec) Script "Devanagari".
```

https://unicode.org/emoji/charts/emoji-list.html

https://www.overleaf.com/learn/latex/Multilingual_typesetting_on_Overleaf_using_polyglossia_and_fontspec


### Summarise and merge the learning from below with above section.
```
% Define document style type ='report' and font size.
\documentclass[12pt,twoside]{report} 
\usepackage{emoji}
% Define language used in the document.
\usepackage[hindi,english]{babel} 

\babelprovide[import]{hindi}
\babelfont[hindi]{rm}
          {Shobhika}
\babelfont{rm}
          [Ligatures=Common, Scale=1.0]{Libertinus Serif}

\babelfont{sf}
          [Ligatures=Common]{Libertinus Sans}
\babelfont{tt}
          {Libertinus Mono}
\newfontscript{Devanagari}{deva}

\usepackage{fontspec}

\usepackage{setspace} %allows the use of '\doublespace' to set line spacing

\usepackage[utf8]{inputenc} %inclusion of this is optional, overleaf includes it in its compiler so it is not necessary, it may be necessary for other compilers.

\usepackage{wrapfig} %if it is desirable to wrap text (see https://www.overleaf.com/learn/latex/Wrapping_text_around_figures).

\usepackage{graphicx} %this allows graphics to be put in easily

\usepackage{float}%this allows you to put them in good places

\usepackage{appendix} %self explanatory
\usepackage{bm} %helps bold things
\usepackage{caption} %allows captions for graphics
\usepackage[nottoc]{tocbibind} %adds the bibliography to the table of contents
\usepackage{subcaption} %allows subcaption for multiple images in one graphic

\PassOptionsToPackage{hyphens}{url}\usepackage{hyperref}
\usepackage{hyperref} %this is great for putting hyperreferences in the document.


\hypersetup{colorlinks=false} %this stops links being colourful, which makes a report look less professional I believe.

\usepackage{natbib}
\usepackage{url}

\usepackage[letterpaper, top=1in, bottom = 1in, right = 1in]{geometry} %this describes the layout of the document and the margins etc.
\usepackage{fontspec}

\doublespacing %self explanatory

% Using emoji in the document.
\usepackage{emoji}

% Define language used in the document.
\usepackage[hindi,english]{babel} 

\babelprovide[import]{hindi}
\babelfont[hindi]{rm}
          {Shobhika}
\babelfont{rm}
          [Ligatures=Common, Scale=1.0]{Libertinus Serif}

\babelfont{sf}
          [Ligatures=Common]{Libertinus Sans}
\babelfont{tt}
          {Libertinus Mono}
\newfontscript{Devanagari}{deva}

{\DejaSans } and even cats: {\DejaSans ��}!

https://unicode.org/emoji/charts/emoji-list.html
\emoji{rolling-on-the-floor-laughing}
\emoji{smiling-face-with-smiling-eyes}
\emoji{frowning-face}
```

### Figure
\begin{figure}
    \centering
    \includegraphics[width=0.6\textwidth]{4-images/MostPopular-SocialMediaNetwork-Jan2020.png}
    \caption{Evolution of Hinglish}
    \label{fig:evolution_of_hinglish}
\end{figure}

### Table
```
\begin{table}[]
    \centering
    \begin{tabular}
        { |s|p{3cm}|p{3cm}|p{3cm}| }
        \hline
        \rowcolor{gray!30}
        & Non-Sarcastic (50\%) & Sarcastic (50\%) & Total \\
        \hline
        Blog Text & 179 (39\%) & 283 (61\%) &462 (23\%)\\
        \hline
        Twitter Text & 821 (53\%) & 717 (47\%) & 1538 (73\%) \\
        \hline
        \rowcolor{gray!10}
        Total & 1000 & 1000 & 2000\\
        \hline
    \end{tabular}
    \caption{ Class Distribution in Dataset}
    \label{tab:Class_Distribution_in_Dataset}
\end{table}

\begin{itemize}
\end{itemize}

\begin{enumerate}
\end{enumerate}
```

### Citation and Bibliography 
```
%Import the natbib package and sets a bibliography  and citation styles
\usepackage{natbib}

\citep{Lee2009} %hardvard style. within paragram.

\bibliographystyle{agsm} % Harvard Style. Bibliography page.
\bibliographystyle{abbrvnat}
\bibliographystyle{abbrv} % Bib page with number.

\bibliography{sample}

\title{Natbib Example}
\author{Overleaf team}
\begin{document}
\maketitle
```

### Special Characters.
- \$  \&  \%  \_  \{   \}   \#
- ! @ * ( ) - + = ? [ ] / 

### LongTable
```
\documentclass[12pt,twoside]{report} 
\usepackage{booktabs, multirow} % for borders and merged ranges
\usepackage{soul}% for underlines
%\usepackage[table]{xcolor} % for cell colors
\usepackage{longtable}
\usepackage{changepage,threeparttable} % for wide tables

\begin{document}

If the table is too wide, replace \begin{table}[!htp]...\end{table} with
%\begin 
%{adjustwidth}{-2.5 cm}{-2.5 %cm}\centering\begin{threeparttable}[!htb]...\end{threeparttable}\end{adjustwidth}
\begin{longtable}[ht] %\centering
\caption{Generated by Spread-LaTeX}\label{tab: }
\scriptsize


\begin{tabular}{p{0.05\linewidth} | p{0.4\linewidth} | p{0.2\linewidth} | p{0.25\linewidth} }
\toprule
\textbf{\#} & \textbf{Paper} & \textbf{Language, Text Type} & \textbf{Metrics} \\

\midrule
\multicolumn{4}{l}{\textbf{Sarcasm Detection Work in English Language}} \\
1 & Irony Detection in Twitter: The Role of Affective Content. (Faŕias et al., 2016) & English, Twitter & Acc: 73-96\% depends upon datasets and classifier. \\
2 & Natural Language Processing Based Features for Sarcasm Detection: An Investigation Using Bilingual Social Media Texts. (Suhaimin et al., 2017) & English, Twitter & Acc: 82.5\% \\
\multicolumn{4}{c}{Sarcasm Detection Work in Hindi Language} &  \\
1 & Sentiment Analysis of Hindi Review based on Negation and Discourse Relation. (Mittal and Agarwal, 2013) & Hindi, Movie Reviews & Acc: 80.21\% \\

\bottomrule
\end{tabular}
\end{longtable}

\end{document}
```

### Other Commands 
```
\vspace{1cm}

\item[\S] Second item

\newcommand{\R}{\mathbb{E}}

This is my text using this new math command \( \R \)

\newcommand\foo{}
\ifx\foo\empty Empty\else Not empty\fi

\setlength{\tabcolsep}{0.7em} % for the horizontal padding
\begin{table}
\caption{Top 10 Best Models}\label{tab:Top_10_Best_Models}
\scriptsize
\begin{tabular}{ |p{1cm}|p{1.2cm}|p{.3cm}|p{.4cm}|p{.8cm}|p{.4cm}|p{.4cm}|}
    \hline
    \rowcolor{gray!30}
       Classifier & Embedding Name & AUC & Acc & Recall & Prec. & F1 \\
    %\midrule
    NB &fastTextWiki &0.8 &0.76 &0.78 &0.75 &0.76 \\ \hline
		
\begin{tabular}{|p{2cm}|p{.3cm}|p{.4cm}|p{.8cm}|p{.4cm}|p{.4cm}|}

\begin{tabular}{p{2cm}p{.3cm}p{.4cm}p{.8cm}p{.4cm}p{.4cm}}

\begin{tabular}{p{1cm}p{1cm}p{.3cm}p{.4cm}p{.8cm}p{.4cm}p{.4cm}}

Embedding Name & AUC & Acc & Recall & Prec & F1\\ \hline

https://www.elsevier.com/__data/assets/pdf_file/0008/56843/elsdoc-1.pdf

https://ctan.org/pkg/:A
```


https://mirror.las.iastate.edu/tex-archive/macros/latex/contrib/els-cas-templates/doc/elsdoc-cas.pdf


https://www.overleaf.com/learn/latex/Typesetting_exams_in_LaTeX
https://mirror.ox.ac.uk/sites/ctan.org/macros/latex/contrib/exam/examdoc.pdf


https://www.giss.nasa.gov/tools/latex/ltx-2.html


typeset 
\rm - Roman
\it - Italics
\em - Emphasis (toggles between \it and \rm)
\emph (LaTeX2e emphasis command)
\bf - Boldface
\sl - Slanted
\sf - Sans serif
\sc - Small caps
\tt - Typewriter
\boldmath and \unboldmath (affects math mode fonts only)

There are four environments that put LaTeX in math mode: math, displaymath, eqnarray, and equation. The math environment is for formulas that appear right in the text. The displaymath and equation environments are for formulas that appear on their own line; they differ only insofar as the latter prints an equation number. LaTeX will not break lines in displaymath or equation environments unless told to do so with a \\ command.


In order to start plot functions and data in TikZ we need to create the axis environment within the tikzpicture environment. All the pgfplots commands must be inside the axis environment.


Latex has 4500 packages.
Each documentclass loads some packages automatically.



https://en.wikibooks.org/wiki/LaTeX

### This is one traditional page order for books.
- https://en.wikibooks.org/wiki/LaTeX/Document_Structure
```
Frontmatter
Half-title
Empty
Title page
Information (copyright notice, ISBN, etc.)
Dedication if any, else empty
Table of contents
List of figures (can be in the backmatter too)
Preface chapter
Mainmatter
Main topic
Appendix
Some subordinate chapters
Backmatter
Bibliography
Glossary / Index
```

### Content inside different sections.
```
\begin{document}
\frontmatter

\maketitle

% Introductory chapters
\chapter{Preface}
% ...

\mainmatter
\chapter{First chapter}
% ...

\appendix
\chapter{First Appendix}

\backmatter
\chapter{Last note}
```

- \setcounter{tocdepth}{4}
- \makeatletter
- \renewcommand*{\toclevel@chapter}{-1} % Put chapter depth at the same level as \part.
- \chapter{Epilogue}
- \renewcommand*{\toclevel@chapter}{0} % Put chapter depth back to its default value.
- \makeatother
- \listoffigures and 
- \listoftables work in exactly the same way as 
- \tableofcontents
-  but you can add extra entries with the \addcontentsline command
- \subsection*{Preface}
- \addcontentsline{toc}{subsection}{Preface}


### Command	Level	Comment
- \part{''part''}	-1	not in letters
- \chapter{''chapter''}	0	only books and reports
- \section{''section''}	1	not in letters
- \subsection{''subsection''}	2	not in letters
- \subsubsection{''subsubsection''}	3	not in letters
- \paragraph{''paragraph''}	4	not in letters
- \subparagraph{''subparagraph''}	5	not in letters

### Document Classes
- article	For articles in scientific journals, presentations, short reports, program documentation, invitations, ...
- IEEEtran	For articles with the IEEE Transactions format.
- proc	A class for proceedings based on the article class.
- minimal	It is as small as it can get. It only sets a page size and a base font. It is mainly used for debugging purposes.
- report	For longer reports containing several chapters, small books, thesis, ...
- book	For books.
- slides	For slides. The class uses big sans serif letters.
- memoir	For sensibly changing the output of the document. It is based on the book class, but you can create any kind of document with it [1]
- letter	For writing letters.
- beamer	For writing presentations (see LaTeX/Presentations).

### Document Class Options
- 10pt, 11pt, 12pt	Sets the size of the main font in the document. If no option is specified, 10pt is assumed.
- a4paper, letterpaper,...	Defines the paper size. The default size is letterpaper; However, many European distributions of TeX now come pre-set for A4, not Letter, and this is also true of all distributions of pdfLaTeX. Besides that, a5paper, b5paper, executivepaper, and legalpaper can be specified.
- fleqn	Typesets displayed formulas left-aligned instead of centered.
- leqno	Places the numbering of formulas on the left hand side instead of the right.
- titlepage, notitlepage	Specifies whether a new page should be started after the document title or not. The article class does not start a new page by default, while report and book do.
- twocolumn	Instructs LaTeX to typeset the document in two columns instead of one.
- twoside, oneside	Specifies whether double or single sided output should be generated. The classes article and report are single sided and the book class is double sided by default. Note that this option concerns the style of the document only. The option twoside does not tell the printer you use that it should actually make a two-sided printout.
- landscape	Changes the layout of the document to print in landscape mode.
- openright, openany	Makes chapters begin either only on right hand pages or on the next page available. This does not work with the article class, as it does not know about chapters. The report class by default starts chapters on the next page available and the book class starts them on right hand pages.
- draft	makes LaTeX indicate hyphenation and justification problems with a small square in the right-hand margin of the problem line so they can be located quickly by a human. It also suppresses the inclusion of images and shows only a frame where they would normally occur.


# learning.edx.org IITBombay LaTex101 - 21-Jun-22
## Course Outline
Topic 2: Styling Pages
- Some Basics, Completed
- Session 6: Paper size and Margins, Completed
- Session 7: Page Styles (Header and footer), Completed
- Session 8: More on formatting pages (Writing footnotes, Orientation, page breaks), Completed
- Session 9: Multicolumn document (multicol package), Completed
- Session 10: Reading error messages, Completed
- Session 11: Recapitulate Topic 2, Completed

Topic 3: Formatting Content, Incomplete section
- Session 12: Formatting Text, Incomplete
- Session 13: Coloring Text, Incomplete
- Session 14: Aligning Text, Incomplete
- Session 15: Spacing Text, Incomplete
- Session 16: Bullets and Numbering, Incomplete
- Session 17: Writing Mathematics - I, Incomplete
- Session 18: Writing Mathematics -- II, Incomplete
- Session 19: Recapitulate Topic 3, Incomplete

Topic 4: Tables and Images, Incomplete section
- Session 20: Creating Tables, Incomplete
- Session 21: Table Borders, Incomplete
- Session 22: Merging Rows and Columns, Incomplete
- Session 23: Saviour for Large Tables, Incomplete
- Session 24: Table Environment, Incomplete
- Session 25: Including Images, Incomplete
- Session 26: Image Properties, Incomplete
- Session 27: Working with Image Borders, Incomplete
- Session 28: Figure and Sub-Figures, Incomplete
- Session 29: Recapitulate Topic 4, Incomplete

Topic 5: Referencing and Indexing, Incomplete section
- Session 30: Creating Title Page, Incomplete
- Session 31: Hyperlinks, Incomplete
- Session 32: Cross Referencing, Incomplete
- Session 33: Creating Indexes, Incomplete
- Session 34: Creating Bibliography, Incomplete
- Session 35: Recapitulate Topic 5, Incomplete

Topic 6: Presentation using Beamer, Incomplete section
- Session 36: Introduction to Beamer, Incomplete
- Session 37: Blocks and Columns, Incomplete
- Session 38: Overlays, Incomplete
- Session 39: Customize Basic Information, Incomplete
- Session 40: Customize Themes, Incomplete
- Session 41: Aspect Ratio, Incomplete
- Session 42: Recapitulate Topic 6


## Dashes
Where there is love there is life --- Mahatma Gandhi
\textemdash

pages 5 -- 7 explain Deep Learning.
\textendash

two-sided

## Quotes
` for opening quotes 
' represents the closing of quotes

\paragraph{}


## Command
\today, \pagebreak, \title{...}, \author{...}, \section{...}[]

## Environment
\begin{...}
   ...
\end{...}

### Package & Class
- In LaTeX, a document can have only 1 class but many packages. 
- Class files have .cls extension and are responsible for the overall layout, structuring (organizing), and formatting of a document. For example, a book class contains chapters, sections, parts; while an article contains sections, subsections. Each of which has a different set and style of formatting. The class files will be available on your system as article.cls, book.cls, etc..
- Packages have a .sty extension also called as style files. The primary objective of the package is to add some functionality, irrespective of the class in which it will be used. Some examples to note are, 'geometry' package, that is used to specify margins and paper size; 'graphicx' package, that is used to include an image, etc.. All of these can be used in any class. The packages will be available on your system as geometry.sty, graphicx.sty, etc.

\usepackage[params]{packagename}
\usepackage[a5paper, margin=1.5in]{geometry}
\usepackage[a5paper, top=1.5in, left=, right=, bottom=]{geometry}
\usepackage[a5paper, inner=1.5in, outer=, ]{geometry}

\pagestyle{empty} => no page number 
\thispagestyle{headings} => this should be written within section. It will have page# in heading.
\setcoutner{page}[1]

\pageumbering{roman}
\tableofcontents
\pageumbering{arabic}
\chapter{Annexure}
\pagenumbering{Alph}
\setcoutner{page}[1]


## Fancy Header 
\usepackage{fancyhdr}
\pagestyle{fancy}
\usepackage{lastpage}

\lhead, \rhead, \chead
\lfoot, \rhead, \chead

if you want to mention chapter 
\thesection \thepage \thechapter

- Define Header
	\lhead{\today}
	\chead{}
	\rhead{Draft}

- Define Footer
	\lfoot{Firuza, Nagesh}
	\cfoot{Sample.pdf}
	\rfoot{Page \thepage of \pageref{LastPage}}



- Horizontal line after header and before footer
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}
Here, X denotes the width of the line

\thispagestyle{plain}

## Orientation
### Landscape 
### Portrait
\usepackge[landscape]{geometry}

\usepackage{lipsum}
\lipsum[1-10]

begin{landscape}
end{landsacpe}

\usepackage{pdflscape}
\pagebreak or \newpage 

\footnote{}


## Two columns
\usepackage[twocolumn]{article}
\usepackage{multicol}

\begin{multicols}{3}
\setlength{\columnsep}{20pt}
\setlength{\columnseprule}{3pt}

\columnbreak
\end{multicols}

\textbf \emph \underline 


## Fontsize 
Unlike other \textbf{WYSIWYG editors}, the \emph{content is written in plain text} along with appropriate commands, thus, allowing the user to \underline{concentrate} on the content rather than the aesthetics (the way it looks). The {\Large TeX} typesetting program which LaTeX uses, was designed such that anyone can create good quality {\footnotesize material with less efforts.}



## Color 
\usepackage[dvipsnames]{xcolors}


- Traditional TeX will output a DVI file, which is usually converted to a PostScript file
 - Hàn Thế Thành and others have written a new implementation of TeX called pdfTeX, which also outputs to PDF and takes advantage of features available in that format
 - XeTeX engine developed by Jonathan Kew, on the other hand, merges modern font technologies and Unicode with TeX
 - XeTeX allows the use of OpenType and TrueType (that is, outlined) fonts for output files
 - https://en.wikipedia.org/wiki/Comparison_of_TeX_editors
  