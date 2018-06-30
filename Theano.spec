#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Theano
Version  : 1.0.1
Release  : 22
URL      : https://pypi.python.org/packages/62/da/ab486aae8e538d8ae91fa0e6ab26d3a454d7c5c7a66541f40300e58a3314/Theano-1.0.1.tar.gz
Source0  : https://pypi.python.org/packages/62/da/ab486aae8e538d8ae91fa0e6ab26d3a454d7c5c7a66541f40300e58a3314/Theano-1.0.1.tar.gz
Summary  : Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: Theano-bin
Requires: Theano-python3
Requires: Theano-python
Requires: Pygments
Requires: Sphinx
Requires: flake8
Requires: nose
Requires: numpy
Requires: openmpi
Requires: scipy
Requires: six
BuildRequires : Sphinx
BuildRequires : beignet
BuildRequires : beignet-dev
BuildRequires : graphviz
BuildRequires : nose
BuildRequires : numpy
BuildRequires : ocl-icd
BuildRequires : ocl-icd-dev
BuildRequires : openblas
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : setuptools
BuildRequires : six

%description
============================================================================================================
`MILA will stop developing Theano <https://groups.google.com/d/msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ>`_.
============================================================================================================

%package bin
Summary: bin components for the Theano package.
Group: Binaries

%description bin
bin components for the Theano package.


%package python
Summary: python components for the Theano package.
Group: Default
Requires: Theano-python3
Provides: theano-python

%description python
python components for the Theano package.


%package python3
Summary: python3 components for the Theano package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Theano package.


%prep
%setup -q -n Theano-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526511259
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/theano-cache
/usr/bin/theano-nose

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
