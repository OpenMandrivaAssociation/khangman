Summary:	Classical hangman game
Name:		khangman
Version:	15.04.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/khangman
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdeedu-devel >= %{version}
BuildRequires:	kdelibs-devel

%description
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%files
%doc COPYING COPYING.DOC README
%doc %{_kde_docdir}/HTML/en/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_bindir}/%{name}
%{_kde_configdir}/%{name}.knsrc
%{_kde_datadir}/appdata/khangman.appdata.xml
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_iconsdir}/*/*/apps/%{name}*
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
