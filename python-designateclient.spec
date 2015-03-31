%global service designate
%global common_desc Client library and command line utility for interacting with Openstack Designate API

Name:       python-%{service}client
Version:    XXX
Release:    XXX{?dist}
Summary:    Python API and CLI for OpenStack Designate

License:    ASL 2.0
URL:        http://launchpad.net/python-%{service}client/
Source0:    https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-d2to1

# TODO: Delorean does not provide proper version yet
Requires: python-cliff
#Requires: python-cliff >= 1.10.0
Requires: python-jsonschema >= 2.0.0
Requires: python-pbr
Requires: python-keystoneclient >= 1.1.0
Requires: python-requests >= 2.2.0
Requires: python-six >= 1.9.0
# TODO: Delorean does not provide proper version yet
Requires: python-stevedore
#Requires: python-stevedore >= 1.3.0


%description
%{common_desc}


%package tests
Summary:	Designate client tests
Requires:	%{name} = %{version}-%{release}


%description tests
%{common_desc}

This package contains Designate client test files.


%prep
%setup -q -n %{name}-%{upstream_version}


%build
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py build


%check
# TODO: add unit test run as a build step


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%license LICENSE
%doc README.rst
%{_bindir}/%{service}
%{python2_sitelib}/%{service}client
%{python2_sitelib}/python_%{service}client-*.egg-info
%exclude %{python2_sitelib}/%{service}client/tests


%files tests
%license LICENSE
%{python2_sitelib}/%{service}client/tests


%changelog
