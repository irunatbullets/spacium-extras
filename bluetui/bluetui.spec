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
BuildRequires:  rust-packaging
BuildRequires:  clang
BuildRequires:  dbus-devel

%description
TUI for managing Bluetooth on Linux.

%prep
%autosetup -n bluetui-%{version}

tar -xf %{SOURCE1}

mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

# Prevent RPM debugsource generation from tripping over vendored Rust sources
rm -rf vendor/.cargo

%build
%cargo_build --release --frozen

%install
install -Dm755 target/release/bluetui %{buildroot}%{_bindir}/bluetui

# Remove vendored crates from debugsource collection
rm -rf vendor

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/bluetui

%changelog
%autochangelog

