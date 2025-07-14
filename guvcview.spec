# NOTE: possible switches:
# - sfml rendering (BR: sfml-graphics >= 2.0) instead of SDL2
# - Qt6 gui (BR: Qt6Core Qt6Gui Qt6Widgets, qt5-build) instead of gtk+3
# All can be compiled in, selectable at runtime.

Summary:	GTK+ based UVC Viewer
Summary(pl.UTF-8):	Przeglądarka UVC oparta na GTK+
Name:		guvcview
Version:	2.2.1
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	https://downloads.sourceforge.net/guvcview/%{name}-src-%{version}.tar.bz2
# Source0-md5:	8dc549d6cf65b496bcd924ed3539142e
Patch0:		link-math.patch
Patch1:		pc-path.patch
URL:		http://guvcview.sourceforge.net/
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	cmake >= 3.14
BuildRequires:	ffmpeg-devel >= 3.0
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gsl-devel >= 1.15
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	libv4l-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
BuildRequires:	pulseaudio-devel >= 0.9.15
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	udev-devel
Requires(post,postun):	desktop-file-utils
Requires:	ffmpeg-libs >= 3.0
Requires:	glib2 >= 1:2.10.0
Requires:	gsl >= 1.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guvcview is a simple GTK+ interface for capturing and viewing video
from devices supported by the Linux UVC driver.

%description -l pl.UTF-8
guvcview to prosty interfejs GTK+ do przechwytywania i oglądania
obrazu z urządzeń obsługiwanych przez linuksowy sterownik UVC.

%package devel
Summary:	Header files for guvcview libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek guvcview
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-devel
Obsoletes:	guvcview-static < 2.2.1

%description devel
Header files for guvcview libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek guvcview.

%prep
%setup -q -n %{name}-src-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%cmake -B build \
	-DINSTALL_DEVKIT:BOOL=ON
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
%find_lang gview_v4l2core -a %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/guvcview
%attr(755,root,root) %{_libdir}/libgviewaudio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewaudio.so.2
%attr(755,root,root) %{_libdir}/libgviewencoder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewencoder.so.2
%attr(755,root,root) %{_libdir}/libgviewrender.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewrender.so.2
%attr(755,root,root) %{_libdir}/libgviewv4l2core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewv4l2core.so.2
%{_datadir}/appdata/guvcview.appdata.xml
%{_desktopdir}/guvcview.desktop
%{_pixmapsdir}/guvcview.png
%{_mandir}/man1/guvcview.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgviewaudio.so
%attr(755,root,root) %{_libdir}/libgviewencoder.so
%attr(755,root,root) %{_libdir}/libgviewrender.so
%attr(755,root,root) %{_libdir}/libgviewv4l2core.so
%{_includedir}/gviewaudio.h
%{_includedir}/gviewencoder.h
%{_includedir}/gviewrender.h
%{_includedir}/gviewv4l2core.h
%{_pkgconfigdir}/libgviewaudio.pc
%{_pkgconfigdir}/libgviewencoder.pc
%{_pkgconfigdir}/libgviewrender.pc
%{_pkgconfigdir}/libgviewv4l2core.pc
