# Conditional build:
# --witht X11 - build wihtt X11/gtk+ interface
#
Summary:	Matt's Traceroute - network diagnostic tool
Summary(pl):	Matt's Traceroute - narzêdzie do diagnostyki sieci
Name:		mtr
Version:	0.44
Release:	5
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-resolv.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-nogtk.patch
#Patch3:	ftp://ftp.kame.net/pub/kame/misc/mtr-042-v6-20010508.diff.gz
Patch3:		mtr-0.44-v6-20010519.patch.gz
Icon:		mtr.xpm
BuildRequires:	autoconf
BuildRequires:	automake
%{?_with_X11:BuildRequires:	gtk+-devel}
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
URL:		http://www.bitwizard.nl/mtr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mtr-gtk
Obsoletes:	mtr-ncurses

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
%patch2 -p1
%patch3 -p1

%build
libtoolize --copy --force
autoheader
aclocal
autoconf
rm -f missing
automake -a -c
%configure \
	--with%{!?_with_X11:out}-gtk \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_applnkdir}/Networking/Misc,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/Misc
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf mtr $RPM_BUILD_ROOT%{_sbindir}/mtr6

gzip -9nf AUTHORS NEWS README SECURITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(4750,root,icmp) %{_sbindir}/mtr
%attr(4750,root,icmp) %{_sbindir}/mtr6
%{_mandir}/man8/*
%{_applnkdir}/Networking/Misc/*
%{_pixmapsdir}/*
