#
# Conditional build:
%bcond_without	x	# without X11 version
#
Summary:	Matt's Traceroute - network diagnostic tool
Summary(es):	Herramienta para diagnСstico de red, combinando ping/traceroute
Summary(pl):	Matt's Traceroute - narzЙdzie do diagnostyki sieci
Summary(pt_BR):	Ferramenta para diagnСstico da rede, combinando ping/traceroute
Summary(ru):	Matt's Traceroute - утилита для диагностики сети
Summary(uk):	Matt's Traceroute - утил╕та для д╕агностики мереж╕
Name:		mtr
Version:	0.54
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
# SOurce0-md5:	7f7ecb50fc37fedb13135a5ef80fda7d
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-resolv.patch
Patch2:		ftp://ftp.kame.net/pub/kame/misc/mtr-052-v6-20030110b.diff.gz
Patch3:		%{name}-nogtk.patch
# required by KAME patch
Patch4:		%{name}-SA_LEN.patch
# prevent exit() with terminal breakage caused by v6 patch
Patch5:		%{name}-v6-notermbreak.patch
Icon:		mtr.xpm
URL:		http://www.bitwizard.nl/mtr/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_x:BuildRequires:	gtk+-devel}
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mtr-ncurses

%description
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description -l es
mtr es una herramienta para diagnСstico de la red que combina ping y
traceroute en un programa. Tiene dos interfaces, una ncurses, Зtil
para uso en sesiones telnet/ssh y una gtk para uso en el X Window.

%description -l pl
mtr jest narzЙdziem do diagnostyki sieci, Ё╠cz╠cym funkcje
traceroute'a oraz pinga. Program ten ╤ledzi trasЙ poЁ╠cznia miЙdzy
punktem z ktСrego zostaЁ uruchomiony, a punktem docelowym. Po
skompletowaniu listy punktСw po╤rednich przez ktСre pzrechodz╠ pakiety
miЙdzy tymi punktami do ka©dego z nich wysyЁane s╠ pakiety ICMP ECHO i
czasy odpowiedzi s╠ nastЙpnie prezentowane na bie©╠co.

%description -l pt_BR
O mtr И uma ferramenta para diagnСstico da rede que combina ping e
traceroute em um programa. Tem duas interfaces, uma ncurses, Зtil para
uso em sessУes telnet/ssh e uma gtk para uso no X Window.

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

%package X11
Summary:	Matt's Traceroute - network diagnostic tool, X11 version
Summary(es):	Interface GTK para mtr
Summary(pl):	Matt's Traceroute - narzЙdzie do diagnostyki sieci, wersja X11
Summary(pt_BR):	Interface GTK para o mtr
Summary(ru):	Matt's Traceroute - утилита для диагностики сети
Summary(uk):	Matt's Traceroute - утил╕та для д╕агностики мереж╕
Group:		Networking/Utilities
Obsoletes:	mtr-gtk

%description X11
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description X11 -l es
mtr es una herramienta para diagnСstico de la red que combina ping y
traceroute en un programa. Tiene dos interfaces, una ncurses, Зtil
para uso en sesiones telnet/ssh y una gtk para uso en el X Window.

%description X11 -l pl
mtr jest narzЙdziem do diagnostyki sieci, Ё╠cz╠cym funkcje
traceroute'a oraz pinga. Program ten ╤ledzi trasЙ poЁ╠cznia miЙdzy
punktem z ktСrego zostaЁ uruchomiony, a punktem docelowym. Po
skompletowaniu listy punktСw po╤rednich przez ktСre pzrechodz╠ pakiety
miЙdzy tymi punktami do ka©dego z nich wysyЁane s╠ pakiety ICMP ECHO i
czasy odpowiedzi s╠ nastЙpnie prezentowane na bie©╠co.

%description X11 -l pt_BR
O mtr И uma ferramenta para diagnСstico da rede que combina ping e
traceroute em um programa. Tem duas interfaces, uma ncurses, Зtil para
uso em sessУes telnet/ssh e uma gtk para uso no X Window.

%description X11 -l ru
mtr - это traceroute и ping в одном флаконе. При старте mtr исследует
сетевое соединение между машиной, на которой он запущен, и машиной,
заданной пользователем. После того, как он определит адреса каждого
хопа между этими двумя машинами, mtr посылает последовательность ICMP
ECHO запросов на каждый из хопов для определения качества линка с
каждой из машин. По мере того, как он это делает, mtr выводит текущую
статистику по каждой машине.

%description X11 -l uk
mtr - це traceroute та ping в одному флакон╕. При запуску mtr
досл╕джу╓ мережеве з'╓днання м╕ж машиною, на як╕й в╕н запущений та
заданою користувачем. П╕сля визначення адрес кожного хопу м╕ж цими
двома машинами, mtr посила╓ посл╕довн╕сть ICMP ECHO запит╕в на кожний
з хоп╕в для визначення якост╕ л╕нка до кожно╖ з машин. В ход╕ цього
процесу mtr виводить поточну статистику по кожн╕й машин╕.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%if %{with x}
%configure \
	--with-gtk \
	--enable-ipv6

%{__make}
mv -f mtr mtr-x11
%{__make} clean
%endif

%configure \
	--without-gtk \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir},/usr/X11R6/sbin}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with x}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install mtr-x11 $RPM_BUILD_ROOT/usr/X11R6/sbin/mtr
%endif

ln -sf mtr $RPM_BUILD_ROOT%{_sbindir}/mtr6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README SECURITY
%attr(4754,root,adm) %{_sbindir}/mtr
%attr(4754,root,adm) %{_sbindir}/mtr6
%{_mandir}/man8/*

%if %{with x}
%files X11
%defattr(644,root,root,755)
%attr(4754,root,adm) /usr/X11R6/sbin/mtr
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
%endif
