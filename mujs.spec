Name:           mujs
Version:        1.3.3
Release:        1
Summary:        An embeddable Javascript interpreter
License:        AGPLv3+
URL:            http://mujs.com/
Source0:        https://mujs.com/downloads/%{name}-%{version}.tar.gz
BuildRequires:  readline-devel
Group:		System/Libraries

%description
MuJS is a lightweight Javascript interpreter designed for embedding in
other software to extend them with scripting capabilities.

%package devel
Summary:        MuJS development files
Provides:       %{name}-static = %{version}-%{release}
Group:		Development/Libraries

%description devel
This package provides the MuJS static library.

%prep
%setup -q -n %{name}-%{version}
chmod a-x -v docs/*

%build
%make_build debug %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}"

%install
make install DESTDIR=%{buildroot} prefix="%{_prefix}" libdir="%{_libdir}" \
 CFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}"

%global _docdir_fmt %{name}

%files
%license COPYING
%doc AUTHORS README docs
%{_bindir}/%{name}
%{_bindir}/%{name}-pp

%files devel
%license COPYING
%doc AUTHORS README
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a
