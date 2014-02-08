Name:		khangman
Summary:	Classical hangman game
Version:	4.12.1
Release:	2
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

%changelog
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Fri Jul 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Thu Jul 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95
- New subpackages libkhangmanengine and devel
- Update file list

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762465
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758058
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744539
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739296
- New upstream tarball $NEW_VERSION

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 731870
- New upstream tarball 4.7.80

* Wed Nov 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 729208
- Import package

