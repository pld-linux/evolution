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
Summary:	The GNOME2 Email/Calendar/Addressbook Suite
Summary(pl):	Klient poczty dla GNOME2/Kalendarz/Ksi±¿ka Adresowa
Summary(pt_BR):	Cliente de email integrado com calendário e catálogo de endereços
Summary(zh_CN):	Evolution - GNOME2¸öÈËºÍ¹¤×÷×éÐÅÏ¢¹ÜÀí¹¤¾ß(°üÀ¨µç×ÓÓÊ¼þ£¬ÈÕÀúºÍµØÖ·±¡)
Name:		evolution
Version:	2.3.7
Release:	2
License:	GPL v2
Group:		Applications/Mail
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	12d29f28f8ecf302547c63ad137e0b4b
Source1:	%{name}-gg16.png
Source2:	%{name}-gg48.png
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-gnome-icon-theme.patch
Patch2:		%{name}-GG-IM.patch
Patch3:		%{name}-desktop.patch
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel >= 1.3.7-2
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.5
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
%{?with_pilot:BuildRequires:	gnome-pilot-devel >= 2.0.13}
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	gtkhtml-devel >= 3.7.6
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libsoup-devel >= 2.2.5
BuildRequires:	libtool
BuildRequires:	libxml2
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.0.0}
%{?with_pilot:BuildRequires:	pilot-link-devel >= 0.11.8}
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	which
Requires(post,postun):	/sbin/ldconfig
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name}-component = %{version}-%{release}
Requires:	GConf2 >= 2.10.0
Requires:	bonobo-activation
Requires:	evolution-data-server >= 1.3.7-2
Requires:	gtkhtml >= 3.7.6
Requires:	hicolor-icon-theme
Requires:	libglade2 >= 1:2.5.1
Requires:	psmisc
Requires:	scrollkeeper >= 0.1.4
Obsoletes:	evolution2
Obsoletes:	gnome-pim
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
Requires:	%{name} = %{version}-%{release}
Requires:	cyrus-sasl-devel
Requires:	freetype-devel
Requires:	gnome-vfs2-devel >= 2.10.0-2
Requires:	gtkhtml-devel >= 3.6.2
Requires:	libglade2-devel >= 1:2.5.1
Requires:	libgnomeprintui-devel >= 2.10.2
Requires:	libgnomeui-devel >= 2.10.0-2
Requires:	libsoup-devel >= 2.2.5
Requires:	nspr-devel
Requires:	nss-devel
%{?with_ldap:Requires:	openldap-devel >= 2.0.0}
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
Requires(post):	/sbin/ldconfig
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
Requires(post):	/sbin/ldconfig
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
Requires(post):	/sbin/ldconfig
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

# strip doesn't pass these files and they aren't necessary, so remove them
# probably this should be done differently, but I have no idea
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/*/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/libemiscwidgets.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/*/*.{a,la}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -r $RPM_BUILD_ROOT%{_datadir}/mime-info

ln -sf evolution-2.4 $RPM_BUILD_ROOT%{_bindir}/evolution

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install apps_evolution_shell-2.4.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall apps_evolution_shell-2.4.schemas

%postun
/sbin/ldconfig
%scrollkeeper_update_postun

%post mail
/sbin/ldconfig
%gconf_schema_install apps-evolution-mail-prompts-checkdefault-2.4.schemas
%gconf_schema_install evolution-mail-2.4.schemas

%preun mail
%gconf_schema_uninstall apps-evolution-mail-prompts-checkdefault-2.4.schemas
%gconf_schema_uninstall evolution-mail-2.4.schemas

%postun mail -p /sbin/ldconfig

%post addressbook
/sbin/ldconfig
%gconf_schema_install apps_evolution_addressbook-2.4.schemas

%preun addressbook
%gconf_schema_uninstall apps_evolution_addressbook-2.4.schemas

%postun addressbook -p /sbin/ldconfig

%post calendar
/sbin/ldconfig
%gconf_schema_install apps_evolution_calendar-2.4.schemas

%preun calendar
%gconf_schema_uninstall apps_evolution_calendar-2.4.schemas

%postun calendar -p /sbin/ldconfig

%files -f evolution.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/evolution/*/libeabutil.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libeconduit.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libecontacteditor.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libecontactlisteditor.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libefilterbar.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libemiscwidgets.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libeshell.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libessmime.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libetable.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libetext.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libetimezonedialog.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libeutil.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-smime.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-widgets-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libfilter.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libmenus.so.*
%attr(755,root,root) %{_libdir}/evolution/*/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/*/killev
%dir %{_libdir}/evolution/*/plugins
%attr(755,root,root) %{_libdir}/evolution/*/plugins/*.so
%{_libdir}/evolution/*/plugins/*.eplug
%{_libdir}/evolution/*/plugins/*.xml
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/*
%dir %{_libdir}/evolution/*/components
%{_libdir}/bonobo/servers/GNOME_Evolution_Shell_*.server
%dir %{_datadir}/idl/evolution-*
%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/*
%dir %{_datadir}/evolution/*/views
%{_datadir}/evolution/*/*.xml
%dir %{_datadir}/evolution/*/default
%dir %{_datadir}/evolution/*/default/C
%lang(de) %dir %{_datadir}/evolution/*/default/de
%lang(ja) %dir %{_datadir}/evolution/*/default/ja
%lang(nl) %dir %{_datadir}/evolution/*/default/nl
%lang(pt) %dir %{_datadir}/evolution/*/default/pt
%lang(zh_CN) %dir %{_datadir}/evolution/*/default/zh_CN
%{_datadir}/evolution/*/errors
%{_datadir}/evolution/*/etspec
%{_datadir}/evolution/*/glade
%{_datadir}/evolution/*/help
%{_datadir}/evolution/*/images
%{_datadir}/evolution/*/ui
%{_datadir}/evolution/*/weather
%{_datadir}/idl/evolution-*/Evolution-Component.idl
%{_datadir}/idl/evolution-*/Evolution-ConfigControl.idl
%{_datadir}/idl/evolution-*/Evolution-Offline.idl
%{_datadir}/idl/evolution-*/Evolution-Shell.idl
%{_datadir}/idl/evolution-*/Evolution.idl
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_sysconfdir}/gconf/schemas/apps_evolution_shell-*.schemas
%{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/*/*.so
%{_libdir}/evolution/*/*.la
%{_libdir}/evolution/*/*/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/evolution/*/*.a

%files mail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-mail-importers.so*
%attr(755,root,root) %{_libdir}/evolution/*/components/libevolution-mail.so
%{_libdir}/bonobo/servers/GNOME_Evolution_Mail_*.server
%{_datadir}/evolution/*/views/mail*
%{_datadir}/evolution/*/default/C/mail
%lang(de) %{_datadir}/evolution/*/default/de/mail
%lang(ja) %{_datadir}/evolution/*/default/ja/mail
%lang(nl) %{_datadir}/evolution/*/default/nl/mail
%lang(pt) %{_datadir}/evolution/*/default/pt/mail
%lang(zh_CN) %{_datadir}/evolution/*/default/zh_CN/mail
%{_datadir}/idl/evolution-*/Composer.idl
%{_datadir}/idl/evolution-*/Evolution-Composer.idl
%{_datadir}/idl/evolution-*/Evolution-Mail.idl
%{_sysconfdir}/gconf/schemas/*-mail-*.schemas

%files addressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/*/evolution-addressbook-clean
%attr(755,root,root) %{_libdir}/evolution/*/evolution-addressbook-export
%attr(755,root,root) %{_libdir}/evolution/*/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/*/components/libevolution-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-addressbook-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-addressbook-importers.so*
%{_libdir}/bonobo/servers/GNOME_Evolution_Addressbook*
%{_datadir}/evolution/*/views/addressbook*
%{_datadir}/evolution/*/ecps
%{_sysconfdir}/gconf/schemas/apps_evolution_addressbook-*.schemas

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/*/components/libevolution-calendar.so
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-calendar-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/*/libevolution-calendar-importers.so*
%{_libdir}/bonobo/servers/GNOME_Evolution_Calendar*
%{_datadir}/evolution/*/views/calendar*
%{_datadir}/evolution/*/views/tasks*
%{_datadir}/idl/evolution-*/evolution-calendar.idl
%{_sysconfdir}/gconf/schemas/apps_evolution_calendar-*.schemas

%if %{with pilot}
%files pilot
%defattr(644,root,root,755)
%dir %{_libdir}/evolution/*/conduits
%attr(755,root,root) %{_libdir}/evolution/*/conduits/*
%{_datadir}/gnome-pilot/conduits/*
%endif
