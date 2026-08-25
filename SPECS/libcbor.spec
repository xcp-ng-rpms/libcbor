Name:		libcbor
Version:	0.11.0
Release:	3.1~xcpng3701.2%{?dist}
Summary:	A CBOR parsing library
%bcond_without xcpng

License:	MIT
URL:		http://libcbor.org
Source0:	https://github.com/PJK/%{name}/archive/v%{version}.tar.gz

BuildRequires:	cmake
# XCP-ng have doxygen, but because we don't have python3-breathe, python3-sphinx,
# python3-sphinx_rtd_theme this package is not needed anymore.
%if %{without xcpng}
BuildRequires:	doxygen
%endif
BuildRequires:	gcc
BuildRequires:	gcc-c++
# XCP-ng does not have python3-breathe, python3-sphinx, python3-sphinx_rtd_theme
%if %{without xcpng}
BuildRequires:	python3-breathe
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
%endif
BuildRequires:	make
BuildRequires:	pkgconfig(cmocka)

%description
libcbor is a C library for parsing and generating CBOR.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel contains development libraries and header files for %{name}.

%prep
%setup -q


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWITH_TESTS=ON
%cmake_build
# XCP-ng don't have the previous BuildRequires, we can't build the documentation.
%if %{without xcpng}
cd doc
make man
%endif


%install
%cmake_install
# XCP-ng can't build the documentation, we will not package it.
%if %{without xcpng}
mkdir -p %{buildroot}%{_mandir}/man3
cp doc/build/man/libcbor.3 %{buildroot}%{_mandir}/man3/
%endif


%check
%ctest


%files
%license LICENSE.md
%doc README.md
# XCP-ng do not support this glob
%if %{without xcpng}
%{_libdir}/libcbor.so.0.11{,.*}
%else
%{_libdir}/libcbor.so.0.11
%{_libdir}/libcbor.so.0.11.*
%endif

%files devel
%{_includedir}/cbor.h
%{_includedir}/cbor
%{_libdir}/libcbor.so
%{_libdir}/pkgconfig/libcbor.pc
%{_libdir}/cmake/libcbor
# XCP-ng does not support this glob & We don't build the documentation
%if %{without xcpng}
%{_mandir}/man3/libcbor.3{,.*}
%endif

%changelog
* Tue Aug 25 2026 Lucas Ravagnier <lucas.ravagnier@vates.tech> - 0.11.0-3.1
- First import of libcbor 0.11.0.3
- Even though we have Doxygen, it isn't enough to build the documentation.
- I removed it because the dependency would be useless.

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 0.11.0-3
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 0.11.0-2
- Bump release for June 2024 mass rebuild

* Sun Feb 04 2024 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.11.0-1
- Update version to 0.11.0 ( resolves: rhbz#2262592 )
- add running of unit tests

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.10.2-3
- Move devel/api manpage to devel package

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.10.2-1
- Update to version 0.10.2 ( resolves: rhbz#1880885 )
- Revise specs per packaging guidelines for globs of soname

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.7.0-8
- Update license to SPDX format
- spec file tidy/modernization
  - use modern cmake build and install
  - properly own include directories in the devel package
  - de-glob some files to follow packaging guidelines

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.7.0-6
- Add missing BR for doxygen

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 20 2020 Kalev Lember <klember@redhat.com> - 0.7.0-2
- Avoid hardcoding man page extension

* Mon Sep 07 2020 Attila Lakatos <alakatos@redhat.com> - 0.7.0-1
- update to 0.7.0
Resolves: rhbz#1813738
Resolves: rhbz#1863978

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-7
- Fix FTBFS, add version for soname, minor cleanups

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 19 2017 Marek Tamaskovic <mtamasko@redhat.com> 0.5.0-1
- Init package.

