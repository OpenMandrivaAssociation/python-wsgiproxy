%define module wsgiproxy
Name:           python-%module
Version:        0.1
Release:        %mkrel 1
Summary:        HTTP proxying tools for WSGI apps
Group:          Development/Python
License:        MIT
URL:            http://pythonpaste.org/wsgiproxy/
Source0:        WSGIProxy-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:      noarch
BuildRequires:  python-setuptools
Requires:       python-paste
Requires:       python-pastedeploy

%description
WSGIProxy gives tools to proxy arbitrary(ish) WSGI requests to other
processes over HTTP.

%prep
%setup -q -n WSGIProxy-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.1-1mdv2011.0
+ Revision: 683274
- import python-wsgiproxy


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.1
- first release for Mandriva 

