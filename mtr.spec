# Conditional build:
# --with X11 - build wihtt X11/gtk+ interface
#
Summary:	Matt's Traceroute - network diagnostic tool
Summary(pl):	Matt's Traceroute - narzЙdzie do diagnostyki sieci
Summary(ru):	Matt's Traceroute - утилита для диагностики сети
Summary(uk):	Matt's Traceroute - утил╕та для д╕агностики мереж╕
Name:		mtr
Version:	0.49
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-resolv.patch
Patch1:		%{name}-makefile.patch
#Patch2:	ftp://ftp.kame.net/pub/kame/misc/mtr-045-v6-20020207.diff.gz
Patch2:		%{name}-0.48-v6-20020306.patch.gz
Patch3:		%{name}-nogtk.patch
Icon:		mtr.xpm
BuildRequires:	autoconf
BuildRequires:	automake
%{?_with_X11:BuildRequires:	gtk+-devel}
BuildRequires:	ncurses-devel >= 5.2
URL:		http://www.bitwizard.nl/mtr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mtr-gtk
Obsoletes:	mtr-ncurses

%description
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description -l pl
mtr jest narzЙdziem do diagnostyki sieci, Ё╠cz╠cym funkcje
traceroute'a oraz ping'a. Program ten ╤ledzi trasЙ poЁ╠cznia miЙdzy
punktem z ktСrego zostaЁ uruchomiony, a punktem docelowym. Po
skompletowaniu listy punktСw po╤rednich przez ktСre pzrechodz╠ pakiety
miЙdzy tymi punktami do ka©dego z nich wysyЁane s╠ pakiety ICMP ECHO i
czasy odpowiedzi s╠ nastЙpnie prezentowane na bie©╠co.

%description -l ru
mtr - это traceroute и ping в одном флаконе. При старте mtr исследует
сетевое соединение между машиной, на которой он запущен, и машиной,
заданной пользователем. После того, как он определит адреса каждого
хопа между этими двумя машинами, mtr посылает последовательность ICMP
ECHO запросов на каждый из хопов для определения качества линка с
каждой из машин. По мере того, как он это делает, mtr выводит текущую
статистику по каждой машине.

%description -l uk
mtr - це traceroute та ping в одному флакон╕. При запуску mtr
досл╕джу╓ мережеве з'╓днання м╕ж машиною, на як╕й в╕н запущений та
заданою користувачем. П╕сля визначення адрес кожного хопу м╕ж цими
двома машинами, mtr посила╓ посл╕довн╕сть ICMP ECHO запит╕в на кожний
з хоп╕в для визначення якост╕ л╕нка до кожно╖ з машин. В ход╕ цього
процесу mtr виводить поточну статистику по кожн╕й машин╕.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoheader
aclocal
autoconf
rm -f missing
automake -a -c -f
%configure \
	--with%{!?_with_X11:out}-gtk \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf mtr $RPM_BUILD_ROOT%{_sbindir}/mtr6

gzip -9nf AUTHORS NEWS README SECURITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(4754,root,adm) %{_sbindir}/mtr
%attr(4754,root,adm) %{_sbindir}/mtr6
%{_mandir}/man8/*
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
