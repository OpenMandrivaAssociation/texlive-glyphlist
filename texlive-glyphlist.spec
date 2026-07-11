%global tl_name glyphlist
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Adobe Glyph List and TeX extensions
Group:		Publishing
URL:		https://www.ctan.org/pkg/glyphlist
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glyphlist.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Map between traditional Adobe glyph names and Unicode points, maintained
by Adobe. The additional texglyphlist.txt is maintained as part of lcdf-
typetools.

