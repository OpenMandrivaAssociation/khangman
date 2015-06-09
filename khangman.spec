Summary:	Classical hangman game
Name:		khangman
Version:	15.04.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/khangman
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(LibKEduVocDocument)

%description
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%files
%doc COPYING COPYING.DOC README
%doc %{_docdir}/HTML/*/%{name}
%{_bindir}/khangman
%{_sysconfdir}/xdg/khangman.knsrc
%{_datadir}/appdata/khangman.appdata.xml
%{_datadir}/applications/org.kde.khangman.desktop
%{_datadir}/config.kcfg/khangman.kcfg
%{_iconsdir}/hicolor/*/apps/*.*[gz]
%{_datadir}/khangman
%{_mandir}/man6/khangman.6.*


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
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
