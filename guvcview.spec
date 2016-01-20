Summary:	GTK+ base UVC Viewer
Name:		guvcview
Version:	2.0.2
Release:	0.1
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO.tasks
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/guvcview.desktop
%{_pixmapsdir}/guvcview
%{_mandir}/man1/guvcview.1*
