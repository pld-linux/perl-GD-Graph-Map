%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Graph-Map
Summary:	GD::Graph::Map Perl module - generate HTML map text for GD::Graph diagrams
Summary(pl):	Modu� Perla GD::Graph::Map - generuj�cy mapy HTML dla diagram�w GD::Graph
Name:		perl-GD-Graph-Map
Version:	1.05
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tgz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD-Graph
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph::Map module generates HTML map text for following GD::Graph
objects: pie, bars, lines, area, point and linespoints. As a result of
its work is created HTML code containing IMG and MAP tags.

%description -l pl
Modu� GD::Graph::Map generuje mapy HTML dla nast�puj�cych obiekt�w
GD::Graph: pie, bars, lines, area, point, linespoints. W wyniku tworzy
kod HTML zawieraj�cy znaczniki IMG i MAP.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%{perl_sitelib}/GD/Graph/Map.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
