
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		eclipse-emf
Version:	2.9.1
Release:	1.0
License:	GPLv3+
Source0:	eclipse-emf-2.9.1-1.0-omv2014.0.noarch.rpm
Source1:	eclipse-emf-core-2.9.1-1.0-omv2014.0.noarch.rpm
Source2:	eclipse-emf-examples-2.9.1-1.0-omv2014.0.noarch.rpm
Source3:	eclipse-emf-sdk-2.9.1-1.0-omv2014.0.noarch.rpm
Source4:	eclipse-emf-xsd-2.9.1-1.0-omv2014.0.noarch.rpm
Source5:	eclipse-emf-xsd-sdk-2.9.1-1.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/eclipse-emf
BuildArch:	noarch
Summary:	eclipse-emf bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-emf-core
Requires:	eclipse-platform >= 1:4.2.0
Requires:	java
Requires:	jpackage-utils
Requires:	osgi(org.apache.ant)
%if 0
Requires:	osgi(org.eclipse.ant.core)
Requires:	osgi(org.eclipse.core.databinding)
Requires:	osgi(org.eclipse.core.databinding.property)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.debug.core)
Requires:	osgi(org.eclipse.emf.common)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.emf.ecore.change)
Requires:	osgi(org.eclipse.emf.ecore.xmi)
Requires:	osgi(org.eclipse.emf.edit)
Requires:	osgi(org.eclipse.jdt.core)
Requires:	osgi(org.eclipse.jdt.launching)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.text)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.views)
Requires:	osgi(org.eclipse.ui.workbench)
%endif
Provides:	eclipse-emf = 2.9.1-1.0:2014.0
Provides:	osgi(org.eclipse.emf.ant) = 2.8.0
Provides:	osgi(org.eclipse.emf.codegen) = 2.9.0
Provides:	osgi(org.eclipse.emf.codegen.ecore) = 2.9.1
Provides:	osgi(org.eclipse.emf.codegen.ecore.ui) = 2.9.1
Provides:	osgi(org.eclipse.emf.codegen.ui) = 2.6.0
Provides:	osgi(org.eclipse.emf.common.ui) = 2.8.0
Provides:	osgi(org.eclipse.emf.converter) = 2.6.0
Provides:	osgi(org.eclipse.emf.databinding) = 1.3.0
Provides:	osgi(org.eclipse.emf.databinding.edit) = 1.3.0
Provides:	osgi(org.eclipse.emf.ecore.change.edit) = 2.5.0
Provides:	osgi(org.eclipse.emf.ecore.edit) = 2.8.0
Provides:	osgi(org.eclipse.emf.ecore.editor) = 2.9.0
Provides:	osgi(org.eclipse.emf.edit.ui) = 2.9.0
Provides:	osgi(org.eclipse.emf.exporter) = 2.7.0
Provides:	osgi(org.eclipse.emf.importer) = 2.8.0
Provides:	osgi(org.eclipse.emf.importer.ecore) = 2.7.0
Provides:	osgi(org.eclipse.emf.importer.java) = 2.7.0
Provides:	osgi(org.eclipse.emf.importer.rose) = 2.7.0
Provides:	osgi(org.eclipse.emf.mapping) = 2.7.0
Provides:	osgi(org.eclipse.emf.mapping.ecore) = 2.6.0
Provides:	osgi(org.eclipse.emf.mapping.ecore.editor) = 2.6.0
Provides:	osgi(org.eclipse.emf.mapping.ecore2ecore) = 2.7.0
Provides:	osgi(org.eclipse.emf.mapping.ecore2ecore.editor) = 2.6.0
Provides:	osgi(org.eclipse.emf.mapping.ecore2xml) = 2.7.0
Provides:	osgi(org.eclipse.emf.mapping.ecore2xml.ui) = 2.6.0
Provides:	osgi(org.eclipse.emf.mapping.ui) = 2.6.0
Obsoletes:	eclipse-emf-sdo < 2.5
Obsoletes:	eclipse-emf-sdo-sdk < 2.5
Obsoletes:	eclipse-emf-standalone < 2.4

%description
eclipse-emf bootstrap version.

%files
/usr/share/doc/eclipse-emf
/usr/share/doc/eclipse-emf/epl-v10.html
/usr/share/doc/eclipse-emf/notice.html
/usr/share/eclipse/dropins/emf
/usr/share/eclipse/dropins/emf/eclipse
/usr/share/eclipse/dropins/emf/eclipse/features
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore.ui_2.9.1.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore.ui_2.9.1.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore.ui_2.9.1.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore.ui_2.9.1.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore.ui_2.9.1.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore_2.9.1.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore_2.9.1.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore_2.9.1.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore_2.9.1.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ecore_2.9.1.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ui_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ui_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ui_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ui_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen.ui_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.codegen_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.common.ui_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.common.ui_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.common.ui_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.common.ui_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.common.ui_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.converter_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.converter_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.converter_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.converter_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.converter_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding.edit_1.3.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding.edit_1.3.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding.edit_1.3.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding.edit_1.3.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding.edit_1.3.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding_1.3.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding_1.3.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding_1.3.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding_1.3.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.databinding_1.3.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.edit_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.edit_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.edit_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.edit_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.edit_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.editor_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.editor_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.editor_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.editor_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.ecore.editor_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.edit.ui_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.edit.ui_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.edit.ui_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.edit.ui_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.edit.ui_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore.editor_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore.editor_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore.editor_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore.editor_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore.editor_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ecore_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ui_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ui_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ui_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ui_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping.ui_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf/eclipse/features/org.eclipse.emf.mapping_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf/eclipse/plugins
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.ant_2.8.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.codegen.ecore.ui_2.9.1.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.codegen.ecore_2.9.1.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.codegen.ui_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.codegen_2.9.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.common.ui_2.8.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.converter_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.databinding.edit_1.3.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.databinding_1.3.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.ecore.change.edit_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.ecore.edit_2.8.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.ecore.editor_2.9.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.edit.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.edit.ui_2.9.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.exporter_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.importer.ecore_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.importer.java_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.importer.rose_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.importer_2.8.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping.ecore.editor_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping.ecore2ecore.editor_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping.ecore2ecore_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping.ecore2xml.ui_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping.ecore2xml_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping.ecore_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping.ui_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf/eclipse/plugins/org.eclipse.emf.mapping_2.7.0.v20130930-0823.jar

#------------------------------------------------------------------------
%package	-n eclipse-emf-core
Epoch:		1
Version:	2.9.1
Release:	1.0
Summary:	eclipse-emf-core bootstrap version
Requires:	javapackages-bootstrap
Requires:	java
%if 0
Requires:	osgi(org.eclipse.core.runtime)
%endif
Provides:	eclipse-emf-core = 1:2.9.1-1.0:2014.0
Provides:	osgi(org.eclipse.emf.common) = 2.9.1
Provides:	osgi(org.eclipse.emf.ecore) = 2.9.1
Provides:	osgi(org.eclipse.emf.ecore.change) = 2.9.0
Provides:	osgi(org.eclipse.emf.ecore.xmi) = 2.9.1
Provides:	osgi(org.eclipse.emf.edit) = 2.9.0
Obsoletes:	eclipse-emf-core < 1:2.8.0-20

%description	-n eclipse-emf-core
eclipse-emf-core bootstrap version.

%files		-n eclipse-emf-core
/usr/share/doc/eclipse-emf-core
/usr/share/doc/eclipse-emf-core/epl-v10.html
/usr/share/doc/eclipse-emf-core/notice.html
/usr/share/java/emf
/usr/share/java/emf/eclipse
/usr/share/java/emf/eclipse/features
/usr/share/java/emf/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823
/usr/share/java/emf/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/epl-v10.html
/usr/share/java/emf/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/feature.properties
/usr/share/java/emf/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/feature.xml
/usr/share/java/emf/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/license.html
/usr/share/java/emf/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823
/usr/share/java/emf/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/epl-v10.html
/usr/share/java/emf/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/feature.properties
/usr/share/java/emf/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/feature.xml
/usr/share/java/emf/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/license.html
/usr/share/java/emf/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823
/usr/share/java/emf/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/epl-v10.html
/usr/share/java/emf/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/feature.properties
/usr/share/java/emf/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/feature.xml
/usr/share/java/emf/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/license.html
/usr/share/java/emf/eclipse/plugins
/usr/share/java/emf/eclipse/plugins/org.eclipse.emf.common.jar
/usr/share/java/emf/eclipse/plugins/org.eclipse.emf.ecore.change.jar
/usr/share/java/emf/eclipse/plugins/org.eclipse.emf.ecore.jar
/usr/share/java/emf/eclipse/plugins/org.eclipse.emf.ecore.xmi.jar
/usr/share/java/emf/eclipse/plugins/org.eclipse.emf.edit.jar

#------------------------------------------------------------------------
%package	-n eclipse-emf-examples
Version:	2.9.1
Release:	1.0
Summary:	eclipse-emf-examples bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-emf = 2.9.1-1.0
Requires:	eclipse-emf-xsd = 2.9.1-1.0
%if 0
Requires:	osgi(org.eclipse.core.databinding)
Requires:	osgi(org.eclipse.core.databinding.property)
Requires:	osgi(org.eclipse.core.expressions)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.emf.codegen)
Requires:	osgi(org.eclipse.emf.codegen.ecore)
Requires:	osgi(org.eclipse.emf.common.ui)
Requires:	osgi(org.eclipse.emf.databinding)
Requires:	osgi(org.eclipse.emf.databinding.edit)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.emf.ecore.xmi)
Requires:	osgi(org.eclipse.emf.edit)
Requires:	osgi(org.eclipse.emf.edit.ui)
Requires:	osgi(org.eclipse.emf.exporter)
Requires:	osgi(org.eclipse.jdt.core)
Requires:	osgi(org.eclipse.jdt.launching)
Requires:	osgi(org.eclipse.jdt.ui)
Requires:	osgi(org.eclipse.jface.databinding)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.ide)
%endif
Provides:	eclipse-emf-examples = 2.9.1-1.0:2014.0
Provides:	osgi(org.eclipse.emf.activities) = 2.6.0
Provides:	osgi(org.eclipse.emf.examples) = 2.6.0
Provides:	osgi(org.eclipse.emf.examples.databinding.project.core) = 1.0.0
Provides:	osgi(org.eclipse.emf.examples.databinding.project.core.model) = 1.0.0
Provides:	osgi(org.eclipse.emf.examples.databinding.project.ui.rcp) = 1.1.0
Provides:	osgi(org.eclipse.emf.examples.generator.validator) = 1.2.0
Provides:	osgi(org.eclipse.emf.examples.jet.article2) = 2.4.0
Provides:	osgi(org.eclipse.emf.examples.library) = 2.5.0
Provides:	osgi(org.eclipse.emf.examples.library.edit) = 2.5.0
Provides:	osgi(org.eclipse.emf.examples.library.editor) = 2.5.0
Provides:	osgi(org.eclipse.emf.examples.source) = 2.9.0
Provides:	osgi(org.eclipse.emf.exporter.html) = 2.6.0
Provides:	osgi(org.eclipse.emf.java) = 2.5.0
Provides:	osgi(org.eclipse.emf.java.edit) = 2.5.0
Provides:	osgi(org.eclipse.emf.java.editor) = 2.5.0

%description	-n eclipse-emf-examples
eclipse-emf-examples bootstrap version.

%files		-n eclipse-emf-examples
/usr/share/eclipse/dropins/emf-examples
/usr/share/eclipse/dropins/emf-examples/eclipse
/usr/share/eclipse/dropins/emf-examples/eclipse/features
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples.source_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-examples/eclipse/features/org.eclipse.emf.examples_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.activities_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.databinding.project.core.model_1.0.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.databinding.project.core_1.0.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.databinding.project.ui.rcp_1.1.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.generator.validator_1.2.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.jet.article2_2.4.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.library.edit_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.library.editor_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.library_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/META-INF
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/plugin.xml
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.core.model_1.0.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.core.model_1.0.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.core.model_1.0.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.core_1.0.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.core_1.0.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.core_1.0.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.ui.rcp_1.1.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.databinding.project.ui.rcp_1.1.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.generator.validator_1.2.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.generator.validator_1.2.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.generator.validator_1.2.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.jet.article2_2.4.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.jet.article2_2.4.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.jet.article2_2.4.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library.edit_2.5.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library.edit_2.5.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library.edit_2.5.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library.editor_2.5.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library.editor_2.5.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library.editor_2.5.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library_2.5.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library_2.5.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.examples.library_2.5.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.exporter.html_2.6.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.exporter.html_2.6.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.exporter.html_2.6.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java.edit_2.5.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java.edit_2.5.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java.edit_2.5.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java.editor_2.5.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java.editor_2.5.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java.editor_2.5.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java_2.5.0.v20130930-0823
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java_2.5.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java_2.5.0.v20130930-0823/release.digest
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java_2.5.0.v20130930-0823/release.properties
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java_2.5.0.v20130930-0823/release.xml
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples.source_2.9.0.v20130930-0823/src/org.eclipse.emf.java_2.5.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.examples_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.exporter.html_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.java.edit_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.java.editor_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-examples/eclipse/plugins/org.eclipse.emf.java_2.5.0.v20130930-0823.jar

#------------------------------------------------------------------------
%package	-n eclipse-emf-sdk
Version:	2.9.1
Release:	1.0
Summary:	eclipse-emf-sdk bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-emf = 2.9.1-1.0
Requires:	eclipse-pde >= 1:4.2.0
Requires:	java-javadoc
%if 0
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.emf.codegen.ecore.ui)
Requires:	osgi(org.eclipse.emf.common)
Requires:	osgi(org.eclipse.emf.common.ui)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.emf.importer)
Requires:	osgi(org.eclipse.emf.importer.java)
Requires:	osgi(org.eclipse.emf.importer.rose)
Requires:	osgi(org.eclipse.help)
Requires:	osgi(org.eclipse.jdt.core)
Requires:	osgi(org.eclipse.jface)
Requires:	osgi(org.eclipse.ui.cheatsheets)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.workbench)
%endif
Provides:	eclipse-emf-sdk = 2.9.1-1.0:2014.0
Provides:	osgi(org.eclipse.emf) = 2.6.0
Provides:	osgi(org.eclipse.emf.cheatsheets) = 2.5.0
Provides:	osgi(org.eclipse.emf.doc) = 2.7.0
Provides:	osgi(org.eclipse.emf.doc.source) = 2.8.0
Provides:	osgi(org.eclipse.emf.edit) = 2.9.0
Provides:	osgi(org.eclipse.emf.example.installer) = 1.3.0
Provides:	osgi(org.eclipse.emf.source) = 2.9.1

%description	-n eclipse-emf-sdk
eclipse-emf-sdk bootstrap version.

%files		-n eclipse-emf-sdk
/usr/share/eclipse/dropins/emf-sdk
/usr/share/eclipse/dropins/emf-sdk/eclipse
/usr/share/eclipse/dropins/emf-sdk/eclipse/features
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc.source_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.doc_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.edit_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.sdk_2.9.1.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.sdk_2.9.1.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.sdk_2.9.1.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.sdk_2.9.1.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.sdk_2.9.1.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.source_2.9.1.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.source_2.9.1.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.source_2.9.1.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.source_2.9.1.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf.source_2.9.1.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf_2.9.1.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf_2.9.1.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf_2.9.1.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf_2.9.1.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/features/org.eclipse.emf_2.9.1.v20130930-0823/license.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.cheatsheets_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/META-INF
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/plugin.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/src
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/src/org.eclipse.emf.cheatsheets_2.5.0.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/src/org.eclipse.emf.cheatsheets_2.5.0.v20130930-0823/about.html
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc.source_2.8.0.v20130930-0823/src/org.eclipse.emf.cheatsheets_2.5.0.v20130930-0823/src.zip
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.doc_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.edit_2.9.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.example.installer_1.3.0.v20130930-0823.jar
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.source_2.9.1.v20130930-0823
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.source_2.9.1.v20130930-0823/META-INF
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.source_2.9.1.v20130930-0823/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf.source_2.9.1.v20130930-0823/plugin.xml
/usr/share/eclipse/dropins/emf-sdk/eclipse/plugins/org.eclipse.emf_2.6.0.v20130930-0823.jar

#------------------------------------------------------------------------
%package	-n eclipse-emf-xsd
Version:	2.9.1
Release:	1.0
Summary:	eclipse-emf-xsd bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-emf = 2.9.1-1.0
%if 0
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.emf.ecore.edit)
Requires:	osgi(org.eclipse.emf.ecore.xmi)
Requires:	osgi(org.eclipse.emf.edit)
Requires:	osgi(org.eclipse.emf.edit.ui)
Requires:	osgi(org.eclipse.emf.exporter)
Requires:	osgi(org.eclipse.emf.importer)
Requires:	osgi(org.eclipse.emf.mapping)
Requires:	osgi(org.eclipse.emf.mapping.ui)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
%endif
Provides:	eclipse-emf-xsd = 2.9.1-1.0:2014.0
Provides:	osgi(org.eclipse.emf.mapping.xsd2ecore) = 2.5.0
Provides:	osgi(org.eclipse.emf.mapping.xsd2ecore.editor) = 2.6.0
Provides:	osgi(org.eclipse.xsd) = 2.9.0
Provides:	osgi(org.eclipse.xsd.ecore.converter) = 2.6.0
Provides:	osgi(org.eclipse.xsd.ecore.exporter) = 2.5.0
Provides:	osgi(org.eclipse.xsd.ecore.importer) = 2.7.0
Provides:	osgi(org.eclipse.xsd.edit) = 2.6.0
Provides:	osgi(org.eclipse.xsd.editor) = 2.6.0
Provides:	osgi(org.eclipse.xsd.mapping) = 2.6.0
Provides:	osgi(org.eclipse.xsd.mapping.editor) = 2.7.0

%description	-n eclipse-emf-xsd
eclipse-emf-xsd bootstrap version.

%files		-n eclipse-emf-xsd
/usr/share/doc/eclipse-emf-xsd
/usr/share/doc/eclipse-emf-xsd/epl-v10.html
/usr/share/doc/eclipse-emf-xsd/notice.html
/usr/share/eclipse/dropins/xsd
/usr/share/eclipse/dropins/xsd/eclipse
/usr/share/eclipse/dropins/xsd/eclipse/features
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.ecore.converter_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.ecore.converter_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.ecore.converter_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.ecore.converter_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.ecore.converter_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.edit_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.edit_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.edit_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.edit_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.edit_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.editor_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.editor_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.editor_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.editor_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.editor_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping.editor_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping.editor_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping.editor_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping.editor_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping.editor_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd.mapping_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd/eclipse/features/org.eclipse.xsd_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd/eclipse/plugins
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.emf.mapping.xsd2ecore.editor_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.emf.mapping.xsd2ecore_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd.ecore.converter_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd.ecore.exporter_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd.ecore.importer_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd.edit_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd.editor_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd.mapping.editor_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd.mapping_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd/eclipse/plugins/org.eclipse.xsd_2.9.0.v20130930-0823.jar

#------------------------------------------------------------------------
%package	-n eclipse-emf-xsd-sdk
Version:	2.9.1
Release:	1.0
Summary:	eclipse-emf-xsd-sdk bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-emf-sdk = 2.9.1-1.0
Requires:	eclipse-emf-xsd = 2.9.1-1.0
Requires:	eclipse-pde >= 1:4.2.0
Requires:	java-javadoc
%if 0
Requires:	osgi(org.eclipse.emf.cheatsheets)
Requires:	osgi(org.eclipse.emf.common.ui)
Requires:	osgi(org.eclipse.help)
Requires:	osgi(org.eclipse.ui.cheatsheets)
Requires:	osgi(org.eclipse.xsd)
Requires:	osgi(org.eclipse.xsd.ecore.importer)
%endif
Provides:	eclipse-emf-xsd-sdk = 2.9.1-1.0:2014.0
Provides:	osgi(org.eclipse.emf.mapping.xsd2ecore.editor.source) = 2.6.0
Provides:	osgi(org.eclipse.emf.mapping.xsd2ecore.source) = 2.5.0
Provides:	osgi(org.eclipse.xsd.cheatsheets) = 2.6.0
Provides:	osgi(org.eclipse.xsd.cheatsheets.source) = 2.6.0
Provides:	osgi(org.eclipse.xsd.doc) = 2.7.0
Provides:	osgi(org.eclipse.xsd.doc.source) = 2.7.0
Provides:	osgi(org.eclipse.xsd.edit.source) = 2.6.0
Provides:	osgi(org.eclipse.xsd.editor.source) = 2.6.0
Provides:	osgi(org.eclipse.xsd.example.installer) = 1.2.0
Provides:	osgi(org.eclipse.xsd.mapping.editor.source) = 2.7.0
Provides:	osgi(org.eclipse.xsd.mapping.source) = 2.6.0

%description	-n eclipse-emf-xsd-sdk
eclipse-emf-xsd-sdk bootstrap version.

%files		-n eclipse-emf-xsd-sdk
/usr/share/eclipse/dropins/xsd-sdk
/usr/share/eclipse/dropins/xsd-sdk/eclipse
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc.source_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc.source_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc.source_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc.source_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc.source_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.doc_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.edit.source_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.edit.source_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.edit.source_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.edit.source_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.edit.source_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.editor.source_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.editor.source_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.editor.source_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.editor.source_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.editor.source_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.editor.source_2.8.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.editor.source_2.8.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.editor.source_2.8.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.editor.source_2.8.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.editor.source_2.8.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.source_2.7.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.source_2.7.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.source_2.7.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.source_2.7.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.mapping.source_2.7.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.sdk_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.sdk_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.sdk_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.sdk_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.sdk_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.source_2.9.0.v20130930-0823
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.source_2.9.0.v20130930-0823/epl-v10.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.source_2.9.0.v20130930-0823/feature.properties
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.source_2.9.0.v20130930-0823/feature.xml
/usr/share/eclipse/dropins/xsd-sdk/eclipse/features/org.eclipse.xsd.source_2.9.0.v20130930-0823/license.html
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.emf.mapping.xsd2ecore.editor.source_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.emf.mapping.xsd2ecore.source_2.5.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.cheatsheets.source_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.cheatsheets_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.doc.source_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.doc_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.edit.source_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.editor.source_2.6.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.example.installer_1.2.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.mapping.editor.source_2.7.0.v20130930-0823.jar
/usr/share/eclipse/dropins/xsd-sdk/eclipse/plugins/org.eclipse.xsd.mapping.source_2.6.0.v20130930-0823.jar

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
rpm2cpio %{SOURCE3} | cpio -id
rpm2cpio %{SOURCE4} | cpio -id
rpm2cpio %{SOURCE5} | cpio -id
