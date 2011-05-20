%define	major 2
%define libname	%mklibname zip %{major}
%define develname %mklibname zip -d

Summary:	A C library for reading, creating, and modifying zip archives
Name:		libzip
Version:	0.10
Release:	%mkrel 3
Group:		System/Libraries
License:	BSD
URL:		http://www.nih.at/libzip/
Source0:	http://www.nih.at/libzip/%{name}-%{version}.tar.gz
Patch0:		libzip-include.diff
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Obsoletes:	%{mklibname zip 1}-devel

%description -n	%{develname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

This package contains the static %{name} library and its header files.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 -b .include

%build
#export WANT_AUTOCONF_2_5=1
#rm -f configure
#libtoolize --copy --force; aclocal-1.7; autoconf --force; autoheader; automake-1.7 --foreign

%configure2_5x

%make

#%%check
#make check <- fails at "FAIL: open_nonarchive.test"

%install
rm -rf %{buildroot}

INSTALL_HEADER=%{_includedir} %makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptorrent
%{_mandir}/man1/zipcmp.1*
%{_mandir}/man1/zipmerge.1*
%{_mandir}/man1/ziptorrent.1*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
# fugly
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/libzip.pc
%{_mandir}/man3/*
