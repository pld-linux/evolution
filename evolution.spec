#
# Conditional build:
%bcond_without	ldap		# build without ldap support

%define		basever	3.12
Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl.UTF-8):	Klient poczty dla GNOME/Kalendarz/Książka Adresowa
Summary(pt_BR.UTF-8):	Cliente de email integrado com calendário e catálogo de endereços
Summary(zh_CN.UTF-8):	Evolution - GNOME个人和工作组信息管理工具(包括电子邮件，日历和地址薄)
Name:		evolution
Version:	3.12.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	2861ecacd698c9dc8ba2bee491fa9569
Source3:	%{name}-addressbook.desktop
Source4:	%{name}-calendar.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-tasks.desktop
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-gnome-icon-theme.patch
URL:		http://wiki.gnome.org/Apps/Evolution/
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	cairo-gobject-devel
BuildRequires:	clutter-gtk-devel >= 0.90
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= %{version}
BuildRequires:	gcr-devel >= 3.4
BuildRequires:	geoclue-devel >= 0.12.0
BuildRequires:	geocode-glib-devel >= 3.10.0
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.34.0
BuildRequires:	gnome-common >= 2.26.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-icon-theme >= 3.2.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.2.0
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+3-devel >= 3.8.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtk-webkit3-devel >= 2.0.1
BuildRequires:	gtkhtml-devel >= 4.5.2
BuildRequires:	gtkspell3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel >= 0.25
BuildRequires:	libchamplain-devel >= 0.12
BuildRequires:	libgdata-devel >= 0.10
BuildRequires:	libgweather-devel >= 3.8.0
BuildRequires:	libical-devel
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libpst-devel >= 0.6.54
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool >= 2.2
BuildRequires:	libxml2-devel >= 1:2.7.3
BuildRequires:	libytnef-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	psmisc
BuildRequires:	python
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	shared-mime-info >= 0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.36.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires:	%{name}-component = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evolution-data-server >= %{version}
Requires:	gnome-icon-theme >= 3.2.0
Requires:	gtkhtml >= 4.5.2
Requires:	hicolor-icon-theme
Requires:	libical >= 0.46
Requires:	psmisc
Suggests:	adwaita-icon-theme
Obsoletes:	evolution-mono
Obsoletes:	evolution-pilot
Obsoletes:	evolution-python
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
Requires:	glib2 >= 1:2.36.0

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
Requires:	cyrus-sasl-devel
Requires:	evolution-data-server-devel >= %{version}
Requires:	glib2-devel >= 1:2.36.0
Requires:	gnome-desktop-devel >= 3.2.0
Requires:	gtk+3-devel >= 3.8.0
Requires:	gtkhtml-devel >= 4.5.3
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
Requires(post,postun):	glib2 >= 1:2.36.0
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
Requires(post,postun):	glib2 >= 1:2.36.0
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
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-component = %{version}-%{release}
Obsoletes:	evolution-caldav
Obsoletes:	evolution-webcal

%description calendar
Evolution calendar and todo component.

%description calendar -l pl.UTF-8
Kalendarz i lista zadań Evolution.

%package apidocs
Summary:	Evolution API documentation
Summary(pl.UTF-8):	Dokumentacja API Evolution
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Evolution API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Evolution.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	BOGOFILTER="/usr/bin/bogofilter" \
	HIGHLIGHT="/usr/bin/highlight" \
	SPAMASSASSIN="/usr/bin/spamassassin" \
	SA_LEARN="/usr/bin/sa-learn" \
	SPAMC="/usr/bin/spamc" \
	SPAMD="/usr/bin/spamd" \
	--disable-silent-rules \
	--enable-static \
	--enable-canberra \
	--enable-pst-import \
	--disable-image-inline \
	--enable-weather \
	--disable-contact-maps \
	%{__with_without ldap openldap} \
	--without-static-ldap \
	--with-nspr-includes="%{_includedir}/nspr" \
	--with-nss-includes="%{_includedir}/nss" \
	--with-nspr-libs="%{_libdir}" \
	--with-nss-libs="%{_libdir}" \
	--enable-plugins=all \
	--enable-nss=yes \
	--enable-smime=yes \
	--with-sub-version=" PLD Linux" \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}

# remove useless files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*/*/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/evolution.desktop
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/%{basever}/*.la

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post mail
%update_desktop_database_post
%glib_compile_schemas

%postun mail
%update_desktop_database_postun
%glib_compile_schemas

%post addressbook
%update_desktop_database_post
%glib_compile_schemas

%postun addressbook
%update_desktop_database_postun
%glib_compile_schemas

%post calendar
%update_desktop_database_post
%glib_compile_schemas

%postun calendar
%update_desktop_database_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%attr(755,root,root) %{_bindir}/evolution
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{basever}/killev
%dir %{_libdir}/evolution/%{basever}/modules
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-composer-autosave.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-contact-photos.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-gravatar.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-offline-alert.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-plugin-lib.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-plugin-manager.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-settings.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-web-inspector.so

%{_datadir}/GConf/gsettings/evolution.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.importer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.gschema.xml

%{_datadir}/appdata/evolution.appdata.xml

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
%{_datadir}/evolution/%{basever}/errors/widgets.error

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
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-backup-restore.so
%{_datadir}/evolution/%{basever}/errors/org-gnome-backup-restore.error

# prefer-plain
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-prefer-plain.so
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-prefer-plain.so
%{evo_plugins_dir}/org-gnome-prefer-plain.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.prefer-plain.gschema.xml

# face plugin
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-face.so
%{evo_plugins_dir}/org-gnome-face.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-face.error
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.face-picture.gschema.xml

# external editor plugin
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-external-editor.so
%{evo_plugins_dir}/org-gnome-external-editor.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-external-editor.error

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/%{basever}
%dir %{evo_plugins_dir}
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libeabutil.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontacteditor.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libecontactlisteditor.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libemail-engine.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libessmime.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-calendar-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-formatter.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-composer.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail-importers.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-mail.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-shell.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-smime.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libevolution-util.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/libgnomecanvas.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-%{basever}
%{_pkgconfigdir}/libemail-engine.pc
%{_pkgconfigdir}/evolution-calendar-3.0.pc
%{_pkgconfigdir}/evolution-mail-3.0.pc
%{_pkgconfigdir}/evolution-shell-3.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/evolution/%{basever}/libeabutil.a
%{_libdir}/evolution/%{basever}/libecontacteditor.a
%{_libdir}/evolution/%{basever}/libecontactlisteditor.a
%{_libdir}/evolution/%{basever}/libemail-engine.a
%{_libdir}/evolution/%{basever}/libessmime.a
%{_libdir}/evolution/%{basever}/libevolution-addressbook-importers.a
%{_libdir}/evolution/%{basever}/libevolution-calendar.a
%{_libdir}/evolution/%{basever}/libevolution-calendar-importers.a
%{_libdir}/evolution/%{basever}/libevolution-mail-composer.a
%{_libdir}/evolution/%{basever}/libevolution-mail-formatter.a
%{_libdir}/evolution/%{basever}/libevolution-mail-importers.a
%{_libdir}/evolution/%{basever}/libevolution-mail.a
%{_libdir}/evolution/%{basever}/libevolution-shell.a
%{_libdir}/evolution/%{basever}/libevolution-smime.a
%{_libdir}/evolution/%{basever}/libevolution-util.a
%{_libdir}/evolution/%{basever}/libgnomecanvas.a

%files mail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-mail.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-mail-config.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-mailto-handler.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-mdn.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-startup-wizard.so
%{_datadir}/evolution/%{basever}/etspec/message-list.etspec
%{_datadir}/evolution/%{basever}/errors/evolution-mdn.error
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
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.mail.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.external-editor.gschema.xml

# PLUGINS
# attachment-reminder
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-attachment-reminder.so
%{evo_plugins_dir}/org-gnome-evolution-attachment-reminder.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-attachment-reminder.error
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.attachment-reminder.gschema.xml

# bbdb
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-bbdb.so
%{evo_plugins_dir}/org-gnome-evolution-bbdb.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.autocontacts.gschema.xml

# bogofilter
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.bogofilter.gschema.xml
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-bogofilter.so

# dbx-import
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-dbx-import.so
%{evo_plugins_dir}/org-gnome-dbx-import.eplug

# email-custom-header
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-email-custom-header.so
%{evo_plugins_dir}/org-gnome-email-custom-header.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.email-custom-header.gschema.xml

# itip-formatter
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-itip-formatter.so
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-itip-formatter.so
%{evo_plugins_dir}/org-gnome-itip-formatter.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-itip-formatter.error
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.itip.gschema.xml

# mail-notification
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mail-notification.so
%{evo_plugins_dir}/org-gnome-mail-notification.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.mail-notification.gschema.xml

# mail-to-task
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mail-to-task.so
%{evo_plugins_dir}/org-gnome-mail-to-task.eplug

# mailing-list-actions
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-mailing-list-actions.so
%{evo_plugins_dir}/org-gnome-mailing-list-actions.eplug
%{_datadir}/evolution/%{basever}/errors/org-gnome-mailing-list-actions.error

# pst-import
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-pst-import.so
%{evo_plugins_dir}/org-gnome-pst-import.eplug

# spamassassin
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-spamassassin.so
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.spamassassin.gschema.xml

# templates
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-templates.so
%{evo_plugins_dir}/org-gnome-templates.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.templates.gschema.xml

# text-highlight
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-text-highlight.so

# tnef-attachment
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-tnef-attachment.so

# vcard-inline
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-vcard-inline.so

%files addressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-export
%{_datadir}/evolution/%{basever}/ecps
%{_datadir}/evolution/%{basever}/errors/addressbook.error
%{_datadir}/evolution/%{basever}/etspec/e-addressbook-view.etspec
%{_datadir}/evolution/%{basever}/views/addressbook
%{_datadir}/evolution/%{basever}/addresstypes.xml

%{_desktopdir}/%{name}-addressbook.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.addressbook.gschema.xml

# PLUGINS
# ldap accounts config
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-book-config-ldap.so

# google accounts config
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-book-config-google.so

# addressbook-local
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-book-config-local.so

# webdav-accounts-setup
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-book-config-webdav.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-calendar.so
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
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.calendar.gschema.xml

# PLUGINS
# caldav
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-cal-config-caldav.so

# contacts
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-cal-config-contacts.so

# calendar-local
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-cal-config-local.so

# calendar-weather
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-cal-config-weather.so

# calendar-weather
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-cal-config-webcal.so

# google-account-setup
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/module-cal-config-google.so

# publish-calendar
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-publish-calendar.so
%{evo_plugins_dir}/org-gnome-publish-calendar.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.publish-calendar.gschema.xml

# save-calendar
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-save-calendar.so
%{evo_plugins_dir}/org-gnome-save-calendar.eplug

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/evolution-mail-composer
%{_gtkdocdir}/evolution-mail-engine
%{_gtkdocdir}/evolution-mail-formatter
%{_gtkdocdir}/evolution-shell
%{_gtkdocdir}/evolution-util
