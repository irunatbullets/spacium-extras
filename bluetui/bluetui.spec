Name:           bluetui
Version:        0.8.0
Release:        1%{?dist}
Summary:        TUI for managing bluetooth on Linux

License:        GPL-3.0-only
URL:            https://github.com/pythops/bluetui

Source0:        bluetui-0.8.0.crate

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang
BuildRequires:  dbus-devel

%description
TUI for managing bluetooth on Linux.

%prep
%autosetup -n bluetui-%{version}

%build
cargo build --release

%install
install -Dm755 target/release/bluetui %{buildroot}%{_bindir}/bluetui

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/bluetui

%changelog
%autochangelog

