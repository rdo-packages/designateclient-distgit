
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global common_desc \
Client library and command line utility for interacting with Openstack Designate API

%global sname designateclient

Name:       python-%{sname}
Version:    4.1.0
Release:    1%{?dist}
Summary:    Python API and CLI for OpenStack Designate

License:    ASL 2.0
URL:        https://launchpad.net/python-%{sname}/
Source0:    https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires: git
BuildRequires: openstack-macros

%description
%{common_desc}

%package -n python3-%{sname}
Summary:    Python API and CLI for OpenStack Designate
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires: python3-pbr
Requires: python3-keystoneauth1 >= 3.4.0
Requires: python3-requests >= 2.14.2
Requires: python3-six >= 1.10.0
Requires: python3-stevedore
Requires: python3-osc-lib >= 1.8.0
Requires: python3-debtcollector
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-cliff
Requires: python3-jsonschema >= 2.6.0

%description -n python3-%{sname}
%{common_desc}


%package -n python3-%{sname}-tests
Summary:    Python API and CLI for OpenStack Designate (tests)
%{?python_provide:%python_provide python3-%{sname}-tests}
Requires:	python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
%{common_desc}

This package contains Designate client tests files.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Designate API Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-keystoneauth1
BuildRequires:    python3-osc-lib
BuildRequires:    python3-jsonschema
BuildRequires:    python3-oslo-serialization

%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
%autosetup -n %{name}-%{upstream_version} -S git

%py_req_cleanup

%build
%{py3_build}

%if 0%{?with_doc}
PYTHONPATH=. sphinx-build-3 -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{sname}

%doc README.rst
%license LICENSE

%{python3_sitelib}/designateclient
%exclude %{python3_sitelib}/%{sname}/tests
%{python3_sitelib}/*.egg-info

%files -n python3-%{sname}-tests
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Mon Sep 21 2020 RDO <dev@lists.rdoproject.org> 4.1.0-1
- Update to 4.1.0

