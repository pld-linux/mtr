Summary:	Matt's Traceroute - network diagnostic tool
Summary(pl):	Matt's Traceroute - narzêdzie do diagnostyki sieci
Name:		mtr
Version:	0.42
Release:	2
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
License:	GPL
Source0:	ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Patch0:		mtr-resolv.patch
Patch1:		mtr-makefile.patch
BuildRequires:	gtk+-devel 
BuildRequires:	ncurses-devel >= 5.0
Icon:		mtr.gif
URL:		http://www.bitwizard.nl/mtr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mtr combines the functionality of the 'traceroute' and 'ping' programs
into a single network diagnostic tool. This version has been compiled
with only the text (ncurses) interface.

%description -l pl
Mtr jest narzêdziem do diagnostyki sieci, ³±cz±cym funkcje
traceroute'a oraz ping'a. Ta wersja zosta³a skompilowana z interfejsem
tekstowym (ncurses) oraz obs³ug± X Window (Gtk).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	AUTHORS NEWS README SECURITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz img/mtr_icon.xpm
%attr(4755,root,root) %{_sbindir}/mtr
%{_mandir}/man8/*
