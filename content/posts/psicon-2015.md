---
title: "Developers' Conference 2015 — Emory"
date: 2015-11-13
author: David Sherrill
image: images/blog/psicon-2015-lowres.jpg
description : "annual psi developers meeting 2015"
categories: ["events"]
aliases:
    - /workshop_nov_2015.php
---

# Meeting Summary
The meeting was held Friday and Saturday, Nov 13-14, at Emory featuring participants from 7 institutions. 36 people attended in person at Emory. The following are outcomes of the meeting:

* The Ambit library seems to be working well for shared-memory systems. We will attempt to adopt Ambit for tensors in shared-memory and distributed-memory environments.
* We will aim to adopt Lightspeed when it becomes available. The Lightspeed classes can serve as a template for communications between modules in Psi4.
* We will work towards removing the legacy libchkpt calls in Psi4 and pass info by Wavefunction objects and/or a new inter-module communication prototol.
* We will move towards a regular release cycle for stable releases. At the same time, we will continue making bugfixes and improvements available on a continuous basis via psi4public and the nightly binaries.
* Regular development is supposed to be done in psi4public now on github. Any code that is not ready to be released, but which requires access to collaborators, may be put in a branch of psi4 (private repo). Anything put in the main branch of psi4 will be regularly synchronized with psi4public.
* We will aim to develop and start adopting a more general library for communication between modules; this will facilitate interoperability with other (non-Psi4) codes.

# Participating Institutions

* Emory University
* University of Georgia
* Virginia Tech
* Georgia Tech
* Florida State University
* Auburn University
* NIH

# Agenda

### Friday, November 13

* 9:30am-10:00am: Welcome (coffee and doughnuts provided)
* 10:00am-11:00am: Update Session 1
	* Lori Burns: Psi4.0 Update and Plans [(slides)](https://github.com/psi4/PsiCon2020/blob/master/PsiCon2015/psi4-11-2015-lori.pdf)
	* Ben Pritchard: Framework for Interoperability
	* Daniel Crawford: The Future of Psi4
* 11:00am-11:15am: Coffee Break
* 11:15am-12:30pm: Update Session 2
	* Francesco Evangelista: Intro to Ambit
	* Justin Turney: CT and DCFT in Psi4 and Future Ambit plans
	* Rob Parrish: Lightspeed
* 12:30pm-1:30pm: Lunch
* 1:30pm-1:45pm: Lori Burns: Psi Licensing
* 1:45pm-2:00pm: David Sherrill: Psi Management Structure
* 2:00pm-5:00pm: Breakout Sessions
	* Passing information in Psi4
	* Psi4 1.0 Release

### Saturday, November 14

* 10:00am-10:30pm: Reports from Saturday discussions
* 10:30am-12:30pm: Infrastructure discussions and hacking
* 12:30pm: Meeting adjourned
