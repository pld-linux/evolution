#
# Conditional build:
%bcond_without	autoar		# archives support in attachments via gnome-autoar
%bcond_without	ldap		# LDAP support
%bcond_without	contact_maps	# contact maps (libchamplain+clutter+geocode)
%bcond_without	glade		# Glade catalog

%define		eds_ver		%{version}

Summary:	The GNOME Email/Calendar/Addressbook Suite
Summary(pl.UTF-8):	Klient poczty, kalendarz i książka adresowa dla GNOME
Summary(pt_BR.UTF-8):	Cliente de email integrado com calendário e catálogo de endereços
Summary(zh_CN.UTF-8):	Evolution - GNOME个人和工作组信息管理工具(包括电子邮件，日历和地址薄)
Name:		evolution
Version:	3.18.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Mail
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	83bdff7421ae30a9c3ef187eb0eeb4d2
Source3:	%{name}-addressbook.desktop
Source4:	%{name}-calendar.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-tasks.desktop
Patch0:		%{name}-nolibs.patch
URL:		http://wiki.gnome.org/Apps/Evolution/
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	cairo-gobject-devel
%{?with_contact_maps:BuildRequires:	clutter-gtk-devel >= 0.90}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant-devel >= 1.1.7
BuildRequires:	evolution-data-server-devel >= %{eds_ver}
BuildRequires:	gcr-devel >= 3.4
BuildRequires:	gdk-pixbuf2-devel >= 2.24.0
BuildRequires:	geoclue-devel >= 0.12.0
%{?with_contact_maps:BuildRequires:	geocode-glib-devel >= 3.10.0}
BuildRequires:	gettext-tools >= 0.18.1
%{?with_glade:BuildRequires:	glade-devel >= 3.10.0}
BuildRequires:	glib2-devel >= 1:2.40.0
%if %{with autoar}
BuildRequires:	gnome-autoar-devel >= 0.1
BuildRequires:	gnome-autoar-gtk-devel >= 0.1
%endif
BuildRequires:	gnome-common >= 2.26.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.2.0
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtk-webkit3-devel >= 2.2.0
BuildRequires:	gtkhtml-devel >= 4.5.2
BuildRequires:	gtkspell3-devel >= 3.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.49
BuildRequires:	libcanberra-gtk3-devel >= 0.25
%{?with_contact_maps:BuildRequires:	libchamplain-devel >= 0.12}
BuildRequires:	libcryptui-devel
BuildRequires:	libgweather-devel >= 3.10.0
BuildRequires:	libical-devel
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libpst-devel >= 0.6.54
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.7.3
BuildRequires:	libytnef-devel
BuildRequires:	nspr-devel >= 4
BuildRequires:	nss-devel >= 3
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	perl-base
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
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires:	%{name}-component = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evolution-data-server >= %{eds_ver}
Requires:	gnome-icon-theme >= 3.2.0
Requires:	gsettings-desktop-schemas >= 3.2.0
Requires:	hicolor-icon-theme
Requires:	iso-codes >= 0.49
Requires:	libical >= 0.46
Requires:	libnotify >= 0.7
Requires:	psmisc
Requires:	shared-mime-info >= 0.22
Suggests:	adwaita-icon-theme
Obsoletes:	evolution-mono
Obsoletes:	evolution-pilot
Obsoletes:	evolution-python
Obsoletes:	evolution2
Obsoletes:	gnome-pim
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		evo_plugins_dir		%{_libdir}/evolution/plugins

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will be tightly
integrated with one another and act as a seamless personal
information-management tool.

%description -l pl.UTF-8
Evolution to program pocztowy, kalendarz, książka adresowa i narzędzie
komunikacyjne dla GNOME.

%description -l pt_BR.UTF-8
Evolution é um cliente de email para o GNOME com calendário e outras
ferramentas interessantes.

%package libs
Summary:	Evolution libraries
Summary(pl.UTF-8):	Biblioteki Evolution
Group:		X11/Libraries
Requires:	enchant >= 1.1.7
Requires:	gcr >= 3.4
Requires:	gdk-pixbuf2 >= 2.24.0
Requires:	glib2 >= 1:2.40.0
%if %{with autoar}
Requires:	gnome-autoar >= 0.1
Requires:	gnome-autoar-gtk >= 0.1
%endif
Requires:	gtk+3 >= 3.10.0
Requires:	gtk-webkit3 >= 2.2.0
Requires:	gtkhtml >= 4.5.2
Requires:	libcanberra-gtk3 >= 0.25
Requires:	libsoup >= 2.42.0
Requires:	libxml2 >= 1:2.7.3

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
Requires:	evolution-data-server-devel >= %{eds_ver}
Requires:	glib2-devel >= 1:2.40.0
Requires:	gnome-desktop-devel >= 3.2.0
Requires:	gtk+3-devel >= 3.10.0
Requires:	gtk-webkit3-devel >= 2.2.0
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

%package glade
Summary:	Evolution catalog file for Glade
Summary(pl.UTF-8):	Plik katalogu Evolution dla Glade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	glade >= 3.10.0

%description glade
Evolution catalog file for Glade.

%description glade -l pl.UTF-8
Plik katalogu Evolution dla Glade.

%package mail
Summary:	Evolution mail component
Summary(pl.UTF-8):	Moduł pocztowy Evolution
Group:		X11/Applications/Mail
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.40.0
# mail composer requires addressbook component
Requires:	%{name}-addressbook = %{version}-%{release}
Requires:	libpst >= 0.6.54
Provides:	%{name}-component = %{version}-%{release}

%description mail
Evolution mail.

%description mail -l pl.UTF-8
Moduł pocztowy Evolution.

%package addressbook
Summary:	Evolution addressbook component
Summary(pl.UTF-8):	Moduł książki adresowej Evolution
Group:		X11/Applications/Mail
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	%{name} = %{version}-%{release}
%{?with_contact_maps:Requires:	clutter-gtk >= 0.90}
%{?with_contact_maps:Requires:	geocode-glib >= 3.10.0}
%{?with_contact_maps:Requires:	libchamplain >= 0.12}
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
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	%{name} = %{version}-%{release}
Requires:	libgdata >= 0.10
Requires:	libgweather >= 3.10.0
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

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
# ac_cv_libiconv=no to look iconv in libc (configure has inverted logic)
%configure \
	BOGOFILTER="/usr/bin/bogofilter" \
	HIGHLIGHT="/usr/bin/highlight" \
	SPAMASSASSIN="/usr/bin/spamassassin" \
	SA_LEARN="/usr/bin/sa-learn" \
	SPAMC="/usr/bin/spamc" \
	SPAMD="/usr/bin/spamd" \
	ac_cv_libiconv=no \
	%{!?with_autoar:--disable-autoar} \
	--enable-canberra \
	%{?with_contact_maps:--enable-contact-maps} \
	--enable-gtk-doc \
	--enable-nss \
	%{__with_without ldap openldap} \
	--enable-plugins=all \
	--enable-pst-import \
	--disable-silent-rules \
	--enable-smime \
	--enable-static \
	--enable-weather \
	%{?with_glade:--with-glade-catalog} \
	--with-html-dir=%{_gtkdocdir} \
	--with-nspr-includes="%{_includedir}/nspr" \
	--with-nspr-libs="%{_libdir}" \
	--with-nss-includes="%{_includedir}/nss" \
	--with-nss-libs="%{_libdir}" \
	--without-static-ldap \
	--with-sub-version=" PLD Linux"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}

# remove useless files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/{modules,plugins}/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*.la
%if %{with glade}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade/modules/libgladeevolution.{la,a}
%endif
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/evolution.desktop

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
%doc AUTHORS ChangeLog MAINTAINERS NEWS* README
%attr(755,root,root) %{_bindir}/evolution
%attr(755,root,root) %{_libdir}/evolution/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/killev
%dir %{_libdir}/evolution/modules
%attr(755,root,root) %{_libdir}/evolution/modules/module-composer-autosave.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-contact-photos.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-gravatar.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-offline-alert.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-plugin-lib.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-plugin-manager.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-settings.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-web-inspector.so

%{_datadir}/GConf/gsettings/evolution.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.importer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.gschema.xml

%{_datadir}/appdata/evolution.appdata.xml

%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/default
%dir %{_datadir}/evolution/default/C
%dir %{_datadir}/evolution/etspec
%dir %{_datadir}/evolution/views

%lang(ca) %dir %{_datadir}/evolution/default/ca
%lang(cs) %dir %{_datadir}/evolution/default/cs
%lang(de) %dir %{_datadir}/evolution/default/de
%lang(es) %dir %{_datadir}/evolution/default/es
%lang(fi) %dir %{_datadir}/evolution/default/fi
%lang(fr) %dir %{_datadir}/evolution/default/fr
%lang(hu) %dir %{_datadir}/evolution/default/hu
%lang(id) %dir %{_datadir}/evolution/default/id
%lang(it) %dir %{_datadir}/evolution/default/it
%lang(ja) %dir %{_datadir}/evolution/default/ja
%lang(ko) %dir %{_datadir}/evolution/default/ko
%lang(lt) %dir %{_datadir}/evolution/default/lt
%lang(mk) %dir %{_datadir}/evolution/default/mk
%lang(nl) %dir %{_datadir}/evolution/default/nl
%lang(pl) %dir %{_datadir}/evolution/default/pl
%lang(pt) %dir %{_datadir}/evolution/default/pt
%lang(ro) %dir %{_datadir}/evolution/default/ro
%lang(sv) %dir %{_datadir}/evolution/default/sv
%lang(sr) %dir %{_datadir}/evolution/default/sr
%lang(sr@latin) %dir %{_datadir}/evolution/default/sr@latin
%lang(zh_CN) %dir %{_datadir}/evolution/default/zh_CN

%{_datadir}/evolution/address_formats.dat
%{_datadir}/evolution/countrytransl.map

%dir %{_datadir}/evolution/errors
%{_datadir}/evolution/errors/e-system.error
%{_datadir}/evolution/errors/filter.error
%{_datadir}/evolution/errors/mail-composer.error
%{_datadir}/evolution/errors/shell.error
%{_datadir}/evolution/errors/evolution-offline-alert.error
%{_datadir}/evolution/errors/widgets.error

%dir %{_datadir}/evolution/help
%dir %{_datadir}/evolution/help/quickref
%dir %{_datadir}/evolution/help/quickref/C

%{_datadir}/evolution/help/quickref/C/quickref.pdf
%lang(ca) %dir %{_datadir}/evolution/help/quickref/ca
%lang(ca) %{_datadir}/evolution/help/quickref/ca/quickref.pdf
%lang(cs) %dir %{_datadir}/evolution/help/quickref/cs
%lang(cs) %{_datadir}/evolution/help/quickref/cs/quickref.pdf
%lang(de) %dir %{_datadir}/evolution/help/quickref/de
%lang(de) %{_datadir}/evolution/help/quickref/de/quickref.pdf
%lang(es) %dir %{_datadir}/evolution/help/quickref/es
%lang(es) %{_datadir}/evolution/help/quickref/es/quickref.pdf
%lang(fr) %dir %{_datadir}/evolution/help/quickref/fr
%lang(fr) %{_datadir}/evolution/help/quickref/fr/quickref.pdf
%lang(hu) %dir %{_datadir}/evolution/help/quickref/hu
%lang(hu) %{_datadir}/evolution/help/quickref/hu/quickref.pdf
%lang(it) %dir %{_datadir}/evolution/help/quickref/it
%lang(it) %{_datadir}/evolution/help/quickref/it/quickref.pdf
%lang(pl) %dir %{_datadir}/evolution/help/quickref/pl
%lang(pl) %{_datadir}/evolution/help/quickref/pl/quickref.pdf
%lang(pt) %dir %{_datadir}/evolution/help/quickref/pt
%lang(pt) %{_datadir}/evolution/help/quickref/pt/quickref.pdf
%lang(sq) %dir %{_datadir}/evolution/help/quickref/sq
%lang(sq) %{_datadir}/evolution/help/quickref/sq/quickref.pdf
%lang(sv) %dir %{_datadir}/evolution/help/quickref/sv
%lang(sv) %{_datadir}/evolution/help/quickref/sv/quickref.pdf

%{_datadir}/evolution/icons
%{_datadir}/evolution/images
%{_datadir}/evolution/sounds
%{_datadir}/evolution/theme
%{_datadir}/evolution/ui

%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/xdg/autostart/evolution-alarm-notify.desktop

# PLUGINS
# backup-restore
%attr(755,root,root) %{_libdir}/evolution/evolution-backup
%attr(755,root,root) %{_libdir}/evolution/modules/module-backup-restore.so
%{_datadir}/evolution/errors/org-gnome-backup-restore.error

# prefer-plain
%attr(755,root,root) %{_libdir}/evolution/modules/module-prefer-plain.so
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-prefer-plain.so
%{evo_plugins_dir}/org-gnome-prefer-plain.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.prefer-plain.gschema.xml

# face plugin
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-face.so
%{evo_plugins_dir}/org-gnome-face.eplug
%{_datadir}/evolution/errors/org-gnome-face.error
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.face-picture.gschema.xml

# external editor plugin
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-external-editor.so
%{evo_plugins_dir}/org-gnome-external-editor.eplug
%{_datadir}/evolution/errors/org-gnome-external-editor.error

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/evolution
%dir %{evo_plugins_dir}
%attr(755,root,root) %{_libdir}/evolution/libeabutil.so
%attr(755,root,root) %{_libdir}/evolution/libecontacteditor.so
%attr(755,root,root) %{_libdir}/evolution/libecontactlisteditor.so
%attr(755,root,root) %{_libdir}/evolution/libemail-engine.so
%attr(755,root,root) %{_libdir}/evolution/libessmime.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-addressbook-importers.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-calendar.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-calendar-importers.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-mail-formatter.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-mail-composer.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-mail-importers.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-mail.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-shell.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-smime.so
%attr(755,root,root) %{_libdir}/evolution/libevolution-util.so
%attr(755,root,root) %{_libdir}/evolution/libgnomecanvas.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/evolution
%{_pkgconfigdir}/libemail-engine.pc
%{_pkgconfigdir}/evolution-calendar-3.0.pc
%{_pkgconfigdir}/evolution-mail-3.0.pc
%{_pkgconfigdir}/evolution-shell-3.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/evolution/libeabutil.a
%{_libdir}/evolution/libecontacteditor.a
%{_libdir}/evolution/libecontactlisteditor.a
%{_libdir}/evolution/libemail-engine.a
%{_libdir}/evolution/libessmime.a
%{_libdir}/evolution/libevolution-addressbook-importers.a
%{_libdir}/evolution/libevolution-calendar.a
%{_libdir}/evolution/libevolution-calendar-importers.a
%{_libdir}/evolution/libevolution-mail-composer.a
%{_libdir}/evolution/libevolution-mail-formatter.a
%{_libdir}/evolution/libevolution-mail-importers.a
%{_libdir}/evolution/libevolution-mail.a
%{_libdir}/evolution/libevolution-shell.a
%{_libdir}/evolution/libevolution-smime.a
%{_libdir}/evolution/libevolution-util.a
%{_libdir}/evolution/libgnomecanvas.a

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade/modules/libgladeevolution.so
%{_datadir}/glade/catalogs/evolution.xml
%endif

%files mail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/modules/module-mail.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-mail-config.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-mailto-handler.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-mdn.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-startup-wizard.so
%{_datadir}/evolution/etspec/message-list.etspec
%{_datadir}/evolution/errors/evolution-mdn.error
%{_datadir}/evolution/errors/mail.error
%{_datadir}/evolution/filtertypes.xml
%{_datadir}/evolution/vfoldertypes.xml
%{_datadir}/evolution/searchtypes.xml
%{_datadir}/evolution/default/C/mail
%{_datadir}/evolution/views/mail

%lang(ca) %{_datadir}/evolution/default/ca/mail
%lang(cs) %{_datadir}/evolution/default/cs/mail
%lang(de) %{_datadir}/evolution/default/de/mail
%lang(es) %{_datadir}/evolution/default/es/mail
%lang(fi) %{_datadir}/evolution/default/fi/mail
%lang(fr) %{_datadir}/evolution/default/fr/mail
%lang(hu) %{_datadir}/evolution/default/hu/mail
%lang(id) %{_datadir}/evolution/default/id/mail
%lang(it) %{_datadir}/evolution/default/it/mail
%lang(ja) %{_datadir}/evolution/default/ja/mail
%lang(ko) %{_datadir}/evolution/default/ko/mail
%lang(lt) %{_datadir}/evolution/default/lt/mail
%lang(mk) %{_datadir}/evolution/default/mk/mail
%lang(nl) %{_datadir}/evolution/default/nl/mail
%lang(pl) %{_datadir}/evolution/default/pl/mail
%lang(pt) %{_datadir}/evolution/default/pt/mail
%lang(ro) %{_datadir}/evolution/default/ro/mail
%lang(sr) %{_datadir}/evolution/default/sr/mail
%lang(sr@latin) %{_datadir}/evolution/default/sr@latin/mail
%lang(sv) %{_datadir}/evolution/default/sv/mail
%lang(zh_CN) %{_datadir}/evolution/default/zh_CN/mail

%{_desktopdir}/evolution-mail.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.mail.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.external-editor.gschema.xml

# PLUGINS
# attachment-reminder
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-attachment-reminder.so
%{evo_plugins_dir}/org-gnome-evolution-attachment-reminder.eplug
%{_datadir}/evolution/errors/org-gnome-attachment-reminder.error
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.attachment-reminder.gschema.xml

# bbdb
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-evolution-bbdb.so
%{evo_plugins_dir}/org-gnome-evolution-bbdb.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.autocontacts.gschema.xml

# bogofilter
%attr(755,root,root) %{_libdir}/evolution/modules/module-bogofilter.so
%{_datadir}/appdata/evolution-bogofilter.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.bogofilter.gschema.xml

# dbx-import
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-dbx-import.so
%{evo_plugins_dir}/org-gnome-dbx-import.eplug

# email-custom-header
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-email-custom-header.so
%{evo_plugins_dir}/org-gnome-email-custom-header.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.email-custom-header.gschema.xml

# itip-formatter
%attr(755,root,root) %{_libdir}/evolution/modules/module-itip-formatter.so
%{_datadir}/evolution/errors/org-gnome-itip-formatter.error
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
%{_datadir}/evolution/errors/org-gnome-mailing-list-actions.error

# pst-import
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-pst-import.so
%{evo_plugins_dir}/org-gnome-pst-import.eplug

# spamassassin
%attr(755,root,root) %{_libdir}/evolution/modules/module-spamassassin.so
%{_datadir}/appdata/evolution-spamassassin.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.spamassassin.gschema.xml

# templates
%attr(755,root,root) %{evo_plugins_dir}/liborg-gnome-templates.so
%{evo_plugins_dir}/org-gnome-templates.eplug
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.templates.gschema.xml

# text-highlight
%attr(755,root,root) %{_libdir}/evolution/modules/module-text-highlight.so

# tnef-attachment
%attr(755,root,root) %{_libdir}/evolution/modules/module-tnef-attachment.so

# vcard-inline
%attr(755,root,root) %{_libdir}/evolution/modules/module-vcard-inline.so

%files addressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/modules/module-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/evolution-addressbook-export
%{_datadir}/evolution/ecps
%{_datadir}/evolution/errors/addressbook.error
%{_datadir}/evolution/etspec/e-addressbook-view.etspec
%{_datadir}/evolution/views/addressbook
%{_datadir}/evolution/addresstypes.xml

%{_desktopdir}/%{name}-addressbook.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.addressbook.gschema.xml

# PLUGINS
# ldap accounts config
%attr(755,root,root) %{_libdir}/evolution/modules/module-book-config-ldap.so

# google accounts config
%attr(755,root,root) %{_libdir}/evolution/modules/module-book-config-google.so

# addressbook-local
%attr(755,root,root) %{_libdir}/evolution/modules/module-book-config-local.so

# webdav-accounts-setup
%attr(755,root,root) %{_libdir}/evolution/modules/module-book-config-webdav.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/modules/module-calendar.so
%{_datadir}/evolution/etspec/e-cal-list-view.etspec
%{_datadir}/evolution/etspec/e-calendar-table.etspec
%{_datadir}/evolution/etspec/e-meeting-time-sel.etspec
%{_datadir}/evolution/etspec/e-memo-table.etspec
%{_datadir}/evolution/errors/calendar.error
%{_datadir}/evolution/views/calendar
%{_datadir}/evolution/views/memos
%{_datadir}/evolution/views/tasks
%{_datadir}/evolution/caltypes.xml
%{_datadir}/evolution/memotypes.xml
%{_datadir}/evolution/tasktypes.xml

%{_desktopdir}/%{name}-calendar.desktop
%{_desktopdir}/%{name}-tasks.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.calendar.gschema.xml

# PLUGINS
# caldav
%attr(755,root,root) %{_libdir}/evolution/modules/module-cal-config-caldav.so

# contacts
%attr(755,root,root) %{_libdir}/evolution/modules/module-cal-config-contacts.so

# calendar-local
%attr(755,root,root) %{_libdir}/evolution/modules/module-cal-config-local.so

# calendar-weather
%attr(755,root,root) %{_libdir}/evolution/modules/module-cal-config-weather.so

# calendar-weather
%attr(755,root,root) %{_libdir}/evolution/modules/module-cal-config-webcal.so

# google-account-setup
%attr(755,root,root) %{_libdir}/evolution/modules/module-cal-config-google.so

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
