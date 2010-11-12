%define upstream_name    Devel-CheckLib
%define upstream_version 0.9

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Check that a library is available
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::CaptureOutput)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

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
%doc CHANGES META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/use-devel-checklib
/usr/share/man/man1/use-devel-checklib.1.xz

