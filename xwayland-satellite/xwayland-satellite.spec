Name:           xwayland-satellite
Version:        0.0.0
Release:        1%{?dist}
Summary:        Xwayland integration helper for Wayland compositors

License:        MPL-2.0
Source0:        xwayland-satellite-0.0.0.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang
BuildRequires:  dbus-devel

%description
Xwayland integration helper for Wayland compositors.

%prep
%autosetup -n xwayland-satellite

%build
cargo build --release

%install
install -Dm755 target/release/xwayland-satellite %{buildroot}/usr/bin/xwayland-satellite

%files
/usr/bin/xwayland-satellite

%changelog
* Thu Jun 04 2026 irunatbullets - 0.0.0-1
- Initial build

