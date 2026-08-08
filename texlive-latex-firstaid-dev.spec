%global tl_name latex-firstaid-dev
%global tl_revision 79901

Name:		texlive-%{tl_name}
Epoch:		1
Version:	pre~release.1
Release:	%{tl_revision}.1
Summary:	Development pre-release of the LaTeX firstaid package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex-dev/required/firstaid
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-firstaid-dev.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-firstaid-dev.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-firstaid-dev.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a pre-release version of the standard LaTeX firstaid package. It
accompanies the pre-testing kernel code (latex-base-dev), and is
intended for testing by knowledgeable users.

