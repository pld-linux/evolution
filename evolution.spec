#
# todo:
# - splitting mail, addressbook and calendar:
#   - etspec?
#   - ui?
#   - dependencies, i.e.: mail should require addressbook?
#
# Conditionals:
%bcond_without ldap     # build without ldap support

%define		mver		1.5
%define		subver	91

Summary:	The GNOME2 Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME2/Kalendarz/Ksi��ka Adresowa
Summary(pt_BR):	Cliente de email integrado com calend�rio e cat�logo de endere�os
Summary(zh_CN):	Evolution - GNOME2���˺͹�������Ϣ������(���������ʼ��������͵�ַ��)
Name:		evolution
Version:	%{mver}.%{subver}
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/%{mver}/%{name}-%{version}.tar.bz2
# Source0-md5:	a811de01ad2d2cff5f908bb677f56510
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-gnome-icon-theme.patch
Patch3:		%{name}-GG-IM.patch
Patch4:		%{name}-desktop.patch
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	GConf2-devel >= 2.6.2
BuildRequires:	ORBit2-devel >= 1:2.10.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	evolution-data-server-devel >= 0.0.96
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.5
BuildRequires:	gal-devel >= 1:2.1.12
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-pilot-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.6.1.1
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	gtkhtml-devel >= 3.1.18
BuildRequires:	intltool >= 0.30
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.6.1
BuildRequires:	libgnomeui-devel >= 2.6.1.1
BuildRequires:	libsoup-devel >= 2.1.12
BuildRequires:	libtool
BuildRequires:	libxml2
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.0.0}
#BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pilot-link-devel >= 0.11.4
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	which
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post):		GConf2
Requires:	%{name}-component = %{version}-%{release}
Requires:	GConf2 >= 2.6.2
Requires:	bonobo-activation
Requires:	evolution-data-server >= 0.0.96
Requires:	gal >= 1:2.1.12
Requires:	gtkhtml >= 3.1.18
Requires:	libglade2 >= 1:2.4.0
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
Evolution to program pocztowy GNOME2, kalendarz, ksi��ka adresowa i
narz�dzie komunikacyjne.

%description -l pt_BR
Evolution � um cliente de email para o GNOME2 com calend�rio e outras
ferramentas interessantes.

%package devel
Summary:	Header files for evolution
Summary(pl):	Pliki nag��wkowe i dokumentacja
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento
Summary(zh_CN):	Evolution���������
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cyrus-sasl-devel
Requires:	freetype-devel
Requires:	gal-devel >= 1:2.1.12
Requires:	gnome-vfs2-devel >= 2.6.1.1
Requires:	gtkhtml-devel >= 3.1.18
Requires:	libglade2-devel >= 1:2.4.0
Requires:	libgnomeprintui-devel >= 2.6.1
Requires:	libgnomeui-devel >= 2.6.1.1
Requires:	libsoup-devel >= 2.1.12
Requires:	nspr-devel
Requires:	nss-devel
%{?with_ldap:Requires:	openldap-devel >= 2.0.0}
#Requires:	openssl-devel >= 0.9.7c
Obsoletes:	evolution2-devel

%description devel
This package contains the files necessary to develop applications
using Evolution's libraries.

%description devel -l pl
Pakiet zawiera pliki potrzebne do rozwoju aplikacji u�ywaj�cych
bibliotek programu Evolution.

%description devel -l pt_BR
Este pacote cont�m os arquivos necess�rios para desenvolvimento de
aplica��es utilizando as bibliotecas do Evolution.

%package static
Summary:	Static libraries for evolution
Summary(pl):	Biblioteki statyczne dla evolution
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	evolution2-static

%description static
This package contains static libraries for Evolution.

%description static -l pl
Pakiet zawiera statyczne biblioteki Evolution.

%description static -l pt_BR
Este pacote cont�m as bibliotecas est�ticas para desenvolvimento de
aplica��es.

%package mail
Summary:	Evolution mail component
Summary(pl):	Modu� pocztowy Evolution
Group:		X11/Applications
# mail composer requires addressbook component
Requires:	%{name}-addressbook = %{version}-%{release}
Requires(post,postun):	/sbin/ldconfig
Requires(post):		GConf2
Provides:	%{name}-component = %{version}-%{release}

%description mail
Evolution mail.

%description mail -l pl
Modu� pocztowy Evolution.

%package addressbook
Summary:	Evolution addressbook component
Summary(pl):	Modu� ksi��ki adresowej Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2
Provides:	%{name}-component = %{version}-%{release}

%description addressbook
Evolution addressbook.

%description addressbook -l pl
Ksi��ka adresowa Evolution.

%package calendar
Summary:	Evolution calendar and todo component
Summary(pl):	Modu� kalendarza i listy zada� Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2
Provides:	%{name}-component = %{version}-%{release}

%description calendar
Evolution calendar and todo component.

%description calendar -l pl
Kalendarz i lista zada� Evolution.

%package pilot
Summary:	Evolution conduits for gnome-pilot
Summary(pl):	Dodatki do wymiany danych z gnome-pilot
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	evolution2-pilot

%description pilot
This package contains conduits needed by gnome-pilot to synchronize
your Palm with Evolution.

%description pilot -l pl
Ten pakiet zawiera dodatki do synchronizacji danych Evolution z
Palmem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-pilot-conduits=yes \
	%{?with_ldap:--with-openldap=yes} \
	%{!?with_ldap:--with-openldap=no} \
	--without-static-ldap \
	--enable-nntp=yes \
	--enable-file-locking=fcntl \
	--enable-dot-locking=no \
	--with-nspr-includes="%{_includedir}/nspr" \
	--with-nss-includes="%{_includedir}/nss" \
	--with-nspr-libs="%{_libdir}" \
	--with-nss-libs="%{_libdir}" \
	--enable-ipv6=yes \
	--with-html-dir=%{_gtkdocdir} \
	--with-kde-applnk-path=no \
	--disable-schemas-install \
	--enable-nss=yes \
	--enable-smime=yes \
	--enable-static

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
	GTKHTML_DATADIR=%{_datadir}/idl \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

# strip doesn't pass these files and they aren't necessary, so remove them
# probably this should be done differently, but I have no idea
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/%{mver}/*/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/%{mver}/libemiscwidgets.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/*/*.{a,la}

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%post mail
/sbin/ldconfig
%gconf_schema_install

%postun mail
/sbin/ldconfig

%post addressbook
/sbin/ldconfig
%gconf_schema_install

%postun addressbook -p /sbin/ldconfig

%post calendar
/sbin/ldconfig
%gconf_schema_install

%postun calendar -p /sbin/ldconfig

%files -f evolution.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libeconduit.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libemiscwidgets.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libeselectnames.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libeshell.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libeutil.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libevolution-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libevolution-importer.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libevolution-widgets-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{mver}/killev
# addressbook requires it:
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libcamel*.so.*
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/%{mver}
%dir %{_libdir}/evolution/%{mver}/components
%{_libdir}/bonobo/servers/GNOME_Evolution_Shell_1.5.server
%dir %{_datadir}/idl/evolution-%{mver}
%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/%{mver}
%dir %{_datadir}/evolution/%{mver}/views
%{_datadir}/evolution/%{mver}/*.xml
%dir %{_datadir}/evolution/%{mver}/default
%dir %{_datadir}/evolution/%{mver}/default/C
%{_datadir}/evolution/%{mver}/errors
%{_datadir}/evolution/%{mver}/etspec
%{_datadir}/evolution/%{mver}/glade
%{_datadir}/evolution/%{mver}/help
%{_datadir}/evolution/%{mver}/images
%{_datadir}/evolution/%{mver}/ui
%{_datadir}/mime-info/*
%{_datadir}/idl/evolution-%{mver}/Evolution-Component.idl
%{_datadir}/idl/evolution-%{mver}/Evolution-ConfigControl.idl
%{_datadir}/idl/evolution-%{mver}/Evolution-Offline.idl
%{_datadir}/idl/evolution-%{mver}/Evolution-Shell.idl
%{_datadir}/idl/evolution-%{mver}/Evolution-Wizard.idl
%{_datadir}/idl/evolution-%{mver}/Evolution-common.idl
%{_datadir}/idl/evolution-%{mver}/Evolution.idl
%{_datadir}/idl/evolution-%{mver}/GNOME_Evolution_Importer.idl
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/apps_evolution_shell-1.5.schemas
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

%files mail
%defattr(644,root,root,755)
%dir %{_libdir}/evolution/%{mver}/camel*
%dir %{_libdir}/evolution/%{mver}/evolution-calendar-importers
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libevolution-mail-importers.so*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/camel/*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/components/libevolution-mail.so
%attr(755,root,root) %{_libdir}/evolution/%{mver}/camel-providers/*.so
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-calendar-importers/*.so
%{_libdir}/bonobo/servers/GNOME_Evolution_Mail_1.5.server
%{_libdir}/bonobo/servers/GNOME_Evolution_Mail_Importers_1.5.server
%{_libdir}/evolution/%{mver}/camel-providers/*.urls
%{_datadir}/evolution/%{mver}/views/mail*
%{_datadir}/evolution/%{mver}/default/C/mail
%{_datadir}/idl/evolution-%{mver}/Composer.idl
%{_datadir}/idl/evolution-%{mver}/Evolution-Composer.idl
%{_sysconfdir}/gconf/schemas/evolution-mail-1.5.schemas

%files addressbook
%defattr(644,root,root,755)
%dir %{_libdir}/evolution/%{mver}/evolution-addressbook-importers
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-addressbook-clean
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-addressbook-export
%attr(755,root,root) %{_libdir}/evolution/%{mver}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{mver}/components/libevolution-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libevolution-addressbook-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{mver}/evolution-addressbook-importers/lib*.so
%{_libdir}/bonobo/servers/GNOME_Evolution_Addressbook*
%{_datadir}/evolution/%{mver}/views/addressbook*
%{_datadir}/evolution/%{mver}/ecps
%{_datadir}/idl/evolution-%{mver}/Evolution-Addressbook-SelectNames.idl
%{_sysconfdir}/gconf/schemas/apps_evolution_addressbook-1.5.schemas

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{mver}/components/libevolution-calendar.so
%attr(755,root,root) %{_libdir}/evolution/%{mver}/libevolution-calendar-a11y.so.*
%{_libdir}/bonobo/servers/GNOME_Evolution_Calendar*
%{_datadir}/evolution/%{mver}/views/calendar*
%{_datadir}/evolution/%{mver}/views/tasks*
%{_datadir}/idl/evolution-%{mver}/evolution-calendar.idl
%{_sysconfdir}/gconf/schemas/apps_evolution_calendar-1.5.schemas

%files pilot
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{mver}/conduits/*
%{_datadir}/gnome-pilot/conduits/*
