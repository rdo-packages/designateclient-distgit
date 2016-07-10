%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname designateclient

%if 0%{?fedora}
%global with_python3 1
%endif

Name:       python-%{sname}
Version:    XXX
Release:    XXX
Summary:    Python API and CLI for OpenStack Designate

License:    ASL 2.0
URL:        http://launchpad.net/python-%{sname}/
Source0:    http://tarballs.openstack.org/python-%{sname}/%{name}/%{name}-%{version}.tar.gz

BuildArch:  noarch

%description
Client library and command line utility for interacting with Openstack Designate API

%package -n python2-%{sname}
Summary:    Python API and CLI for OpenStack Designate
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr

Requires: python-cliff
Requires: python-jsonschema >= 2.0.0
Requires: python-pbr
Requires: python-keystoneauth1
Requires: python-requests >= 2.2.0
Requires: python-six >= 1.9.0
Requires: python-stevedore
Requires: python-osc-lib
Requires: python-debtcollector
Requires: python-oslo-utils

%description -n python2-%{sname}
Client library and command line utility for interacting with Openstack Designate API

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:    Python API and CLI for OpenStack Designate
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires: python3-cliff
Requires: python3-jsonschema >= 2.0.0
Requires: python3-pbr
Requires: python3-keystoneauth1
Requires: python3-requests >= 2.2.0
Requires: python3-six >= 1.9.0
Requires: python3-stevedore
Requires: python3-osc-lib
Requires: python3-debtcollector
Requires: python3-oslo-utils

%description -n python3-%{sname}
Client library and command line utility for interacting with Openstack Designate API
%endif

%package doc
Summary:          Documentation for OpenStack Designate API Client

BuildRequires:    python-sphinx
BuildRequires:    python-oslo-sphinx

%description      doc
Client library and command line utility for interacting with Openstack Designate API

This package contains auto-generated documentation.

%prep
%setup -q -n %{name}-%{upstream_version}

rm -rf {,test-}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/designate %{buildroot}%{_bindir}/designate-%{python3_version}
ln -s ./designate-%{python3_version} %{buildroot}%{_bindir}/designate-3
# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/designateclient/tests
%endif

%py2_install
mv %{buildroot}%{_bindir}/designate %{buildroot}%{_bindir}/designate-%{python2_version}
ln -s ./designate-%{python2_version} %{buildroot}%{_bindir}/designate-2

ln -s ./designate-2 %{buildroot}%{_bindir}/designate

# Delete tests
rm -fr %{buildroot}%{python2_sitelib}/designateclient/tests


export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

%files -n python2-%{sname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/designateclient
%{python2_sitelib}/*.egg-info
%{_bindir}/designate
%{_bindir}/designate-2
%{_bindir}/designate-%{python2_version}

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/*.egg-info
%{_bindir}/designate-3
%{_bindir}/designate-%{python3_version}
%endif

%files doc
%doc html
%license LICENSE

%changelog
