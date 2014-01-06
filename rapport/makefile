TEX = pdflatex
SOURCES=$(wildcard *.tex)

.PHONY: all clean           

all: rapport.pdf

rapport.pdf: rapport.tex ${SOURCES} 
	$(TEX) $< 
	$(TEX) $< 

clean:
	rm *.aux *.toc *.log *.pdf *.out
