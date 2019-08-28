#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-shared-utils
Version  : 0.6
Release  : 9
URL      : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.6/maven-shared-utils-0.6.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.6/maven-shared-utils-0.6.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.1/maven-shared-utils-0.1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.1/maven-shared-utils-0.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.3/maven-shared-utils-0.3.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.3/maven-shared-utils-0.3.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.4/maven-shared-utils-0.4.jar
Source6  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.4/maven-shared-utils-0.4.pom
Source7  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.6/maven-shared-utils-0.6.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.7/maven-shared-utils-0.7.jar
Source9  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/0.7/maven-shared-utils-0.7.pom
Source10  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.0.0/maven-shared-utils-3.0.0.jar
Source11  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.0.0/maven-shared-utils-3.0.0.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.0.1/maven-shared-utils-3.0.1.jar
Source13  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.0.1/maven-shared-utils-3.0.1.pom
Source14  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.jar
Source15  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.pom
Source16  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.2.0/maven-shared-utils-3.2.0.jar
Source17  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.2.0/maven-shared-utils-3.2.0.pom
Source18  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.2.1/maven-shared-utils-3.2.1.jar
Source19  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-utils/3.2.1/maven-shared-utils-3.2.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1 Apache-2.0
Requires: mvn-maven-shared-utils-data = %{version}-%{release}
Requires: mvn-maven-shared-utils-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-shared-utils package.
Group: Data

%description data
data components for the mvn-maven-shared-utils package.


%package license
Summary: license components for the mvn-maven-shared-utils package.
Group: Default

%description license
license components for the mvn-maven-shared-utils package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-maven-shared-utils
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-maven-shared-utils/LICENSE
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-maven-shared-utils/LICENSE.txt
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-maven-shared-utils/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.6/maven-shared-utils-0.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.1/maven-shared-utils-0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.1/maven-shared-utils-0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.3/maven-shared-utils-0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.3/maven-shared-utils-0.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.4/maven-shared-utils-0.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.4/maven-shared-utils-0.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.6
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.6/maven-shared-utils-0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.7
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.7/maven-shared-utils-0.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.7
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.7/maven-shared-utils-0.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.0/maven-shared-utils-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.0/maven-shared-utils-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.1/maven-shared-utils-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.1/maven-shared-utils-3.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.1.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.1.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.0/maven-shared-utils-3.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.0/maven-shared-utils-3.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.1
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.1/maven-shared-utils-3.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.1
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.1/maven-shared-utils-3.2.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.1/maven-shared-utils-0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.1/maven-shared-utils-0.1.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.3/maven-shared-utils-0.3.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.3/maven-shared-utils-0.3.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.4/maven-shared-utils-0.4.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.4/maven-shared-utils-0.4.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.6/maven-shared-utils-0.6.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.6/maven-shared-utils-0.6.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.7/maven-shared-utils-0.7.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.7/maven-shared-utils-0.7.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.0/maven-shared-utils-3.0.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.0/maven-shared-utils-3.0.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.1/maven-shared-utils-3.0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.0.1/maven-shared-utils-3.0.1.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.0/maven-shared-utils-3.2.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.0/maven-shared-utils-3.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.1/maven-shared-utils-3.2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-utils/3.2.1/maven-shared-utils-3.2.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-maven-shared-utils/LICENSE
/usr/share/package-licenses/mvn-maven-shared-utils/LICENSE.txt
/usr/share/package-licenses/mvn-maven-shared-utils/NOTICE
