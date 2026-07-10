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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an implementation of the bibliography styles of
both the AIP and the APS for BibLaTeX. This implementation follows
standard BibLaTeX conventions, and can be used simply by loading
BibLaTeX with the appropriate option: \usepackage[style=phys]{biblatex}
A demonstration database is provided to show how to format input for the
style. Style options are provided to cover the minor formatting
variations between the AIP and APS bibliography styles.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-phys
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-phys
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-phys/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-phys/biblatex-phys.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-phys/biblatex-phys.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-phys/biblatex-phys.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-phys/phys.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-phys/phys.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-phys/phys.dbx
