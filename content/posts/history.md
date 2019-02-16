---
title: "History"
date: 2019-02-03T02:17:19-05:00
draft: false
---

The Psi package originated in the group of Prof. Henry F. Schaefer while
he was at the University of California, Berkeley. The code featured a
direct CI code (written in 1976 by Robert Lucchese), a graphical unitary
group configuration interaction (GUGA-CI) code (written in 1977-79 by
Bernard Brooks and later extended to the shape-driven GUGA-CI code by Paul
Saxe), and a Gaussian integral code (written in 1978 by Russell Pitzer).
The code was originally known as the `BERKELEY` suite; it was renamed to
Psi after the Schaefer group moved to the University of Georgia. Curt
Janssen and Ed Seidl ported the package to UNIX and started converting it
from Fortran to C. Psi2 featured coupled-cluster codes developed by Curt
Janssen, Gustavo Scuseria, and others, and the `INTDER` vibrational
analysis and derivative transformation program by Wesley Allen.

Development of `Psi3` began in 1999. Much of the infrastructure code was
rewritten to be more flexible on different architectures and to remove
hardwired limits on the number of atoms, basis functions, file sizes, etc.
The new code, developed primarily by Daniel Crawford, David Sherrill, and
Edward Valeev, featured rewritten coupled-cluster code (including
excited-state capabilities), very efficient determinant-based CI code, and
multi-configurational self-consistent-field capabilities. Later releases
of `Psi3` added the first production-level implementation of Mukherjee's
multi-reference coupled-cluster method (`PSIMRCC`), thanks to Francesco
Evangelista and Andy Simmonett. Psi3 was released free of charge under an
open-source license.

Development of PSI4 began around 2007. PSI4 introduces a completely new
input parser and driver program which were designed with two goals in
mind: (1) to make the input as user-friendly as possible, and (2) to make
complex tasks very easy to perform. This work was performed primarily by
Andy Simmonett, Justin Turney, and Lori Burns. Standard computations are
specified by a very simple syntax, but the user is also free to add Python
code to the input file in order to automate more complex procedures (such
as potential energy scans). Built-in Python subroutines handle procedures
like counterpoise correction and basis set extrapolation. A new database
functionality, developed by Lori Burns, allows the program to
automatically perform a series of computations on all members in a given
collection of molecules (and tabulate errors against benchmark energies in
the database, if desired). A PSI4 interface to the WebMO graphical user
interface, released in 2013, was developed by Ashley Ringer McDonald and
Matthew Kennedy, with contributions from Eugene DePrince.

A new layer of utility functions was developed by Justin Turney in 2009-12
to make it easier for developers to implement new functionality in PSI4.
Especially important is the `LIBMINTS` library which makes it easier to
access one- and two-electron integrals from the underlying `LIBINT`
library of Edward Valeev (the `LIBINT` library is based on work in the
late 1990's by Justin Fermann and Edward Valeev). Following up on earlier
work and suggestions by Edward Valeev that we migrate Psi to an
object-oriented C++ design, Justin Turney also developed various C++
classes for basis sets, molecules, and wavefunctions, inspired by similar
work done much earlier by the Massively Parallel Quantum Chemistry
(`MPQC`) package; work on these classes is ongoing. To ease the path
toward adding distributed-parallel capabilities, PSI4 moved the code to a
"single-executable" model, away from the previous model in which each
program module (integrals, SCF, etc.) was a separate executable program,
with information passed by files.

Other new features developed for PSI4 include a new ``plugin'' system,
written by Justin Turney and Andy Simmonett, that allows developers to
create a new feature for PSI4 in a standalone module that can be compiled
separately and loaded at runtime. This helps decouple development of the
core PSI4 capabilities from the development of new features, shortening
the development cycle. Edward Hohenstein wrote a new, efficient
density-fitted symmetry-adapted perturbation theory (SAPT) code for PSI4
in 2010-11. A newer SAPT code was developed by Rob Parrish in 2014-15 to
allow atomic- and fragment-based partitioning of the energies (A-SAPT and
F-SAPT) and intramolecular SAPT (I-SAPT). Rob also brought density
functional theory (DFT) capabilities to PSI4 in 2011-12. The DFT framework
allows any functional to be entered into MATLAB, and using
automatic-differentiation techniques, C++ code is automatically generated.
This allows PSI4 to include essentially all popular density functionals. A
new density-fitted/Cholesky decomposition (DF/CD) coupled-cluster code for
CCSD(T) energies was added by Eugene DePrince in 2013. The DF/CD
approximations work very well in concert with Frozen Natural Orbitals
(FNO's), a capability also released in 2013.

In 2012-14, Alex Sokolov added several variants of density cumulant
functional theory to PSI4. Ugur Bozkaya added several analytic gradient
methods from 2012-15, including MP2, MP3, MP2.5, CEPA(0), and optimized
orbital versions of all these. Density-fitted versions of MP2 (including
UHF references) and optimized-orbital MP2 analytic gradients were also
added. In 2015, Dr. Bozkaya added density-fitted CCSD analytic gradients.

Lori Burns introduced numerous major generalizations of the PSI4 driver
from 2014-15, allowing it to call features from other programs like
`CFOUR` and `MOLPRO` and perform basic combinations of these results with
PSI4 results. This formed the basis of our current project to develop a
Common Driver for Quantum Chemistry. In early 2016, Daniel Smith and Lori
Burns changed the way information is passed from one module to another in
PSI4, using the Wavefunction object. This new mechanism allowed orbitals
to be passed between modules in a more flexible way, and it allowed
operations like exporting natural orbitals to `Molden` for plotting, etc.
Interfaces to additional external projects like libefp, GDMA, ChemPS2, and
PCMSolver were added or extended. With these additions, the longstanding
"Beta" tag was removed and PSI4 1.0 was released in July 2016, with both
source code and pre-packaged binaries available for Linux and Mac.

Substantial additional changes to the driver were made in 2016 by Lori
Burns and Daniel Smith, allowing us to make PSI4 a full-fledged Python
library (wrapping a C++ core). This allows users to call PSI4 from a
Python script, and greatly simplifies interoperability with other Python
modules. Also in 2016, the code attained analytic RHF CCSD(T) gradients,
analytic RHF Hessians, and fragment-based, intramolecular, and open-shell
SAPT. Support for Grimme's semi-empirical HF-3C and PBEh-3C was also
added. The 1.1 release was announced at the 2016 SETCA meeting, and an
accompanying paper was published by J. Chem. Theory Comput.

## [Psi Publications]({{< ref "software_pubs.md" >}})

## [Cumulative Psi Author List](https://github.com/psi4/psi4/blob/master/codemeta.json)

{{< cmAuthors url="https://raw.githubusercontent.com/psi4/psi4/master/codemeta.json" >}}

