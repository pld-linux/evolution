%define		_prefix		/usr/X11R6

Summary:	The GNOME Email/Calendar/Addressbook Suite
Name:		evolution
Version: 	0.5.1
Release:	1
Copyright:	GPL
Group:		Applications/Productivity
Source: 	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.helixcode.com/aoos/evolution.php3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	camel
Requires:	gtkhtml >= 0.6.1
Requires:	libunicode >= 0.4
Requires:	libxml >= 1.8.7
BuildRequires:	bonobo-devel >= 0.18
BuildRequires:	gtkhtml-devel >= 0.6.1
BuildRequires:	gnome-vfs-devel >= 0.3.1
BuildRequires:	libunicode-devel >= 0.4
BuildRequires:	oaf-devel >= 0.5.1
BuildRequires:	gnome-print-devel >= 0.20
BuildRequires:	gdk-pixbuf-devel >= 0.8

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool.  The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool. 

%package devel
Summary:        Development libraries and header files for evolution
Group:          Development/Libraries
Requires:       %name = %{PACKAGE_VERSION}
Provides:	camel-devel

%description devel
Evolution is the GNOME mailer, calendar, contact manager and
communications tool.  The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

This package contains the files necessary to develop applications
using Evolution's libraries.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="-pipe $RPM_OPT_FLAGS" ./configure	\
	--prefix=%{_prefix} --sysconfdir=%{_sysconfdir}	\
	--localstatedir=%{_localstatedir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} \
	localstatedir=$RPM_BUILD_ROOT%{_localstatedir} install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_prefix}/share/evolution
%{_prefix}/share/oaf/*.oafinfo
%{_prefix}/share/idl/*.idl
%{_prefix}/share/gnome/help/evolution
%{_prefix}/share/gnome/apps/Applications/*.desktop
%{_prefix}/share/images/evolution
%{_prefix}/share/locale/*
%{_prefix}/share/pixmaps/*
%{_prefix}/share/mime-info/*
%{_prefix}/bin/*
%{_prefix}/lib/evolution/camel-providers/*/*.so*
%{_prefix}/lib/evolution/camel-providers/*/*.urls
%{_prefix}/lib/*.so.*

%files devel
%{_prefix}/include/camel
%{_prefix}/include/ename
%{_prefix}/include/evolution
%{_prefix}/lib/*so
%{_prefix}/lib/*a
%{_prefix}/lib/evolution/camel-providers/*/*a
