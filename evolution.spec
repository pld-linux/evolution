#
# Conditional build:
%bcond_without	ldap		# build without ldap support
%bcond_without	kerberos5	# build without kerberos5 support
#
%define		basever	3.2
#
Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl.UTF-8):	Klient poczty dla GNOME/Kalendarz/Książka Adresowa
Summary(pt_BR.UTF-8):	Cliente de email integrado com calendário e catálogo de endereços
Summary(zh_CN.UTF-8):	Evolution - GNOME个人和工作组信息管理工具(包括电子邮件，日历和地址薄)
Name:		evolution
Version:	3.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	7c2143fe69343158ca220903b4f4b569
Source1:	%{name}-gg16.png
Source2:	%{name}-gg48.png
Source3:	%{name}-addressbook.desktop
Source4:	%{name}-calendar.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-tasks.desktop
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-gnome-icon-theme.patch
Patch2:		champlain-0.12.patch
URL:		http://www.gnome.org/projects/evolution/
BuildRequires:	GConf2-devel >= 2.28.0
BuildRequires:	NetworkManager-devel >= 0.7
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	cairo-gobject-devel
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.90
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 3.2.0
BuildRequires:	geoclue-devel >= 0.11.1
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.26.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-icon-theme >= 3.2.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.2.0
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+3-devel >= 3.0.2
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gtkhtml-devel >= 4.2.0
#BuildRequires:	gtkimageview-devel >= 2.0
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel >= 0.25
BuildRequires:	libchamplain-devel >= 0.12
BuildRequires:	libgdata-devel >= 0.9
BuildRequires:	libgweather-devel >= 3.0.0
BuildRequires:	libical-devel
BuildRequires:	libnotify-devel >= 0.5.1
BuildRequires:	libpst-devel >= 0.6.41
BuildRequires:	libsoup-gnome-devel >= 2.31.2
BuildRequires:	libtool >= 2.2
BuildRequires:	libxml2-devel >= 1:2.7.3
BuildRequires:	libytnef-devel
BuildRequires:	mono-devel
BuildRequires:	mx-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	shared-mime-info >= 0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-component = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2 >= 2.28.0
Requires:	evolution-data-server >= 3.2.0
Requires:	gnome-icon-theme >= 3.2.0
Requires:	gtkhtml >= 4.2.0
Requires:	libical >= 0.46
Requires:	psmisc
Obsoletes:	evolution-pilot
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
Requires:	glib2 >= 1:2.28.0

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
Requires:	GConf2-devel >= 2.28.0
Requires:	cyrus-sasl-devel
Requires:	evolution-data-server-devel >= 3.2.0
Requires:	glib2-devel >= 1:2.28.0
Requires:	gnome-desktop-devel >= 3.2.0
Requires:	gtk+3-devel >= 3.0.2
Requires:	gtkhtml-devel >= 4.2.0
Requires:	libxml2-devel >= 1:2.7.3
%{?with_ldap:Requires:	openldap-devel >= 2.4.6}
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
Requires(post,postun):	desktop-file-utils
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
Requires(post,postun):	desktop-file-utils
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-component = %{version}-%{release}

%description calendar
Evolution calendar and todo component.

%description calendar -l pl.UTF-8
Kalendarz i lista zadań Evolution.

%package python
Summary:	Python embedding hooks for Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description python
Python embedding hooks for Evolution.

%package mono
Summary:	Mono embedding hooks for Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description mono
Mono embedding hooks for Evolution.

%package apidocs
Summary:	Evolution API documentation
Summary(pl.UTF-8):	Dokumentacja API Evolution
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Evolution API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Evolution.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper \
	--disable-schemas-install \
	--disable-silent-rules \
	--enable-static \
	--enable-canberra \
	--enable-pst-import \
	--disable-image-inline \
	--enable-weather \
	--enable-audio-inline \
	--enable-goa \
	--with-clutter \
	--enable-contact-maps \
	%{__with_without ldap openldap} \
	%{__with_without kerberos5 krb5 %{_prefix}} \
	--without-static-ldap \
	--with-nspr-includes="%{_includedir}/nspr" \
	--with-nss-includes="%{_includedir}/nss" \
	--with-nspr-libs="%{_libdir}" \
	--with-nss-libs="%{_libdir}" \
	--with-kde-applnk-path=no \
	--enable-plugins=all \
	--enable-nss=yes \
	--enable-smime=yes \
	--with-sub-version=" PLD Linux" \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--enable-python \
	--enable-mono

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,48x48}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

install %{SOURCE1} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/im-gadugadu.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/im-gadugadu.png
install %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}

# remove useless files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*/*/*.{a,la}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/mime-info
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/evolution.desktop
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/%{basever}/*.la

%find_lang %{name} --all-name --with-omf --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_evolution_shell.schemas
%gconf_schema_install apps_evolution_eplugin_face.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_evolution_shell.schemas
%gconf_schema_uninstall apps_evolution_eplugin_face.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post mail
%gconf_schema_install apps-evolution-attachment-reminder.schemas
%gconf_schema_install apps-evolution-mail-prompts-checkdefault.schemas
%gconf_schema_install apps-evolution-mail-notification.schemas
%gconf_schema_install apps-evolution-template-placeholders.schemas
%gconf_schema_install apps_evolution_email_custom_header.schemas
%gconf_schema_install evolution-bogofilter.schemas
%gconf_schema_install evolution-spamassassin.schemas
%gconf_schema_install evolution-mail.schemas
%update_desktop_database_post

%preun mail
%gconf_schema_uninstall apps-evolution-attachment-reminder.schemas
%gconf_schema_uninstall apps-evolution-mail-prompts-checkdefault.schemas
%gconf_schema_uninstall apps-evolution-mail-notification.schemas
%gconf_schema_uninstall apps-evolution-template-placeholders.schemas
%gconf_schema_uninstall apps_evolution_email_custom_header.schemas
%gconf_schema_uninstall evolution-bogofilter.schemas
%gconf_schema_uninstall evolution-spamassassin.schemas
%gconf_schema_uninstall evolution-mail.schemas

%postun mail
%update_desktop_database_postun

%post addressbook
%update_desktop_database_post
%gconf_schema_install apps_evolution_addressbook.schemas

%preun addressbook
%gconf_schema_uninstall apps_evolution_addressbook.schemas

%postun addressbook
%update_desktop_database_postun

%post calendar
%gconf_schema_install apps_evolution_calendar.schemas
%update_desktop_database_post

%preun calendar
%gconf_schema_uninstall apps_evolution_calendar.schemas

%postun calendar
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%attr(755,root,root) %{_bindir}/evolution
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{basever}/killev
%dir %{_libdir}/evolution/%{basever}/modules
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-composer-autosave.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-network-manager.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-plugin-lib.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-offline-alert.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-plugin-manager.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-online-accounts.so


%{_sysconfdir}/gconf/schemas/apps_evolution_shell.schemas

%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/%{basever}
%dir %{_datadir}/evolution/%{basever}/default
%dir %{_datadir}/evolution/%{basever}/default/C
%dir %{_datadir}/evolution/%{basever}/etspec
%dir %{_datadir}/evolution/%{basever}/views

%lang(ca) %dir %{_datadir}/evolution/%{basever}/default/ca
%lang(cs) %dir %{_datadir}/evolution/%{basever}/default/cs
%lang(de) %dir %{_datadir}/evolution/%{basever}/default/de
%lang(es) %dir %{_datadir}/evolution/%{basever}/default/es
%lang(fi) %dir %{_datadir}/evolution/%{basever}/default/fi
%lang(fr) %dir %{_datadir}/evolution/%{basever}/default/fr
%lang(hu) %dir %{_datadir}/evolution/%{basever}/default/hu
%lang(id) %dir %{_datadir}/evolution/%{basever}/default/id
%lang(it) %dir %{_datadir}/evolution/%{basever}/default/it
%lang(ja) %dir %{_datadir}/evolution/%{basever}/default/ja
%lang(ko) %dir %{_datadir}/evolution/%{basever}/default/ko
%lang(lt) %dir %{_datadir}/evolution/%{basever}/default/lt
%lang(mk) %dir %{_datadir}/evolution/%{basever}/default/mk
%lang(nl) %dir %{_datadir}/evolution/%{basever}/default/nl
%lang(pl) %dir %{_datadir}/evolution/%{basever}/default/pl
%lang(pt) %dir %{_datadir}/evolution/%{basever}/default/pt
%lang(ro) %dir %{_datadir}/evolution/%{basever}/default/ro
%lang(sv) %dir %{_datadir}/evolution/%{basever}/default/sv
%lang(sr) %dir %{_datadir}/evolution/%{basever}/default/sr
%lang(sr@latin) %dir %{_datadir}/evolution/%{basever}/default/sr@latin
%lang(zh_CN) %dir %{_datadir}/evolution/%{basever}/default/zh_CN

%{_datadir}/evolution/%{basever}/address_formats.dat
%{_datadir}/evolution/%{basever}/countrytransl.map

%dir %{_datadir}/evolution/%{basever}/errors
%{_datadir}/evolution/%{basever}/errors/e-system.error
%{_datadir}/evolution/%{basever}/errors/filter.error
%{_datadir}/evolution/%{basever}/errors/mail-composer.error
%{_datadir}/evolution/%{basever}/errors/shell.error
%{_datadir}/evolution/%{basever}/errors/evolution-offline-alert.error

%dir %{_datadir}/evolution/%{basever}/help
%dir %{_datadir}/evolution/%{basever}/help/quickref
%dir %{_datadir}/evolution/%{basever}/help/quickref/C

%{_datadir}/evolution/%{basever}/help/quickref/C/quickref.pdf
%lang(ca) %dir %{_datadir}/evolution/%{basever}/help/quickref/ca
%lang(ca) %{_datadir}/evolution/%{basever}/help/quickref/ca/quickref.pdf
%lang(cs) %dir %{_datadir}/evolution/%{basever}/help/quickref/cs
%lang(cs) %{_datadir}/evolution/%{basever}/help/quickref/cs/quickref.pdf
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
%lang(pl) %dir %{_datadir}/evolution/%{basever}/help/quickref/pl
%lang(pl) %{_datadir}/evolution/%{basever}/help/quickref/pl/quickref.pdf
%lang(pt) %dir %{_datadir}/evolution/%{basever}/help/quickref/pt
%lang(pt) %{_datadir}/evolution/%{basever}/help/quickref/pt/quickref.pdf
%lang(sq) %dir %{_datadir}/evolution/%{basever}/help/quickref/sq
%lang(sq) %{_datadir}/evolution/%{basever}/help/quickref/sq/quickref.pdf
%lang(sv) %dir %{_datadir}/evolution/%{basever}/help/quickref/sv
%lang(sv) %{_datadir}/evolution/%{basever}/help/quickref/sv/quickref.pdf

%{_datadir}/evolution/%{basever}/icons
%{_datadir}/evolution/%{basever}/images
%{_datadir}/evolution/%{basever}/sounds
%{_datadir}/evolution/%{basever}/theme
%{_datadir}/evolution/%{basever}/ui

%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/xdg/autostart/evolution-alarm-notify.desktop

# PLUGINS
# backup-restore
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-backup
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-backup-restore.so
%{evo_plugins_dir}/org-gnome-backup-restore.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-backup-restore.error

# default-source
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-default-source.so
%{evo_plugins_dir}/org-gnome-default-source.eplug

# plugin-manager
#%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-plugin-manager.so
#%{evo_plugins_dir}/org-gnome-plugin-manager.eplug

# prefer-plain
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-prefer-plain.so
%{evo_plugins_dir}/org-gnome-prefer-plain.eplug

# face plugin
%{_sysconfdir}/gconf/schemas/apps_evolution_eplugin_face.schemas
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-face.so
%{evo_plugins_dir}/org-gnome-face.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-face.error

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/%{basever}
%dir %{evo_plugins_dir}
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libcomposer.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeabutil.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontacteditor.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontactlisteditor.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libemformat.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libemiscwidgets.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeshell.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libessmime.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetable.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetext.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetimezonedialog.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeutil.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-a11y.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar-importers.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-importers.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-settings.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-smime.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libfilter.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libgnomecanvas.so.*
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libmenus.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libcomposer.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeabutil.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontacteditor.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontactlisteditor.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libemformat.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libemiscwidgets.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeshell.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libessmime.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetable.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetext.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libetimezonedialog.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeutil.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-a11y.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-settings.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-smime.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libfilter.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libgnomecanvas.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libmenus.so
%{_includedir}/%{name}-%{basever}
%{_pkgconfigdir}/evolution-calendar-3.0.pc
%{_pkgconfigdir}/evolution-mail-3.0.pc
%{_pkgconfigdir}/evolution-plugin-3.0.pc
%{_pkgconfigdir}/evolution-shell-3.0.pc

%files static
%defattr(644,root,root,755)
#%{_libdir}/evolution/%{basever}/libart_lgpl.a
%{_libdir}/evolution/%{basever}/libcomposer.a
%{_libdir}/evolution/%{basever}/libeabutil.a
%{_libdir}/evolution/%{basever}/libecontacteditor.a
%{_libdir}/evolution/%{basever}/libecontactlisteditor.a
%{_libdir}/evolution/%{basever}/libemformat.a
%{_libdir}/evolution/%{basever}/libemiscwidgets.a
%{_libdir}/evolution/%{basever}/libeshell.a
%{_libdir}/evolution/%{basever}/libessmime.a
%{_libdir}/evolution/%{basever}/libetable.a
%{_libdir}/evolution/%{basever}/libetext.a
%{_libdir}/evolution/%{basever}/libetimezonedialog.a
%{_libdir}/evolution/%{basever}/libeutil.a
%{_libdir}/evolution/%{basever}/libevolution-a11y.a
%{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.a
%{_libdir}/evolution/%{basever}/libevolution-calendar.a
%{_libdir}/evolution/%{basever}/libevolution-calendar-importers.a
%{_libdir}/evolution/%{basever}/libevolution-mail-importers.a
%{_libdir}/evolution/%{basever}/libevolution-mail.a
%{_libdir}/evolution/%{basever}/libevolution-mail-settings.a
%{_libdir}/evolution/%{basever}/libevolution-smime.a
%{_libdir}/evolution/%{basever}/libfilter.a
%{_libdir}/evolution/%{basever}/libgnomecanvas.a
%{_libdir}/evolution/%{basever}/libmenus.a

%files mail
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/evolution-settings
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-mail.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-mailto-handler.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-startup-wizard.so
%{_datadir}/evolution/%{basever}/mail-autoconfig
%{_datadir}/evolution/%{basever}/etspec/message-list.etspec
%{_datadir}/evolution/%{basever}/errors/mail.error
%{_datadir}/evolution/%{basever}/filtertypes.xml
%{_datadir}/evolution/%{basever}/vfoldertypes.xml
%{_datadir}/evolution/%{basever}/searchtypes.xml
%{_datadir}/evolution/%{basever}/default/C/mail
%{_datadir}/evolution/%{basever}/views/mail

%lang(ca) %{_datadir}/evolution/%{basever}/default/ca/mail
%lang(cs) %{_datadir}/evolution/%{basever}/default/cs/mail
%lang(de) %{_datadir}/evolution/%{basever}/default/de/mail
%lang(es) %{_datadir}/evolution/%{basever}/default/es/mail
%lang(fi) %{_datadir}/evolution/%{basever}/default/fi/mail
%lang(fr) %{_datadir}/evolution/%{basever}/default/fr/mail
%lang(hu) %{_datadir}/evolution/%{basever}/default/hu/mail
%lang(id) %{_datadir}/evolution/%{basever}/default/id/mail
%lang(it) %{_datadir}/evolution/%{basever}/default/it/mail
%lang(ja) %{_datadir}/evolution/%{basever}/default/ja/mail
%lang(ko) %{_datadir}/evolution/%{basever}/default/ko/mail
%lang(lt) %{_datadir}/evolution/%{basever}/default/lt/mail
%lang(mk) %{_datadir}/evolution/%{basever}/default/mk/mail
%lang(nl) %{_datadir}/evolution/%{basever}/default/nl/mail
%lang(pl) %{_datadir}/evolution/%{basever}/default/pl/mail
%lang(pt) %{_datadir}/evolution/%{basever}/default/pt/mail
%lang(ro) %{_datadir}/evolution/%{basever}/default/ro/mail
%lang(sr) %{_datadir}/evolution/%{basever}/default/sr/mail
%lang(sr@latin) %{_datadir}/evolution/%{basever}/default/sr@latin/mail
%lang(sv) %{_datadir}/evolution/%{basever}/default/sv/mail
%lang(zh_CN) %{_datadir}/evolution/%{basever}/default/zh_CN/mail

%{_desktopdir}/evolution-mail.desktop
%{_desktopdir}/evolution-settings.desktop
%{_sysconfdir}/gconf/schemas/evolution-mail.schemas
%{_sysconfdir}/gconf/schemas/apps-evolution-mail-prompts-checkdefault.schemas

# PLUGINS
# attachment-reminder
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-attachment-reminder.so
%{_sysconfdir}/gconf/schemas/apps-evolution-attachment-reminder.schemas
%{evo_plugins_dir}/org-gnome-evolution-attachment-reminder.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-attachment-reminder.error

# audio-inline
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-audio-inline.so
%{evo_plugins_dir}/org-gnome-audio-inline.eplug

# bbdb
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-bbdb.so
%{evo_plugins_dir}/org-gnome-evolution-bbdb.eplug

# bogo-junk-plugin
#%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-bogo-junk-plugin.so
#%{evo_plugins_dir}/org-gnome-bogo-junk-plugin.eplug
%{_sysconfdir}/gconf/schemas/evolution-bogofilter.schemas
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-bogofilter.so

# dbx-import
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-dbx-import.so
%{evo_plugins_dir}/org-gnome-dbx-import.eplug

# email-custom-header
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-email-custom-header.so
%{evo_plugins_dir}/org-gnome-email-custom-header.eplug
%{_sysconfdir}/gconf/schemas/apps_evolution_email_custom_header.schemas

# image-inline
#%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-image-inline.so
#%{evo_plugins_dir}/org-gnome-image-inline.eplug

# groupwise-features
#%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-groupwise-features.so
#%{evo_plugins_dir}/org-gnome-groupwise-features.eplug
#%{evo_plugins_dir}/org-gnome-compose-send-options.xml
#%{_datadir}/evolution/%{basever}/errors/org-gnome-mail-retract.error
#%{_datadir}/evolution/%{basever}/errors/org-gnome-process-meeting.error
#%{_datadir}/evolution/%{basever}/errors/org-gnome-proxy-login.error
#%{_datadir}/evolution/%{basever}/errors/org-gnome-proxy.error
#%{_datadir}/evolution/%{basever}/errors/org-gnome-shared-folder.error

# imap-features
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-imap-features.so
%{evo_plugins_dir}/org-gnome-imap-features.eplug

# itip-formatter
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-itip-formatter.so
%{evo_plugins_dir}/org-gnome-itip-formatter.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-itip-formatter.error

# mail-notification
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mail-notification.so
%{evo_plugins_dir}/org-gnome-mail-notification.eplug
%{_sysconfdir}/gconf/schemas/apps-evolution-mail-notification.schemas

# mail-to-task
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mail-to-task.so
%{evo_plugins_dir}/org-gnome-mail-to-task.eplug

# mailing-list-actions
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mailing-list-actions.so
%{evo_plugins_dir}/org-gnome-mailing-list-actions.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-mailing-list-actions.error

# mark-all-read
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mark-all-read.so
%{evo_plugins_dir}/org-gnome-mark-all-read.eplug

# pst-import
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-pst-import.so
%{evo_plugins_dir}/org-gnome-pst-import.eplug

# sa-junk-plugin
#%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-sa-junk-plugin.so
#%{evo_plugins_dir}/org-gnome-sa-junk-plugin.eplug
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-spamassassin.so
%{_sysconfdir}/gconf/schemas/evolution-spamassassin.schemas

# subject-thread
#%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-subject-thread.so
#%{evo_plugins_dir}/org-gnome-subject-thread.eplug

# templates
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-templates.so
%{evo_plugins_dir}/org-gnome-templates.eplug
%{_sysconfdir}/gconf/schemas/apps-evolution-template-placeholders.schemas

# vcard-inline
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-vcard-inline.so
%{evo_plugins_dir}/org-gnome-vcard-inline.eplug

%files addressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-clean
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-export
%{_datadir}/evolution/%{basever}/ecps
%{_datadir}/evolution/%{basever}/errors/addressbook.error
%{_datadir}/evolution/%{basever}/etspec/e-addressbook-view.etspec
%{_datadir}/evolution/%{basever}/views/addressbook
%{_datadir}/evolution/%{basever}/addresstypes.xml

%{_desktopdir}/%{name}-addressbook.desktop
%{_sysconfdir}/gconf/schemas/apps_evolution_addressbook.schemas

# PLUGINS
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-addressbook-file.so
%{evo_plugins_dir}/org-gnome-addressbook-file.eplug

# webdav-accounts-setup
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-webdav.so
%{evo_plugins_dir}/org-gnome-evolution-webdav.eplug

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-calendar.so
%{_datadir}/evolution/%{basever}/etspec/e-cal-list-view.etspec
%{_datadir}/evolution/%{basever}/etspec/e-calendar-table.etspec
%{_datadir}/evolution/%{basever}/etspec/e-meeting-time-sel.etspec
%{_datadir}/evolution/%{basever}/etspec/e-memo-table.etspec
%{_datadir}/evolution/%{basever}/errors/calendar.error
%{_datadir}/evolution/%{basever}/views/calendar
%{_datadir}/evolution/%{basever}/views/memos
%{_datadir}/evolution/%{basever}/views/tasks
%{_datadir}/evolution/%{basever}/caltypes.xml
%{_datadir}/evolution/%{basever}/memotypes.xml
%{_datadir}/evolution/%{basever}/tasktypes.xml

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

# google-account-setup
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-google.so
%{evo_plugins_dir}/org-gnome-evolution-google.eplug

# publish-calendar
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-publish-calendar.so
%{evo_plugins_dir}/org-gnome-publish-calendar.eplug

# save-calendar
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-save-calendar.so
%{evo_plugins_dir}/org-gnome-save-calendar.eplug

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-plugin-python.so

%files mono
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-plugin-mono.so

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/eshell
