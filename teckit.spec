Name:           teckit
Version:        2.5.1
Release:        4.1%{?dist}
Summary:        Conversion library and mapping compiler
License:        LGPLv2+ or CPL
Group:          Development/Libraries
URL:            http://scripts.sil.org/teckit
Source0:        http://scripts.sil.org/svn-view/teckit/TAGS/TECkit_2_5_1.tar.gz
BuildRequires:  expat-devel zlib-devel libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0:         TECkit_2_5_1-includes.patch

%description
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%package devel
Summary:        Conversion library and mapping compiler
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description devel
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%prep
%setup -q -n TECkit_2_5_1
%patch0 -p1 -b .includes

%{__chmod} 0755 ./autogen.sh
%{__chmod} 0755 ./configure
%{__rm} -r zlib*

%build
./autogen.sh
%configure --disable-static
make %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{_libdir}/*.la

%check
make check

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING INSTALL NEWS README
%doc license/{LICENSING.txt,License_CPLv05.txt,License_LGPLv21.txt}
%attr(0755,root,root) %{_bindir}/sfconv
%attr(0755,root,root) %{_bindir}/teckit_compile
%attr(0755,root,root) %{_bindir}/txtconv
%attr(0755,root,root) %{_libdir}/libTECkit.so.*
%attr(0755,root,root) %{_libdir}/libTECkit_Compiler.so.*

%files devel
%defattr(0644,root,root,0755)
%doc docs/*.pdf
%{_includedir}/teckit/
%{_libdir}/libTECkit.so
%{_libdir}/libTECkit_Compiler.so

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.5.1-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 2.5.1-3
- include stdio.h for sprintf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Jindrich Novy <jnovy@redhat.com> 2.5.1-1
- update to 2.5.1

* Tue Jan 08 2008 Jindrich Novy <jnovy@redhat.com> 2.2.1-3
- gcc-4.3 fixes

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 2.2.1-2
- update License
- rebuild for ppc32

* Tue Jul 17 2007 Jindrich Novy <jnovy@redhat.com> 2.2.1-1
- first Fedora build

* Wed Jul 11 2007 Jindrich Novy <jnovy@redhat.com> 2.2.1-0.3
- add missing licenses as documentation

* Wed Jul 11 2007 Jindrich Novy <jnovy@redhat.com> 2.2.1-0.2
- review fixes (#247615)
- add libtool BR
- enable parallel build
- fix filelist
- run ldconfig in post

* Tue Jul 10 2007 Jindrich Novy <jnovy@redhat.com> 2.2.1-0.1
- port TECkit to Fedora
- remove static libs

* Fri Jun 22 2007 David Walluck <walluck@mandriva.org> 2.2.1-3mdv2008.0
+ Revision: 42653
- workaround broken fix-eol rpm-helper script
- bump release
- BuildRequires: libexpat-devel
- Import teckit

* Thu Jun 21 2007 David Walluck <walluck@mandriva.org> 0:2.2.1-1mdv2008.0
- release
