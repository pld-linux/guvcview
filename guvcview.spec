Summary:	GTK+ base UVC Viewer
#Summary(pl.UTF-8):	-
Name:		guvcview
Version:	1.4.4
Release:	0.1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://download.berlios.de/guvcview/%{name}-src-%{version}.tar.gz
# Source0-md5:	5a71d271c23476bdec3c7ae32dc7b0ca
URL:		http://guvcview.berlios.de/
BuildRequires:	ffmpeg-devel
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	libpng-devel
BuildRequires:	libv4l-devel
BuildRequires:	portaudio-devel
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guvcview is a simple GTK+ interface for capturing and viewing video
from devices supported by the Linux UVC driver.

#%description -l pl.UTF-8

%prep
%setup -q -n %{name}-src-%{version}

%build
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
