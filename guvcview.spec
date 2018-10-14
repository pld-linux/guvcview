# NOTE: possible switches:
# - sfml rendering (BR: sfml-graphics >= 2.0) instead of SDL2
# - Qt5 gui (BR: Qt5Widgets, qt5-build) instead of gtk+3
# All can be compiled in, selectable at runtime.
Summary:	GTK+ based UVC Viewer
Summary(pl.UTF-8):	Przeglądarka UVC oparta na GTK+
Name:		guvcview
Version:	2.0.6
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/guvcview/%{name}-src-%{version}.tar.gz
# Source0-md5:	ea35acb3a97952ceca26d92478b6e7ea
URL:		http://guvcview.sourceforge.net/
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 3.0
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gsl-devel >= 1.15
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	libv4l-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
BuildRequires:	pulseaudio-devel >= 0.9.15
BuildRequires:	udev-devel
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

%description devel
Header files for guvcview libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek guvcview.

%package static
Summary:	Static guvcview libraries
Summary(pl.UTF-8):	Statyczne biblioteki guvcview
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static guvcview libraries.

%description static -l pl.UTF-8
Statyczne biblioteki guvcview.

%prep
%setup -q -n %{name}-src-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-debian-menu \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgview*.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}
%find_lang gview_v4l2core -a %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/guvcview
%attr(755,root,root) %{_libdir}/libgviewaudio-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewaudio-2.0.so.2
%attr(755,root,root) %{_libdir}/libgviewencoder-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewencoder-2.0.so.2
%attr(755,root,root) %{_libdir}/libgviewrender-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewrender-2.0.so.2
%attr(755,root,root) %{_libdir}/libgviewv4l2core-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgviewv4l2core-2.0.so.2
%{_datadir}/appdata/guvcview.appdata.xml
%{_desktopdir}/guvcview.desktop
%{_pixmapsdir}/guvcview
%{_mandir}/man1/guvcview.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgviewaudio.so
%attr(755,root,root) %{_libdir}/libgviewencoder.so
%attr(755,root,root) %{_libdir}/libgviewrender.so
%attr(755,root,root) %{_libdir}/libgviewv4l2core.so
%{_includedir}/guvcview-2
%{_pkgconfigdir}/libgviewaudio.pc
%{_pkgconfigdir}/libgviewencoder.pc
%{_pkgconfigdir}/libgviewrender.pc
%{_pkgconfigdir}/libgviewv4l2core.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgviewaudio.a
%{_libdir}/libgviewencoder.a
%{_libdir}/libgviewrender.a
%{_libdir}/libgviewv4l2core.a
