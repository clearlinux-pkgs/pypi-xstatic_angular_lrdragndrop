#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-xstatic_angular_lrdragndrop
Version  : 1.0.2.6
Release  : 10
URL      : https://files.pythonhosted.org/packages/22/4c/92093256c67c042166ca70d5ff7db2971a25db13c6402fa988ad2c080d76/XStatic-Angular-lrdragndrop-1.0.2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/22/4c/92093256c67c042166ca70d5ff7db2971a25db13c6402fa988ad2c080d76/XStatic-Angular-lrdragndrop-1.0.2.6.tar.gz
Summary  : Angular-lrdragndrop 1.0.2 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: pypi-xstatic_angular_lrdragndrop-python = %{version}-%{release}
Requires: pypi-xstatic_angular_lrdragndrop-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
---------------------------
        
        lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package
        `XStatic`.

%package python
Summary: python components for the pypi-xstatic_angular_lrdragndrop package.
Group: Default
Requires: pypi-xstatic_angular_lrdragndrop-python3 = %{version}-%{release}

%description python
python components for the pypi-xstatic_angular_lrdragndrop package.


%package python3
Summary: python3 components for the pypi-xstatic_angular_lrdragndrop package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_angular_lrdragndrop)

%description python3
python3 components for the pypi-xstatic_angular_lrdragndrop package.


%prep
%setup -q -n XStatic-Angular-lrdragndrop-1.0.2.6
cd %{_builddir}/XStatic-Angular-lrdragndrop-1.0.2.6
pushd ..
cp -a XStatic-Angular-lrdragndrop-1.0.2.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689783359
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
