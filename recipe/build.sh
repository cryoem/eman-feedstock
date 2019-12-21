#!/bin/bash

set -xe

build_dir="${SRC_DIR}/../build_eman"

rm -rf $build_dir
mkdir -p $build_dir
cd $build_dir

cmake --version
if [[ ${HOST} =~ .*linux.* ]]; then
    cmake $SRC_DIR -DCMAKE_TOOLCHAIN_FILE="${RECIPE_DIR}/cross-linux.cmake" -DENABLE_OPTIMIZE_MACHINE=ON -DENABLE_WARNINGS=OFF
else
    cmake $SRC_DIR -DENABLE_WARNINGS=OFF
fi

make -j${CPU_COUNT}
make install
