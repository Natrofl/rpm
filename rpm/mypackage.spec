Name:           mypackage
Version:        1.0
Release:        1%{?dist}
Summary:        Example package containing a text file
License:        MIT
Source0:        1.txt

%description
This package contains a single text file named 1.txt.

%prep

%build

%install
install -Dpm 644 %{SOURCE0} %{buildroot}/%{_datadir}/mypackage/1.txt

%files
%license LICENSE
%{_datadir}/mypackage/1.txt

