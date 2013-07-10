#
# Conditional build:
%bcond_without	x	# without X11/GTK+2 version
#
Summary:	Matt's Traceroute - network diagnostic tool
Summary(es.UTF-8):	Herramienta para diagnóstico de red, combinando ping/traceroute
Summary(pl.UTF-8):	Matt's Traceroute - narzędzie do diagnostyki sieci
Summary(pt_BR.UTF-8):	Ferramenta para diagnóstico da rede, combinando ping/traceroute
Summary(ru.UTF-8):	Matt's Traceroute - утилита для диагностики сети
Summary(uk.UTF-8):	Matt's Traceroute - утиліта для діагностики мережі
Name:		mtr
Version:	0.85
Release:	1
Epoch:		1
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
# Source0-md5:	aba1e111d270178eb1d65e51ebf6503f
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-Makefile.patch

Patch2:		%{name}-mtr6.patch
Patch3:		%{name}-display.patch
Patch4:		%{name}-usage_first_max_hop.patch
Patch5:		%{name}-noraw.patch
Patch6:		%{name}-nox.patch
URL:		http://www.bitwizard.nl/mtr/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
%{?with_x:BuildRequires:	gtk+2-devel >= 2:2.6.0}
BuildRequires:	ncurses-devel >= 5.2
%{?with_x:BuildRequires:	pkgconfig}
Obsoletes:	mtr-ncurses
Requires:	glib2 >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description -l es.UTF-8
mtr es una herramienta para diagnóstico de la red que combina ping y
traceroute en un programa. Tiene dos interfaces, una ncurses, útil
para uso en sesiones telnet/ssh y una GTK+ para uso en el X Window.

%description -l pl.UTF-8
mtr jest narzędziem do diagnostyki sieci, łączącym funkcje
traceroute'a oraz pinga. Program ten śledzi trasę połączenia między
punktem z którego został uruchomiony, a punktem docelowym. Po
skompletowaniu listy punktów pośrednich przez które przechodzą pakiety
między tymi punktami do każdego z nich wysyłane są pakiety ICMP ECHO i
czasy odpowiedzi są następnie prezentowane na bieżąco.

%description -l pt_BR.UTF-8
O mtr é uma ferramenta para diagnóstico da rede que combina ping e
traceroute em um programa. Tem duas interfaces, uma ncurses, útil para
uso em sessões telnet/ssh e uma GTK+ para uso no X Window.

%description -l ru.UTF-8
mtr - это traceroute и ping в одном флаконе. При старте mtr исследует
сетевое соединение между машиной, на которой он запущен, и машиной,
заданной пользователем. После того, как он определит адреса каждого
хопа между этими двумя машинами, mtr посылает последовательность ICMP
ECHO запросов на каждый из хопов для определения качества линка с
каждой из машин. По мере того, как он это делает, mtr выводит текущую
статистику по каждой машине.

%description -l uk.UTF-8
mtr - це traceroute та ping в одному флаконі. При запуску mtr
досліджує мережеве з'єднання між машиною, на якій він запущений та
заданою користувачем. Після визначення адрес кожного хопу між цими
двома машинами, mtr посилає послідовність ICMP ECHO запитів на кожний
з хопів для визначення якості лінка до кожної з машин. В ході цього
процесу mtr виводить поточну статистику по кожній машині.

%package X11
Summary:	Matt's Traceroute - network diagnostic tool, X11 version
Summary(es.UTF-8):	Interface GTK+ para mtr
Summary(pl.UTF-8):	Matt's Traceroute - narzędzie do diagnostyki sieci, wersja X11
Summary(pt_BR.UTF-8):	Interface GTK+ para o mtr
Summary(ru.UTF-8):	Matt's Traceroute - утилита для диагностики сети
Summary(uk.UTF-8):	Matt's Traceroute - утиліта для діагностики мережі
Group:		Networking/Utilities
%{?with_x:Requires:	gtk+2 >= 2:2.6.0}
Obsoletes:	mtr-gtk

%description X11
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description X11 -l es.UTF-8
mtr es una herramienta para diagnóstico de la red que combina ping y
traceroute en un programa. Tiene dos interfaces, una ncurses, útil
para uso en sesiones telnet/ssh y una GTK+ para uso en el X Window.

%description X11 -l pl.UTF-8
mtr jest narzędziem do diagnostyki sieci, łączącym funkcje
traceroute'a oraz pinga. Program ten śledzi trasę połączenia między
punktem z którego został uruchomiony, a punktem docelowym. Po
skompletowaniu listy punktów pośrednich przez które przechodzą pakiety
między tymi punktami do każdego z nich wysyłane są pakiety ICMP ECHO i
czasy odpowiedzi są następnie prezentowane na bieżąco.

%description X11 -l pt_BR.UTF-8
O mtr é uma ferramenta para diagnóstico da rede que combina ping e
traceroute em um programa. Tem duas interfaces, uma ncurses, útil para
uso em sessões telnet/ssh e uma GTK+ para uso no X Window.

%description X11 -l ru.UTF-8
mtr - это traceroute и ping в одном флаконе. При старте mtr исследует
сетевое соединение между машиной, на которой он запущен, и машиной,
заданной пользователем. После того, как он определит адреса каждого
хопа между этими двумя машинами, mtr посылает последовательность ICMP
ECHO запросов на каждый из хопов для определения качества линка с
каждой из машин. По мере того, как он это делает, mtr выводит текущую
статистику по каждой машине.

%description X11 -l uk.UTF-8
mtr - це traceroute та ping в одному флаконі. При запуску mtr
досліджує мережеве з'єднання між машиною, на якій він запущений та
заданою користувачем. Після визначення адрес кожного хопу між цими
двома машинами, mtr посилає послідовність ICMP ECHO запитів на кожний
з хопів для визначення якості лінка до кожної з машин. В ході цього
процесу mtr виводить поточну статистику по кожній машині.

%prep
%setup -q
%patch0 -p1

%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1

#echo 'AC_DEFUN([AM_PATH_GTK],[$3])' >> acinclude.m4
%{!?with_x:echo 'AC_DEFUN([AM_PATH_GTK_2_0],[$3])' >> acinclude.m4}

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
mv -f mtr mtr-gtk
%{__make} clean
%endif

%configure \
	--without-gtk \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	sbindir=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with x}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install mtr-gtk $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/mtr-gtk $RPM_BUILD_ROOT%{_sbindir}
%endif

ln -sf %{_bindir}/mtr $RPM_BUILD_ROOT%{_sbindir}/mtr
ln -sf mtr $RPM_BUILD_ROOT%{_bindir}/mtr6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README SECURITY
%attr(4755,root,root) %{_bindir}/mtr
%attr(4755,root,root) %{_bindir}/mtr6
%{_sbindir}/mtr
%{_mandir}/man8/mtr.8*

%if %{with x}
%files X11
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/mtr-gtk
%{_sbindir}/mtr-gtk
%{_desktopdir}/mtr.desktop
%{_pixmapsdir}/mtr.png
%endif
