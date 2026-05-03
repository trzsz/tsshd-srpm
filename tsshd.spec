Name:           tsshd
Version:        0.1.7
Release:        1
Summary:        UDP-based SSH server with roaming support.

License:        MIT
URL:            https://github.com/trzsz/tsshd
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang >= 1.25
BuildRequires:  git

%if 0%{?rhel} >= 8 && 0%{?rhel} <= 9 || 0%{?mageia}
%undefine _debugsource_packages
%endif

%if 0%{?openEuler} || 0%{?mageia} == 8
%define debug_package %{nil}
%endif

%description
tsshd is a UDP-based SSH server with roaming support.

%prep
%autosetup -n %{name}-%{version}

%build
%if 0%{?mageia} == 8
export GOPROXY=direct
%endif
go build -o %{_builddir}/bin/tsshd ./cmd/tsshd

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/bin/tsshd %{buildroot}%{_bindir}/tsshd

%files
%{_bindir}/tsshd

%changelog
* Sun May 3 2026 Lonny Wong <lonnywong@qq.com> - 0.1.7-1
- Initial RPM spec for tsshd
