Name:		texlive-biblatex-phys
Version:	55643
Release:	1
Summary:	A biblatex implementation of the AIP and APS bibliography style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-phys
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-phys.r55643.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-phys.doc.r55643.tar.xz
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
%{_texmfdistdir}/tex/latex/biblatex-phys
%doc %{_texmfdistdir}/doc/latex/biblatex-phys

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
