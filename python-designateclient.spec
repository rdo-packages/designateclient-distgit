Name:           python-designateclient
Version:        1.1.1
Release:        1%{?dist}
Summary:        Client library for OpenStack DNSaaS API

License:        ASL 2.0
URL:            http://wiki.openstack.org/designate
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch0:         0001-Remove-runtime-dependency-on-python-pbr.patch
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires:       python-jsonschema
Requires:       python-keystoneclient
Requires:       python-requests
Requires:       python-six
Requires:       python-stevedore

%description
Client library and command line utility for interacting with OpenStack DNSaaS API.

%prep
%setup -q
%patch0 -p1 -b .pbr
# remove runtime dep on PBR
sed -i s/REDHATDESIGNATECLIENTVERSION/%{version}/ designateclient/version.py
rm -rf {,test-}requirements.txt

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files 
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python2_sitelib}/designateclient
%{python2_sitelib}/python_designateclient-%{version}-py?.?.egg-info
%{_bindir}/designate

%changelog
* Wed Feb 25 2015 Victoria Martinez de la Cruz <vimartin@redhat.com> - 1.1.1-1
- Initial package.
