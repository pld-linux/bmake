Summary:	NetBSD make utility
Summary(pl.UTF-8):	Narzędzie make z NetBSD
Name:		bmake
Version:	20250308
Release:	2
License:	BSD
Group:		Development/Tools
Source0:	https://ftp.netbsd.org/pub/NetBSD/misc/sjg/%{name}-%{version}.tar.gz
# Source0-md5:	9a30bd359a8027001ef1e0e5847f6e46
URL:		https://ftp.netbsd.org/pub/NetBSD/misc/sjg/
BuildRequires:	sed >= 4.0
# see mk/install-mk /MK_VERSION
Provides:	mk-files = 20250314-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
make is a program designed to simplify the maintenance of other
programs. Its input is a list of specifications as to the files upon
which programs and other files depend.

This package contains a port of the BSD make tool (from NetBSD).

%description -l pl.UTF-8
make to program zaprojektowany w celu uproszczenia utrzymywania innych
programów. Jego wejściem jest lista specyfikacji jako plików, od
których zależą programy i inne pliki.

Ten pakiet zawiera port narzędzia make BSD (z NetBSD).

%prep
%setup -q -n %{name}

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python3},' mk/meta2deps.py

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	STRIP_FLAG=

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README PSD.doc/tutorial.ms mk/mk-files.txt
%attr(755,root,root) %{_bindir}/bmake
%dir %{_datadir}/mk
%{_datadir}/mk/sys
%{_datadir}/mk/*.mk
%{_datadir}/mk/mkopt.sh
%{_datadir}/mk/setopts.sh
%attr(755,root,root) %{_datadir}/mk/install-sh
%attr(755,root,root) %{_datadir}/mk/meta2deps.py
%attr(755,root,root) %{_datadir}/mk/meta2deps.sh
%attr(755,root,root) %{_datadir}/mk/newlog.sh
%attr(755,root,root) %{_datadir}/mk/stage-install.sh
%{_mandir}/man1/bmake.1*
