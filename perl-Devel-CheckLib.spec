%define upstream_name    Devel-CheckLib
%define upstream_version 1.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Check that a library is available
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/release/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-CheckLib-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::CaptureOutput)
# For tests
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Capture::Tiny)
BuildArch:	noarch

%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc CHANGES META.yml README
%{_bindir}/use-devel-checklib
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/use-devel-checklib.1*
