#!/bin/bash

BINARY=enum
BINARY_HOME=$PREFIX/bin

git clone --recursive https://github.com/msg-byu/enumlib.git

cd $SRC_DIR/enumlib/symlib/src

export F90=gfortran
make

cd $SRC_DIR/enumlib/src

make
make enum.x
make makestr.x

cp enum.x $BINARY_HOME
cp makestr.x $BINARY_HOME

# Cleanup.
rm -rf $SRC_DIR/enumlib
