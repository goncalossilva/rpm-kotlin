BuildRoot:          %{_tmppath}/%{name}-%{version}-build
BuildArchitectures: noarch
Name:               kotlin
Version:            1.4.10
Release:            1%{?dist}
Summary:            Statically typed programming language

License:            ASL 2.0
URL:                https://kotlinlang.org/
Source0:            https://github.com/JetBrains/kotlin/releases/download/v%{version}/kotlin-compiler-%{version}.zip

BuildRequires:      unzip
BuildRequires:      sed
BuildRequires:      bash
BuildRequires:      (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:           (java-headless >= 1:1.8.0 or java >= 1.8.0)


%description
Kotlin is a statically typed programming language that targets the JVM,
Android, JavaScript and Native (via kotlin-native). Developed by JetBrains,
the project started in 2010 and had its official 1.0 release in 2016.


%prep
unzip -o %{SOURCE0} && cd kotlinc
sed -i "s|\(DIR *= *\).*|\1%{_bindir}|" bin/*
sed -i "s|\(KOTLIN_HOME *= *\).*|\1%{_datadir}/%{name}|" bin/*


%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/ && cd kotlinc
install -m 0755 bin/kotlin %{buildroot}%{_bindir}/
install -m 0755 bin/kotlin-dce-js %{buildroot}%{_bindir}/
install -m 0755 bin/kotlinc %{buildroot}%{_bindir}/
install -m 0755 bin/kotlinc-js %{buildroot}%{_bindir}/
install -m 0755 bin/kotlinc-jvm %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -m 0644 build.txt %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_datadir}/%{name}/lib/
install -m 0644 lib/* %{buildroot}%{_datadir}/%{name}/lib/
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cd license/ && find * -type f -exec install -Dm 0644 {} %{buildroot}%{_datadir}/licenses/%{name}/{} \;


%verifyscript
rm -rf test && mkdir test && cd test
cat <<EOT > test.kt
fun main(args: Array<String>) {
    println("Hello, world!")
}
EOT
kotlinc test.kt && %{buildroot}%{_bindir}/kotlin TestKt
%{buildroot}%{_bindir}/kotlinc test.kt -include-runtime -d test.jar
%{buildroot}%{_bindir}/kotlinc-js test.kt -output test.js
%{buildroot}%{_bindir}/kotlinc-jvm test.kt -include-runtime -d test.jar


%files
%{_bindir}/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/build.txt
%dir %{_datadir}/%{name}/lib/
%{_datadir}/%{name}/lib/*
%dir %{_datadir}/licenses/%{name}/
%{_datadir}/licenses/%{name}/*
%license kotlinc/license/LICENSE.txt


%changelog
* Thu Sep 10 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.10
* Fri Aug 14 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.0
* Sat Apr 18 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.3.72
* Mon Apr 13 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Kotlin 1.3.71
