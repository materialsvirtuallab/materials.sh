#!/bin/bash

BINARY=bader
BINARY_HOME=$PREFIX/bin

# go to build
cd $SRC_DIR

# build source
# had to comment the setting of CMAKE_OSX_DEPLOYMENT_TARGET in
# /usr/local/Cellar/cmake/2.8.12.1/share/cmake/Modules/Platform/Darwin.cmake
cp makefile.osx_gfortran makefile
make
cp bader $BINARY_HOME
