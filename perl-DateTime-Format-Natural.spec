%define upstream_name    DateTime-Format-Natural
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Base class for DateTime::Format::Natural::Lang::
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Natural-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Clone)
BuildRequires:	perl(Carp)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Util)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Time::Piece)
BuildRequires:	perl(Term::ReadLine)
BuildRequires:	perl(Test::MockTime)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(boolean)
# not autodetected 
Requires:	perl(boolean)
BuildArch:	noarch

%description
'DateTime::Format::Natural' takes a string with a human readable date/time
and creates a machine readable one by applying natural parsing logic.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/DateTime
%{_bindir}/dateparse
%{_mandir}/man1/dateparse.1*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.960.0-1mdv2011.0
+ Revision: 684740
- update to new version 0.96

* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.950.0-1
+ Revision: 674796
- update to new version 0.95

* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.940.0-1
+ Revision: 650295
- update to new version 0.94

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.930.0-2
+ Revision: 640766
- rebuild to obsolete old packages

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.930.0-1
+ Revision: 636591
- update to new version 0.93

* Mon Jan 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.920.0-1
+ Revision: 634429
- update to new version 0.92

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.910.0-1mdv2011.0
+ Revision: 602041
- new version

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.890.0-1mdv2011.0
+ Revision: 569935
- update to 0.89

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-1mdv2011.0
+ Revision: 553119
- update to 0.88

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.860.0-2mdv2010.1
+ Revision: 543054
- fix Requires

* Wed Apr 21 2010 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.1
+ Revision: 537578
- update to 0.86

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.850.0-1mdv2010.1
+ Revision: 519951
- update to 0.85

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.840.0-1mdv2010.1
+ Revision: 510074
- update to 0.84

* Thu Jan 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.830.0-1mdv2010.1
+ Revision: 491163
- update to 0.83

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.820.0-1mdv2010.1
+ Revision: 480714
- update to 0.82

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.810.0-1mdv2010.1
+ Revision: 471409
- adding missing buildrequires:
- import perl-DateTime-Format-Natural


* Sun Nov 29 2009 cpan2dist 0.81-1mdv
- initial mdv release, generated with cpan2dist

