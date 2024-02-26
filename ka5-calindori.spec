#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		calindori
Summary:	Calendar application for Plasma Mobile
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	61d27aa27a2efc3428c8350e79c19c8f
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Qml-devel >= 5.15.9
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.95.0
BuildRequires:	kf6-kcalendarcore-devel >= 5.95.0
BuildRequires:	kf6-kconfig-devel >= 5.95.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.95.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.95.0
BuildRequires:	kf6-ki18n-devel >= 5.95.0
BuildRequires:	kf6-kirigami-devel >= 5.95.0
BuildRequires:	kf6-knotifications-devel >= 5.95.0
BuildRequires:	kf6-kpeople-devel >= 5.95.0
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
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
%{_datadir}/knotifications6/calindac.notifyrc
%{_datadir}/metainfo/org.kde.calindori.appdata.xml
