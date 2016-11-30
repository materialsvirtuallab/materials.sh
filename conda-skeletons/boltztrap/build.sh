#!/bin/bash

BINARY=BoltzTrap
BINARY_HOME=$PREFIX/bin

export F90=gfortran
cd $SRC_DIR/src

make

cp BoltzTraP $BINARY_HOME
cp x_trans $BINARY_HOME

