#
# todo:
# - splitting mail, addressbook and calendar:
#   - etspec?
#   - ui?
#   - dependencies, i.e.: mail should require addressbook?
#
# Conditional build:
%bcond_without	ldap		# build without ldap support
%bcond_without	kerberos5	# build without kerberos5 support
%bcond_without	pilot		# build without pilot support
#
%define		basever	2.6
#
Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME/Kalendarz/Ksi±¿ka Adresowa
Summary(pt_BR):	Cliente de email integrado com calendário e catálogo de endereços
Summary(zh_CN):	Evolution - GNOME¸öÈËºÍ¹¤×÷×éÐÅÏ¢¹ÜÀí¹¤¾ß(°üÀ¨µç×ÓÓÊ¼þ£¬ÈÕÀúºÍµØÖ·±¡)
Name:		evolution
Version:	2.6.0
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	5c98650b2ccf3581e7cf5af3927b95d1
Source1:	%{name}-gg16.png
Source2:	%{name}-gg48.png
Source3:	%{name}-addressbook.desktop
Source4:	%{name}-calendar.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-tasks.desktop
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-gnome-icon-theme.patch
Patch2:		%{name}-GG-IM.patch
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	GConf2-devel >= 2.12.0
BuildRequires:	ORBit2-devel >= 1:2.12.3
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel >= 1.6.0
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.5
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
%{?with_pilot:BuildRequires:	gnome-pilot-devel >= 2.0.13}
BuildRequires:	gnome-vfs2-devel >= 2.12.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	gtkhtml-devel >= 3.8.1
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.12.0
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libsoup-devel >= 2.2.6.1
BuildRequires:	libtool
BuildRequires:	libxml2
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_pilot:BuildRequires:	pilot-link-devel >= 0.11.8}
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	which
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name}-component = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2 >= 2.12.0
Requires:	bonobo-activation
Requires:	evolution-data-server >= 1.6.0
Requires:	gtkhtml >= 3.10.0
Requires:	hicolor-icon-theme
Requires:	libglade2 >= 1:2.5.1
Requires:	psmisc
Requires:	scrollkeeper >= 0.1.4
Obsoletes:	evolution2
Obsoletes:	gnome-pim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package libs
Summary:	Evolution libraries
Summary(pl):	Biblioteki Evolution
Group:		Development/Libraries

%description libs
This package contains Evolution libraries.

%description libs -l pl
Pakiet zawiera biblioteki Evolution.

%package devel
Summary:	Header files for evolution
Summary(pl):	Pliki nag³ówkowe i dokumentacja
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento
Summary(zh_CN):	Evolution×é¼þ¿ª·¢¿â
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cyrus-sasl-devel
Requires:	evolution-data-server-devel >= 1.6.0
Requires:	freetype-devel
Requires:	gnome-vfs2-devel >= 2.12.1
Requires:	gtkhtml-devel >= 3.10.0
Requires:	libglade2-devel >= 1:2.5.1
Requires:	libgnomeprintui-devel >= 2.12.0
Requires:	libgnomeui-devel >= 2.12.0
Requires:	libsoup-devel >= 2.2.6.1
Requires:	nspr-devel
Requires:	nss-devel
%{?with_ldap:Requires:	openldap-devel >= 2.3.0}
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
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	evolution2-static

%description static
This package contains static libraries for Evolution.

%description static -l pl
Pakiet zawiera statyczne biblioteki Evolution.

%description static -l pt_BR
Este pacote contém as bibliotecas estáticas para desenvolvimento de
aplicações.

%package mail
Summary:	Evolution mail component
Summary(pl):	Modu³ pocztowy Evolution
Group:		X11/Applications
# mail composer requires addressbook component
Requires:	%{name}-addressbook = %{version}-%{release}
Requires(post,preun):	GConf2
Provides:	%{name}-component = %{version}-%{release}

%description mail
Evolution mail.

%description mail -l pl
Modu³ pocztowy Evolution.

%package addressbook
Summary:	Evolution addressbook component
Summary(pl):	Modu³ ksi±¿ki adresowej Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,preun):	GConf2
Provides:	%{name}-component = %{version}-%{release}

%description addressbook
Evolution addressbook.

%description addressbook -l pl
Ksi±¿ka adresowa Evolution.

%package calendar
Summary:	Evolution calendar and todo component
Summary(pl):	Modu³ kalendarza i listy zadañ Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,preun):	GConf2
Provides:	%{name}-component = %{version}-%{release}

%description calendar
Evolution calendar and todo component.

%description calendar -l pl
Kalendarz i lista zadañ Evolution.

%package pilot
Summary:	Evolution conduits for gnome-pilot
Summary(pl):	Dodatki do wymiany danych z gnome-pilot
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-pilot
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

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	%{?with_pilot:--enable-pilot-conduits=yes} \
	%{!?with_pilot:--enable-pilot-conduits=no} \
	%{?with_ldap:--with-openldap=yes} \
	%{!?with_ldap:--with-openldap=no} \
	%{?with_kerberos5:--with-krb5=%{_prefix}} \
	%{!?with_kerberos5:--with-krb5=no} \
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
	--enable-plugins=base \
	--enable-nss=yes \
	--enable-smime=yes \
	--enable-static \
	--enable-file-chooser

# hack to rebuild *.c and *.h from *.idl (check if needed with new versions)
# (required if you use ORBit2-devel 2.7.2)
find -name \*.idl -exec touch {} \;

%{__make} \
	GTKHTML_DATADIR=%{_datadir}/idl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,48x48}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	KDE_APPLNK_DIR=%{_applnkdir}/Network/Mail \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GTKHTML_DATADIR=%{_datadir}/idl \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

install %{SOURCE1} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/im-gadugadu.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/im-gadugadu.png
install %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}

# remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/*/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/*/*.{a,la}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -r $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -r $RPM_BUILD_ROOT%{_desktopdir}/evolution.desktop

ln -sf evolution-%{basever} $RPM_BUILD_ROOT%{_bindir}/evolution

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_evolution_shell-%{basever}.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall apps_evolution_shell-%{basever}.schemas

%postun
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post mail
%gconf_schema_install evolution-mail-%{basever}.schemas

%preun mail
%gconf_schema_uninstall evolution-mail-%{basever}.schemas

%post addressbook
%gconf_schema_install apps_evolution_addressbook-%{basever}.schemas

%preun addressbook
%gconf_schema_uninstall apps_evolution_addressbook-%{basever}.schemas

%post calendar
%gconf_schema_install apps_evolution_calendar-%{basever}.schemas

%preun calendar
%gconf_schema_uninstall apps_evolution_calendar-%{basever}.schemas

%files -f evolution.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%attr(755,root,root) %{_bindir}/*

%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{basever}/killev
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/%{basever}
%dir %{_libdir}/evolution/%{basever}/plugins
%dir %{_libdir}/evolution/%{basever}/components
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/*.so
%{_libdir}/bonobo/servers/GNOME_Evolution_Shell_*.server
%{_libdir}/evolution/%{basever}/plugins/*.eplug
%{_libdir}/evolution/%{basever}/plugins/*.xml

%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/%{basever}
%dir %{_datadir}/evolution/%{basever}/default
%dir %{_datadir}/evolution/%{basever}/default/C
%dir %{_datadir}/evolution/%{basever}/views
%dir %{_datadir}/idl/evolution-%{basever}

%{_datadir}/evolution/%{basever}/*.xml
%lang(de) %dir %{_datadir}/evolution/%{basever}/default/de
%lang(ja) %dir %{_datadir}/evolution/%{basever}/default/ja
%lang(nl) %dir %{_datadir}/evolution/%{basever}/default/nl
%lang(pt) %dir %{_datadir}/evolution/%{basever}/default/pt
%lang(zh_CN) %dir %{_datadir}/evolution/%{basever}/default/zh_CN

%{_datadir}/evolution/%{basever}/errors
%{_datadir}/evolution/%{basever}/etspec
%{_datadir}/evolution/%{basever}/glade
%{_datadir}/evolution/%{basever}/help
%{_datadir}/evolution/%{basever}/images
%{_datadir}/evolution/%{basever}/ui
%{_datadir}/evolution/%{basever}/weather

%{_datadir}/idl/evolution-%{basever}/Evolution-Component.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-ConfigControl.idl
%{_datadir}/idl/evolution-%{basever}/Evolution.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-Shell.idl

%{_iconsdir}/hicolor/*/apps/*.png
%{_pixmapsdir}/*.png

%{_omf_dest_dir}/%{name}

%{_sysconfdir}/gconf/schemas/apps_evolution_shell-%{basever}.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/*.so
%{_libdir}/evolution/%{basever}/*.la

%{_includedir}/%{name}-%{basever}
%{_pkgconfigdir}/evolution-*-%{basever}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/evolution/%{basever}/*.a

%files mail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/components/libevolution-mail.so
%{_libdir}/bonobo/servers/GNOME_Evolution_Mail_*.server

%{_datadir}/evolution/%{basever}/default/C/mail
%{_datadir}/evolution/%{basever}/views/mail
%lang(de) %{_datadir}/evolution/%{basever}/default/de/mail
%lang(fi) %{_datadir}/evolution/%{basever}/default/fi/mail
%lang(fr) %{_datadir}/evolution/%{basever}/default/fr/mail
%lang(ja) %{_datadir}/evolution/%{basever}/default/ja/mail
%lang(lt) %{_datadir}/evolution/%{basever}/default/lt/mail
%lang(mk) %{_datadir}/evolution/%{basever}/default/mk/mail
%lang(nl) %{_datadir}/evolution/%{basever}/default/nl/mail
%lang(pt) %{_datadir}/evolution/%{basever}/default/pt/mail
%lang(zh_CN) %{_datadir}/evolution/%{basever}/default/zh_CN/mail
%{_datadir}/idl/evolution-%{basever}/Composer.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-Composer.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-Mail.idl

%{_desktopdir}/%{name}-mail.desktop
%{_sysconfdir}/gconf/schemas/evolution-mail-%{basever}.schemas

%files addressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/components/libevolution-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-clean
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-export
%{_libdir}/bonobo/servers/GNOME_Evolution_Addressbook*

%{_datadir}/evolution/%{basever}/views/addressbook
%{_datadir}/evolution/%{basever}/ecps

%{_desktopdir}/%{name}-addressbook.desktop

%{_sysconfdir}/gconf/schemas/apps_evolution_addressbook-%{basever}.schemas

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/components/libevolution-calendar.so
%{_libdir}/bonobo/servers/GNOME_Evolution_Calendar*
%{_libdir}/evolution/%{basever}/plugins/publish-calendar.glade

%{_datadir}/evolution/%{basever}/views/calendar
%{_datadir}/evolution/%{basever}/views/memos
%{_datadir}/evolution/%{basever}/views/tasks

%{_datadir}/idl/evolution-%{basever}/evolution-calendar.idl

%{_desktopdir}/%{name}-calendar.desktop
%{_desktopdir}/%{name}-tasks.desktop

%{_sysconfdir}/gconf/schemas/apps_evolution_calendar-%{basever}.schemas

%if %{with pilot}
%files pilot
%defattr(644,root,root,755)
%dir %{_libdir}/evolution/%{basever}/conduits
%attr(755,root,root) %{_libdir}/evolution/%{basever}/conduits/*.so
%{_datadir}/gnome-pilot/conduits/*
%endif
