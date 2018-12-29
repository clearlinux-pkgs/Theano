#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Theano
Version  : 1.0.3
Release  : 30
URL      : https://files.pythonhosted.org/packages/4d/b1/d490d88ab47f01f367f413bd2e47d86acf92c84157c5172c23903798bd70/Theano-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/b1/d490d88ab47f01f367f413bd2e47d86acf92c84157c5172c23903798bd70/Theano-1.0.3.tar.gz
Summary  : Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: Theano-bin = %{version}-%{release}
Requires: Theano-license = %{version}-%{release}
Requires: Theano-python = %{version}-%{release}
Requires: Theano-python3 = %{version}-%{release}
Requires: numpy
Requires: openmpi
Requires: scipy
Requires: six
BuildRequires : Sphinx
BuildRequires : beignet
BuildRequires : beignet-dev
BuildRequires : buildreq-distutils3
BuildRequires : graphviz
BuildRequires : nose
BuildRequires : numpy
BuildRequires : ocl-icd
BuildRequires : ocl-icd-dev
BuildRequires : openblas
BuildRequires : scipy
BuildRequires : six

%description
============================================================================================================
`MILA will stop developing Theano <https://groups.google.com/d/msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ>`_.
============================================================================================================

%package bin
Summary: bin components for the Theano package.
Group: Binaries
Requires: Theano-license = %{version}-%{release}

%description bin
bin components for the Theano package.


%package license
Summary: license components for the Theano package.
Group: Default

%description license
license components for the Theano package.


%package python
Summary: python components for the Theano package.
Group: Default
Requires: Theano-python3 = %{version}-%{release}
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
%setup -q -n Theano-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541280283
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Theano
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/Theano/LICENSE.txt
cp doc/LICENSE.txt %{buildroot}/usr/share/package-licenses/Theano/doc_LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/theano-cache
/usr/bin/theano-nose

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Theano/LICENSE.txt
/usr/share/package-licenses/Theano/doc_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
