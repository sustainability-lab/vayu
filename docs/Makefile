# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS      =
SPHINXBUILD     = python $(shell which sphinx-build)
# SPHINXBUILD     = sphinx-build
SPHINXPROJ      = vayu
SOURCEDIR       = .
BUILDDIR        = _build

APIDOCOUTDIR    = ./pages
PROJDIR         = ../$(SPHINXPROJ)
SPHINXAPIDOC    = sphinx-apidoc

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# environment:
# 	@source ../../.env/bin/activate

clean: 
	@rm -rf _build

github:
# 	@make environment
	@make clean
	@$(SPHINXAPIDOC) -o "$(APIDOCOUTDIR)" "$(PROJDIR)"
	@make html
	@cp -a _build/html/. ../docs
	@rm -r _build/html/