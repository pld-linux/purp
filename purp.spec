Summary:	A ncurses-based RPM-handler
Summary(pl.UTF-8):	Program terminalowy (na ncurses) do zarządzania pakietami RPM
Name:		purp
Version:	1.1.0
Release:	1
License:	GPL
Vendor:		Anders Karlsson <pugo@lysator.liu.se>
Group:		Applications/System
Source0:	ftp://ftp.lysator.liu.se/pub/unix/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4a5fa4d75c97eb5edb81e89561f08ffe
Patch0:		%{name}-addch-fix.patch
URL:		http://www.lysator.liu.se/purp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	rpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A ncurses-based RPM-handler which provides a fast and powerful way to
navigate, install, upgrade and uninstall RPM-packages on
text-terminal-devices.

%description -l pl.UTF-8
Program do zarządzania pakietami RPM bazujący na ncurses. purp pozwala
na szybkie i wydajne instalowanie, odinstalowywanie oraz aktualizację
pakietów.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make} \
	YY="bison -y"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}}

install purp $RPM_BUILD_ROOT%{_sbindir}
install purprc $RPM_BUILD_ROOT%{_sysconfdir}
install purp.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_sbindir}/*
%{_sysconfdir}/*
%{_mandir}/man8/*
