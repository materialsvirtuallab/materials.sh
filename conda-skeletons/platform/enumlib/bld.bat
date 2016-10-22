#!/bin/bash

SET BINARY=enum
SET BINARY_HOME=%PREFIX%\bin

git clone https://github.com/msg-byu/enumlib.git
git clone https://github.com/msg-byu/symlib.git

cd %SRC_DIR%\symlib\src

SET F90=gfortran
make

cd %SRC_DIR%\enumlib\src

make
make enum.x
make makestr.x

copy enum.x %BINARY_HOME%
copy makestr.x %BINARY_HOME%
