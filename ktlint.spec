BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Name:           ktlint
Version:        0.46.0
Release:        1%{?dist}
Summary:        Anti-bikeshedding Kotlin linter with built-in formatter.

License:        MIT
URL:            https://ktlint.github.io/
Source0:        https://github.com/pinterest/ktlint/releases/download/%{version}/ktlint
Source1:        https://raw.githubusercontent.com/pinterest/ktlint/%{version}/LICENSE

BuildRequires:  bash
BuildRequires:  (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:       (java-headless >= 1:1.8.0 or java >= 1.8.0)


%description
Opinionated Kotlin linter with built-in formatter that promotes convention
over configuration. It can be used from the command-line or integrated with
Maven and Gradle.


%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/


%verifyscript
rm -rf test && mkdir test && cd test
cat <<EOT > dirty.kt
fun main( )
EOT
cat <<EOT > clean.kt
fun main()
EOT
%{buildroot}%{_bindir}/ktlint -F dirty.kt
output=$(< output.txt)
[ "$(< dirty.kt)" == "$(< clean.kt)" ]


%files
%{_bindir}/ktlint
%{_datadir}/licenses/%{name}/LICENSE
%license LICENSE


%changelog
* Sun Jun 19 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.46.0
* Thu Apr 07 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.45.2
* Thu Apr 07 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.45.1
* Wed Apr 06 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.45.2
* Mon Mar 21 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.45.1
* Fri Mar 18 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.45.0
* Tue Feb 15 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.44.0
* Wed Dec 01 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.43.2
* Wed Dec 01 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.43.1
* Tue Nov 02 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.43.0
* Fri Aug 06 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.42.1
* Thu Jul 29 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.42.0
* Tue Mar 16 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.41.0
* Fri Dec 04 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.40.0
* Mon Sep 14 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.39.0
* Thu Aug 27 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.38.1
* Wed Aug 26 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.38.0
* Mon Aug 24 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.38.1
* Fri Aug 21 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.38.0
* Tue Jun 16 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.37.2
* Mon Jun 08 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.37.1
* Wed Jun 03 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.37.0
* Sun Apr 26 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Ktlint 0.36.0
