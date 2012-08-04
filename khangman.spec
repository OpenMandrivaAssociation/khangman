Name:		khangman
Summary:	Classical hangman game
Version: 4.9.0
Release: 1
Group:		Graphical desktop/KDE
License:	GPLv2 GFLD
URL:		http://edu.kde.org/khangman
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libkdeedu-devel >= %{version}
Requires:	libkdeedu = %{version}

%description
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%files
%doc COPYING COPYING.DOC README
%doc %{_kde_docdir}/HTML/en/%{name}
%{_kde_appsdir}/%{name}
%{_kde_bindir}/%{name}
%{_kde_iconsdir}/*/*/apps/%{name}*
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_configdir}/%{name}.knsrc
%{_kde_mandir}/man6/%{name}.6.*

#----------------------------------------------------------------------------

%define khangmanengine_major 4
%define libkhangmanengine %mklibname khangmanengine %{khangmanengine_major}

%package -n %{libkhangmanengine}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries

%description -n %{libkhangmanengine}
Runtime library for KDE Education Application.

%files -n %{libkhangmanengine}
%{_kde_libdir}/libkhangmanengine.so.%{khangmanengine_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkhangmanengine} = %{version}-%{release}
Requires:	kdelibs4-devel
Requires:	libkdeedu-devel

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libkhangmanengine.so
%{_includedir}/%{name}

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

