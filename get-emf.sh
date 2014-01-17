#!/bin/sh
#actual tag to checkout
TAG=R2_9_1
XSD_TAG=R2_9_0
#name of the version to put in the source
VERSION=2.9.1

rm -rf org.eclipse.emf
rm -rf org.eclipse.xsd
rm -rf emf-$VERSION

git clone git://git.eclipse.org/gitroot/emf/org.eclipse.emf.git
pushd org.eclipse.emf
  git checkout $TAG
popd

git clone git://git.eclipse.org/gitroot/xsd/org.eclipse.xsd.git
pushd org.eclipse.xsd
  git checkout $XSD_TAG
popd


#mv org.eclipse.test emf-$VERSION/
#mv org.eclipse.ant.optional.junit emf-$VERSION/
mkdir emf-$VERSION/
mv org.eclipse.emf/{doc,examples,features,plugins,tests}/* emf-$VERSION/
cp -fr org.eclipse.xsd/{doc,examples,features,plugins}/* emf-$VERSION/
tar czf emf-$TAG.tar.gz emf-$VERSION

rm -rf org.eclipse.emf
rm -rf org.eclipse.xsd
rm -rf emf-$VERSION/