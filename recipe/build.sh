#!/bin/bash

set -xe

build_dir="${SRC_DIR}/../build_eman"

rm -rf $build_dir
mkdir -p $build_dir
cd $build_dir

cmake --version
if [[ ${HOST} =~ .*linux.* ]]; then
    cmake $SRC_DIR -DCMAKE_TOOLCHAIN_FILE="${RECIPE_DIR}/cross-linux.cmake" -DENABLE_OPTIMIZE_COMPATIBILITY=ON -DENABLE_WARNINGS=OFF
elif [[ "$target_platform" == "osx-arm64" ]]; then
    cmake $SRC_DIR -DENABLE_WARNINGS=OFF ${CMAKE_ARGS}
else
    cmake $SRC_DIR -DENABLE_WARNINGS=OFF
fi

make -j${CPU_COUNT}
make install
