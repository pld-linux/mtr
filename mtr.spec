Summary:	Matt's Traceroute - network diagnostic tool
Summary(pl):	Matt's Traceroute - narzêdzie do diagnostyki sieci.
Name:		mtr
Version:	0.35
Release:	1
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Copyright:	GPL
Source:		ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Patch:		%{name}-resolv.patch
BuildPrereq:	glib-devel
BuildPrereq:	gtk+-devel
%requires_pkg	glib
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
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
    ./configure \
	--prefix=/usr 
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{sbin,man/man8,X11R6/share/pixmaps}
make prefix=$RPM_BUILD_ROOT/usr install

install img/mtr_icon.xpm $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps

gzip -9fn $RPM_BUILD_ROOT/usr/man/man8/* \
	AUTHORS NEWS README SECURITY 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,SECURITY}.gz

%attr(4755,root,root) /usr/sbin/mtr
/usr/man/man8/*
/usr/X11R6/share/pixmaps/*

%changelog
* Thu Mar 11 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.33-1]
- removed man group from man pages
- removed mtr.patch
- added mtr-resolv.patch (link with -lresolv )

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
