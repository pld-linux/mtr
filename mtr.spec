Summary:	Matt's Traceroute - network diagnostic tool
Summary(pl):	Matt's Traceroute - narzêdzie do diagnostyki sieci.
Name:		mtr
Version:	0.34
Release:	1
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Copyright:	GPL
Source:		ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Requires:	glib = 1.2.0
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

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{sbin,man/man8}
make prefix=$RPM_BUILD_ROOT/usr install

gzip -9fn $RPM_BUILD_ROOT/usr/man/man8/* \
	AUTHORS NEWS README SECURITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz img/mtr_icon.xpm

%attr(4755,root,root) /usr/sbin/mtr
/usr/man/man8/*

%changelog
* Wed Apr  7 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.34-1]
- removed patch which restrict use mtr for icmp group.

* Mon Jan 18 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.28-2d]
- changed permission of mtr to 2711, 
- compressed man pages,
- compressed %doc,
- added Group(pl).

* Sat Nov 07 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.28-1d]
- updated to 0.28,
- added LDFLAGS before ./configure,
- added URL to Source,
- minor changes.

* Wed Jul 08 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.21-4d]
- build against glibc-2.1,
- translation modified for pl,
- added %changelog,
- restricted ELF binary permission.
