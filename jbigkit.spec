#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	JBIG-KIT lossless image compression library
Summary(pl.UTF-8):	JBIG-KIT - biblioteka do bezstratnej kompresji obrazków
Name:		jbigkit
Version:	2.1
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://www.cl.cam.ac.uk/~mgk25/jbigkit/download/%{name}-%{version}.tar.gz
# Source0-md5:	ebcf09bed9f14d7fa188d3bd57349522
Source1:	%{name}.pl.po
Patch0:		%{name}-shared.patch
URL:		http://www.cl.cam.ac.uk/~mgk25/jbigkit/
BuildRequires:	gettext-tools
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JBIG-KIT implements a highly effective data compression algorithm for
bi-level high-resolution images such as fax pages or scanned
documents.

%description -l pl.UTF-8
JBIG-KIT zawiera implementację wydajnego algorytmu kompresji dla
2-kolorowych obrazków wysokiej rozdzielczości, takich jak faksy albo
skanowane dokumenty.

%package devel
Summary:	JBIG-KIT - development part
Summary(pl.UTF-8):	JBIG-KIT - plik nagłówkowy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file needed to build programs using JBIG library.

%description devel -l pl.UTF-8
Plik nagłówkowy potrzebny do kompilacji programów korzystających z
biblioteki JBIG.

%package static
Summary:	JBIG-KIT - static library
Summary(pl.UTF-8):	JBIG-KIT - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static JBIG library.

%description static -l pl.UTF-8
Statyczna biblioteka JBIG.

%package progs
Summary:	JBIG-KIT - conversion utilities
Summary(pl.UTF-8):	JBIG-KIT - programy do konwersji
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Package contains utilities to convert between JBIG and PBM images.

%description progs -l pl.UTF-8
Narzędzia do konwersji plików między formatami JBIG i PBM.

%prep
%setup -q
%patch0 -p1

cp %{SOURCE1} libjbig/po/pl.po

%build
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	prefix=%{_prefix} \
	libdir=%{_libdir}

for l in libjbig/po/*.po ; do
	msgfmt -c -v -o "${l%.po}.mo" "$l"
done

%{?with_tests:%{__make} -j1 test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir}

for l in libjbig/po/*.mo ; do
	install -D "$l" "$RPM_BUILD_ROOT%{_datadir}/locale/$(basename $l .mo)/LC_MESSAGES/jbig.mo"
done

%find_lang jbig

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f jbig.lang
%defattr(644,root,root,755)
# INSTALL is about "installing and using" jbigkit
%doc ANNOUNCE CHANGES INSTALL TODO
%attr(755,root,root) %{_libdir}/libjbig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjbig.so.2
%attr(755,root,root) %{_libdir}/libjbig85.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjbig85.so.2

%files devel
%defattr(644,root,root,755)
%doc libjbig/{jbig,jbig85}.txt
%attr(755,root,root) %{_libdir}/libjbig.so
%attr(755,root,root) %{_libdir}/libjbig85.so
%{_libdir}/libjbig.la
%{_libdir}/libjbig85.la
%{_includedir}/jbig.h
%{_includedir}/jbig85.h
%{_includedir}/jbig_ar.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjbig.a
%{_libdir}/libjbig85.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jbgtopbm
%attr(755,root,root) %{_bindir}/pbmtojbg
%{_mandir}/man1/jbgtopbm.1*
%{_mandir}/man1/pbmtojbg.1*
