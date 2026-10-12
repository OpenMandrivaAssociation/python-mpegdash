%define module mpegdash

Name:		python-%{module}
Version:	0.4.1
Release:	2
Summary:	MPEG-DASH MPD(Media Presentation Description) Parser
Source0:	https://files.pythonhosted.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
URL:		https://github.com/sangwonl/python-mpegdash
License:	MIT
Group:		Development/Python

BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python
BuildArch:	noarch

%description
MPEG-DASH MPD (Media Presentation Description) Parser compatible with Python 3+.

%files
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info

