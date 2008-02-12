#
# Conditional build:
%bcond_without	ldap		# build without ldap support
%bcond_without	kerberos5	# build without kerberos5 support
%bcond_without	pilot		# build without pilot support
#
%define		basever	2.22
#
Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl.UTF-8):	Klient poczty dla GNOME/Kalendarz/Książka Adresowa
Summary(pt_BR.UTF-8):	Cliente de email integrado com calendário e catálogo de endereços
Summary(zh_CN.UTF-8):	Evolution - GNOME个人和工作组信息管理工具(包括电子邮件，日历和地址薄)
Name:		evolution
Version:	2.21.91
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	52a892cb2d0566c579350adad46a2222
Source1:	%{name}-gg16.png
Source2:	%{name}-gg48.png
Source3:	%{name}-addressbook.desktop
Source4:	%{name}-calendar.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-tasks.desktop
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-gnome-icon-theme.patch
Patch2:		%{name}-groupwise-features-link.patch
Patch3:		%{name}-composer_includes.patch
Patch4:		%{name}-as_needed-fix.patch
URL:		http://www.gnome.org/projects/evolution/
BuildRequires:	GConf2-devel >= 2.21.90
BuildRequires:	NetworkManager-devel
BuildRequires:	ORBit2-devel >= 1:2.14.8
BuildRequires:	atk-devel >= 1:1.21.5
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	evolution-data-server-devel >= 2.21.91
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.15.5
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
%{?with_pilot:BuildRequires:	gnome-pilot-devel >= 2.0.14}
BuildRequires:	gnome-vfs2-devel >= 2.21.90
BuildRequires:	gtk+2-devel >= 2:2.12.5
BuildRequires:	gtkhtml-devel >= 3.17.91
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.37.0
%{?with_kerberos5:BuildRequires:	krb5-devel}
BuildRequires:	libbonoboui-devel >= 2.20.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.21.91
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libsoup-devel >= 2.3.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
%{?with_pilot:BuildRequires:	pilot-link-devel >= 0.11.8}
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	sed >= 4.0
BuildRequires:	which
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-component = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2 >= 2.21.90
Requires:	bonobo-activation
Requires:	evolution-data-server >= 2.21.91
Requires:	gtkhtml >= 3.17.91
Requires:	psmisc
Obsoletes:	evolution2
Obsoletes:	gnome-pim
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		evo_plugins_dir		%{_libdir}/evolution/%{basever}/plugins

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will be tightly
integrated with one another and act as a seamless personal
information-management tool.

%description -l pl.UTF-8
Evolution to program pocztowy GNOME, kalendarz, książka adresowa i
narzędzie komunikacyjne.

%description -l pt_BR.UTF-8
Evolution é um cliente de email para o GNOME com calendário e outras
ferramentas interessantes.

%package libs
Summary:	Evolution libraries
Summary(pl.UTF-8):	Biblioteki Evolution
Group:		X11/Libraries
Requires:	glib2 >= 1:2.15.5

%description libs
This package contains Evolution libraries.

%description libs -l pl.UTF-8
Pakiet zawiera biblioteki Evolution.

%package devel
Summary:	Header files for evolution
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento
Summary(zh_CN.UTF-8):	Evolution组件开发库
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2-devel >= 2.21.90
Requires:	ORBit2-devel >= 1:2.14.8
Requires:	cyrus-sasl-devel
Requires:	evolution-data-server-devel >= 2.21.91
Requires:	glib2-devel >= 1:2.15.5
Requires:	gtk+2-devel >= 2:2.12.5
Requires:	gtkhtml-devel >= 3.17.91
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libgnomeui-devel >= 2.21.91
Requires:	libxml2-devel >= 1:2.6.31
%{?with_ldap:Requires:	openldap-devel >= 2.4.6}
%{?with_pilot:Requires:	pilot-link-devel >= 0.11.8}
Obsoletes:	evolution2-devel

%description devel
This package contains the files necessary to develop applications
using Evolution's libraries.

%description devel -l pl.UTF-8
Pakiet zawiera pliki potrzebne do rozwoju aplikacji używających
bibliotek programu Evolution.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos necessários para desenvolvimento de
aplicações utilizando as bibliotecas do Evolution.

%package static
Summary:	Static libraries for evolution
Summary(pl.UTF-8):	Biblioteki statyczne dla evolution
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	evolution2-static

%description static
This package contains static libraries for Evolution.

%description static -l pl.UTF-8
Pakiet zawiera statyczne biblioteki Evolution.

%description static -l pt_BR.UTF-8
Este pacote contém as bibliotecas estáticas para desenvolvimento de
aplicações.

%package mail
Summary:	Evolution mail component
Summary(pl.UTF-8):	Moduł pocztowy Evolution
Group:		X11/Applications/Mail
Requires(post,preun):	GConf2
# mail composer requires addressbook component
Requires:	%{name}-addressbook = %{version}-%{release}
Provides:	%{name}-component = %{version}-%{release}

%description mail
Evolution mail.

%description mail -l pl.UTF-8
Moduł pocztowy Evolution.

%package addressbook
Summary:	Evolution addressbook component
Summary(pl.UTF-8):	Moduł książki adresowej Evolution
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-component = %{version}-%{release}

%description addressbook
Evolution addressbook.

%description addressbook -l pl.UTF-8
Książka adresowa Evolution.

%package calendar
Summary:	Evolution calendar and todo component
Summary(pl.UTF-8):	Moduł kalendarza i listy zadań Evolution
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-component = %{version}-%{release}

%description calendar
Evolution calendar and todo component.

%description calendar -l pl.UTF-8
Kalendarz i lista zadań Evolution.

%package pilot
Summary:	Evolution conduits for gnome-pilot
Summary(pl.UTF-8):	Dodatki do wymiany danych z gnome-pilot
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-pilot
Obsoletes:	evolution2-pilot

%description pilot
This package contains conduits needed by gnome-pilot to synchronize
your Palm with Evolution.

%description pilot -l pl.UTF-8
Ten pakiet zawiera dodatki do synchronizacji danych Evolution z
Palmem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv po/sr@{Latn,latin}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper \
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
	--with-kde-applnk-path=no \
	--disable-schemas-install \
	--enable-plugins=all \
	--enable-nss=yes \
	--enable-smime=yes \
	--enable-static \
	--with-sub-version=" PLD Linux" \
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
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GTKHTML_DATADIR=%{_datadir}/idl \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

install %{SOURCE1} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/im-gadugadu.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/im-gadugadu.png
install %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}

# remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/*/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/*/*.{a,la}
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -r $RPM_BUILD_ROOT%{_desktopdir}/evolution.desktop

# test plugins
rm -f $RPM_BUILD_ROOT%{evo_plugins_dir}/*org-gnome-prefer-plain.{so,eplug}

%find_lang %{name} --all-name --with-omf --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_evolution_shell.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_evolution_shell.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post mail
%gconf_schema_install apps-evolution-attachment-reminder.schemas
%gconf_schema_install apps-evolution-mail-prompts-checkdefault.schemas
%gconf_schema_install apps-evolution-mail-notification.schemas
%gconf_schema_install bogo-junk-plugin.schemas
%gconf_schema_install evolution-mail.schemas

%preun mail
%gconf_schema_uninstall apps-evolution-attachment-reminder.schemas
%gconf_schema_uninstall apps-evolution-mail-prompts-checkdefault.schemas
%gconf_schema_uninstall apps-evolution-mail-notification.schemas
%gconf_schema_uninstall bogo-junk-plugin.schemas
%gconf_schema_uninstall evolution-mail.schemas

%post addressbook
%update_desktop_database_post
%gconf_schema_install apps_evolution_addressbook.schemas

%preun addressbook
%gconf_schema_uninstall apps_evolution_addressbook.schemas

%postun addressbook
%update_desktop_database_postun

%post calendar
%gconf_schema_install apps_evolution_calendar.schemas

%preun calendar
%gconf_schema_uninstall apps_evolution_calendar.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%attr(755,root,root) %{_bindir}/evolution
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{basever}/killev

%{_libdir}/bonobo/servers/GNOME_Evolution_Shell.server
%{_sysconfdir}/gconf/schemas/apps_evolution_shell.schemas

%{_datadir}/evolution/%{basever}/glade/e-active-connection-dialog.glade
%{_datadir}/evolution/%{basever}/glade/e-attachment.glade
%{_datadir}/evolution/%{basever}/glade/e-send-options.glade
%{_datadir}/evolution/%{basever}/glade/e-table-config.glade
%{_datadir}/evolution/%{basever}/glade/e-table-field-chooser.glade
%{_datadir}/evolution/%{basever}/glade/e-timezone-dialog.glade
%{_datadir}/evolution/%{basever}/glade/filter.glade
%{_datadir}/evolution/%{basever}/glade/gal-categories.glade
%{_datadir}/evolution/%{basever}/glade/gal-define-views.glade
%{_datadir}/evolution/%{basever}/glade/gal-view-instance-save-as-dialog.glade
%{_datadir}/evolution/%{basever}/glade/gal-view-new-dialog.glade
%{_datadir}/evolution/%{basever}/glade/import.glade
%{_datadir}/evolution/%{basever}/glade/smime-ui.glade

%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/%{basever}
%dir %{_datadir}/evolution/%{basever}/default
%dir %{_datadir}/evolution/%{basever}/default/C
%dir %{_datadir}/evolution/%{basever}/etspec
%dir %{_datadir}/evolution/%{basever}/views

%lang(de) %dir %{_datadir}/evolution/%{basever}/default/de
%lang(es) %dir %{_datadir}/evolution/%{basever}/default/es
%lang(fi) %dir %{_datadir}/evolution/%{basever}/default/fi
%lang(fr) %dir %{_datadir}/evolution/%{basever}/default/fr
%lang(ja) %dir %{_datadir}/evolution/%{basever}/default/ja
%lang(lt) %dir %{_datadir}/evolution/%{basever}/default/lt
%lang(mk) %dir %{_datadir}/evolution/%{basever}/default/mk
%lang(nl) %dir %{_datadir}/evolution/%{basever}/default/nl
%lang(pl) %dir %{_datadir}/evolution/%{basever}/default/pl
%lang(pt) %dir %{_datadir}/evolution/%{basever}/default/pt
%lang(sv) %dir %{_datadir}/evolution/%{basever}/default/sv
%lang(zh_CN) %dir %{_datadir}/evolution/%{basever}/default/zh_CN

%dir %{_datadir}/evolution/%{basever}/errors
%{_datadir}/evolution/%{basever}/errors/e-system.error
%{_datadir}/evolution/%{basever}/errors/filter.error
%{_datadir}/evolution/%{basever}/errors/mail-composer.error
%{_datadir}/evolution/%{basever}/errors/shell.error

%dir %{_datadir}/evolution/%{basever}/glade
%dir %{_datadir}/evolution/%{basever}/help
%dir %{_datadir}/evolution/%{basever}/help/quickref
%dir %{_datadir}/evolution/%{basever}/help/quickref/C

%{_datadir}/evolution/%{basever}/help/quickref/C/quickref.pdf
%lang(de) %dir %{_datadir}/evolution/%{basever}/help/quickref/de
%lang(de) %{_datadir}/evolution/%{basever}/help/quickref/de/quickref.pdf
%lang(es) %dir %{_datadir}/evolution/%{basever}/help/quickref/es
%lang(es) %{_datadir}/evolution/%{basever}/help/quickref/es/quickref.pdf
%lang(fr) %dir %{_datadir}/evolution/%{basever}/help/quickref/fr
%lang(fr) %{_datadir}/evolution/%{basever}/help/quickref/fr/quickref.pdf
%lang(hu) %dir %{_datadir}/evolution/%{basever}/help/quickref/hu
%lang(hu) %{_datadir}/evolution/%{basever}/help/quickref/hu/quickref.pdf
%lang(it) %dir %{_datadir}/evolution/%{basever}/help/quickref/it
%lang(it) %{_datadir}/evolution/%{basever}/help/quickref/it/quickref.pdf
%lang(pt) %dir %{_datadir}/evolution/%{basever}/help/quickref/pt
%lang(pt) %{_datadir}/evolution/%{basever}/help/quickref/pt/quickref.pdf
%lang(sq) %dir %{_datadir}/evolution/%{basever}/help/quickref/sq
%lang(sq) %{_datadir}/evolution/%{basever}/help/quickref/sq/quickref.pdf
%lang(sv) %dir %{_datadir}/evolution/%{basever}/help/quickref/sv
%lang(sv) %{_datadir}/evolution/%{basever}/help/quickref/sv/quickref.pdf

%{_datadir}/evolution/%{basever}/icons
%{_datadir}/evolution/%{basever}/images
%{_datadir}/evolution/%{basever}/sounds
%{_datadir}/evolution/%{basever}/ui

%dir %{_datadir}/idl/evolution-%{basever}
%{_datadir}/idl/evolution-%{basever}/Evolution-Component.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-ConfigControl.idl
%{_datadir}/idl/evolution-%{basever}/Evolution.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-Shell.idl

%{_iconsdir}/hicolor/*/apps/*

# PLUGINS
# backup-restore
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-backup
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-backup-restore.so
%{evo_plugins_dir}/org-gnome-backup-restore.eplug
%{evo_plugins_dir}/org-gnome-backup-restore.xml
%{_datadir}/evolution/%{basever}/errors/org-gnome-backup-restore.error

# default-source
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-default-source.so
%{evo_plugins_dir}/org-gnome-default-source.eplug

# plugin-manager
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-plugin-manager.so
%{evo_plugins_dir}/org-gnome-plugin-manager.eplug
%{evo_plugins_dir}/org-gnome-plugin-manager.xml

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/%{basever}
%dir %{_libdir}/evolution/%{basever}/components
%dir %{evo_plugins_dir}
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeabutil.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeconduit.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontacteditor.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontactlisteditor.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libefilterbar.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libemiscwidgets.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeshell.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libessmime.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetable.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetext.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetimezonedialog.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeutil.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-addressbook-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar-importers.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-importers.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-smime.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-widgets-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libfilter.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libmenus.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeabutil.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeconduit.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontacteditor.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontactlisteditor.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libefilterbar.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libemiscwidgets.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeshell.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libessmime.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetable.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetext.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetimezonedialog.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeutil.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-a11y.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-addressbook-a11y.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar-a11y.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-smime.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-widgets-a11y.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libfilter.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libmenus.so
%{_libdir}/evolution/%{basever}/libeabutil.la
%{_libdir}/evolution/%{basever}/libeconduit.la
%{_libdir}/evolution/%{basever}/libecontacteditor.la
%{_libdir}/evolution/%{basever}/libecontactlisteditor.la
%{_libdir}/evolution/%{basever}/libefilterbar.la
%{_libdir}/evolution/%{basever}/libemiscwidgets.la
%{_libdir}/evolution/%{basever}/libeshell.la
%{_libdir}/evolution/%{basever}/libessmime.la
%{_libdir}/evolution/%{basever}/libetable.la
%{_libdir}/evolution/%{basever}/libetext.la
%{_libdir}/evolution/%{basever}/libetimezonedialog.la
%{_libdir}/evolution/%{basever}/libeutil.la
%{_libdir}/evolution/%{basever}/libevolution-a11y.la
%{_libdir}/evolution/%{basever}/libevolution-addressbook-a11y.la
%{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.la
%{_libdir}/evolution/%{basever}/libevolution-calendar-a11y.la
%{_libdir}/evolution/%{basever}/libevolution-calendar-importers.la
%{_libdir}/evolution/%{basever}/libevolution-mail-importers.la
%{_libdir}/evolution/%{basever}/libevolution-smime.la
%{_libdir}/evolution/%{basever}/libevolution-widgets-a11y.la
%{_libdir}/evolution/%{basever}/libfilter.la
%{_libdir}/evolution/%{basever}/libmenus.la
%{_includedir}/%{name}-%{basever}
%{_pkgconfigdir}/evolution-plugin.pc
%{_pkgconfigdir}/evolution-shell.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/evolution/%{basever}/libeabutil.a
%{_libdir}/evolution/%{basever}/libeconduit.a
%{_libdir}/evolution/%{basever}/libecontacteditor.a
%{_libdir}/evolution/%{basever}/libecontactlisteditor.a
%{_libdir}/evolution/%{basever}/libefilterbar.a
%{_libdir}/evolution/%{basever}/libemiscwidgets.a
%{_libdir}/evolution/%{basever}/libeshell.a
%{_libdir}/evolution/%{basever}/libessmime.a
%{_libdir}/evolution/%{basever}/libetable.a
%{_libdir}/evolution/%{basever}/libetext.a
%{_libdir}/evolution/%{basever}/libetimezonedialog.a
%{_libdir}/evolution/%{basever}/libeutil.a
%{_libdir}/evolution/%{basever}/libevolution-a11y.a
%{_libdir}/evolution/%{basever}/libevolution-addressbook-a11y.a
%{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.a
%{_libdir}/evolution/%{basever}/libevolution-calendar-a11y.a
%{_libdir}/evolution/%{basever}/libevolution-calendar-importers.a
%{_libdir}/evolution/%{basever}/libevolution-mail-importers.a
%{_libdir}/evolution/%{basever}/libevolution-smime.a
%{_libdir}/evolution/%{basever}/libevolution-widgets-a11y.a
%{_libdir}/evolution/%{basever}/libfilter.a
%{_libdir}/evolution/%{basever}/libmenus.a

%files mail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/components/libevolution-mail.so
%{_datadir}/evolution/%{basever}/etspec/message-list.etspec
%{_datadir}/evolution/%{basever}/errors/mail.error
%{_datadir}/evolution/%{basever}/glade/mail-config.glade
%{_datadir}/evolution/%{basever}/glade/mail-dialogs.glade
%{_datadir}/evolution/%{basever}/filtertypes.xml
%{_datadir}/evolution/%{basever}/vfoldertypes.xml
%{_datadir}/evolution/%{basever}/searchtypes.xml
%{_datadir}/evolution/%{basever}/default/C/mail
%{_datadir}/evolution/%{basever}/views/mail

%lang(de) %{_datadir}/evolution/%{basever}/default/de/mail
%lang(es) %{_datadir}/evolution/%{basever}/default/es/mail
%lang(fi) %{_datadir}/evolution/%{basever}/default/fi/mail
%lang(fr) %{_datadir}/evolution/%{basever}/default/fr/mail
%lang(ja) %{_datadir}/evolution/%{basever}/default/ja/mail
%lang(lt) %{_datadir}/evolution/%{basever}/default/lt/mail
%lang(mk) %{_datadir}/evolution/%{basever}/default/mk/mail
%lang(nl) %{_datadir}/evolution/%{basever}/default/nl/mail
%lang(pl) %{_datadir}/evolution/%{basever}/default/pl/mail
%lang(pt) %{_datadir}/evolution/%{basever}/default/pt/mail
%lang(sv) %{_datadir}/evolution/%{basever}/default/sv/mail
%lang(zh_CN) %{_datadir}/evolution/%{basever}/default/zh_CN/mail

%{_datadir}/idl/evolution-%{basever}/Composer.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-Composer.idl
%{_datadir}/idl/evolution-%{basever}/Evolution-Mail.idl
%{_libdir}/bonobo/servers/GNOME_Evolution_Mail.server

%{_desktopdir}/%{name}-mail.desktop
%{_sysconfdir}/gconf/schemas/evolution-mail.schemas

# PLUGINS
# attachment-reminder
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-attachment-reminder.so
%{_sysconfdir}/gconf/schemas/apps-evolution-attachment-reminder.schemas
%{evo_plugins_dir}/attachment-reminder.glade
%{evo_plugins_dir}/org-gnome-evolution-attachment-reminder.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-attachment-reminder.error

# audio-inline
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-audio-inline.so
%{evo_plugins_dir}/org-gnome-audio-inline.eplug

# bbdb
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-bbdb.so
%{evo_plugins_dir}/org-gnome-evolution-bbdb.eplug

# bogo-junk-plugin
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-bogo-junk-plugin.so
%{evo_plugins_dir}/org-gnome-bogo-junk-plugin.eplug
%{_sysconfdir}/gconf/schemas/bogo-junk-plugin.schemas

# copy-tool
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-copy-tool.so
%{evo_plugins_dir}/org-gnome-copy-tool.eplug

# default-mailer
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-default-mailer.so
%{evo_plugins_dir}/org-gnome-default-mailer.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-default-mailer.error
%{_sysconfdir}/gconf/schemas/apps-evolution-mail-prompts-checkdefault.schemas

# exchange-operations
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-exchange-operations.so
%{evo_plugins_dir}/org-gnome-exchange-operations.eplug
%{evo_plugins_dir}/org-gnome-exchange-ab-subscription.xml
%{evo_plugins_dir}/org-gnome-exchange-cal-subscription.xml
%{evo_plugins_dir}/org-gnome-exchange-tasks-subscription.xml
%{evo_plugins_dir}/org-gnome-folder-permissions.xml
%{evo_plugins_dir}/org-gnome-folder-subscription.xml
%{_datadir}/evolution/%{basever}/errors/org-gnome-exchange-operations.error
%{_datadir}/evolution/%{basever}/glade/e-foreign-folder-dialog.glade
%{_datadir}/evolution/%{basever}/glade/exchange-change-password.glade
%{_datadir}/evolution/%{basever}/glade/exchange-delegates.glade
%{_datadir}/evolution/%{basever}/glade/exchange-folder-tree.glade
%{_datadir}/evolution/%{basever}/glade/exchange-oof.glade
%{_datadir}/evolution/%{basever}/glade/exchange-passwd-expiry.glade
%{_datadir}/evolution/%{basever}/glade/exchange-permissions-dialog.glade
%{_datadir}/evolution/%{basever}/glade/exchange-send-options.glade

# face
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-face.so
%{evo_plugins_dir}/org-gnome-face-ui.xml
%{evo_plugins_dir}/org-gnome-face.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-face.errors.xml

# groupwise-account-setup
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-gw-account-setup.so
%{evo_plugins_dir}/org-gnome-gw-account-setup.eplug

# groupwise-features
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-groupwise-features.so
%{evo_plugins_dir}/org-gnome-groupwise-features.eplug
%{evo_plugins_dir}/org-gnome-compose-send-options.xml
%{_datadir}/evolution/%{basever}/errors/org-gnome-mail-retract-errors.xml
%{_datadir}/evolution/%{basever}/errors/org-gnome-proxy-errors.xml
%{_datadir}/evolution/%{basever}/errors/org-gnome-proxy-login-errors.xml
%{_datadir}/evolution/%{basever}/errors/org-gnome-shared-folder.errors.xml
%{_datadir}/evolution/%{basever}/glade/properties.glade
%{_datadir}/evolution/%{basever}/glade/junk-settings.glade
%{_datadir}/evolution/%{basever}/glade/proxy-add-dialog.glade
%{_datadir}/evolution/%{basever}/glade/proxy-listing.glade
%{_datadir}/evolution/%{basever}/glade/proxy-login-dialog.glade

# imap-features
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-imap-features.so
%{evo_plugins_dir}/org-gnome-imap-features.eplug
%{_datadir}/evolution/%{basever}/glade/imap-headers.glade

# import-ics-attachments
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-mail-attachments-import-ics.so
%{evo_plugins_dir}/org-gnome-evolution-mail-attachments-import-ics.eplug

# itip-formatter
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-itip-formatter.so
%{evo_plugins_dir}/org-gnome-itip-formatter.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-itip-formatter.error

# mail-account-disable
%attr(755,root,root) %{evo_plugins_dir}/libmail-account-disable.so
%{evo_plugins_dir}/org-gnome-mail-account-disable.eplug

# mail-notification
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mail-notification.so
%{evo_plugins_dir}/org-gnome-mail-notification.eplug
%{_sysconfdir}/gconf/schemas/apps-evolution-mail-notification.schemas

# mail-to-task
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mail-to-task.so
%{evo_plugins_dir}/org-gnome-mail-to-task.eplug
%{evo_plugins_dir}/org-gnome-mail-to-task.xml

# mailing-list-actions
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mailing-list-actions.so
%{evo_plugins_dir}/org-gnome-mailing-list-actions.eplug
%{evo_plugins_dir}/org-gnome-mailing-list-actions.xml
%{_datadir}/evolution/%{basever}/errors/org-gnome-mailing-list-actions.error

# mark-all-read
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mark-all-read.so
%{evo_plugins_dir}/org-gnome-mark-all-read.eplug

# print-message
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-print-message.so
%{evo_plugins_dir}/org-gnome-print-message.eplug
%{evo_plugins_dir}/org-gnome-print-message.xml

# sa-junk-plugin
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-sa-junk-plugin.so
%{evo_plugins_dir}/org-gnome-sa-junk-plugin.eplug

# startup-wizard
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-startup-wizard.so
%{evo_plugins_dir}/org-gnome-evolution-startup-wizard.eplug

# subject-thread
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-subject-thread.so
%{evo_plugins_dir}/org-gnome-subject-thread.eplug

%files addressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/components/libevolution-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-clean
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-export
%{_datadir}/evolution/%{basever}/ecps
%{_datadir}/evolution/%{basever}/errors/addressbook.error
%{_datadir}/evolution/%{basever}/etspec/e-addressbook-view.etspec
%{_datadir}/evolution/%{basever}/glade/ldap-config.glade
%{_datadir}/evolution/%{basever}/glade/im.glade
%{_datadir}/evolution/%{basever}/glade/contact-editor.glade
%{_datadir}/evolution/%{basever}/glade/e-contact-print.glade
%{_datadir}/evolution/%{basever}/glade/fulladdr.glade
%{_datadir}/evolution/%{basever}/glade/fullname.glade
%{_datadir}/evolution/%{basever}/glade/contact-list-editor.glade
%{_datadir}/evolution/%{basever}/glade/eab-contact-commit-duplicate-detected.glade
%{_datadir}/evolution/%{basever}/glade/eab-contact-duplicate-detected.glade
%{_datadir}/evolution/%{basever}/views/addressbook
%{_datadir}/evolution/%{basever}/addresstypes.xml
%{_libdir}/bonobo/servers/GNOME_Evolution_Addressbook.server

%{_desktopdir}/%{name}-addressbook.desktop
%{_sysconfdir}/gconf/schemas/apps_evolution_addressbook.schemas

# PLUGINS
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-addressbook-file.so
%{evo_plugins_dir}/org-gnome-addressbook-file.eplug

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/components/libevolution-calendar.so
%{_datadir}/evolution/%{basever}/etspec/e-cal-list-view.etspec
%{_datadir}/evolution/%{basever}/etspec/e-calendar-table.etspec
%{_datadir}/evolution/%{basever}/etspec/e-meeting-time-sel.etspec
%{_datadir}/evolution/%{basever}/etspec/e-memo-table.etspec
%{_datadir}/evolution/%{basever}/errors/calendar.error
%{_datadir}/evolution/%{basever}/glade/alarm-dialog.glade
%{_datadir}/evolution/%{basever}/glade/alarm-list-dialog.glade
%{_datadir}/evolution/%{basever}/glade/alarm-notify.glade
%{_datadir}/evolution/%{basever}/glade/cal-prefs-dialog.glade
%{_datadir}/evolution/%{basever}/glade/e-delegate-dialog.glade
%{_datadir}/evolution/%{basever}/glade/e-itip-control.glade
%{_datadir}/evolution/%{basever}/glade/event-page.glade
%{_datadir}/evolution/%{basever}/glade/goto-dialog.glade
%{_datadir}/evolution/%{basever}/glade/meeting-page.glade
%{_datadir}/evolution/%{basever}/glade/memo-page.glade
%{_datadir}/evolution/%{basever}/glade/recurrence-page.glade
%{_datadir}/evolution/%{basever}/glade/schedule-page.glade
%{_datadir}/evolution/%{basever}/glade/task-details-page.glade
%{_datadir}/evolution/%{basever}/glade/task-page.glade
%{_datadir}/evolution/%{basever}/views/calendar
%{_datadir}/evolution/%{basever}/views/memos
%{_datadir}/evolution/%{basever}/views/tasks
%{_datadir}/evolution/%{basever}/caltypes.xml
%{_datadir}/evolution/%{basever}/memotypes.xml
%{_datadir}/evolution/%{basever}/tasktypes.xml
%{_datadir}/idl/evolution-%{basever}/evolution-calendar.idl
%{_libdir}/bonobo/servers/GNOME_Evolution_Calendar.server
%{_libdir}/bonobo/servers/GNOME_Evolution_Calendar_AlarmNotify.server

%{_desktopdir}/%{name}-calendar.desktop
%{_desktopdir}/%{name}-tasks.desktop
%{_sysconfdir}/gconf/schemas/apps_evolution_calendar.schemas

# PLUGINS
# caldav
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-caldav.so
%{evo_plugins_dir}/org-gnome-evolution-caldav.eplug

# calendar-file
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-calendar-file.so
%{evo_plugins_dir}/org-gnome-calendar-file.eplug

# calendar-http
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-calendar-http.so
%{evo_plugins_dir}/org-gnome-calendar-http.eplug

# calendar-weather
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-calendar-weather.so
%{evo_plugins_dir}/org-gnome-calendar-weather.eplug
%{_datadir}/evolution/%{basever}/weather

# google-account-setup
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-google.so
%{evo_plugins_dir}/org-gnome-evolution-google.eplug

# hula-account-setup
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-hula-account-setup.so
%{evo_plugins_dir}/org-gnome-evolution-hula-account-setup.eplug

# mark-calendar-offline
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mark-calendar-offline.so
%{evo_plugins_dir}/org-gnome-mark-calendar-offline.eplug

# publish-calendar
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-publish-calendar.so
%{evo_plugins_dir}/org-gnome-publish-calendar.eplug
%{evo_plugins_dir}/org-gnome-publish-calendar.xml
%{_datadir}/evolution/%{basever}/glade/publish-calendar.glade

# save-calendar
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-save-calendar.so
%{evo_plugins_dir}/org-gnome-save-calendar.eplug

# select-one-source
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-select-one-source.so
%{evo_plugins_dir}/org-gnome-select-one-source.eplug

%if %{with pilot}
%files pilot
%defattr(644,root,root,755)
%dir %{_libdir}/evolution/%{basever}/conduits
%attr(755,root,root) %{_libdir}/evolution/%{basever}/conduits/libeaddress_conduit.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/conduits/libecalendar_common_conduit.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/conduits/libecalendar_conduit.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/conduits/libememo_conduit.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/conduits/libetodo_conduit.so
%{_datadir}/gnome-pilot/conduits/e-address.conduit
%{_datadir}/gnome-pilot/conduits/e-calendar.conduit
%{_datadir}/gnome-pilot/conduits/e-memo.conduit
%{_datadir}/gnome-pilot/conduits/e-todo.conduit
%endif
