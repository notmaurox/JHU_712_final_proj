# JHU_712_final_proj
Final project code repository for 410.712 (Advanced Practical Computer Concepts for Bioinformatics) Spring 2020 for a VADR web application

## About

VADR (Viral Annotation DefineR) is a software package for classifying and analyzing viral sequences against sets of reference genomes and is important because it serves as an institutional check that determines whether or not a submitted viral sequence is accepted into the GenBank database. In this project, I deployed VADR wrapped in a REST server to AWS (https://github.com/notmaurox/microVADR) and wrote the front end for the web app in this repo.

On the student server, my work directory is: `/var/www/html/mchavez8/final_exam`

The swagger UI for the VADR micro service can be found here: `http://13.56.20.142:5001/`. The server itself is running on an Amazon Linux 2 AMI t2.medium instance with 2 virtual CPUs, 4g of memory and 8g of storage. The micro service utilizes the FLASK framework and runs via Docker, making it easily deployable to other machines.

## VADR
VADR itself can be found here: `https://github.com/ncbi/vadr`. Two major pieces of VADR data are surfaced in this web app. The first being whether or not the submitted sequence passed VADR validation. The second being the list of sequence features VADR was able to identify. For a sequence that passes, none of these features will have "alerts". However, sequences that fail will have features where the "alert" field explains what is wrong with the highlighted region.

`Schäffer, Alejandro A, et al. “VADR: Validation and Annotation of Virus Sequence Submissions to GenBank.” 2019, doi:10.1101/852657. `

## Usage

The web page has two main sections as shown in the top bar. With the "Submit New Run" page, a user can provide their email, a sequence name, and a sequence to submit to VADR. Pressing submit starts a count down timer were at the end a button appears that allows users to poll the VADR micro service for their job status. The "View Past Runs" section allows a user to enter their email and get a list of runs they have submitted. They can pick a run ID and use it to pull up the sequence annotations fron that run. 

## Repo contents

### /docs
contains written documentation completed during project life cycle

### /src
python modules that are called in cgi scripts

### /js
java script files

### test_seqs.fasta
a FASTA file containing two sequences for testing, the first will pass VADR validation and the second will fail.

### ddl.sql
file containing the create table statements for the data base used by the web app to store VADR results returned by the microservice.

### vadr_submission.html
web app home page

### *.cgi
python scripts called via AJAX from a javascript to either talk to the VADR micro service or local database
