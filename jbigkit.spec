Summary:	JBIG-KIT lossless image compression library
Summary(pl):	JBIG-KIT - biblioteka do bezstratnej kompresji obrazk�w
Name:		jbigkit
Version:	1.2
Release:	3
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.informatik.uni-erlangen.de/pub/doc/ISO/JBIG/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-libtool.patch
URL:		http://www.jpeg.org/public/jbighomepage.htm
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JBIG-KIT implements a highly effective data compression algorithm for
bi-level high-resolution images such as fax pages or scanned
documents.

%description -l pl
JBIG-KIT zawiera implementacj� wydajnego algorytmu kompresji dla
2-kolorowych obrazk�w wysokiej rozdzielczo�ci, takich jak faksy albo
skanowane dokumenty.

%package devel
Summary:	JBIG-KIT - development part
Summary(pl):	JBIG-KIT - plik nag��wkowy
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header file needed to build programs using JBIG library.

%description devel -l pl
Plik nag��wkowy potrzebny do kompilacji program�w korzystaj�cych z
biblioteki JBIG.

%package static
Summary:	JBIG-KIT - static library
Summary(pl):	JBIG-KIT - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static JBIG library.

%description static -l pl
Statyczna biblioteka JBIG.

%package progs
Summary:	JBIG-KIT - conversion utilities
Summary(pl):	JBIG-KIT - programy do konwersji
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
Package contains utilities to convert between JBIG and PBM images.

%description progs -l pl
Narz�dzia do konwersji plik�w mi�dzy formatami JBIG i PBM.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} CCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ANNOUNCE TODO libjbig/jbig.doc

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz libjbig/*.gz
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
