Summary:	Access, organize and share your photos on GNOME
Summary(pl.UTF-8):	Dostęp do zdjęć, organizowanie i współdzielenie ich w środowisku GNOME
Name:		gnome-photos
Version:	3.38.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/gnome-photos/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	96f87446e960eff4e7d0a4a112181f6b
URL:		https://wiki.gnome.org/Apps/Photos
BuildRequires:	babl-devel
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	cairo-gobject-devel >= 1.14.0
BuildRequires:	dbus-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.36.8
BuildRequires:	gegl-devel >= 0.4.0
BuildRequires:	geocode-glib-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gexiv2-devel >= 0.10.8
BuildRequires:	gfbgraph-devel >= 0.2.1
BuildRequires:	glib2-devel >= 1:2.57.2
BuildRequires:	gnome-online-accounts-devel >= 3.8.0
BuildRequires:	grilo-devel >= 0.3.5
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.22.16
BuildRequires:	libdazzle-devel >= 3.26.0
BuildRequires:	libexif-devel >= 0.6.14
BuildRequires:	libgdata-devel >= 0.16.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.6
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 2.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.57.2
Requires:	cairo >= 1.14.0
Requires:	cairo-gobject >= 1.14.0
Requires:	gdk-pixbuf2 >= 2.36.8
Requires:	gegl >= 0.4.0
Requires:	gexiv2 >= 0.10.8
Requires:	gfbgraph >= 0.2.1
Requires:	glib2 >= 1:2.57.2
Requires:	gnome-online-accounts-libs >= 3.8.0
Requires:	grilo >= 0.3.5
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.22.16
Requires:	libdazzle >= 3.26.0
Requires:	libgdata >= 0.16.0
Requires:	tracker >= 2.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ARTISTS AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-photos
%attr(755,root,root) %{_libexecdir}/gnome-photos-thumbnailer
%dir %{_libdir}/gnome-photos
%attr(755,root,root) %{_libdir}/gnome-photos/libgnome-photos.so
%{_datadir}/dbus-1/services/org.gnome.Photos.service
%{_datadir}/dbus-1/services/org.gnome.Photos.Tracker1.service
%{_datadir}/dbus-1/services/org.gnome.Photos.Tracker1.Miner.Extract.service
%{_datadir}/dbus-1/services/org.gnome.Photos.Tracker1.Miner.Files.service
%{_datadir}/glib-2.0/schemas/org.gnome.photos.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Photos.search-provider.ini
%{_datadir}/metainfo/org.gnome.Photos.appdata.xml
%{_datadir}/tracker/domain-ontologies/org.gnome.Photos.rule
%{_datadir}/tracker/miners/org.gnome.Photos.Tracker1.Miner.Extract.service
%{_datadir}/tracker/miners/org.gnome.Photos.Tracker1.Miner.Files.service
%{_desktopdir}/org.gnome.Photos.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Photos.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Photos-symbolic.svg
