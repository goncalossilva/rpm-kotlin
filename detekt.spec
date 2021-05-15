BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Name:           detekt
Version:        1.17.0
Release:        1%{?dist}
Summary:        Static code analysis for Kotlin.

License:        ASL 2.0
URL:            https://detekt.github.io/detekt/
Source0:        https://github.com/detekt/detekt/releases/download/v%{version}/detekt-cli-%{version}-all.jar
Source1:        https://raw.githubusercontent.com/detekt/detekt/v%{version}/LICENSE

BuildRequires:  bash
BuildRequires:  (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:       (java-headless >= 1:1.8.0 or java >= 1.8.0)


%description
A configurable static code analysis tool for Kotlin that generates complexity
reports based on lines of code, cyclomatic complexity and code smells.
Integrates with Gradle, Maven, SonarQube and IntelliJ.


%prep
printf '#!/bin/sh\n\nexec java -jar "$0" "$@"\n\n' > detekt
cat %{SOURCE0} >> detekt
mv detekt %{SOURCE0}


%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/detekt
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
* Sat May 15 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.17.0
* Wed Mar 10 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.16.0
* Thu Mar 04 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.16.0-RC3
* Tue Feb 23 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.16.0-RC2
* Tue Jan 26 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.16.0-RC1
* Fri Dec 18 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.15.0
* Mon Dec 14 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.15.0-RC2
* Mon Nov 16 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.15.0-RC1
* Tue Oct 20 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.14.2
* Wed Sep 30 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.14.1
* Sat Sep 26 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.14.0
* Sun Sep 13 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.13.1
* Tue Sep 08 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.13.0
* Tue Aug 25 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.12.0
* Thu Aug 20 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.12.0-RC1
* Wed Aug 19 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.11.2
* Tue Aug 18 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.11.1
* Thu Aug 13 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.11.0
* Sun Aug 09 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.11.0-RC2
* Sun Aug 02 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.11.0-RC1
* Sat Jun 27 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.10.0
* Sat Jun 13 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.10.0-RC1
* Sun May 17 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.9.1
* Tue May 12 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.9.0
* Sun Apr 26 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Detekt 1.8.0
