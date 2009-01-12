%define eclipse_base     %{_libdir}/eclipse
%define eclipse_dropin   %{_datadir}/eclipse/dropins/emf

Name:      eclipse-emf
Version:   2.4.1
Release:   %mkrel 1
Summary:   Eclipse Modeling Framework (EMF) Eclipse plugin
Group:     Development/Java
License:   EPL
URL:       http://www.eclipse.org/modeling/emf/

# source tarball and the script used to generate it from upstream's source control
# script usage:
# $ sh get-emf.sh
Source0:   emf-%{version}.tar.gz
Source1:   get-emf.sh

# don't depend on ANT_HOME and JAVA_HOME environment vars
Patch0:    %{name}-make-homeless.patch
# look inside correct directory for platform docs
Patch1:    %{name}-platform-docs-location.patch
# look inside all symlink'd plugin directories when building javadocs
Patch2:    %{name}-symlinked-classpath.patch
# don't include hidden files in source plugins
# (mostly to shut rpmlint up, but these files aren't needed for source plugins; they are
# only needed so the example-installer plugins can create full projects in your workspace)
Patch3:    %{name}-build-props.patch
# bundle examples in example-installer plugins from source in tarball instead of from cvs
Patch4:    %{name}-bundle-examples.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:        noarch

# we require 1.6.0 because the javadocs fail to build otherwise
BuildRequires:    java-devel
BuildRequires:    java-rpmbuild
BuildRequires:    java-javadoc
BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 1:3.4.1
BuildRequires:    dos2unix
BuildRequires:    zip
Requires:         java
Requires:         jpackage-utils
Requires:         eclipse-platform >= 1:3.4.1

# the standalone package was deprecated and removed in EMF 2.3 (see eclipse.org bug #191837)
Obsoletes:        %{name}-standalone < %{version}

%description
The Eclipse Modeling Framework (EMF) allows developers to build tools and
other applications based on a structured data model. From a model
specification described in XMI, EMF provides tools and runtime support to
produce a set of Java classes for the model, along with a set of adapter
classes that enable viewing and command-based editing of the model, and a
basic editor.

%package   sdk
Summary:   Eclipse EMF SDK
Group:     Development/Java
Requires:  java-javadoc
Requires:  %{name} = %{version}-%{release}

%description sdk
Documentation and source for the Eclipse Modeling Framework (EMF).

%package   sdo
Summary:   Service Data Objects (SDO) Eclipse plugin
Group:     Development/Java
Requires:  %{name} = %{version}-%{release}

%description sdo
Service Data Objects (SDO) is a framework for data application development,
which includes an architecture and API. It simplifies the J2EE data
programming model and abstracts data in a service oriented architecture.

%package   sdo-sdk
Summary:   Eclipse SDO SDK
Group:     Development/Java
Requires:  %{name}-sdo = %{version}-%{release}
Requires:  %{name}-sdk = %{version}-%{release}

%description sdo-sdk
Documentation and source for the Eclipse Service Data Objects (SDO) plugin.

%package   xsd
Summary:   XML Schema Definition (XSD) Eclipse plugin
Group:     Development/Java
Requires:  %{name} = %{version}-%{release}

%description xsd
The XML Schema Definition (XSD) plugin is a library that provides an API for
manipulating the components of an XML Schema as described by the W3C XML
Schema specifications, as well as an API for manipulating the DOM-accessible
representation of XML Schema as a series of XML documents.

%package   xsd-sdk
Summary:   Eclipse XSD SDK
Group:     Development/Java
Requires:  %{name}-xsd = %{version}-%{release}
Requires:  %{name}-sdk = %{version}-%{release}

%description xsd-sdk
Documentation and source for the Eclipse XML Schema Definition (XSD) plugin.

%package   examples
Summary:   Eclipse EMF/XSD examples
Group:     Development/Java
Requires:  %{name}         = %{version}-%{release}
Requires:  %{name}-sdk     = %{version}-%{release}
Requires:  %{name}-xsd     = %{version}-%{release}
Requires:  %{name}-xsd-sdk = %{version}-%{release}

%description examples
Example projects that demonstrate how to use the Eclipse Modeling Framework
(EMF) and XML Schema Definition (XSD) plugins.

%prep
%setup -q -n emf-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm org.eclipse.emf.doc/tutorials/jet2/jetc-task.jar
rm org.eclipse.emf.test.core/data/data.jar

# link to local java api javadocs
sed -i -e "s|http://java.sun.com/j2se/1.5/docs/api/|%{_javadocdir}/java|" -e "s|\${javaHome}/docs/api/|%{_javadocdir}/java|" \
  org.eclipse.emf.doc/build/javadoc.xml.template \
  org.eclipse.emf.ecore.sdo.doc/build/javadoc.xml.template \
  org.eclipse.xsd.doc/build/javadoc.xml.template

# make sure upstream hasn't sneaked in any jars we don't know about
JARS=""
for j in `find -name "*.jar"`; do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
   echo "These jars should be deleted and symlinked to system jars: $JARS"
   exit 1
fi

%build
# build all features
# we use forceContextQualifier because the docs plugins use custom build scripts and don't work otherwise
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.emf.all \
  -a "-DjavacTarget=1.5 -DjavacSource=1.5 -DforceContextQualifier=`date +%Y%m%d%H%M`"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{eclipse_dropin}
unzip -q -d %{buildroot}%{eclipse_dropin} build/rpmBuild/org.eclipse.emf.all.zip

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{eclipse_dropin}
%doc %{eclipse_dropin}/eclipse/epl-v10.html
%doc %{eclipse_dropin}/eclipse/notice.html
%{eclipse_dropin}/eclipse/content.xml
%{eclipse_dropin}/eclipse/features/org.eclipse.emf_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.codegen_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.codegen.ui_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.codegen.ecore_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.codegen.ecore.ui_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.common_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.common.ui_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.converter_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.databinding_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.databinding.edit_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.edit_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.editor_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.edit_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.edit.ui_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.mapping_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.mapping.ui_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.mapping.ecore_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.mapping.ecore.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ant_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.codegen_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.codegen.ui_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.codegen.ecore_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.codegen.ecore.ui_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.common_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.common.ui_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.converter_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.databinding_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.databinding.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.change_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.change.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.xmi_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.edit.ui_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.exporter_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.importer_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.importer.ecore_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.importer.java_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.importer.rose_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.ui_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.ecore_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.ecore.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.ecore2ecore_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.ecore2ecore.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.ecore2xml_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.ecore2xml.ui_*

%files sdk
%defattr(-,root,root,-)
%doc %{eclipse_dropin}/eclipse/epl-v10.html
%doc %{eclipse_dropin}/eclipse/notice.html
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.doc_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.sdk_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.source_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.cheatsheets_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.doc_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.source_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.example.installer_*

%files sdo
%defattr(-,root,root,-)
%doc %{eclipse_dropin}/eclipse/epl-v10.html
%doc %{eclipse_dropin}/eclipse/notice.html
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.sdo_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.sdo.edit_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.sdo.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.commonj.sdo_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.sdo_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.sdo.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.sdo.editor_*

%files sdo-sdk
%defattr(-,root,root,-)
%doc %{eclipse_dropin}/eclipse/epl-v10.html
%doc %{eclipse_dropin}/eclipse/notice.html
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.sdo.doc_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.sdo.sdk_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.ecore.sdo.source_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.sdo.doc_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.ecore.sdo.source_*

%files xsd
%defattr(-,root,root,-)
%doc %{eclipse_dropin}/eclipse/epl-v10.html
%doc %{eclipse_dropin}/eclipse/notice.html
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd_*
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.ecore.converter_*
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.edit_*
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.editor_*
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.mapping_*
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.mapping.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.xsd2ecore_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.mapping.xsd2ecore.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.ecore.converter_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.ecore.exporter_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.ecore.importer_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.mapping_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.mapping.editor_*

%files xsd-sdk
%defattr(-,root,root,-)
%doc %{eclipse_dropin}/eclipse/epl-v10.html
%doc %{eclipse_dropin}/eclipse/notice.html
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.doc_*
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.sdk_*
%{eclipse_dropin}/eclipse/features/org.eclipse.xsd.source_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.cheatsheets_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.doc_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.source_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.example.installer_*

%files examples
%defattr(-,root,root,-)
%doc %{eclipse_dropin}/eclipse/epl-v10.html
%doc %{eclipse_dropin}/eclipse/notice.html
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.all_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.examples_*
%{eclipse_dropin}/eclipse/features/org.eclipse.emf.examples.source_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.activities_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.examples_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.examples.generator.validator_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.examples.library_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.examples.library.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.examples.library.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.examples.source_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.exporter.html_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.java_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.java.edit_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.emf.java.editor_*
%{eclipse_dropin}/eclipse/plugins/org.eclipse.xsd.example_*

