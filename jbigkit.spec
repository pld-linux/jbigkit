#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	JBIG-KIT lossless image compression library
Summary(pl):	JBIG-KIT - biblioteka do bezstratnej kompresji obrazków
Name:		jbigkit
Version:	1.6
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://www.cl.cam.ac.uk/~mgk25/download/%{name}-%{version}.tar.gz
# Source0-md5:	ce196e45f293d40ba76af3dc981ccfd7
Patch0:		%{name}-shared.patch
Patch1:		%{name}-Makefiles.patch
URL:		http://www.cl.cam.ac.uk/~mgk25/jbigkit/
BuildRequires:	libtool >= 2:1.4e
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JBIG-KIT implements a highly effective data compression algorithm for
bi-level high-resolution images such as fax pages or scanned
documents.

%description -l pl
JBIG-KIT zawiera implementacjê wydajnego algorytmu kompresji dla
2-kolorowych obrazków wysokiej rozdzielczo¶ci, takich jak faksy albo
skanowane dokumenty.

%package devel
Summary:	JBIG-KIT - development part
Summary(pl):	JBIG-KIT - plik nag³ówkowy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file needed to build programs using JBIG library.

%description devel -l pl
Plik nag³ówkowy potrzebny do kompilacji programów korzystaj±cych z
biblioteki JBIG.

%package static
Summary:	JBIG-KIT - static library
Summary(pl):	JBIG-KIT - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static JBIG library.

%description static -l pl
Statyczna biblioteka JBIG.

%package progs
Summary:	JBIG-KIT - conversion utilities
Summary(pl):	JBIG-KIT - programy do konwersji
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Package contains utilities to convert between JBIG and PBM images.

%description progs -l pl
Narzêdzia do konwersji plików miêdzy formatami JBIG i PBM.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	CFLAGS="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# INSTALL is about "installing and using" jbigkit
%doc ANNOUNCE CHANGES INSTALL TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc libjbig/jbig.doc
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
