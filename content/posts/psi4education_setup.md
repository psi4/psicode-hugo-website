---
title: "Installing Psi4 for Psi4Education labs"
date: 2020-07-31
draft: false
image: images/psi4banner_education.png
---

To use any of the Psi4Education jupyter notebook labs, you will need to create a psi4 environment.  We recommend the all-in-one python package manager Anaconda.

## Install Anaconda or Miniconda
1. Navigate to the [download page](https://www.anaconda.com/products/individual).
2. Download the appropriate installer for your operating system. **Be sure you get the installer listed under Python 3 (not 2).**
3. Double click the installer and follow the setup instructions, keeping most of the default options.  If you are on Windows, make sure to choose the option **Make Anaconda the default Python** during installation.

Note: Anaconda is a rather large download. It automatically installs lots of useful python packages. If you would prefer to save space on your computer, you can [install miniconda](https://docs.conda.io/en/latest/miniconda.html), which will not install a lot of these extra packages.

## Create a conda environment for Psi4
Environments let you install a particular set of packages, without messing up anything else you already have installed on your computer. We recommend setting up a conda environment for using psi4.

1. Open a Terminal window.  If you are on a Mac, there is a built-in Terminal application called Terminal. If you are on Windows, Anaconda installs a Terminal program called the Anaconda prompt.
2. Create a new environment for psi4 called p4env. \\
```
conda create --name p4env
```
3. Activate the psi4 environment. \\
```
conda activate p4env
```

## Install necessary python packages.
Most Psi4Education Jupyter notebook labs use Psi4, matplotlib, and numpy; instructions for installing these packages are given below. A few use additional packages as well.  If additional packages are required, this information is provided in the instructor notes for that lab.

4. Install psi4 in the environment.  Use the correct command for your operating system. \\
Mac/Linux \\
```
conda install psi4 psi4-rt python=3.7 -c psi4
```
\\
Windows \\
```
conda install -c raimis -c psi4 -c conda-forge psi4=1.3.2
```
5. Install matplotlib in the psi4 environment; numpy is automatically installed with psi4. \\
```
conda install -c conda-forge matplotlib
```
\\
6. Install jupyter notebook. \\
```
conda install -c conda-forge notebook
```
5. Start a jupyter notebook.  
```
jupyter notebook
```
6. Once you have started a juypter notebook, you can either create a new juypter notebook or open one that you downloaded.  While you only need to install all the software once, you will need to activate your psi4 environment before starting your jupyter notebook anytime you want to use psi4. \\
```
conda activate p4env
```
