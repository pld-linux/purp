Summary:	A ncurses-based RPM-handler
Summary(pl):	Program na konsolê do zarz±dzania pakietami RPM (ncurses)
Name:		purp
Version:	0.4.1
Release:	4
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.lysator.liu.se/pub/unix/purp/%{name}-%{version}.tgz
Patch:		%{name}-%{version}.diff
URL:		http://www.lysator.liu.se/purp/
Vendor:		Anders Karlsson <pugo@lysator.liu.se>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A ncurses-based RPM-handler which provides a fast and powerful
way to navigate, install, upgrade and uninstall RPM-packages on 
text-terminal-devices.

%description -l pl
Program do zarz±dzania pakietami RPM bazuj±cy na ncurses. purp pozwala
na szybkie i wydajne instalowanie, odinstalowywanie oraz aktualizacjê
pakietów.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install -s purp $RPM_BUILD_ROOT%{_sbindir}
install purp.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755) 
%doc README.gz CHANGES.gz

%{_mandir}/man8/*
%attr(755,root,root) %{_sbindir}/*
