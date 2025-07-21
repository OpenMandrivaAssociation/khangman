#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Classical hangman game
Name:		khangman
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/khangman
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/khangman/-/archive/%{gitbranch}/khangman-%{gitbranchd}.tar.bz2#/khangman-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/khangman-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
# Can't do this while KF5 is still in the tree, it provides it too
#BuildRequires:	cmake(LibKEduVocDocument)
BuildRequires:	%mklibname KEduVocDocument6 -d
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:  qt6-qtbase-theme-gtk3
Obsoletes:		%{mklibname khangmanengine 4} < 16.04.2
Obsoletes:		khangman-devel  < 16.04.2

%rename plasma6-khangman

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%files -f %{name}.lang
%doc COPYING COPYING.DOC README
%{_bindir}/khangman
%{_datadir}/applications/org.kde.khangman.desktop
%{_datadir}/config.kcfg/khangman.kcfg
%{_iconsdir}/hicolor/*/apps/*.*[gz]
%{_datadir}/khangman
%{_mandir}/man6/khangman.6.*
%{_datadir}/metainfo/*.xml
%{_datadir}/knsrcfiles/khangman.knsrc
