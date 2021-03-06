%define		pdir	GD
%define		pnam	Graph-Map
Summary:	GD::Graph::Map Perl module - generate HTML map text for GD::Graph diagrams
Summary(pl.UTF-8):	Moduł Perla GD::Graph::Map - generowanie mapy HTML dla diagramów GD::Graph
Name:		perl-GD-Graph-Map
Version:	1.05
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tgz
# Source0-md5:	cd9019ac7ed29e37fab6707ce0c10aef
URL:		http://search.cpan.org/dist/GD-Graph-Map/
BuildRequires:	perl-GD-Graph
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph::Map module generates HTML map text for following GD::Graph
objects: pie, bars, lines, area, point and linespoints. As a result of
its work is created HTML code containing IMG and MAP tags.

%description -l pl.UTF-8
Moduł GD::Graph::Map generuje mapy HTML dla następujących obiektów
GD::Graph: pie, bars, lines, area, point, linespoints. W wyniku tworzy
kod HTML zawierający znaczniki IMG i MAP.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%{perl_vendorlib}/GD/Graph/Map.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
