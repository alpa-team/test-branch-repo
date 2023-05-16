Name:           uwu
Version:        0.13.0
Release:        1%{?dist}
Summary:        Testing upstream program for test-repo

License:        GPLv3
URL:            https://github.com/alpa-team/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel


%description
%{summary}


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}


%files -n %{name} -f %{pyproject_files}
%{_bindir}/%{name}


%changelog
* Sat Mar 04 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com>
- some comment
