Name:           xwayland-satellite
Version:        0.8.2
Release:        1%{?dist}
Summary:        Xwayland integration helper for Wayland compositors

License:        MPL-2.0
Source0:        xwayland-satellite-0.0.0.tar.gz
Source1:        vendor.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang
BuildRequires:  dbus-devel
BuildRequires:  xcb-util-cursor-devel

%description
Xwayland integration helper for Wayland compositors.

%prep
%autosetup -n xwayland-satellite

# Unpack vendored dependencies
tar -xzf %{SOURCE1}

# Force cargo to use vendored crates only
mkdir -p .cargo
cat > .cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CARGO_NET_OFFLINE=true
export CARGO_BUILD_JOBS=%{_smp_build_ncpus}

cargo build --release

%install
install -Dm755 target/release/xwayland-satellite \
    %{buildroot}%{_bindir}/xwayland-satellite

%files
%{_bindir}/xwayland-satellite

%changelog
%autochangelog

