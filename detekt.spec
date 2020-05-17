BuildRoot:          %{_tmppath}/%{name}-%{version}-build
BuildArchitectures: noarch
Name:               detekt
Version:            1.9.1
Release:            1%{?dist}
Summary:            Static code analysis for Kotlin.

License:            ASL 2.0
URL:                https://detekt.github.io/detekt/
Source0:            https://github.com/detekt/detekt/releases/download/v%{version}/detekt
Source1:            https://raw.githubusercontent.com/detekt/detekt/v%{version}/LICENSE

BuildRequires:      bash
BuildRequires:      (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:           (java-headless >= 1:1.8.0 or java >= 1.8.0)


%description
A configurable static code analysis tool for Kotlin that generates complexity
reports based on lines of code, cyclomatic complexity and code smells.
Integrates with Gradle, Maven, SonarQube and IntelliJ.


%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/


%verifyscript
rm -rf test && mkdir test && cd test
cat <<EOT > test.kt
fun main() {

}
EOT
cat <<EOT > detekt.yml
empty-blocks:
    EmptyFunctionBlock:
        active: true
EOT
%{buildroot}%{_bindir}/detekt --input test.kt --report txt:output.txt --config detekt.yml
output=$(< output.txt)
[ "${output//[[:space:]]/}" == "EmptyFunctionBlock" ]


%files
%{_bindir}/detekt
%{_datadir}/licenses/%{name}/LICENSE
%license LICENSE


%changelog
* Sun May 17 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.9.1
* Tue May 12 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.9.0
* Sun Apr 26 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Detekt 1.8.0
