%define upstream_name    Devel-CheckLib
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Check that a library is available
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-CheckLib-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::CaptureOutput)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

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
%doc CHANGES META.yml README
%{_bindir}/use-devel-checklib
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/use-devel-checklib.1.xz

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.930.0-1mdv2011.0
+ Revision: 654063
- update to new version 0.93

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.920.0-1mdv2011.0
+ Revision: 622681
- update to new version 0.92

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.910.0-1mdv2011.0
+ Revision: 601873
- update to new version 0.91

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1mdv2011.0
+ Revision: 596522
- update to new version 0.9

* Tue Nov 09 2010 Shlomi Fish <shlomif@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 595433
- import perl-Devel-CheckLib


