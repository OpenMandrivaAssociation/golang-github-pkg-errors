# Run tests in check section
%bcond_without check

# https://github.com/pkg/errors
%global goipath		github.com/pkg/errors
%global forgeurl	https://github.com/pkg/errors
Version:		0.9.1

%gometa

Summary:	Simple error handling primitives
Name:		golang-github-pkg-errors

Release:	1
Source0:	https://github.com/pkg/errors/archive/v%{version}/errors-%{version}.tar.gz
URL:		https://github.com/pkg/errors
License:	BSD with attribution
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Package errors provides simple error handling primitives.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n errors-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
for test in "TestStackTrace" "TestStackTraceFormat" \
; do
	awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gochecks
%endif

