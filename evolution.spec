
%bcond_without ldap

%define		mver		1.4
%define		subver	5
%define		_db3ver	3.1.17
%define		_dbdir	$RPM_BUILD_DIR/%{name}-%{version}/db-%{_db3ver}

Summary:	The GNOME2 Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME2/Kalendarz/Ksi笨ka Adresowa
Summary(pt_BR):	Cliente de email integrado com calend醨io e cat醠ogo de endere鏾s
Summary(zh_CN):	Evolution - GNOME2个人和工作组信息管理工具(包括电子邮件，日历和地址薄)
Name:		evolution
Version:	%{mver}.%{subver}
Release:	8
License:	GPL
Group:		Applications/Mail
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/%{mver}/%{name}-%{version}.tar.bz2
# Source0-md5:	f16a86d6eaa9d9683f215586fcdac374
Source1:	http://www.sleepycat.com/update/snapshot/db-%{_db3ver}.tar.gz
# Source1-md5:	5baeb94fb934d0bf783ea42117c400be
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-configure_in.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-pldify.patch
Patch4:		%{name}-iconv_flush.patch
Patch5:		%{name}-div_by_zero.patch
Patch6:		%{name}-ipv6.patch
Patch7:		%{name}-ipv6_smtp.patch
Patch8:		%{name}-timezone_offsets.patch
Patch9:		%{name}-gethostbyaddr.patch
Patch10:	%{name}-addrconfig.patch
Patch11:	%{name}-libpcs_libpas.patch
Patch12:	%{name}-no-static-in-shared.patch
Patch13:	%{name}-attachment_require_terminal.patch
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 2.8.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.5
BuildRequires:	gal-devel >= 1:1.99.9
BuildRequires:	gcc-g77
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-pilot-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	gtkhtml-devel >= 3.0.8
BuildRequires:	intltool >= 0.18
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libsoup-devel >= 1.99.26-3
BuildRequires:	libtool
BuildRequires:	libxml2
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.0.0}
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pilot-link-devel >= 0.11.4
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	which
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post):		GConf2
Requires:	GConf2
Requires:	bonobo-activation
Requires:	gal >= 1:1.99.9
Requires:	gtkhtml >= 3.0.8
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
Evolution to program pocztowy GNOME2, kalendarz, ksi笨ka adresowa i
narz阣zie komunikacyjne.

%description -l pt_BR
Evolution � um cliente de email para o GNOME2 com calend醨io e outras
ferramentas interessantes.

%package devel
Summary:	Header files for evolution
Summary(pl):	Pliki nag丑wkowe i dokumentacja
Summary(pt_BR):	Bibliotecas e arquivos de inclus鉶 para desenvolvimento
Summary(zh_CN):	Evolution组件开发库
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	cyrus-sasl-devel
Requires:	freetype-devel
Requires:	gal-devel >= 1:1.99.9
Requires:	gnome-vfs2-devel >= 2.4.0
Requires:	gtkhtml-devel >= 3.0.8
Requires:	libglade2-devel >= 2.0.1
Requires:	libgnomeprintui-devel >= 2.4.0
Requires:	libgnomeui-devel >= 2.4.0
Requires:	libsoup-devel >= 1.99.23
Requires:	nspr-devel
Requires:	nss-devel
%{?with_ldap:Requires:	openldap-devel >= 2.0.0}
Requires:	openssl-devel >= 0.9.7c
Obsoletes:	evolution2-devel

%description devel
This package contains the files necessary to develop applications
using Evolution's libraries.

%description devel -l pl
Pakiet zawiera pliki potrzebne do rozwoju aplikacji u縴waj眂ych
bibliotek programu Evolution.

%description devel -l pt_BR
Este pacote cont閙 os arquivos necess醨ios para desenvolvimento de
aplica珲es utilizando as bibliotecas do Evolution.

%package static
Summary:	Static libraries for evolution
Summary(pl):	Biblioteki statyczne dla evolution
Summary(pt_BR):	Bibliotecas est醫icas para desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	evolution2-static

%description static
This package contains static libraries for Evolution.

%description static -l pl
Pakiet zawiera statyczne biblioteki Evolution.

%description static -l pt_BR
Este pacote cont閙 as bibliotecas est醫icas para desenvolvimento de
aplica珲es.

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
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch10 -p0
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
# first build db3 (only static, C interface)
cd %{_dbdir}/build_unix
CFLAGS="%{rpmcflags}" \
../dist/configure \
	--prefix=%{_prefix} \
	--enable-static
%{__make}
cd $RPM_BUILD_DIR/%{name}-%{version}

# build evolution
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__autoconf}
%{__automake}
cd libical
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
# don't use -f here
automake -a -c --foreign
cd ..
%configure \
	--enable-gtk-doc \
	--enable-pilot-conduits=yes \
	%{?with_ldap:--with-openldap=yes} \
	%{!?with_ldap:--with-openldap=no} \
	--without-static-ldap \
	--enable-nntp=no \
	--enable-file-locking=fcntl --enable-dot-locking=no \
	--with-nspr-includes="%{_includedir}/nspr" \
	--with-nss-includes="%{_includedir}/nss" \
	--with-nspr-libs="%{_libdir}" \
	--with-nss-libs="%{_libdir}" \
	--enable-ipv6=yes \
	--with-html-dir=%{_gtkdocdir} \
	--with-db3-includes=%{_dbdir}/build_unix \
	--with-db3-libs=%{_dbdir}/build_unix \
	--with-kde-applnk-path=no

# hack to rebuild *.c and *.h from *.idl (check if needed with new versions)
# (required if you use ORBit2-devel 2.7.2)
find -name \*.idl -exec touch {} \;

%{__make} \
	GTKHTML_DATADIR=%{_datadir}/idl

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	KDE_APPLNK_DIR=%{_applnkdir}/Network/Mail \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GTKHTML_DATADIR=%{_datadir}/idl

# strip doesn't pass these files and they aren't necessary, so remove them
# probably this should be done differently, but I have no idea
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/%{mver}/*/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/%{mver}/libemiscwidgets.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/*/*.{a,la}

%find_lang evolution-1.4 --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f evolution-1.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/evolution/*/*/*.so*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/*.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/camel/*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-ldif-importer
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-vcard-importer
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-wombat
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-addressbook-clean
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-addressbook-import
%attr(755,root,root) %{_libdir}/evolution/%{mver}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{mver}/killev
%attr(755,root,root) %{_libdir}/evolution/%{mver}/load-*
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
%{_datadir}/evolution/%{mver}/views
%{_datadir}/evolution/%{mver}/zoneinfo
%{_datadir}/mime-info/*
%{_datadir}/idl/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
%{_omf_dest_dir}/%{name}

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
%attr(755,root,root) %{_libdir}/gnome-pilot/conduits/*
%{_datadir}/gnome-pilot/conduits/*
