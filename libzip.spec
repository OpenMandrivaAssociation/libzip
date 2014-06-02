%define	major 2
%define libname %mklibname zip %{major}
%define devname %mklibname zip -d

Summary:	A C library for reading, creating, and modifying zip archives
Name:		libzip
Version:	0.11.2
Release:	1
Group:		System/Libraries
License:	BSD
Url:		http://www.nih.at/libzip/
Source0:	http://www.nih.at/libzip/%{name}-%{version}.tar.xz
Patch0:		libzip-0.10-fix_pkgconfig.patch
Patch1:		libzip-0.10_rc1-fix_headers.patch
Patch2:		libzip-0.10-php.patch
Patch3:		libzip-0.10.1-long-crc.patch
Patch4:		libzip-0.10.1-automake-1.13.patch
BuildRequires:	libtool
BuildRequires:	libtool
BuildRequires:	pkgconfig(zlib)

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n	%{libname}
Summary:	A C library for reading, creating, and modifying zip archives
Group:          System/Libraries

%description -n	%{libname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n	%{devname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure

%make

%install
INSTALL_HEADER=%{_includedir} %makeinstall_std

%files
%doc AUTHORS NEWS README THANKS TODO
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptorrent
%{_mandir}/man1/zipcmp.1*
%{_mandir}/man1/zipmerge.1*
%{_mandir}/man1/ziptorrent.1*

%files -n %{libname}
%{_libdir}/libzip.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README THANKS TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libzip.pc
%{_mandir}/man3/*

