Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME/Kalendarz/Ksi±¿ka Adresowa
Name:		evolution
Version: 	0.8
Release:	1
Copyright:	GPL
Group:		Applications/Mail
Source: 	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.helixcode.com/aoos/evolution.php3
BuildRequires:	libxml-devel >= 1.8.7
BuildRequires:	bonobo-devel >= 0.20
BuildRequires:	gtkhtml-devel >= 0.8-2
BuildRequires:	libunicode-devel >= 0.4
BuildRequires:	oaf-devel >= 0.5.1
BuildRequires:  gnome-vfs-devel >= 0.3.1
BuildRequires:	gnome-print-devel >= 0.20
BuildRequires:	gnome-libs-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	gal-devel >= 0.2.1
BuildRequires:	libglade-devel
BuildRequires:	ORBit-devel
BuildRequires:	gettext-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool.  The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool. 

%description -l pl
Evolution to program pocztowy GNOME, kalendarz, ksi±¿ka adresowa
i narzêdzie komunikacyjne. 

%package devel
Summary:        Header files for evolution
Summary(pl):	Pliki nag³ówkowe i dokumentacja
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
This package contains the files necessary to develop applications
using Evolution's libraries.

%description -l pl devel
Pakiet zawiera pliki potrzebne do rozwoju aplikacji u¿ywaj±cych
bibliotek programu Evolution.

%package static
Summary:        Static libraries for evolution
Summary(pl):	Biblioteki statyczne dla evolution
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description static
This package contains static libraries for Evolution.

%description -l pl static
Pakiet zawiera statyczne biblioteki Evolution.

%prep
%setup -q

%build
gettextize -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Mail

gzip -9nf AUTHORS ChangeLog NEWS

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/evolution/camel-providers/*/*.so*
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/evolution/camel-providers/*/*.urls
%{_datadir}/evolution
%{_datadir}/oaf/*.oafinfo
%{_datadir}/idl/*.idl
%{_datadir}/gnome/apps/Applications/*.desktop
%{_datadir}/gnome/html
%{_datadir}/gnome/ui
%{_datadir}/images/evolution
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/evolution/camel-providers/*/*.a
