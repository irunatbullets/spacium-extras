%global cargo_install_lib 0
%global crate bluetui

Name:           bluetui
Version:        0.8.0
Release:        %autorelease
Summary:        TUI for managing bluetooth on Linux

License:        GPL-3.0-only
URL:            https://github.com/pythops/bluetui

Source0:        bluetui-0.8.0.crate

BuildRequires:  cargo-rpm-macros >= 26

%description
TUI for managing bluetooth on Linux.

%prep
%autosetup -n %{crate}-%{version}
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%{_bindir}/bluetui

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog

