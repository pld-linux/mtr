Summary:	Matt's Traceroute - network diagnostic tool
Summary(pl):	Matt's Traceroute - narzêdzie do diagnostyki sieci.
Name:		mtr
Version:	0.37
Release:	2
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Copyright:	GPL
Source:		ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Patch0:		mtr-resolv.patch
BuildRequires:	gtk+-devel 
URL:		http://www.mkimball.org/mtr.html
Buildroot:	/tmp/%{name}-%{version}-root

%description
mtr combines the functionality of the 'traceroute' and 'ping'
programs into a single network diagnostic tool. This version
has been compiled with only the text (ncurses) interface.

%description -l pl
Mtr jest narzêdziem do diagnostyki sieci, podobnym do traceroute'a.
Ta wersja by³a kompilowana tylko z interfejsem tekstowym (ncurses).

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
aclocal && autoconf && %configure
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/{sbin,share/man/man8}
make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    sbindir=$RPM_BUILD_ROOT%{_sbindir} \
    install

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man8/* AUTHORS NEWS README SECURITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz img/mtr_icon.xpm

%attr(4711,root,root) %{_sbindir}/mtr
%{_mandir}/man8/*
