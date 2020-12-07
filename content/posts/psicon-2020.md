---
title: "PsiCon 2020 and Psi4Education Meetings — Virtual"
date: 2020-11-25
author: David Sherrill
image: images/blog/psicon-2020.png
description : "annual psi developers meeting 2020"
categories: ["events"]
---

# Meeting Time and Location

This year's meeting will be held virtually over BlueJeans.
The program is shown below.
Participants are welcome to attend any or all days.
Optional tutorials and breakout sessions will be held in the afternoons.
[Registration](https://forms.gle/S63JcyRgM5DpihGE8) is free.
Mornings will be 10am-12pm; all times in Eastern Standard Time.

# Participating Institutions, Speakers

* Auburn University
* Belhaven University
* Bethel University
* BrianQC
* Cal Poly San Luis Obispo 
* Emory University
* Entos
* European National Competence Centre Sweden
* Florida State University
* Georgia Institute of Technology
* Hacettepe University
* Institute of Biophysics of the Czech Academy of Sciences
* National Institutes of Health
* OpenEye Scientific Software
* Princeton University
* Purdue University
* Sandia National Laboratories
* University of Georgia
* University of Heidelberg
* University of Richmond
* Virginia Tech

<!--
# Participating Institutions, Attendees

* Auburn University
* Belhaven University
* Bethel University
* BrianQC
#* Bristol-Myers Squibb
* Cal Poly San Luis Obispo 
* Emory University
* Entos
* European National Competence Centre Sweden
* Florida State University
#* Franklin & Marshall College
#* Fritz Haber Institute
* Georgia Institute of Technology
#* Georgia Southern University
#* Georgia State University
* Hacettepe University
#* Hylleraas Centre for Quantum Molecular Sciences
* Institute of Biophysics of the Czech Academy of Sciences
#* Khalifa University
#* McMaster University
#* Morehouse College
* National Institutes of Health
#* Open Force Field Initiative / MSKCC
* OpenEye Scientific Software
#* Pontificia Universidad Católica de Chile
* Princeton University
* Purdue University
* Sandia National Laboratories
#* Universidad de Concepción
#* University of California, Berkeley
* University of Georgia
* University of Heidelberg
#* University of Mississippi
#* University of Oxford
* University of Richmond
* Virginia Tech

-->

# PsiCon 2020 Agenda

### Thursday, December 3
#### Users Day

* 9:45am--10:00am --- Meeting open for login
* 10:00am-10:30am --- [General introduction to Psi4](https://www.youtube.com/watch?v=1WybjSppXTg) -- Daniel Crawford, Virginia Tech, and David Sherrill, Georgia Tech
* 10:30am--10:40am --- What's new in Psi4 1.4 -- David Sherrill, Georgia Tech, and contributors
* 10:40am--10:50am --- [GPU Computing with Psi4 and BrianQC](https://www.youtube.com/watch?v=PT7dWp6aAEQ) -- István Ladjánszki, BrianQC
* 10:50am--10:55am --- How to Get Psi4 -- Lori Burns, Georgia Tech [(slides)](https://github.com/psi4/PsiCon2020/blob/master/LoriBurns_2020_How-to-get-Psi4.pdf)
* 10:55am--11:10am --- [The PyOptKing optimizer](https://www.youtube.com/watch?v=WQBvTRbLPvc) -- Rollin King, Bethel University
* 11:10am--11:20am --- Break
* 11:20am--11:35am --- [Introduction to Psi4Education](https://www.youtube.com/watch?v=uhNjFcTsGo8) -- Ashley McDonald, Cal Poly
* 11:35am--11:50am --- [Using Psi4 through Jupyter for Teaching](https://www.youtube.com/watch?v=ItNdmODVgp0) -- Francesco Evangelista, Emory University
* 11:50am--12:20pm --- Lightning Talks
  1. [Using Psi4 for Crystal Structure Prediction](https://www.youtube.com/watch?v=DW3DHnFqspI) -- Tom Darden, OpenEye Scientific Software
  1. [Quantum-based Structure Refinement of Biomolecules](https://www.youtube.com/watch?v=d_1jgrcyIuA) -- Holger Kruse, Institute of Biophysics of the Czech Academy of Sciences
  1. Polymer Featurization with Psi4 on the Azure Cloud -- Carlos Borca, Princeton
  1. [Using MBIS in Psi4 1.4](https://www.youtube.com/watch?v=9oIuK2O6TLg) -- Andy Jiang, Georgia Tech
  1. [Dataset Generation with Psi4: Fitting Force Fields and Machine Learning Models](https://www.youtube.com/watch?v=lKBJmj2GgVw) -- Zach Glick, Georgia Tech
* 1:30pm-2:30pm: Tutorial for Psi4 Users
  1. [Basic Introduction to Using Psi4](https://www.youtube.com/watch?v=Z0gmVDI5mkQ) -- David Sherrill, Georgia Tech
  1. [Using Symmetry-Adapted Perturbation Theory in Psi4](https://www.youtube.com/watch?v=mKhbBoiklNE) -- Zach Glick, Georgia Tech [(repo)](https://github.com/zachglick/PsiCon2020-SAPT)
  1. [TDDFT Computations in Psi4, and Using the Python API](https://www.youtube.com/watch?v=MmG-g3SEFbk) -- Roberto Di Remigio, European National Competence Centre Sweden

### Friday, December 4
#### Developers Day

* 9:45am--10:00am --- Meeting open for login
* 10:00am--11:00am --- Overview of Recent Infrastructure Changes
* 10:00am--10:15am --- Psithon, PsiAPI, and QCSchema: Data Paths to Use Psi4 -- Lori Burns, Georgia Tech [(repo)](https://github.com/psi4/PsiCon2020/blob/master/LoriBurns_2020_Psithon-PsiAPI-QCSchema.ipynb)
* 10:15am--10:20am --- The Distributed Driver -- Lori Burns, Georgia Tech [(slides)](https://github.com/psi4/PsiCon2020/blob/master/LoriBurns_2020_Distributed-driver.pdf)
* 10:20am--10:40am ---The QCArchive Infrastructure and Psi4 -- Daniel Smith, Entos
* 10:40am--10:50am --- The Upgrade to libint2, Andy Simmonett, NIH
* 10:50am--11:00am --- DFT Grid Options, Pruning, and Density Screening, Holger Kruse
* 11:00am--11:10am --- Break
* 11:10am--11:20am --- Linear Scaling Coupled-Cluster Methods -- Ugur Bozkaya, Hacettepe University
* 11:20am--12:00pm --- Lightning talks by developers
  1. Coupled-Cluster-Based Descriptions of Photon-Electron Interactions -- Eugene DePrince, Florida State University
  1. Revisiting the Hellmann-Feynman Theorem -- Joshua Rackers, Sandia National Laboratories
  1. CLIFF:A Machine-Learned, Component-Based Intermolecular Force Field -- Jeff Schriber, Georgia Tech
  1. Polarizable Embedding in Psi4 -- Maximilian Scheurer, University of Heidelberg
  1. Multicore and Psi4 -- David Sherrill, Georgia Tech
  1. Diagrammatic Coupled Cluster Monte Carlo -- Roberto Di Remigio, European National Competence Centre Sweden
  1. The HelPME Library for Periodic Calculations -- Andy Simmonett, NIH
* 1:30pm--3:00pm --- Tutorial for New Psi4 Developers
  1. How to Make Simple Changes to Psi4 -- Jeff Schriber, Georgia Tech
  1. [How to Use the libmints Library](https://www.youtube.com/watch?v=dvzS3RwL6Do) -- Justin Turney, University of Georgia
  1. Where in Psi4 is X? -- Lori Burns, Georgia Tech
  1. How to Compile Psi4 (without Compilers) -- Lori Burns, Georgia Tech

### Saturday, December 5
#### Psi4Education Day

* 9:45am--10:00am --- Meeting open for login
* 10:00am--10:20am --- [Psi4Education General Update](https://www.youtube.com/watch?v=x3zqC4vJKSw) -- Ashley McDonald, CalPoly
* 10:20am--11:00am --- Lightning Talks Highlighting the Newest Labs
  1. Intermolecular Interactions and Symmetry-Adapted Perturbation Theory -- Konrad Patkowski, Auburn University
  1. Determining Structure from Microwave Spectroscopy -- Brandon Magers, Belhaven University
  1. Machine Learning in Computational Chemistry -- Ben Peyton, Virginia Tech [(repo)](https://github.com/Psi4Education/psi4education/blob/master/labs/Machine_Learning/Machine_Learning_Student.ipynb)
  1. Analysis of Basis Sets in Quantum Chemistry Calculations -- Victor H. Chavez, Purdue University [(repo)](https://github.com/Psi4Education/psi4education/blob/master/labs/Basis_Sets/Basis_Sets_student.ipynb)
* 11:00am--11:20am --- How to Contribute to Psi4Education
* 11:20am--12:00pm --- Discussion/Brainstorm New Lab Ideas

