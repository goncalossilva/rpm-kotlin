BuildRoot:          %{_tmppath}/%{name}-%{version}-build
BuildArchitectures: noarch
Name:               ktlint
Version:            0.40.0
Release:            1%{?dist}
Summary:            Anti-bikeshedding Kotlin linter with built-in formatter.

License:            MIT
URL:                https://ktlint.github.io/
Source0:            https://github.com/pinterest/ktlint/releases/download/%{version}/ktlint
Source1:            https://raw.githubusercontent.com/pinterest/ktlint/%{version}/LICENSE

BuildRequires:      bash
BuildRequires:      (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:           (java-headless >= 1:1.8.0 or java >= 1.8.0)


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
