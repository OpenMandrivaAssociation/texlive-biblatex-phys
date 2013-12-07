# revision 29139
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-phys
# catalog-date 2013-02-15 22:57:04 +0100
# catalog-license lppl1.3
# catalog-version 0.9e
Name:		texlive-biblatex-phys
Version:	0.9e
Release:	4
Summary:	A biblatex implementation of the AIP and APS bibliography style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-phys
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-phys.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-phys.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The biblatex-phys package provides an implementation of the
bibliography styles of both the AIP and the APS for biblatex.
This implementation follows standard biblatex conventions, and
can be used simply by loading biblatex with the appropriate
option: \usepackage[style=phys]{biblatex} A demonstration
database is provided to show how to format input for the style.
Style options are provided to cover the minor formatting
variations between the AIP and APS bibliography styles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-phys/phys.bbx
%{_texmfdistdir}/tex/latex/biblatex-phys/phys.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-phys/README
%doc %{_texmfdistdir}/doc/latex/biblatex-phys/biblatex-phys.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-phys/biblatex-phys.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-phys/biblatex-phys.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
