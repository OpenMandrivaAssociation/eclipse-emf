%{?_javapackages_macros:%_javapackages_macros}
%{?scl:%scl_package eclipse-emf}
%{!?scl:%global pkg_name %{name}}


%if 0%{?rhel} >= 6
%global debug_package %{nil}
%endif
%global eclipse_dropin   %{_datadir}/eclipse/dropins

%global emf_tag R2_9_1
%global context_qualifier v20130930-0823

%define __requires_exclude osgi*

Name:      %{?scl_prefix}eclipse-emf
Version:   2.9.1
Release:   1.0%{?dist} 
Summary:   Eclipse Modeling Framework (EMF) Eclipse plugin

License:   EPL
URL:       http://www.eclipse.org/modeling/emf/

# source tarball and the script used to generate it from upstream's source control
# script usage:
# $ sh get-emf.sh
Source0:   emf-%{emf_tag}.tar.gz
Source1:   get-emf.sh

# don't depend on ANT_HOME and JAVA_HOME environment vars, patch upstream
#Patch0:    %{name}-make-homeless.patch
# look inside correct directory for platform docs
Patch1:    %{pkg_name}-platform-docs-location.patch
# Build docs correctly
Patch3:    %{pkg_name}-build-docs.patch
# Remove xsd2ecore components from SDK, they are not in the main feature
Patch4:    %{pkg_name}-no-xsd2ecore.patch
Patch5:    %{pkg_name}-fix-missing-index.patch

BuildArch:        noarch

# we require 1.6.0 because the javadocs fail to build otherwise
BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    java-javadoc
BuildRequires:    jpackage-utils
BuildRequires:    %{?scl_prefix}eclipse-pde >= 1:4.2.0
BuildRequires:    dos2unix
Requires:         java
Requires:         jpackage-utils
Requires:         %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires:         %{name}-core

# the standalone package was deprecated and removed in EMF 2.3 (see eclipse.org bug #191837)
Obsoletes:        %{name}-standalone < 2.4

# the SDO sub-project was terminated upstream and removed in EMF 2.5 (see eclipse.org bug #251402)
Obsoletes:        %{name}-sdo < 2.5
Obsoletes:        %{name}-sdo-sdk < 2.5

#TODO: ODA, GWT and RAP components are not packaged.
#TODO: Possibly spin XSD off into it's own package, upstream have moved it to it's project

%description
The Eclipse Modeling Framework (EMF) allows developers to build tools and
other applications based on a structured data model. From a model
specification described in XMI, EMF provides tools and runtime support to
produce a set of Java classes for the model, along with a set of adapter
classes that enable viewing and command-based editing of the model, and a
basic editor.

%package   core
Epoch:      1
Summary:   Eclipse EMF Core

Requires:  java
Obsoletes: eclipse-emf-core < 1:2.8.0-20

%description core
The core of Eclipse Modeling Framework
 
%package   sdk
Summary:   Eclipse EMF SDK

Requires:  java-javadoc
Requires:  %{?scl_prefix}eclipse-pde >= 1:4.2.0
Requires:  %{name} = %{version}-%{release}

%description sdk
Documentation and source for the Eclipse Modeling Framework (EMF).

%package   xsd
Summary:   XML Schema Definition (XSD) Eclipse plugin

Requires:  %{name} = %{version}-%{release}

%description xsd
The XML Schema Definition (XSD) plugin is a library that provides an API for
manipulating the components of an XML Schema as described by the W3C XML
Schema specifications, as well as an API for manipulating the DOM-accessible
representation of XML Schema as a series of XML documents.

%package   xsd-sdk
Summary:   Eclipse XSD SDK

Requires:  java-javadoc
Requires:  %{?scl_prefix}eclipse-pde >= 1:4.2.0
Requires:  %{name}-xsd = %{version}-%{release}
Requires:  %{name}-sdk = %{version}-%{release}

%description xsd-sdk
Documentation and source for the Eclipse XML Schema Definition (XSD) plugin.

%package   examples
Summary:   Eclipse EMF/XSD examples

Requires:  %{name}         = %{version}-%{release}
Requires:  %{name}-xsd     = %{version}-%{release}

%description examples
Installable versions of the example projects from the SDKs that demonstrate how
to use the Eclipse Modeling Framework (EMF) and XML Schema Definition (XSD)
plugins.

%prep
%setup -q -n emf-%{version}
%patch1 -p0
#https://bugs.eclipse.org/bugs/show_bug.cgi?id=406981
#$patch2 -p1 -b .orig
%patch3 -p1
%patch4 -p1
%patch5

rm org.eclipse.emf.doc/tutorials/jet2/jetc-task.jar
rm org.eclipse.emf.test.core/data/data.jar

# link to local java api javadocs
sed -i -e "s|http://java.sun.com/j2se/1.5/docs/api/|%{_javadocdir}/java|" -e "s|\${javaHome}/docs/api/|%{_javadocdir}/java|" \
  org.eclipse.emf.doc/build/javadoc.xml.template \
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
# Note: We use forceContextQualifier because the docs plugins use custom build
#       scripts and don't work otherwise.
OPTIONS="-DjavacTarget=1.5 -DjavacSource=1.5 -DforceContextQualifier=%{context_qualifier}"

# Work around pdebuild entering/leaving symlink it is unaware of.
ln -s %{_builddir}/emf-%{version}/org.eclipse.emf.license-feature %{_builddir}/emf-%{version}/org.eclipse.emf.license
ln -s %{_builddir}/emf-%{version}/org.eclipse.xsd.license-feature %{_builddir}/emf-%{version}/org.eclipse.xsd.license

# We build the emf, xsd and examples features seperately, rather than just
# building the "all" feature, because it makes the files section easier to
# maintain (i.e. we don't have to know when upstream adds a new plugin)

# build core features
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.common -a "$OPTIONS"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.ecore -a "$OPTIONS"

# build emf features - order is important
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.common.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.edit.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.ecore.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.ecore.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen.ecore -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping.ecore -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen.ecore.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping.ecore.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.databinding -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.databinding.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.converter -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.sdk -a "$OPTIONS" -d "eclipse-emf-core"

# build xsd features
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.mapping -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.mapping.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.ecore.converter -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.sdk -a "$OPTIONS" -d "eclipse-emf-core"

# build examples features
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.examples -a "$OPTIONS" -d "eclipse-emf-core"

%install
install -d -m 755 %{buildroot}%{eclipse_dropin}
install -d -m 755 %{buildroot}%{_javadir}/emf

unzip -q -n -d %{buildroot}%{_javadir}/emf          build/rpmBuild/org.eclipse.emf.common.zip
unzip -q -n -d %{buildroot}%{_javadir}/emf          build/rpmBuild/org.eclipse.emf.ecore.zip
unzip -q -n -d %{buildroot}%{_javadir}/emf          build/rpmBuild/org.eclipse.emf.edit.zip


unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.common.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.edit.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.ecore.edit.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.ecore.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.ecore.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.converter.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.ecore.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.ecore.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.ecore.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.databinding.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.databinding.edit.zip

unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf-sdk      build/rpmBuild/org.eclipse.emf.sdk.zip

unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.edit.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.mapping.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.mapping.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.ecore.converter.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd-sdk      build/rpmBuild/org.eclipse.xsd.sdk.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf-examples build/rpmBuild/org.eclipse.emf.examples.zip

# the non-sdk builds are a subset of the sdk builds, so delete duplicate features & plugins from the sdks
(cd %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/features && ls %{buildroot}%{eclipse_dropin}/emf/eclipse/features | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins  && ls %{buildroot}%{eclipse_dropin}/emf/eclipse/plugins  | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/xsd-sdk/eclipse/features && ls %{buildroot}%{eclipse_dropin}/xsd/eclipse/features | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/xsd-sdk/eclipse/plugins  && ls %{buildroot}%{eclipse_dropin}/xsd/eclipse/plugins  | xargs rm -rf)

# remove duplicated plugins and features
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/features/org.eclipse.emf.common_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.common_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/features/org.eclipse.emf.ecore_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.ecore_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.ecore.change_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.ecore.xmi_*

pushd %{buildroot}%{_javadir}/emf/eclipse/plugins/
for f in org.eclipse.emf.common \
		org.eclipse.emf.ecore.change \
		org.eclipse.emf.ecore.xmi \
		org.eclipse.emf.ecore \
		org.eclipse.emf.edit ; do
	mv ${f}_* ${f}.jar
done
popd
pushd %{buildroot}%{eclipse_dropin}/emf/eclipse/plugins
	ln -s %{_javadir}/emf/eclipse/plugins/org.eclipse.emf.edit.jar
popd
%files
%{eclipse_dropin}/emf
%doc org.eclipse.emf.license-feature/rootfiles/*

%files core
%{_javadir}/emf
%doc org.eclipse.emf.license-feature/rootfiles/*

%files sdk
%{eclipse_dropin}/emf-sdk

%files xsd
%{eclipse_dropin}/xsd
%doc org.eclipse.xsd.license-feature/rootfiles/*

%files xsd-sdk
%{eclipse_dropin}/xsd-sdk

%files examples
%{eclipse_dropin}/emf-examples

%changelog
* Mon Sep 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.9.1-1
- Update to latest upstream.  

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.9.0-1
- Update to Kepler release.

* Fri Jun 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.9.0-0.2.git352e28
- 974108: Remove versions and timestamps from EMF filenames.

* Wed May 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.9.0-0.1.git352e28
- Update to latest upstream.

* Thu Mar 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.1-20
- Initial SCLization.

* Mon Jan 28 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.1-7
- Really fix RHBZ#894154.

* Thu Jan 17 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.1-6
- Move emf.edit back to eclipse-emf-core and symlink it.

* Thu Jan 17 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.1-5
- Fix for RHBZ#894154

* Mon Dec 17 2012 Alexander Kurtakov <akurtako@redhat.com> 1:2.8.1-4
- Remove unneeded things.

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.1-3
- Avoid generating automatic OSGi dependencies (yet another attempt).

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.1-2
- Avoid generating automatic OSGi dependencies. (fix)

* Mon Oct 1 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.1-1
- Update to upstream 2.8.1 release

* Wed Sep 12 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.0-17
- Avoid generating automatic OSGi dependencies.

* Tue Aug 15 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.0-16
- Removed obsolete.

* Tue Aug 14 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.0-15
- Moved Obs emf-core to emf-core package.
- Removed dropins symlinks.

* Tue Aug 14 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:2.8.0-14
- Added Epoch to eclipse-emf-core.
- Updated eclipse-pde dependency version to 4.2.0.

* Mon Aug 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-13
- Move emf.edit to eclipse-emf-core.

* Fri Aug 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-12
- Lower eclipse-platform version requirement (CBI Eclipse is not in yet).

* Fri Aug 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-11
- Get rid off conflicts clause.

* Thu Aug 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-10
- Moving core back to emf package (for CBI build).

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-1
- Update to upstream Juno.

* Mon May 7 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-0.7.e674bb28ad412fc9bc786f2f9b3c157eb2cbdae0
- Update to M7.

* Mon Apr 16 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-0.6.postM6
- Bugs 812870, 812872 - fix building index for documentation.

* Tue Apr 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-0.5.postM6
- Remove %clean section.
- Remove duplicated plugins.

* Mon Apr 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-0.4.postM6
- Use %{bindir}/eclipse-pdebuild.

* Thu Mar 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-0.3.postM6
- Back noarch.
- Use the eclipse-emf-core from main eclipse-emf.

* Thu Mar 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-0.2.postM6
- Removed the noarch tag.

* Thu Mar 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.8.0-0.1.postM6
- Update to latest upstream version.
- Package eclipse-emf-core created for the need of Eclipse 4.2. 
- Removed usage of Eclipse reconciler script.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Jeff Johnston <jjohnstn@redhat.com> 2.7.1-1
- Update to 2.7.1.
- Add rhel flags.

* Wed Oct 5 2011 Sami Wagiaalla <swagiaal@redhat.com> 2.7.0-2
- Use the reconciler to install/uninstall plugins during rpm
  post and postun respectively.

* Thu Sep 15 2011 Roland Grunberg <rgrunber@redhat.com> 2.7.0-1
- Update to 2.7.0.
- Re-apply necessary patches, content-handler error fixed upstream.
- licenses now exist in org.eclipse.{emf,xsd}.license-feature only.

* Wed Sep 14 2011 Roland Grunberg <rgrunber@redhat.com> 2.6.1-2
- Fix RHBZ #716165 using old patches.
- Fix ContentHandler casting issue.

* Fri Mar 18 2011 Mat Booth <fedora@matbooth.co.uk> 2.6.1-1
- Update to 2.6.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 19 2010 Charley Wang <chwang@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Sat Sep 19 2009 Mat Booth <fedora@matbooth.co.uk> - 2.5.0-4
- Re-enable jar repacking now that RHBZ #461854 has been resolved.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Mat Booth <fedora@matbooth.co.uk> 2.5.0-2
- SDK requires PDE for example plug-in projects.

* Sun Jun 28 2009 Mat Booth <fedora@matbooth.co.uk> 2.5.0-1
- Update to 2.5.0 final release (Galileo).
- Build the features seperately to allow for a saner %%files section.

* Fri May 22 2009 Alexander Kurtakov <akurtako@redhat.com> 2.5.0-0.2.RC1
- Update to 2.5.0 RC1.
- Use %%global instead of %%define. 

* Sat Apr 18 2009 Mat Booth <fedora@matbooth.co.uk> 2.5.0-0.1.M6
- Update to Milestone 6 release of 2.5.0.
- Require Eclipse 3.5.0.

* Tue Apr 7 2009 Alexander Kurtakov <akurtako@redhat.com> 2.4.2-3
- Fix directory ownership.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 2.4.2-2
- Rebuild to not ship p2 context.xml.
- Remove context.xml from %%files section.

* Sat Feb 28 2009 Mat Booth <fedora@matbooth.co.uk> 2.4.2-1
- Update for Ganymede SR2.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Mat Booth <fedora@matbooth.co.uk> 2.4.1-4
- Make context qualifier the same as upstream.

* Sat Jan 10 2009 Mat Booth <fedora@matbooth.co.uk> 2.4.1-3
- Removed AOT bits and change package names to what they used to be.
- Obsolete standalone package.

* Tue Dec 23 2008 Mat Booth <fedora@matbooth.co.uk> 2.4.1-2
- Build example installer plugins using the source from the tarball instead of
  trying to get the examples from source control a second time.

* Fri Dec 12 2008 Mat Booth <fedora@matbooth.co.uk> 2.4.1-1
- Initial release, based on eclipse-gef spec file, but with disabled AOT
  compiled bits because of RHBZ #477707.
