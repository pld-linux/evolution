# TODO:
# - avoid linking with static db3
Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME/Kalendarz/Ksi±¿ka Adresowa
Name:		evolution
Version: 	0.11
Release:	1
License:	GPL
Group:		Applications/Mail
Source: 	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.bz2
#Patch0:		%{name}-DESTDIR.patch
#Patch1:		%{name}-use_AM_GNU_GETTEXT.patch
URL:		http://www.helixcode.com/apps/evolution.php3
BuildRequires:	libxml-devel >= 1.8.7
BuildRequires:	bonobo-devel >= 0.37
BuildRequires:	bonobo-conf-devel
BuildRequires:	gtkhtml-devel >= 0.10.1
BuildRequires:	libunicode-devel >= 0.4
BuildRequires:	oaf-devel >= 0.6.2
BuildRequires:  gnome-vfs-devel >= 1.0.1
BuildRequires:	gnome-print-devel >= 0.25
BuildRequires:	gnome-libs-devel >= 1.2.9
# needed for PALM Pilot support - not yet
#BuildRequires:	gnome-pilot-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	gal-devel >= 0.9.1
BuildRequires:	openldap-devel >= 2.0.0
BuildRequires:	openssl-devel
BuildRequires:	libglade-devel
BuildRequires:	ORBit-devel >= 0.5.6
BuildRequires:	GConf-devel >= 0.6
BuildRequires:	xml-i18n-tools > 0.8.2
BuildRequires:	db3-devel
BuildRequires:	db3-static
BuildRequires:	gettext-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	autoconf
BuildRequires:	automake
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
#%patch0 -p1
#%patch1 -p1

%build
rm missing
#libtoolize --copy --force
#gettextize --copy --force
#aclocal -I macros
#autoconf
automake -a -c

%configure2_13 \
	--prefix=%{_prefix} \
	--enable-pilot-conduits=no \
	--enable-ldap=yes \
	--enable-nntp=yes
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
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/evolution/*/*/*.so*
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/evolution/camel-providers/*/*.urls
%dir %{_datadir}/evolution/*
%{_datadir}/oaf/*.oaf
%{_datadir}/gnome/html
%{_datadir}/gnome/ui
#%{_datadir}/gnome/help
%{_datadir}/images/evolution
%{_datadir}/mime-info/*
%{_datadir}/libical/zoneinfo
#%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_applnkdir}/Network/Mail/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/evolution/*/*/*.la
%{_includedir}/*.h
%{_includedir}/camel/*.h
%{_includedir}/ename/*.h
%{_includedir}/evolution/*/*.h
%{_includedir}/libicalvcal/*.h
%{_datadir}/idl/*.idl

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/evolution/*/*/*.a
