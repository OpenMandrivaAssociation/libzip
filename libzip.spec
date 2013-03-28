%define	major 2
%define libname	%mklibname zip %{major}
%define develname %mklibname zip -d

Summary:	A C library for reading, creating, and modifying zip archives
Name:		libzip
Version:	0.10.1
Release:	3
Group:		System/Libraries
License:	BSD
URL:		http://www.nih.at/libzip/
Source0:	http://www.nih.at/libzip/%{name}-%{version}.tar.gz
Patch0:		libzip-include.diff
Patch1:		libzip-0.10-php.patch
BuildRequires:	libtool
BuildRequires:	zlib-devel

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
%patch1 -p1 -b .php

%build
#export WANT_AUTOCONF_2_5=1
#rm -f configure
#libtoolize --copy --force; aclocal-1.7; autoconf --force; autoheader; automake-1.7 --foreign
autoreconf -fi
%configure2_5x

%make

#%%check
#make check <- fails at "FAIL: open_nonarchive.test"

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
%doc AUTHORS NEWS README THANKS TODO
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/%{name}/include/zipconf.h
# fugly
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/libzip.pc
%{_mandir}/man3/*


%changelog
* Wed Mar 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-0.1
- 0.10.1 (fixes CVE-2012-1162, CVE-2012-1163)
- added P1 from fedora to add missing functions for php

* Fri May 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.10-3mdv2011.0
+ Revision: 676413
- P0 good place for zipconf.h

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10-2
+ Revision: 662433
- mass rebuild

* Mon Mar 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10-1
+ Revision: 647300
- actually commit all fixes this time...
- 0.10

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-3mdv2011.0
+ Revision: 601065
- rebuild

* Mon Apr 26 2010 Emmanuel Andry <eandry@mandriva.org> 0.9.3-2mdv2010.1
+ Revision: 539363
- apply librairies policy
- doesn't need autotools

* Fri Feb 12 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-1mdv2010.1
+ Revision: 504721
- 0.9.3

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9-3mdv2010.0
+ Revision: 425977
- rebuild

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9-2mdv2009.1
+ Revision: 315646
- rebuild

* Sat Jul 26 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9-1mdv2009.0
+ Revision: 250084
- 0.9

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8-5mdv2009.0
+ Revision: 229719
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8-3mdv2008.1
+ Revision: 169560
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-2mdv2008.0
+ Revision: 89855
- rebuild

* Thu Jun 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdv2008.0
+ Revision: 36504
- 0.8


* Sun Mar 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8-0.20070304.1mdv2007.0
+ Revision: 132044
- new snap (20070304)
- enable the test suite

* Tue Jan 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8-0.20070116.1mdv2007.1
+ Revision: 109377
- use a recent snap (20070116)

* Thu Nov 16 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-5mdv2007.1
+ Revision: 84765
- disable borked tests for now
- bs f*uk
- Import libzip

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-3
- fix deps

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-2mdk
- oops! major bump required

* Fri May 19 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdk
- 0.7.1

* Sun Mar 05 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-1mdk
- initial Mandriva package

