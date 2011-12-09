Name: khangman
Summary: Classical hangman game
Version: 4.7.90
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFLD
URL: http://edu.kde.org/khangman
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: libkdeedu-devel >= %{version}

Requires: libkdeedu = %{version}

%description
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%files
%_kde_appsdir/khangman
%_kde_bindir/khangman
%_kde_iconsdir/*/*/apps/khangman.*
%_kde_datadir/applications/kde4/khangman.desktop
%_kde_datadir/config.kcfg/khangman.kcfg
%_kde_datadir/config/khangman.knsrc
%doc COPYING COPYING.DOC README
%doc %_kde_docdir/HTML/en/khangman
%_kde_mandir/man6/khangman.6.*

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

