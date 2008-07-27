#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PHP
%define		pnam	Serialization
Summary:	PHP::Serialization - converting between PHP's serialize() output and Perl memory structure equivalent
Summary(pl.UTF-8):	PHP::Serialization - konwersja między wyjściem serialize() z PHP i odpowiednikiem perlowych struktur w pamięci
Name:		perl-PHP-Serialization
Version:	0.27
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2fb3f63071c5c2119b4eebe39b329684
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a simple, quick means of serializing Perl memory structures
(including object data!) into a format that PHP can deserialize() and
access, and vice versa.

NOTE: Converts PHP arrays into Perl Arrays when the PHP array used
exclusively numeric indexes, and into Perl Hashes when the PHP array
did not.

%description -l pl.UTF-8
Ten moduł dostarcza proste, szybkie środki do serializacji struktur
perlowych w pamięci (włącznie z danymi obiektów!) na format nadający
się do dostępu i deserialize() w PHP oraz w drugą stronę.

UWAGA: konwertuje tablice PHP na tablice perlowe, kiedy tablica PHP
używa wyłącznie numerycznych indeksów, a na perlowe tablice
asocjacyjne w przeciwnym wypadku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/PHP/*.pm
%{_mandir}/man3/*
