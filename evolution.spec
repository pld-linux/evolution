Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME/Kalendarz/Ksi±¿ka Adresowa
Summary(pt_BR):	Cliente de email integrado com calendário e catálogo de endereços
Name:		evolution
Version:	1.0.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.gnome.org/pub/gnome/stable/sources/evolution/%{name}-%{version}.tar.bz2
Patch0:		%{name}-nostaticdb3.patch
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	GConf-devel >= 1.0.7
BuildRequires:	ORBit-devel >= 0.5.8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bonobo-conf-devel >= 0.11
BuildRequires:	bonobo-devel >= 1.0.15-2
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db3-devel
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.5
BuildRequires:	gal-devel >= 0.19
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.9
BuildRequires:	gnome-print-devel >= 0.25
BuildRequires:	gnome-vfs-devel >= 1.0.1
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	gtkhtml-devel >= 1.0.1
BuildRequires:	intltool
BuildRequires:	libglade-devel >= 0.14
BuildRequires:	libunicode-devel >= 0.4
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	oaf-devel >= 0.6.7
BuildRequires:	openldap-devel >= 2.0.0
BuildRequires:	openssl-devel
BuildRequires:	python
BuildRequires:	scrollkeeper
Requires:	scrollkeeper >= 0.1.4
Requires:	bonobo >= 1.0.14
Requires:	GConf >= 1.0.7
Requires:	oaf >= 0.6.7
Requires:	libglade >= 0.17
Requires:	gtkhtml >= 1.0.0-2
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will be tightly
integrated with one another and act as a seamless personal
information-management tool.

%description -l pl
Evolution to program pocztowy GNOME, kalendarz, ksi±¿ka adresowa i
narzêdzie komunikacyjne.

%description -l pt_BR
Evolution é um cliente de email para o GNOME com calendário e outras
ferramentas interessantes.

%package devel
Summary:	Header files for evolution
Summary(pl):	Pliki nag³ówkowe i dokumentacja
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento
Group:		Development/Libraries
Requires:	cyrus-sasl-devel
Requires:	freetype-devel
Requires:	gal-devel
Requires:	gdk-pixbuf-devel
Requires:	gnome-libs-devel
Requires:	gnome-print-devel
Requires:	gnome-vfs-devel
Requires:	gtkhtml-devel
Requires:	libglade-devel
Requires:	libunicode-devel
Requires:	nspr-devel
Requires:	nss-devel
Requires:	oaf-devel
Requires:	openldap-devel
Requires:	openssl-devel
Requires:	%{name} = %{version}

%description devel
This package contains the files necessary to develop applications
using Evolution's libraries.

%description devel -l pl
Pakiet zawiera pliki potrzebne do rozwoju aplikacji u¿ywaj±cych
bibliotek programu Evolution.

%description devel -l pt_BR
Este pacote contém os arquivos necessários para desenvolvimento de
aplicações utilizando as bibliotecas do Evolution.

%package static
Summary:	Static libraries for evolution
Summary(pl):	Biblioteki statyczne dla evolution
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
This package contains static libraries for Evolution.

%description static -l pl
Pakiet zawiera statyczne biblioteki Evolution.

%description static -l pt_BR
Este pacote contém as bibliotecas estáticas para desenvolvimento de
aplicações.

%prep
%setup -q
%patch0 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
xml-i18n-toolize --copy --force
libtoolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c -f
cd libical; autoconf; cd ..

CFLAGS="%{rpmcflags} -I/usr/include/orbit-1.0"
%configure \
	--disable-gtk-doc \
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
	desktopdir=%{_applnkdir}/Network/Mail \
	omf_dest_dir=%{_omf_dest_dir}/omf/%{name}

gzip -9nf AUTHORS ChangeLog NEWS

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/evolution/*/*/*.so*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/*
%dir %{_libdir}/evolution/*/*
%{_mandir}/man1/*
%{_libdir}/evolution/camel-providers/*/*.urls
%{_datadir}/evolution
%{_datadir}/oaf/*.oaf
%{_datadir}/gnome/ui
%{_datadir}/gnome/html/*
%{_datadir}/images
%{_datadir}/mime-info/*
%{_datadir}/libical-evolution
%{_datadir}/idl/*.idl
%{_omf_dest_dir}/omf/%{name}
%{_applnkdir}/Network/Mail/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.??
%attr(755,root,root) %{_libdir}/evolution/*/*/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/evolution/*/*/*.a
