---
title: "Psi4Education: Computational Labs Using Free Software"
date: 2020-07-30
image: images/psi4banner_education.png
draft: false
aliases:
    - /labs.php
---
Psi4Education is the education and outreach program of Psi4, the free, open-source quantum chemistry software package.  We offer a suite of free, open-source lab activities, suitable for use in classes across the chemistry curriculum, which use Psi4, the Psi4Numpy Python API, and WebMO, a graphical front end to help build molecules and set up calculations for Psi4.  Psi4Education aims to increase students exposure to scientific programming and computational chemistry and help students learn chemistry through computation.

## Getting Started

__[Installation and Setup Guide](https://docs.google.com/document/d/1bFqPYZidGyJ_MBXkayVISjsjepDXhvDaJ5BencBgkOg/edit?usp=sharing)__
Instruction for installing WebMO and Psi4, along with information about creating and administering user accounts.

__[Tutorial Lab for using WebMO](https://docs.google.com/document/d/1kZAGOTsjPRN_eoKvTxvnZ-V80fiXjjgib7V7uTj5xCM/edit?usp=sharing)__
This introductory lab introduces the key features of WebMO and Psi4, including building molecules, setting up calculations, and visualizing results.

__[About Psi4Education Jupyter Labs]({{< ref "psi4jupyter_labs.md" >}})__
Many of the lab activities use [Psi4Numpy](https://github.com/psi4/psi4numpy), the Psi4 Python API.  Psi4Numpy allows you to import and use Psi4 functions directly in Jupyter notebooks.  These labs assume some prerequisite knowledge of python.  See [this page]({{< ref "psi4jupyter_labs.md" >}}) for an explanation of these prerequisites.  If you need resources to learn these prerequisite skills, we recommend [these lessons](https://education.molssi.org/python_scripting_cms/) from the Molecular Sciences Software Institute.  Lessons 1, 4, and 5 cover all of the prerequisite skills needed.

## Resources for Instructors
Lab activities are distributed as Jupyter notebooks or PDF files.  Editable Jupyter notebooks can be downloaded from the links below.  LaTeX source documents for the PDF files are available through GitHub to instructors who register with Psi4Education.

Annotated instructors guides, including solutions, are available for all lab activities. If you would like to register with us and receive access to these materials, please [contact us](mailto:armcdona@calpoly.edu?subject=Psi4Education) with your name, university information, GitHub username, and a list of courses in which you might use the lab activities.

## Lab Activities

All of the lab activities can be found on the [Psi4Education GitHub repository](https://github.com/Psi4Education/psi4education) or downloaded from the links below. 

__[Understanding the Iterative Nature of the Hartree-Fock Procedure](https://github.com/Psi4Education/psi4education/blob/master/labs/Hartree_Fock/HF_student.ipynb)__ This lab activity is intended to teach students the mechanics of the Hartree-Fock procedure, without getting into the details of calculating the 1 and 2 electron integrals, by using the machinery of the Psi4 quantum chemistry software package. The lab emphasizes understanding why HF is an iterative procedure and what you calculate in one iteration that goes into the next iteration. Dirac notation and the relevant linear algebra Einstein summation notation is taught within the lab.  \\
[Right click to download](https://raw.githubusercontent.com/Psi4Education/psi4education/master/labs/Hartree_Fock/HF_student.ipynb) \\
*Jupyter notebook, physical chemistry*

__[Machine Learning in Computational Chemistry](https://github.com/Psi4Education/psi4education/blob/master/labs/Machine_Learning/Machine_Learning_Student.ipynb)__ This lab is meant to introduce students to simple machine-learning (ML) techniques and their application to computational chemistry problems. Students will learn to calculate a potential energy surface using Psi4, generate a Coulomb matrix representation for any molecule, and use linear and kernel ridge regression through the `scikit-learn` ML package to predict electronic and atomization energies from their own calculations and the pre-existing ANI-1 database. \\
[Right click to download](https://raw.githubusercontent.com/Psi4Education/psi4education/master/labs/Machine_Learning/Machine_Learning_Student.ipynb) \\
*Jupyter notebook, computational chemistry*

__[Determining Structure from Microwave Spectroscopy](https://github.com/Psi4Education/psi4education/blob/master/labs/Microwave_Spectroscopy/Microwave_Spectroscopy_student.ipynb)__ This lab activity is intended to show students the information that can be obtained from spectroscopic physical observables - specifically using rotational constants obtained from microwave spectroscopy to determine the geometry of a molecule, r0. Rotational constants can also be obtained computational using the Psi4 quantum chemistry software package. \\
[Right click to download](https://raw.githubusercontent.com/Psi4Education/psi4education/master/labs/Microwave_Spectroscopy/Microwave_Spectroscopy_student.ipynb) \\
*Jupyter notebook, physical chemistry*

__[Intermolecular Interactions and Symmetry-Adapted Perturbation Theory](https://github.com/Psi4Education/psi4education/blob/master/labs/Symmetry_Adapted_Perturbation_Theory/sapt0_student.ipynb)__ This lab activity is designed to teach students about weak intermolecular interactions, and the calculation and interpretation of the interaction energy between two molecules. The interaction energy can be broken down into physically meaningful contributions (electrostatics, induction, dispersion, and exchange) using symmetry-adapted perturbation theory (SAPT). \\
[Right click to download](https://raw.githubusercontent.com/Psi4Education/psi4education/master/labs/Symmetry_Adapted_Perturbation_Theory/sapt0_student.ipynb) \\
*Jupyter notebook, computational chemistry, interaction energies*

__[What is the radius of an atom?](https://github.com/Psi4Education/psi4education/blob/master/labs/Atomic_radius/Atom_radius_student.pdf)__
This lab will expose students to the way in which electrons define the size of an atom. It will demonstrate how the difference in nuclear-electronic interactions shift the size the atom for various trends including going across the periodic table for various charge states of a given atom. \\
[Right click to download](https://github.com/Psi4Education/psi4education/raw/master/labs/Atomic_radius/Atom_radius_student.pdf) \\
*WebMO, general chemistry*

__[What makes a molecule polar or non-polar?](https://github.com/Psi4Education/psi4education/blob/master/labs/Polarity/Polar_student.pdf)__
This lab will teach students how to use a Lewis structure to determine the electronic geometry and molecular shape of a molecule.  The students will use WebMO to calculate the partial charges on atoms in a molecule.  From this information they will draw bond dipole vectors.  Using WebMO, the students can visualize a 3D representation of the molecule and determine whether the bond dipole vectors cancel or not. \\
[Right click to download](https://github.com/Psi4Education/psi4education/raw/master/labs/Polarity/Polar_student.pdf) \\
*WebMO, general chemsitry*

__[Calculating Spectroscopic Constants from a Potential Energy Surface](https://github.com/Psi4Education/psi4education/blob/master/labs/spectroscopic_constants/spectroscopic_constants_student.ipynb)__ This lab uses psi4 functions imported into a Jupyter notebook to calculate the potential energy surfaces for diatomic molecules using psi4.  The students will graph the potential energy surfaces, study the affects of anharmonicity, and determine force constants. \\
[Right click to download](https://raw.githubusercontent.com/Psi4Education/psi4education/master/labs/spectroscopic_constants/spectroscopic_constants_student.ipynb) \\
*Jupyter notebook, quantum mechanics, spectroscopy*

__[How do we calculate the most accurate energies for a boron atom?](https://github.com/Psi4Education/psi4education/blob/master/labs/B_atom_basis_sets/Basis_Sets_student.ipynb)__
In order to gain a better understanding of how computational chemistry functions and what types of questions it answers, this lab calculates the energy of the boron atom using different basis sets and levels of theory. The students will see the patterns that emerge from the usage of basis sets as well as computational methods such as Hartree-Fock (HF/SCF), MP2/MP4, and CCSD/CCSD(T). Electron affinities and spin states are also discussed. \\
[Right click to download](https://raw.githubusercontent.com/Psi4Education/psi4education/master/labs/B_atom_basis_sets/Basis_Sets_student.ipynb) \\
*Jupyter notebook, quantum mechanics, computational chemistry*

__[Can we visually predict binding energies?](https://github.com/Psi4Education/psi4education/blob/master/labs/CationPi/CationPi_student.pdf)__
The role that visual depictions play in a student's understanding of abstract concepts can be quite substantial. This laboratory exercise depicts the density of the electron cloud around various aromatic systems. The students introduce a sodium cation into the system in a place that makes sense based on the location of the most electron density. The students are asked to make a semi-quantitative connection between what they are seeing in the electrostatic potential and the ultimate strength of the cationic binding energy. \\
[Right click to downlaod](https://github.com/Psi4Education/psi4education/raw/master/labs/CationPi/CationPi_student.pdf) \\
*WebMO, physical chemistry, interaction energies*

__[When does water become OH + H? (A study in molecular orbitals)](https://github.com/Psi4Education/psi4education/blob/master/labs/water_MO/waterMO_student.pdf)__
Molecular orbitals are the basis for bonding, the very essence of chemistry. In this laboratory, the students will create the water molecule and then begin to dissociate it in order to understand how bonding and molecular orbitals overlap. This lab can be done in conjunction with the PIB Molecular Orbitals lab to make a longer lab on molecular orbitals. \\
[Right click to download](https://github.com/Psi4Education/psi4education/raw/master/labs/water_MO/waterMO_student.pdf) \\
*WebMO, quantum mechanics*

__[What happens to the orbitals as a one-dimensional box gets longer? (A study in molecular orbitals)](https://github.com/Psi4Education/psi4education/blob/master/labs/PIB/Box1D_student.pdf)__
The particle-in-a-box model has long been used to explain the electronic absorption of linear carbon chains. This lab invites the student to explore this phenomenon within the realm of the molecular orbitals that allow the transitions to take place. This lab can be done in conjunction with the H2O Molecular Lab to make a longer, more traditional lab assignment. Further questions can be added by the instructor to augment the exercises incorporated herein. \\
[Right click to download](https://github.com/Psi4Education/psi4education/raw/master/labs/PIB/Box1D_student.pdf) \\
*WebMO, quantum mechanics, molecular orbital theory*

__[Is C<sub>3</sub>H<sup>+</sup> present in the Horsehead nebula?](https://github.com/Psi4Education/psi4education/blob/master/labs/Astrochem/CH3Spec_student.pdf)__
This is a lab to engage students in the search for a possible carrier of rotational lines observed in the Horsehead Nebula Photodissociation Region (PDR). Since rotational spectroscopy is the most reliable means for the detection of new molecules in the interstellar medium, this lab brings together computational chemistry and astrochemistry in novel ways. \\
[Right click to download](https://github.com/Psi4Education/psi4education/raw/master/labs/Astrochem/CH3Spec_student.pdf) \\
*WebMO, astrochemistry, computational chemistry*

__[What is symmetry in chemistry?](https://docs.google.com/document/d/1zWjGSYxi8Jy96fo5ahLty0cbAgFamwNlcDrjPE6LK1I/edit?usp=sharing)__
Symmetry is often a difficult concept for chemistry students to grasp without some type of visual or tangible tool. This laboratory aims to give students experience with immediate feedback in order to give them instantaneous and formative assessment of their skills. The students will perform designated tasks of assigning point group symmetries to given molecules as well as the converse where they must provide examples of molecules for certain point group symmetries. \\
*WebMO, quantum mechanics*

## Contributors

* Prof. Ashley Ringer McDonald, Cal Poly San Luis Obispo, Director, Psi4Education
* Victor H. Chavez, Purdue University
* Prof. Ryan C. Fortenberry, University of Mississippi
* Prof. D. Brandon Magers, Belhaven University
* Prof. Konrad Patkowski, Auburn University
* Dr. Tricia D. Shepherd, The POGIL Project
* Prof. C. David Sherrill, Georgia Tech
* Dr. Dominic Sirianni, University of Richmond
