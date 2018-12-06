# Run tests in check section
%bcond_without check

%global goipath         github.com/fatih/set
%global common_description %{expand:
Set is a basic and simple, hash-based, Set data structure implementation in Go
(Golang).}

Version:        0.2.1

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Set data structure for Go 
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE.md
%doc README.md

%changelog
* Thu Aug 9 2018 Gabe <redhatrises@gmail.com> - 0.2.1-1
- First package for Fedora
