Summary:	JBIG-KIT lossless image compression library
Summary(pl):	JBIG-KIT - biblioteka do bezstratnej kompresji obrazkÛw
Name:		jbigkit
Version:	1.2
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.informatik.uni-erlangen.de/pub/doc/ISO/JBIG/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
URL:		http://www.jpeg.org/public/jbighomepage.htm
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JBIG-KIT implements a highly effective data compression algorithm for
bi-level high-resolution images such as fax pages or scanned
documents.

%description -l pl
JBIG-KIT zawiera implementacjÍ wydajnego algorytmu kompresji dla
2-kolorowych obrazkÛw wysokiej rozdzielczo∂ci, takich jak faksy albo
skanowane dokumenty.

%package devel
Summary:	JBIG-KIT - development part
Summary(pl):	JBIG-KIT - plik nag≥Ûwkowy
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header file needed to build programs using JBIG library.

%description devel -l pl
Plik nag≥Ûwkowy potrzebny do kompilacji programÛw korzystaj±cych z
biblioteki JBIG.

%package static
Summary:	JBIG-KIT - static library
Summary(pl):	JBIG-KIT - biblioteka statyczna
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static JBIG library.

%description static -l pl
Statyczna biblioteka JBIG.

%package progs
Summary:	JBIG-KIT - conversion utilities
Summary(pl):	JBIG-KIT - programy do konwersji
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	AplicaÁıes/Gr·ficos
Requires:	%{name} = %{version}

%description progs
Package contains utilities to convert between JBIG and PBM images.

%description progs -l pl
NarzÍdzia do konwersji plikÛw miÍdzy formatami JBIG i PBM.

%prep
%setup -q -n %{name}
%patch0 -p1

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
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
