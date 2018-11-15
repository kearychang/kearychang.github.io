---
layout: post
title:  "BCNF/3NF Generator"
date:   2018-11-14
excerpt: "Decompose your table to BCNF/3NF format."
project: true
tag:
- frontend
- algorithm
comments: true
---

![BCNF/3NF Generator Homepage](https://raw.githubusercontent.com/kearychang/kearychang.github.io/master/assets/post-project/bcnf-3nf.png)    
    
<center>Decompose your table to BCNF/3NF format.</center>
     
This [project](https://kearychang.github.io/BCNF-3NFgenerator/) was to implement 2 algorithms for breaking up a table so would be in Boyce Codd Normal Form or 3 Normal Form. When you put all your attributes in a single table, you get
* redundancies
* deletion anomalies
* update anomalies
* insertion anomalies

To avoid this, we decompose our table. This has to be done properly so the original information is retrieved, meaning there is no loss or extraneous information.

---

**Input**
* Number of attributes in your table (<=10)
* Functional Dependencies

**Output**
* Decomposed Tables

---

![Output](https://raw.githubusercontent.com/kearychang/kearychang.github.io/master/assets/post-project/bcnf-3nf2.png)

More indepth tutorial is on my [Readme](https://github.com/kearychang/BCNF-3NFgenerator/blob/master/README.md).
The site walks you through the algorithm and intermediate steps.
Source code is public so you can study its implementation [here](https://github.com/kearychang/BCNF-3NFgenerator/blob/master/fd.js).