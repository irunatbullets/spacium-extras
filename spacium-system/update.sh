#!/usr/bin/env bash
set -euo pipefail

VERSION=$(
    awk '/^Version:/ {print $2}' spacium-system.spec
)

PKG="spacium-system"

rm -rf "${PKG}-${VERSION}"

mkdir "${PKG}-${VERSION}"
cp -a files "${PKG}-${VERSION}/"

tar czf "${PKG}-${VERSION}.tar.gz" \
    "${PKG}-${VERSION}"

rm -rf "${PKG}-${VERSION}"

