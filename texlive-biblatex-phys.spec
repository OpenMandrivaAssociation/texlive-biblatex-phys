%global tl_name biblatex-phys
%global tl_revision 74898

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1e
Release:	%{tl_revision}.1
Summary:	A BibLaTeX implementation of the AIP and APS bibliography style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-phys
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-phys.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-phys.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an implementation of the bibliography styles of
both the AIP and the APS for BibLaTeX. This implementation follows
standard BibLaTeX conventions, and can be used simply by loading
BibLaTeX with the appropriate option: \usepackage[style=phys]{biblatex}
A demonstration database is provided to show how to format input for the
style. Style options are provided to cover the minor formatting
variations between the AIP and APS bibliography styles.

