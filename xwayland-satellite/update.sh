#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/Supreeeme/xwayland-satellite.git"
WORKDIR="$(mktemp -d)"

echo "Using temporary directory: $WORKDIR"

cleanup() {
rm -rf "$WORKDIR"
}
trap cleanup EXIT

git clone "$REPO_URL" "$WORKDIR/xwayland-satellite"

cd "$WORKDIR/xwayland-satellite"

echo "Generating vendored dependencies..."
cargo vendor

echo "Creating source tarball..."
tar
--exclude-vcs
--transform='s,^,xwayland-satellite/,'
-czf "$OLDPWD/xwayland-satellite-0.0.0.tar.gz" .

echo "Creating vendor tarball..."
tar
-czf "$OLDPWD/vendor.tar.gz"
vendor/

echo
echo "Done."
echo "Generated:"
echo "  $OLDPWD/xwayland-satellite-0.0.0.tar.gz"
echo "  $OLDPWD/vendor.tar.gz"

