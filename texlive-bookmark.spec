%global tl_name bookmark
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.32
Release:	%{tl_revision}.1
Summary:	A new bookmark (outline) organization for hyperref
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bookmark
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookmark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookmark.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookmark.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a new bookmark (outline) organization for
package hyperref. Bookmark properties such as style and color can now be
set. Other action types are available (URI, GoToR, Named). The bookmarks
are generated in the first compile run. Package hyperref uses two runs.

