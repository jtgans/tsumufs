#!/usr/bin/make
#
# $Id$
#
# This makefile uses graphvis and gpic to generate all images
# included in the design doc. The gpic files also include the macros
# created by $NAME, located at <http://www.kohala.com/start/troff/Setup.pic.txt>.

DOT_TARGETS   := $(addsuffix .png, $(basename $(wildcard *.dot)))
CIRCO_TARGETS := $(addsuffix .png, $(basename $(wildcard *.circo)))
PIC_TARGETS   := $(addsuffix .png, $(basename $(wildcard *.pic)))

IMAGE_TARGETS := $(DOT_TARGETS) $(CIRCO_TARGETS) $(PIC_TARGETS)

all: images

images: $(IMAGE_TARGETS)

clean:
	rm -f $(IMAGE_TARGETS)

mrclean: clean
	find -iname \*~ -exec rm -rf '{}' ';' -prune

%.png: %.dot
	dot -Tpng $< > $@

%.png: %.circo
	circo -Tpng $< > $@

%.png: %.pic
	pic2graph -trim -bordercolor white -border 20 < $< > $@

.PHONY: clean mrclean
