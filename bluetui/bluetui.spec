%global __brp_mangle_shebangs %{nil}

Name:           bluetui
Version:        0.8.0
Release:        1%{?dist}
Summary:        TUI for managing Bluetooth on Linux

License:        GPL-3.0-only
URL:            https://github.com/pythops/bluetui

Source0:        bluetui-0.8.0.crate
Source1:        vendor.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang
BuildRequires:  dbus-devel

%description
TUI for managing Bluetooth on Linux.

%prep
%autosetup -n bluetui-%{version}

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
install -Dm755 target/release/bluetui \
    %{buildroot}%{_bindir}/bluetui

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/bluetui

%changelog
%autochangelog

