%define		gitcommit	a18ca48

Summary:	Python macros, which simplifies creation of RPM packages with Python software
Summary(pl.UTF-8):	Makra ułatwiające tworzenie pakietów RPM z programami napisanymi w Pythonie
Name:		python-rpm-packaging
Version:	1
Release:	2
License:	GPL v2
Group:		Base
Source0:	https://github.com/rpm-software-management/python-rpm-packaging/archive/%{gitcommit}/%{name}-%{version}.tar.gz
# Source0-md5:	915891c1e0d04b6fc77d258b6201c181
Patch0:		x32.patch
Patch1:		noarch.patch
URL:		https://github.com/rpm-software-management/python-rpm-packaging
BuildRequires:	rpm-build >= 4.6
Requires:	python3
Requires:	python3-modules
Requires:	python3-packaging
Requires:	rpm
Provides:	rpm-pythonprov = 1:4.17
Obsoletes:	rpm-pythonprov < 1:4.17
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_rpmlibdir /usr/lib/rpm

%description
Python macros, which simplifies creation of RPM packages with Python
software.

%description -l pl.UTF-8
Makra ułatwiające tworzenie pakietów RPM z programami napisanymi w
Pythonie.

%prep
%setup -q -c
%{__mv} %{name}-%{gitcommit}*/* .
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '1s,/usr/bin/python,%{__python3},' scripts/pythondistdeps.py

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_rpmlibdir}/fileattrs

cp -p fileattrs/*.attr $RPM_BUILD_ROOT%{_rpmlibdir}/fileattrs
cp -p scripts/pythondistdeps.py $RPM_BUILD_ROOT%{_rpmlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_rpmlibdir}/pythondistdeps.py
%{_rpmlibdir}/fileattrs/python.attr
%{_rpmlibdir}/fileattrs/pythondist.attr
