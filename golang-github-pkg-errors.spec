# http://github.com/pkg/errors
%global goipath         github.com/pkg/errors
%global commit          645ef00459ed84a119197bfb8d8205042c6df63d

%gometa

Name:           %{goname}
Version:        0.8.0
Release:        0.2%{?dist}
Summary:        Simple error handling primitives
# Detected licences
# - BSD (2 clause) at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Thu Jun 21 2018 Jan Chaloupka <jchaloup@redhat.com>
- Upload glide files

* Sat Mar 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.8.0-0.1.git645ef00
- It's actually v0.8.0
  resolves: #1504175

* Sat Mar 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.7.1-0.8.git645ef00
- Bump to 645ef00459ed84a119197bfb8d8205042c6df63d

* Sat Mar 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.7.1-0.7.gita887431
- Update to spec 3.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.6.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.5.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.4.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.3.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.7.1-0.2.gita887431
- Extend the default architectures, consolidate with_ macros
  related: #1387115

* Thu Oct 20 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gita887431
- First package for Fedora
  resolves: #1387115
