%define		mver		1.3
%define		subver	3
%define		_db3ver	3.1.17
%define		_dbdir	$RPM_BUILD_DIR/%{name}-%{version}/db3-headers-%{_db3ver}

Summary:	The GNOME2 Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME2/Kalendarz/Ksi±¿ka Adresowa
Summary(pt_BR):	Cliente de email integrado com calendário e catálogo de endereços
Summary(zh_CN):	Evolution - GNOME2¸öÈËºÍ¹¤×÷×éÐÅÏ¢¹ÜÀí¹¤¾ß(°üÀ¨µç×ÓÓÊ¼þ£¬ÈÕÀúºÍµØÖ·±¡)
Name:		evolution
Version:	%{mver}.%{subver}
Release:	0.1
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.gnome.org/mirror/gnome.org/sources/evolution/%{mver}/%{name}-%{version}.tar.bz2
Source1:	%{name}-db3-headers-%{_db3ver}.tar.bz2
Patch0:		%{name}-nostaticdb3.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-configure_in.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-gnome_prefix.patch
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 2.3.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.5
BuildRequires:	gal-devel >= 1.99.3.99-0.20030425.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-pilot-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
Buildrequires:	gtk-doc >= 0.6
BuildRequires:	gtkhtml-devel >= 3.0.2-0.20030425.1
BuildRequires:	intltool >= 0.18
BuildRequires:	libbonoboui-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgnomeprintui-devel >= 2.2.1
BuildRequires:	libgnomeui-devel
BuildRequires:	libsoup-devel >= 1.99.17-0.20030425.1
BuildRequires:	libtool
BuildRequires:	libunicode-devel >= 0.4
BuildRequires:	libxml2
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	openldap-devel >= 2.0.0
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pilot-link-devel >= 0.11.4
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	scrollkeeper >= 0.1.4
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post):		GConf2
Requires:	GConf2
Requires:	bonobo-activation
Requires:	db3 = %{_db3ver}
Requires:	gal >= 1.99.3.99-0.20030425.1
Requires:	gtkhtml >= 3.0.2-0.20030425.1
Requires:	libglade2
Requires:	psmisc
Requires:	scrollkeeper >= 0.1.4
Obsoletes:	evolution2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Evolution is the GNOME2 mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will be tightly
integrated with one another and act as a seamless personal
information-management tool.

%description -l pl
Evolution to program pocztowy GNOME2, kalendarz, ksi±¿ka adresowa i
narzêdzie komunikacyjne.

%description -l pt_BR
Evolution é um cliente de email para o GNOME2 com calendário e outras
ferramentas interessantes.

%package devel
Summary:	Header files for evolution
Summary(pl):	Pliki nag³ówkowe i dokumentacja
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento
Summary(zh_CN):	Evolution×é¼þ¿ª·¢¿â
Group:		Development/Libraries
Requires:	cyrus-sasl-devel
Requires:	freetype-devel
Requires:	gal-devel >= 1.99.3.99-0.20030425.1
Requires:	gnome-vfs2-devel
Requires:	gtkhtml-devel >= 3.0.2-0.20030425.1
Requires:	libglade2-devel
Requires:	libgnomeprintui-devel >= 2.2.1
Requires:	libgnomeui-devel
Requires:	libunicode-devel
Requires:	nspr-devel
Requires:	nss-devel
Requires:	openldap-devel
Requires:	openssl-devel >= 0.9.7
Requires:	%{name} = %{version}
Obsoletes:	evolution2-devel

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
Obsoletes:	evolution2-static

%description static
This package contains static libraries for Evolution.

%description static -l pl
Pakiet zawiera statyczne biblioteki Evolution.

%description static -l pt_BR
Este pacote contém as bibliotecas estáticas para desenvolvimento de
aplicações.

%package pilot
Summary:	Evolution conduits for gnome-pilot
Summary(pl):	Dodatki do wymiany danych z gnome-pilot
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	evolution2-pilot

%description pilot
This package contains conduits needed by gnome-pilot to synchronize
your Palm with Evolution.

%description pilot -l pl
Ten pakiet zawiera dodatki do synchronizacji danych Evolution z
Palmem.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__autoconf}
%{__automake}
cd libical
# workaround for libtoolize to install ltmain.sh in . not ..
touch install-sh
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
cd ..
%configure \
	--enable-gtk-doc \
	--enable-pilot-conduits=yes \
	--with-openldap=yes \
	--without-static-ldap \
	--enable-nntp=no \
	--enable-file-locking=fcntl --enable-dot-locking=no \
	--with-nspr-includes="%{_includedir}/nspr" \
	--with-nss-includes="%{_includedir}/nss" \
	--with-nspr-libs="%{_libdir}" \
	--with-nss-libs="%{_libdir}" \
	--enable-ipv6=yes \
	--with-html-dir=%{_gtkdocdir} \
	--with-db3-includes=%{_dbdir} \
	--with-db3-libs=/lib \
	--with-kde-applnk-path=no

%{__make} \
	GTKHTML_DATADIR=%{_datadir}/idl

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	KDE_APPLNK_DIR=%{_applnkdir}/Network/Mail \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GTKHTML_DATADIR=%{_datadir}/idl

# strip doesn't pass this files and they aren't necessary, so remove them
# probably this should be done differently, but I have no idea
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/%{mver}/*/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/%{mver}/libemiscwidgets.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/*/*.a

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig %{_libdir}/evolution/%{mver}
/sbin/ldconfig
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/evolution/*/*/*.so*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/camel/*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-ldif-importer
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-vcard-importer
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-wombat
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-addressbook-clean
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-addressbook-import
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-launch-composer
%attr(755,root,root) %{_libdir}/evolution/%{mver}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{mver}/killev
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/%{mver}
%dir %{_libdir}/evolution/%{mver}/camel*
%dir %{_libdir}/evolution/%{mver}/components
%dir %{_libdir}/evolution/%{mver}/evolution-mail-importers
%{_libdir}/bonobo/servers/*
%{_libdir}/evolution/%{mver}/camel-providers/*.urls
%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/%{mver}
%{_datadir}/evolution/%{mver}/*.xml
%{_datadir}/evolution/%{mver}/*.schema
%{_datadir}/evolution/%{mver}/Locations
%{_datadir}/evolution/%{mver}/default_user
%{_datadir}/evolution/%{mver}/ecps
%{_datadir}/evolution/%{mver}/etspec
%{_datadir}/evolution/%{mver}/glade
%{_datadir}/evolution/%{mver}/images
%{_datadir}/evolution/%{mver}/ui
%dir %{_datadir}/evolution/%{mver}/tools
%attr(755,root,root) %{_datadir}/evolution/%{mver}/tools/*
%{_datadir}/evolution/%{mver}/views
%{_datadir}/evolution/%{mver}/zoneinfo
%{_datadir}/mime-info/*
%{_datadir}/idl/*
%{_datadir}/applications/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
%{_omf_dest_dir}/%{name}
%{_datadir}/gnome/help/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{mver}/*.so
%{_libdir}/evolution/%{mver}/*.la
%{_libdir}/evolution/*/*/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/evolution/%{mver}/*.a

%files pilot
%defattr(644,root,root,755)
%{_libdir}/gnome-pilot/conduits/*
%{_datadir}/gnome-pilot/conduits/*
