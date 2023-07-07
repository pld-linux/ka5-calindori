#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		calindori
Summary:	Calendar application for Plasma Mobile
Name:		ka5-%{kaname}
Version:	23.04.3
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ffab22288b21f781f6541185236746ad
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Qml-devel >= 5.15.9
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.95.0
BuildRequires:	kf5-kcalendarcore-devel >= 5.95.0
BuildRequires:	kf5-kconfig-devel >= 5.95.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.95.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.95.0
BuildRequires:	kf5-ki18n-devel >= 5.95.0
BuildRequires:	kf5-kirigami2-devel >= 5.95.0
BuildRequires:	kf5-knotifications-devel >= 5.95.0
BuildRequires:	kf5-kpeople-devel >= 5.95.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calindori is a touch friendly calendar application. It has been
designed for mobile devices but it can also run on desktop
environments. It offers:

- Monthly agenda
- Multiple calendars
- Event management
- Task management
- Calendar import

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/org.kde.calindac.desktop
%attr(755,root,root) %{_bindir}/calindac
%attr(755,root,root) %{_bindir}/calindori
%{_desktopdir}/org.kde.calindori.desktop
%{_datadir}/dbus-1/services/org.kde.calindac.service
%{_iconsdir}/hicolor/scalable/apps/calindori.svg
%{_datadir}/knotifications5/calindac.notifyrc
%{_datadir}/metainfo/org.kde.calindori.appdata.xml
