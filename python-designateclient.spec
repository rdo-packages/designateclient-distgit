%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Client library and command line utility for interacting with Openstack Designate API

%global sname designateclient

%if 0%{?fedora}
%global with_python3 1
%endif

Name:       python-%{sname}
Version:    XXX
Release:    XXX
Summary:    Python API and CLI for OpenStack Designate

License:    ASL 2.0
URL:        https://launchpad.net/python-%{sname}/
Source0:    https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires: git
BuildRequires: openstack-macros

%description
%{common_desc}

%package -n python2-%{sname}
Summary:    Python API and CLI for OpenStack Designate
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pbr

Requires: python2-pbr
Requires: python2-keystoneauth1 >= 3.4.0
Requires: python2-requests >= 2.14.2
Requires: python2-six >= 1.10.0
Requires: python2-stevedore
Requires: python2-osc-lib >= 1.8.0
Requires: python2-debtcollector
Requires: python2-oslo-utils >= 3.33.0
%if 0%{?fedora} > 0
Requires: python2-cliff
Requires: python2-jsonschema >= 2.6.0
%else
Requires: python-cliff
Requires: python-jsonschema >= 2.6.0
%endif

%description -n python2-%{sname}
%{common_desc}


%package -n python2-%{sname}-tests
Summary:    Python API and CLI for OpenStack Designate (tests)
%{?python_provide:%python_provide python2-%{sname}-tests}
Requires:	python2-%{sname} = %{version}-%{release}

%description -n python2-%{sname}-tests
%{common_desc}

This package contains Designate client tests files.


%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:    Python API and CLI for OpenStack Designate
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires: python3-cliff
Requires: python3-jsonschema >= 2.6.0
Requires: python3-pbr
Requires: python3-keystoneauth1 >= 3.4.0
Requires: python3-requests >= 2.14.2
Requires: python3-six >= 1.10.0
Requires: python3-stevedore
Requires: python3-osc-lib >= 1.8.0
Requires: python3-debtcollector
Requires: python3-oslo-utils >= 3.33.0

%description -n python3-%{sname}
%{common_desc}


%package -n python3-%{sname}-tests
Summary:    Python API and CLI for OpenStack Designate (tests)
%{?python_provide:%python_provide python3-%{sname}-tests}
Requires:	python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
%{common_desc}

This package contains Designate client tests files.
%endif


%package doc
Summary:          Documentation for OpenStack Designate API Client

BuildRequires:    python2-sphinx
BuildRequires:    python2-openstackdocstheme
BuildRequires:    python2-keystoneauth1
BuildRequires:    python2-osc-lib
%if 0%{?fedora} > 0
BuildRequires:    python2-jsonschema
%else
BuildRequires:    python-jsonschema
%endif

%description      doc
%{common_desc}

This package contains auto-generated documentation.

%prep
%autosetup -n %{name}-%{upstream_version} -S git

%py_req_cleanup

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
%endif

%py2_install
mv %{buildroot}%{_bindir}/designate %{buildroot}%{_bindir}/designate-%{python2_version}
ln -s ./designate-%{python2_version} %{buildroot}%{_bindir}/designate-2

ln -s ./designate-2 %{buildroot}%{_bindir}/designate


%{__python2} setup.py build_sphinx -b html

%files -n python2-%{sname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/designateclient
%exclude %{python2_sitelib}/%{sname}/tests
%{python2_sitelib}/*.egg-info
%{_bindir}/designate
%{_bindir}/designate-2
%{_bindir}/designate-%{python2_version}

%files -n python2-%{sname}-tests
%{python2_sitelib}/%{sname}/tests

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{sname}
%exclude %{python3_sitelib}/%{sname}/tests
%{python3_sitelib}/*.egg-info
%{_bindir}/designate-3
%{_bindir}/designate-%{python3_version}

%files -n python3-%{sname}-tests
%{python3_sitelib}/%{sname}/tests
%endif

%files doc
%doc doc/build/html
%license LICENSE

%changelog
