%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname Werkzeug

Name:           python-werkzeug
Version:        0.5.1
Release:        1%{?dist}
Summary:        The Swiss Army knife of Python web development 

Group:          Development/Libraries
License:        BSD
URL:            http://werkzeug.pocoo.org/
Source0:        http://pypi.python.org/packages/source/W/Werkzeug/%{srcname}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-nose
BuildRequires:  python-setuptools-devel

%description
Werkzeug
========

Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).

%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}


%description doc
Documentation and examples for %{name}.

%prep
%setup -q -n %{srcname}-%{version}
%{__sed} -i 's/\r//' LICENSE
%{__sed} -i 's/\r//' docs/makearchive.py
%{__sed} -i 's/\r//' docs/_build/html/_static/pygments.css
%{__sed} -i 's/\r//' docs/_build/html/objects.inv
%{__sed} -i 's/\r//' PKG-INFO

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__rm} -rf docs/_build/html/.buildinfo

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE PKG-INFO CHANGES
%{python_sitelib}/*

%files doc
%defattr(-,root,root,-)
%doc docs/_build/html examples

%changelog
* Tue Aug 25 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.5.1-1
- Initial package
