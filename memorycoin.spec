%define	snap	20131215
Summary:	memorycoin
Name:		memorycoin
Version:	0.1
Release:	1.%{snap}.1
License:	MIT/X11
Group:		X11/Applications
Source0:	memorycoin-%{snap}.tar.bz2
# Source0-md5:	8ea54e0ae9e4ae451021f6a7dc834b3d
Patch0:		%{name}-build.patch
URL:		http://www.memorycoin.info/
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	boost-devel
BuildRequires:	db-cxx-devel
BuildRequires:	miniupnpc-devel >= 1.5
BuildRequires:	openssl-devel
BuildRequires:	qrencode-devel
BuildRequires:	qt4-qmake
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MemoryCoin

%package qt
Summary:	Qt-based MemoryCoin Wallet
Group:		X11/Applications

%description qt
Qt-based MemoryCoin Wallet.

%prep
%setup -q -n memorycoin
%patch0 -p1

%build
install -d build
cd build
%{cmake} ../ \
	-DDOXYGEN_FOUND=FALSE

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_mandir}/man{1,5},%{_localedir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/kde4/services}

install build/src/memorycoind $RPM_BUILD_ROOT%{_bindir}/memorycoind
install build/src/qt/memorycoin-qt $RPM_BUILD_ROOT%{_bindir}/memorycoin-qt

sed -e 's#bitcoin#memorycoin#g' contrib/debian/bitcoin-qt.desktop > $RPM_BUILD_ROOT%{_desktopdir}/memorycoin-qt.desktop
sed -e 's#bitcoin#memorycoin#g' contrib/debian/bitcoin-qt.protocol > $RPM_BUILD_ROOT%{_datadir}/kde4/services/memorycoin-qt.protocol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/memorycoind

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/memorycoin-qt
%{_datadir}/kde4/services/memorycoin-qt.protocol
%{_desktopdir}/memorycoin-qt.desktop
