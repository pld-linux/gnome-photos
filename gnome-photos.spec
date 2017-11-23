Summary:	Access, organize and share your photos on GNOME
Summary(pl.UTF-8):	Dostęp do zdjęć, organizowanie i współdzielenie ich w środowisku GNOME
Name:		gnome-photos
Version:	3.26.2
Release:	3
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-photos/3.26/%{name}-%{version}.tar.xz
# Source0-md5:	80a815e50a55ffe800d5b31b715aea07
URL:		https://live.gnome.org/GnomePhotos
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	babl-devel
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	cairo-gobject-devel >= 1.14.0
BuildRequires:	desktop-file-utils
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gegl-devel >= 0.3.15
BuildRequires:	geocode-glib-devel
BuildRequires:	gettext-tools
BuildRequires:	gexiv2-devel
BuildRequires:	gfbgraph-devel >= 0.2.1
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gnome-online-accounts-devel >= 3.8.0
BuildRequires:	grilo-devel >= 0.3.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.22.16
BuildRequires:	lcms2-devel
BuildRequires:	libexif-devel >= 0.6.14
BuildRequires:	libgdata-devel >= 0.16.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.6
BuildRequires:	librsvg-devel >= 2.26.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tracker-devel >= 2.0.0
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	cairo >= 1.14.0
Requires:	cairo-gobject >= 1.14.0
Requires:	gegl >= 0.3.15
Requires:	gfbgraph >= 0.2.1
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-online-accounts-libs >= 3.8.0
Requires:	gtk+3 >= 3.22.16
Requires:	libgdata >= 0.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Photos is an application to access, organize and share your photos
with GNOME 3.

%description -l pl.UTF-8
Photos to aplikacja pozwalająca na dostęp do swoich zdjęć,
organizowanie i współdzielenie ich przy użyciu środowiska GNOME 3.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_libexecdir}/gnome-photos-thumbnailer
%{_datadir}/appdata/org.gnome.Photos.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Photos.service
%{_datadir}/glib-2.0/schemas/org.gnome.photos.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Photos.search-provider.ini
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/org.gnome.Photos.desktop
