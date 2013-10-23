%define module wsgiproxy
Name:           python-%module
Version:        0.2.2
Release:        1
Summary:        HTTP proxying tools for WSGI apps
Group:          Development/Python
License:        MIT
URL:            http://pythonpaste.org/wsgiproxy/
Source0:        http://pypi.python.org/packages/source/W/WSGIProxy/WSGIProxy-%{version}.tar.gz
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
%{__python} setup.py install --root %{buildroot} --install-purelib=%{py_puresitedir}

%clean

%files
%{py_puresitedir}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.1-1mdv2011.0
+ Revision: 683274
- import python-wsgiproxy


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.1
- first release for Mandriva 


