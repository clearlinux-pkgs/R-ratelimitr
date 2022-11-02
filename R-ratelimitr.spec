#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ratelimitr
Version  : 0.4.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/ratelimitr_0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ratelimitr_0.4.1.tar.gz
Summary  : Rate Limiting for R
Group    : Development/Tools
License  : MIT
Requires: R-assertthat
BuildRequires : R-assertthat
BuildRequires : buildreq-R

%description
ratelimitr
================
[![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/ratelimitr)](https://cran.r-project.org/package=ratelimitr) [![Travis-CI Build Status](https://travis-ci.org/tarakc02/ratelimitr.svg?branch=master)](https://travis-ci.org/tarakc02/ratelimitr) [![Coverage Status](https://codecov.io/github/tarakc02/ratelimitr/badge.svg?branch=master)](https://codecov.io/github/tarakc02/ratelimitr?branch=master)

%prep
%setup -q -c -n ratelimitr
cd %{_builddir}/ratelimitr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641088184

%install
export SOURCE_DATE_EPOCH=1641088184
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ratelimitr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ratelimitr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ratelimitr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ratelimitr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ratelimitr/DESCRIPTION
/usr/lib64/R/library/ratelimitr/INDEX
/usr/lib64/R/library/ratelimitr/LICENSE
/usr/lib64/R/library/ratelimitr/Meta/Rd.rds
/usr/lib64/R/library/ratelimitr/Meta/features.rds
/usr/lib64/R/library/ratelimitr/Meta/hsearch.rds
/usr/lib64/R/library/ratelimitr/Meta/links.rds
/usr/lib64/R/library/ratelimitr/Meta/nsInfo.rds
/usr/lib64/R/library/ratelimitr/Meta/package.rds
/usr/lib64/R/library/ratelimitr/Meta/vignette.rds
/usr/lib64/R/library/ratelimitr/NAMESPACE
/usr/lib64/R/library/ratelimitr/NEWS.md
/usr/lib64/R/library/ratelimitr/R/ratelimitr
/usr/lib64/R/library/ratelimitr/R/ratelimitr.rdb
/usr/lib64/R/library/ratelimitr/R/ratelimitr.rdx
/usr/lib64/R/library/ratelimitr/doc/index.html
/usr/lib64/R/library/ratelimitr/doc/introduction.R
/usr/lib64/R/library/ratelimitr/doc/introduction.Rmd
/usr/lib64/R/library/ratelimitr/doc/introduction.html
/usr/lib64/R/library/ratelimitr/help/AnIndex
/usr/lib64/R/library/ratelimitr/help/aliases.rds
/usr/lib64/R/library/ratelimitr/help/paths.rds
/usr/lib64/R/library/ratelimitr/help/ratelimitr.rdb
/usr/lib64/R/library/ratelimitr/help/ratelimitr.rdx
/usr/lib64/R/library/ratelimitr/html/00Index.html
/usr/lib64/R/library/ratelimitr/html/R.css
/usr/lib64/R/library/ratelimitr/tests/testthat.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-function-errors.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-function-integrity.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-limit-rate.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-network-lag.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-repeated-calls.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-reset.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-update-rate.R
/usr/lib64/R/library/ratelimitr/tests/testthat/test-window.R
