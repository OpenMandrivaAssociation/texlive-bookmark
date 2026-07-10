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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a new bookmark (outline) organization for
package hyperref. Bookmark properties such as style and color can now be
set. Other action types are available (URI, GoToR, Named). The bookmarks
are generated in the first compile run. Package hyperref uses two runs.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bookmark
%dir %{_datadir}/texmf-dist/source/latex/bookmark
%dir %{_datadir}/texmf-dist/tex/latex/bookmark
%doc %{_datadir}/texmf-dist/doc/latex/bookmark/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bookmark/bookmark-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/bookmark/bookmark.pdf
%doc %{_datadir}/texmf-dist/source/latex/bookmark/bookmark.dtx
%doc %{_datadir}/texmf-dist/source/latex/bookmark/bookmark.ins
%{_datadir}/texmf-dist/tex/latex/bookmark/bkm-dvipdfmx.def
%{_datadir}/texmf-dist/tex/latex/bookmark/bkm-dvips.def
%{_datadir}/texmf-dist/tex/latex/bookmark/bkm-luatex.def
%{_datadir}/texmf-dist/tex/latex/bookmark/bkm-pdftex.def
%{_datadir}/texmf-dist/tex/latex/bookmark/bkm-vtex.def
%{_datadir}/texmf-dist/tex/latex/bookmark/bkm-xetex.def
%{_datadir}/texmf-dist/tex/latex/bookmark/bookmark.sty
