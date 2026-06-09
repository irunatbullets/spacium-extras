Name:           spacium-system
Version:        1.0
Release:        1%{?dist}
Summary:        System files and services for Spacium

License:        MIT
BuildArch:      noarch

Source0:        %{name}-%{version}.tar.gz

Requires:       greetd

%description
System configuration files, user services, and helper scripts used by Spacium.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}
cp -a files/* %{buildroot}/

%files
%dir /etc/greetd
%config(noreplace) /etc/greetd/config.toml

/usr/lib/systemd/user/spacium.service
/usr/lib/systemd/user/dsearch.service.d/override.conf

/usr/libexec/spacium

%changelog
%autochangelog

