Summary:	GTK+ base UVC Viewer
Name:		guvcview
Version:	2.0.2
Release:	0.2
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/guvcview/%{name}-src-%{version}.tar.gz
# Source0-md5:	d88a1bcf80c0d989ffcb19d71bdd8c1e
URL:		http://guvcview.sourceforge.net/
Patch0:		link.patch
BuildRequires:	SDL2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gsl-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libpng-devel
BuildRequires:	libv4l-devel
BuildRequires:	portaudio-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guvcview is a simple GTK+ interface for capturing and viewing video
from devices supported by the Linux UVC driver.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1

%build
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/guvcview-2
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la,so}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{bg,fo}
%{__rm} $RPM_BUILD_ROOT%{_localedir}/bs/LC_MESSAGES/gview_v4l2core.mo

%find_lang %{name}
%find_lang gview_v4l2core -a %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgviewaudio-1.1.so.1.0.1
%attr(755,root,root) %{_libdir}/libgviewencoder-1.1.so.1.0.1
%attr(755,root,root) %{_libdir}/libgviewrender-1.1.so.1.0.1
%attr(755,root,root) %{_libdir}/libgviewv4l2core-1.1.so.1.0.1
%attr(755,root,root) %ghost %{_libdir}/libgviewaudio-1.1.so.1
%attr(755,root,root) %ghost %{_libdir}/libgviewencoder-1.1.so.1
%attr(755,root,root) %ghost %{_libdir}/libgviewrender-1.1.so.1
%attr(755,root,root) %ghost %{_libdir}/libgviewv4l2core-1.1.so.1
%{_desktopdir}/guvcview.desktop
%{_pixmapsdir}/guvcview
%{_mandir}/man1/guvcview.1*
