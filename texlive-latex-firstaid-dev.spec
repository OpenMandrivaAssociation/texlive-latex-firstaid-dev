Name:		texlive-latex-firstaid-dev
Version:	64899
Release:	2
Summary:	Development pre-release of the LaTeX firstaid package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-firstaid-dev
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-firstaid-dev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-firstaid-dev.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-firstaid-dev.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a pre-release version of the standard LaTeX firstaid
package. It accompanies the pre-testing kernel code
(latex-base-dev), and is intended for testing by knowledgeable
users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/source
%doc %{_texmfdistdir}/source/latex-dev
%doc %{_texmfdistdir}/source/latex-dev/firstaid
%doc %{_texmfdistdir}/source/latex-dev/firstaid/latex2e-first-aid-for-external-files.dtx
%doc %{_texmfdistdir}/source/latex-dev/firstaid/firstaid.ins
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/latex-dev
%{_texmfdistdir}/tex/latex-dev/firstaid
%{_texmfdistdir}/tex/latex-dev/firstaid/latex2e-first-aid-for-external-files.ltx
%{_texmfdistdir}/tex/latex-dev/firstaid/filehook-ltx.sty
%{_texmfdistdir}/tex/latex-dev/firstaid/everysel-ltx.sty
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/latex-dev
%doc %{_texmfdistdir}/doc/latex-dev/firstaid
%doc %{_texmfdistdir}/doc/latex-dev/firstaid/latex2e-first-aid-for-external-files.pdf
%doc %{_texmfdistdir}/doc/latex-dev/firstaid/changes.txt
%doc %{_texmfdistdir}/doc/latex-dev/firstaid/README.md

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
