%define upstream_name    DateTime-Format-Natural
%define upstream_version 0.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Base class for DateTime::Format::Natural::Lang::
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(DateTime)
BuildRequires: perl(Exporter)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable)
BuildRequires: perl(Time::Piece)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Test::MockTime)
BuildRequires: perl(Test::More)
BuildRequires: perl(boolean)
# not autodetected 
Requires: perl(boolean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'DateTime::Format::Natural' takes a string with a human readable date/time
and creates a machine readable one by applying natural parsing logic.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/DateTime
%{_bindir}/dateparse
%{_mandir}/man1/dateparse.1*
