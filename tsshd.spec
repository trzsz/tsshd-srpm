Name:           tsshd
Version:        0.1.8
Release:        1
Summary:        UDP-based SSH server with roaming support.

License:        MIT
URL:            https://trzsz.github.io/tsshd
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang-bin >= 1.25

%undefine _debugsource_packages
%define debug_package %{nil}

%description
tsshd is a UDP-based SSH server with roaming support.

%prep
%autosetup -n %{name}-%{version}

%build
export CGO_ENABLED=0
export GOPROXY=direct
go build -ldflags="-s -w" -o %{_builddir}/bin/tsshd ./cmd/tsshd

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/bin/tsshd %{buildroot}%{_bindir}/tsshd

%files
%{_bindir}/tsshd

%changelog
* Sun May 10 2026 Lonny Wong <lonnywong@qq.com> - 0.1.8-1
- Update to tsshd v0.1.8

* Sun May 3 2026 Lonny Wong <lonnywong@qq.com> - 0.1.7-1
- Initial RPM spec for tsshd
