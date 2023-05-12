# Testing dependencies: deepdiff, flexmock are missing on EPEL 9. Cannot use testing environment
%if 0%{?el9}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           packit
Version:        0.75.0
Release:        1%{?dist}
Summary:        A tool for integrating upstream projects with Fedora operating system

License:        MIT
URL:            https://github.com/packit/packit
Source0:        %{pypi_source packitos}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(click-man)
Requires:       python3-packit = %{version}-%{release}

%description
This project provides tooling and automation to integrate upstream open source
projects into Fedora operating system.

%package -n     python3-packit
Summary:        %{summary}
# new-sources
Requires:       fedpkg
Requires:       git
# kinit
Requires:       krb5-workstation
# rpmbuild
Requires:       rpm-build
# bumpspec
Requires:       rpmdevtools
# Copying files between repositories
Requires:       rsync

%description -n python3-packit
Python library for Packit,
check out packit package for the executable.


%prep
%autosetup -n packitos-%{version}


%generate_buildrequires
# The -w flag is required for EPEL 9's older hatchling
%pyproject_buildrequires %{?with_tests:-x testing} %{?el9:-w}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files packit
PYTHONPATH="%{buildroot}%{python3_sitelib}" click-man packit --target %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{bash_completions_dir}
cp files/bash-completion/packit %{buildroot}%{bash_completions_dir}/packit


%files
%license LICENSE
%{_bindir}/packit
%{_mandir}/man1/packit*.1*
%{bash_completions_dir}/packit

%files -n python3-packit -f %{pyproject_files}
# Epel9 does not tag the license file in pyproject_files as a license. Manually install it in this case
%if 0%{?el9}
%license LICENSE
%endif
%doc README.md

%changelog
* Fri Apr 28 2023 Packit Team <hello@packit.dev> - 0.75.0-1
- New upstream release 0.75.0
