# (tpg) reduce bloat by excluding cmake requires on devel packages
%global __requires_exclude ^cmake.*$

%define	major 5
%define libname %mklibname zip %{major}
%define devname %mklibname zip -d

Summary:	A C library for reading, creating, and modifying zip archives
Name:		libzip
Version:	1.10.0
Release:	1
Group:		System/Libraries
License:	BSD
Url:		https://libzip.org/
Source0:	https://libzip.org/download/%{name}-%{version}.tar.xz
Patch0:		libzip-1.7.3-multi-compilers.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n %{libname}
Summary:	A C library for reading, creating, and modifying zip archives
Group:		System/Libraries

%description -n %{libname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n %{devname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -p1

%build
%global optflags %{optflags} -O3
sed -i -e 's,@LIB@,%{_lib},g' CMakeLists.txt */CMakeLists.txt
%cmake -G Ninja
%ninja

%install
%ninja_install -C build

%files
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptool
%{_mandir}/man1/zipcmp.1*
%{_mandir}/man1/zipmerge.1*
%{_mandir}/man1/ziptool.1*

%files -n %{libname}
%{_libdir}/libzip.so.%{major}*

%files -n %{devname}
%doc AUTHORS THANKS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libzip.pc
%{_mandir}/man3/*
%{_libdir}/cmake/%{name}/libzip-*.cmake
