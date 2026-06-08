#!/usr/bin/env bash
set -euo pipefail

REPO="https://github.com/pythops/bluetui.git"
VERSION="0.8.0"

WORKDIR="$(mktemp -d)"
OUTDIR="$(pwd)"

cleanup() {
    rm -rf "$WORKDIR"
}
trap cleanup EXIT

echo "Checking build dependencies..."

install_if_missing() {
    local pkg="$1"
    if ! rpm -q "$pkg" >/dev/null 2>&1; then
        echo "Missing $pkg -> installing..."
        sudo dnf install -y "$pkg"
    else
        echo "$pkg already installed"
    fi
}

# Required system deps for this Rust crate
install_if_missing dbus-devel
install_if_missing pkgconf-pkg-config

echo "Cloning repo..."
git clone "$REPO" "$WORKDIR/bluetui"

cd "$WORKDIR/bluetui"

echo "Generating vendor directory..."
cargo vendor

echo "Creating vendor tarball..."
tar -czf "$OUTDIR/vendor.tar.gz" vendor/

echo "Creating crate tarball..."
cargo package --allow-dirty

CRATE_FILE=$(ls target/package/*.crate | head -n 1)

echo "Copying crate..."
cp "$CRATE_FILE" "$OUTDIR/bluetui-${VERSION}.crate"

echo "Done."
echo "Generated:"
echo "  $OUTDIR/bluetui-${VERSION}.crate"
echo "  $OUTDIR/vendor.tar.gz"

