Name:           python-designateclient
Version:        1.5.0
Release:        2%{?dist}
Summary:        Client library for OpenStack DNSaaS API

License:        ASL 2.0
URL:            http://wiki.openstack.org/designate
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
Requires:       python-jsonschema
Requires:       python-keystoneclient
Requires:       python-requests
Requires:       python-six
Requires:       python-stevedore
Requires:       python-pbr
Requires:       python-cliff
Requires:       python-debtcollector
Requires:       python-oslo-utils


%description
Client library and command line utility for interacting with OpenStack DNSaaS API.

%prep
%setup -q
# Remove requirements listings
rm -rf {,test-}requirements.txt

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
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Alan Pevec <alan.pevec@redhat.com> 1.5.0-1
- Update to upstream 1.5.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Victoria Martinez de la Cruz <vkmc@fedoraproject.com> - 1.2.0-1
- Update to 1.2.0.
* Mon Mar 30 2015 Victoria Martinez de la Cruz <vimartin@redhat.com> - 1.1.1-2
- Removes pbr patch.
* Wed Feb 25 2015 Victoria Martinez de la Cruz <vimartin@redhat.com> - 1.1.1-1
- Initial package.
