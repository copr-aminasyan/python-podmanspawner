# Created by pyp2rpm-3.3.7
%global pypi_name podmanspawner
%global pypi_version 0.2.7

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        4%{?dist}
Summary:        PodmanSpawner for JupyterHub

License:        BSD
URL:            https://github.com/gatoniel/podmanspawner
Source0:        %{pypi_name}-%{pypi_version}.tar.gz
Patch0:         podmanspawner-v3-hub.patch
BuildArch:      noarch

Requires:       python3dist(jupyterhub)
Requires:       python3dist(traitlets) >= 4.3.2
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 podmanspawner OverviewSpawner to use podman with JupyterHubSee also this
[issue]( on dockerspawner.**This Spawner is still in development and might not
work properly.** Please feel free to file issues, when you encounter problems.
Version 0.2 seems to work in my case... TechnicalRight now we use
subprocess.Popen to make the calls to Podman. We should use [podman RestAPI](
InstallationVia pip:...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 podmanspawner OverviewSpawner to use podman with JupyterHubSee also this
[issue]( on dockerspawner.**This Spawner is still in development and might not
work properly.** Please feel free to file issues, when you encounter problems.
Version 0.2 seems to work in my case... TechnicalRight now we use
subprocess.Popen to make the calls to Podman. We should use [podman RestAPI](
InstallationVia pip:...


%prep
%autosetup -p1 -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}.dev0-py%{python3_version}.egg-info

%changelog
* Sat Jan 14 2023 Aram Minasyan <aram_dot_minasyan_at_yahoo_dot_com> - 0.2.7-4
- Add USERNAME feature to jupyter_additional_cmds

* Sat Jan 14 2023 Aram Minasyan <aram_dot_minasyan_at_yahoo_dot_com> - 0.2.7-3
- More patching of env var to support jupyterhub 3.1.0

* Thu Mar 24 2022 Aram Minasyan <aram_dot_minasyan_at_yahoo_dot_com> - 0.2.7-2
- Patch some env var quoting and config tags

* Thu Mar 24 2022 Aram Minasyan <aram_dot_minasyan_at_yahoo_dot_com> - 0.2.7-1
- Initial package.
