Summary:	A ncurses-based RPM-handler
Summary(pl):	Program terminalowy (na ncurses) do zarz±dzania pakietami RPM
Name:		purp
Version:	1.1.0
Release:	1
License:	GPL
Vendor:		Anders Karlsson <pugo@lysator.liu.se>
Group:		Applications/System
Source0:	ftp://ftp.lysator.liu.se/pub/unix/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-addch-fix.patch
URL:		http://www.lysator.liu.se/purp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	rpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A ncurses-based RPM-handler which provides a fast and powerful way to
navigate, install, upgrade and uninstall RPM-packages on
text-terminal-devices.

%description -l pl
Program do zarz±dzania pakietami RPM bazuj±cy na ncurses. purp pozwala
na szybkie i wydajne instalowanie, odinstalowywanie oraz aktualizacjê
pakietów.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}}

install purp $RPM_BUILD_ROOT%{_sbindir}
install purprc $RPM_BUILD_ROOT%{_sysconfdir}
install purp.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README CHANGES COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz CHANGES.gz COPYING.gz
%attr(755,root,root) %{_sbindir}/*
%{_sysconfdir}/*
%{_mandir}/man8/*
