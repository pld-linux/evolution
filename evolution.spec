# TODO:
# - avoid linking with static db3
Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME/Kalendarz/Ksi±øka Adresowa
Name:		evolution
Version:	1.0
Release:	3
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	AplicaÁıes/Correio EletrÙnico
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-use_AM_GNU_GETTEXT.patch
URL:		http://www.ximian.com/products/ximian_evolution/
Requires: scrollkeeper >= 0.1.4
Requires: bonobo >= 1.0.14
Requires: GConf >= 1.0.7
Requires: oaf >= 0.6.7
Requires: libglade >= 0.17
Requires: gtkhtml >= 1.0.0-2
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	bonobo-devel >= 1.0.15-2
BuildRequires:	bonobo-conf-devel >= 0.11
BuildRequires:	gtkhtml-devel >= 1.0.0-2
BuildRequires:	libunicode-devel >= 0.4
BuildRequires:	oaf-devel >= 0.6.7
BuildRequires:	gnome-vfs-devel >= 1.0.1
BuildRequires:	gnome-print-devel >= 0.25
BuildRequires:	gnome-libs-devel >= 1.2.9
#BuildRequires:	gnome-xml >= 1.8.10
BuildRequires:	gnome-print-devel >= 0.25
# needed for PALM Pilot support - not yet
#BuildRequires:	gnome-pilot-devel
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	gal-devel >= 0.18
BuildRequires:	openldap-devel >= 2.0.0
BuildRequires:	openssl-devel
BuildRequires:	libglade-devel >= 0.14
BuildRequires:	ORBit-devel >= 0.5.8
BuildRequires:	GConf-devel >= 1.0.7
BuildRequires:	intltool 
BuildRequires:	db3-devel
BuildRequires:	db3-static
BuildRequires:	gettext-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  freetype-static >= 2.0.5
BuildRequires:	scrollkeeper
BuildRequires:	kernel-headers
BuildRequires:  cyrus-sasl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will be tightly
integrated with one another and act as a seamless personal
information-management tool.

%description -l pl
Evolution to program pocztowy GNOME, kalendarz, ksi±øka adresowa i
narzÍdzie komunikacyjne.

%package devel
Summary:	Header files for evolution
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package contains the files necessary to develop applications
using Evolution's libraries.

%description -l pl devel
Pakiet zawiera pliki potrzebne do rozwoju aplikacji uøywaj±cych
bibliotek programu Evolution.

%package static
Summary:	Static libraries for evolution
Summary(pl):	Biblioteki statyczne dla evolution
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
This package contains static libraries for Evolution.

%description -l pl static
Pakiet zawiera statyczne biblioteki Evolution.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
#rm -f missing
#libtoolize --copy --force
#gettextize --copy --force
#aclocal -I macros
#autoconf
#automake -a -c

CFLAGS="%{rpmcflags} -I/usr/include/orbit-1.0"
%configure2_13 \
	--prefix=%{_prefix} \
	--enable-pilot-conduits=no \
	--with-openldap=yes \
	--with-static-ldap=no \
	--enable-nntp=yes \
	--with-gnome-includes=%{_includedir}/gnome-vfs-1.0/ \
	--enable-file-locking=fcntl --enable-dot-locking=no \
	--with-nspr-includes="/usr/include/nspr" \
	--with-nss-includes="/usr/include/nss" \
	--with-nspr-libs="/usr/lib" \
	--with-nss-libs="/usr/lib"
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
%attr(755,root,root) %{_libdir}/*.so.*
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/*
%dir %{_libdir}/evolution/*/*
%{_libdir}/evolution/camel-providers/*/*.urls
%{_datadir}/evolution
%{_datadir}/oaf/*.oaf
%{_datadir}/omf/*
%{_datadir}/gnome/ui
%{_datadir}/gnome/html/*
%{_datadir}/images/evolution
%{_datadir}/mime-info/*
%{_datadir}/libical-evolution
%{_applnkdir}/Network/Mail/*
%{_applnkdir}/Applications/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/evolution/*/*/*.la
%{_includedir}/*
%{_datadir}/idl/*.idl

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/evolution/*/*/*.a
