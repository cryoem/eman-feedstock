About eman
==========

Home: http://blake.bcm.edu/emanwiki/EMAN2

Package license: 

Feedstock license: BSD 3-Clause

Summary: A scientific image processing software suite with a focus on CryoEM and CryoET



Current build status
====================

Linux: [![Circle CI](https://circleci.com/gh/cryoem/eman-feedstock.svg?style=shield)](https://circleci.com/gh/cryoem/eman-feedstock)
OSX: [![TravisCI](https://travis-ci.org/cryoem/eman-feedstock.svg?branch=master)](https://travis-ci.org/cryoem/eman-feedstock)
Windows: [![AppVeyor](https://ci.appveyor.com/api/projects/status/github/cryoem/eman-feedstock?svg=True)](https://ci.appveyor.com/project/cryoem/eman-feedstock/branch/master)

Current release info
====================
Version: [![Anaconda-Server Badge](https://anaconda.org/cryoem/eman/badges/version.svg)](https://anaconda.org/cryoem/eman)
Downloads: [![Anaconda-Server Badge](https://anaconda.org/cryoem/eman/badges/downloads.svg)](https://anaconda.org/cryoem/eman)

Installing eman
===============

Installing `eman` from the `cryoem` channel can be achieved by adding `cryoem` to your channels with:

```
conda config --add channels cryoem
```

Once the `cryoem` channel has been enabled, `eman` can be installed with:

```
conda install eman
```

It is possible to list all of the versions of `eman` available on your platform with:

```
conda search eman --channel cryoem
```




Updating eman-feedstock
=======================

If you would like to improve the eman recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`cryoem` channel, whereupon the built conda packages will be available for
everybody to install and use from the `cryoem` channel.
Note that all branches in the cryoem/eman-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](http://conda.pydata.org/docs/building/meta-yaml.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](http://conda.pydata.org/docs/building/meta-yaml.html#build-number-and-string)
   back to 0.