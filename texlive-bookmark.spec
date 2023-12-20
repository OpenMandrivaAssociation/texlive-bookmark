Name:		texlive-bookmark
Version:	69084
Release:	1
Summary:	A new bookmark (outline) organization for hyperref
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bookmark
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookmark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookmark.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookmark.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a new bookmark (outline) organization
for package hyperref. Bookmark properties such as style and
color can now be set. Other action types are available (URI,
GoToR, Named). The bookmarks are generated in the first compile
run. Package hyperref uses two runs.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bookmark
%{_texmfdistdir}/tex/latex/bookmark
%doc %{_texmfdistdir}/doc/latex/bookmark

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
