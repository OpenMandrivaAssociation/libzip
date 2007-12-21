%define	major 1
%define libname	%mklibname zip %{major}

Summary:	A C library for reading, creating, and modifying zip archives
Name:		libzip
Version:	0.8
Release:	%mkrel 2
Group:		System/Libraries
License:	BSD
URL:		http://www.nih.at/libzip/
Source0:	http://www.nih.at/libzip/%{name}-%{version}.tar.gz
BuildRequires:	libtool
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Obsoletes:	%{mklibname zip 0}-devel

%description -n	%{libname}-devel
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

This package contains the static %{name} library and its header files.

%prep

%setup -q -n %{name}-%{version}

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal-1.7; autoconf --force; autoheader; automake-1.7 --foreign

%configure2_5x

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_mandir}/man1/zipcmp.1*
%{_mandir}/man1/zipmerge.1*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/libzip.pc
%{_mandir}/man3/*
