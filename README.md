About eman-dev-feedstock
========================

Feedstock license: [BSD-3-Clause](https://github.com/cryoem/eman-feedstock/blob/main/LICENSE.txt)



Package license: 

Summary: Eman development package

Current build status
====================


<table><tr>
    <td>GitHub Actions</td>
    <td>
      <a href="https://github.com/cryoem/eman-feedstock/actions/workflows/conda-build.yml">
        <img src="https://github.com/cryoem/eman-feedstock/actions/workflows/conda-build.yml/badge.svg?event=push&branch=main">
      </a>
    </td>
  </tr>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-eman--dev-green.svg)](https://anaconda.org/cryoem/eman-dev) | [![Conda Downloads](https://img.shields.io/conda/dn/cryoem/eman-dev.svg)](https://anaconda.org/cryoem/eman-dev) | [![Conda Version](https://img.shields.io/conda/vn/cryoem/eman-dev.svg)](https://anaconda.org/cryoem/eman-dev) | [![Conda Platforms](https://img.shields.io/conda/pn/cryoem/eman-dev.svg)](https://anaconda.org/cryoem/eman-dev) |

Installing eman-dev
===================

Installing `eman-dev` from the `cryoem` channel can be achieved by adding `cryoem` to your channels with:

```
conda config --add channels cryoem
conda config --set channel_priority strict
```

How to use
----------

<details>
<summary>With conda</summary>

```
conda install eman-dev
```

</details>

<details>
<summary>With mamba</summary>

```
mamba install eman-dev
```

</details>

<details>
<summary>With pixi</summary>

```
# for adding to your local project
pixi add eman-dev
# for installing globally
pixi global install eman-dev
```

</details>

Search package versions
-----------------------

It is possible to list all of the versions of `eman-dev` available on your platform:

<details>
<summary>With conda</summary>

```
conda search eman-dev --channel cryoem
```

</details>

<details>
<summary>With mamba</summary>

```
mamba search eman-dev --channel cryoem
```

</details>

<details>
<summary>With pixi</summary>

```
pixi search eman-dev --channel cryoem
```

</details>

<details>
<summary>With mamba repoquery, which may provide more information</summary>

```
# Search all versions available on your platform:
mamba repoquery search eman-dev --channel cryoem

# List packages depending on `eman-dev`:
mamba repoquery whoneeds eman-dev --channel cryoem

# List dependencies of `eman-dev`:
mamba repoquery depends eman-dev --channel cryoem
```

</details>




Updating eman-dev-feedstock
===========================

If you would like to improve the eman-dev recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`cryoem` channel, whereupon the built conda packages will be available for
everybody to install and use from the `cryoem` channel.
Note that all branches in the cryoem/eman-dev-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks, and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================


