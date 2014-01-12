TEX = pdflatex

SOURCES=$(wildcard *.tex)
IMAGE=$(wildcard *.[png,jpg])
TIKZ_SOURCES=$(wildcard graphTikZ/*.tex)

.PHONY: all clean           

all: rapport.pdf

rapport.pdf: rapport.tex ${SOURCES} ${TIKZ_SOURCES} ${IMAGE}
	$(TEX) $< 
	$(TEX) $< 

clean:
	rm *.aux *.toc *.log *.pdf *.out
