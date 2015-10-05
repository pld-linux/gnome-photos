Summary:	Access, organize and share your photos on GNOME
Name:		gnome-photos
Version:	3.18.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-photos/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	8498c977cfbbc6b38d2acaf29691e7a4
URL:		https://live.gnome.org/GnomePhotos
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	babl-devel
BuildRequires:	cairo-devel
BuildRequires:	cairo-gobject-devel
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gegl-devel
BuildRequires:	gettext-tools
BuildRequires:	gfbgraph-devel > 0.2.1
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-online-accounts-devel >= 3.8.0
BuildRequires:	grilo-devel >= 0.2.6
BuildRequires:	gtk+3-devel >= 3.11.5
BuildRequires:	intltool >= 0.50.1
BuildRequires:	lcms2-devel
BuildRequires:	libexif-devel >= 0.6.14
BuildRequires:	libgdata-devel >= 0.16.0
BuildRequires:	librsvg-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tracker-devel >= 1.0.0
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.11.5
Requires:	libgdata >= 0.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Photos is an application to access, organize and share your photos
with GNOME 3.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ARTISTS AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-photos
%{_datadir}/appdata/org.gnome.Photos.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Photos.service
%{_datadir}/glib-2.0/schemas/org.gnome.photos.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Photos.search-provider.ini
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/org.gnome.Photos.desktop
