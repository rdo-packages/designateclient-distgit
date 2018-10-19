# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%global pymicrover %{python3_version}
%else
%global pyver 2
%global pymicrover %{python2_version}
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Client library and command line utility for interacting with Openstack Designate API

%global sname designateclient

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

%package -n python%{pyver}-%{sname}
Summary:    Python API and CLI for OpenStack Designate
%{?python_provide:%python_provide python%{pyver}-%{sname}}

BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-pbr

Requires: python%{pyver}-pbr
Requires: python%{pyver}-keystoneauth1 >= 3.4.0
Requires: python%{pyver}-requests >= 2.14.2
Requires: python%{pyver}-six >= 1.10.0
Requires: python%{pyver}-stevedore
Requires: python%{pyver}-osc-lib >= 1.8.0
Requires: python%{pyver}-debtcollector
Requires: python%{pyver}-oslo-utils >= 3.33.0

# Handle python2 exceptions
%if %{pyver} == 2
Requires: python2-cliff
Requires: python2-jsonschema >= 2.6.0
%else
Requires: python-cliff
Requires: python-jsonschema >= 2.6.0
%endif

%description -n python%{pyver}-%{sname}
%{common_desc}


%package -n python%{pyver}-%{sname}-tests
Summary:    Python API and CLI for OpenStack Designate (tests)
%{?python_provide:%python_provide python%{pyver}-%{sname}-tests}
Requires:	python%{pyver}-%{sname} = %{version}-%{release}

%description -n python%{pyver}-%{sname}-tests
%{common_desc}

This package contains Designate client tests files.

%package doc
Summary:          Documentation for OpenStack Designate API Client

BuildRequires:    python%{pyver}-sphinx
BuildRequires:    python%{pyver}-openstackdocstheme
BuildRequires:    python%{pyver}-keystoneauth1
BuildRequires:    python%{pyver}-osc-lib

# Handle python2 exceptions
%if %{pyver} == 0
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
%{pyver_build}

%install
%{pyver_install}
mv %{buildroot}%{_bindir}/designate %{buildroot}%{_bindir}/designate-%{pymicrover}
ln -s ./designate-%{pymicrover} %{buildroot}%{_bindir}/designate-%{pyver}
ln -s ./designate-%{pyver} %{buildroot}%{_bindir}/designate


%files -n python%{pyver}-%{sname}
%doc README.rst
%license LICENSE
%{pyver_sitelib}/designateclient
%exclude %{pyver_sitelib}/%{sname}/tests
%{pyver_sitelib}/*.egg-info
%{_bindir}/designate
%{_bindir}/designate-%{pyver}
%{_bindir}/designate-%{pymicrover}

%files -n python%{pyver}-%{sname}-tests
%{pyver_sitelib}/%{sname}/tests

%files doc
%doc doc/build/html
%license LICENSE

%changelog