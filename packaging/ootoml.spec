Name:           ootoml
Version:        0.1.0
Release:        1%{?dist}
Summary:        TOML 1.0 parser and serializer for declarative config inspection and mutation.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootoml
Source0:        ootoml-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootoml is a sovereign, capability-bounded TOML ENGINE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootoml
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootoml-uninstall

%files
/usr/bin/ootoml
/usr/bin/ootoml-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
