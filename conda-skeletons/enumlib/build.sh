#!/bin/bash

BINARY=enum
BINARY_HOME=$PREFIX/bin

git clone https://github.com/msg-byu/enumlib.git
git clone https://github.com/msg-byu/symlib.git

#unzip symlib
#unzip enumlib

cd $SRC_DIR/symlib/src

export F90=gfortran
make

cd $SRC_DIR/enumlib/src

make
make enum.x
make makestr.x

cp enum.x $BINARY_HOME
cp makestr.x $BINARY_HOME

# Cleanup.
rm -rf $SRC_DIR/symlib
rm -rf $SRC_DIR/enumlib
