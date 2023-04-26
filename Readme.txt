# Selection of ARG candidates not included in ResFinderFG v2.0 which would require validation 

ARG candidates are defined as follow :
- Insert sequences which was shown to confer resistance to an antibiotic in a functional metagenomics experiment.
- Insert sequences containing one unique ORF

**DATA** contains the data needed for selection of ARG candidates.
- ResFinder_FG.fasta which is the final version of the database obtained in the ResFinderFG_Construction repository.
- db.fasta which is the version of the database before a last deduplication step using cdhit. 
- gb_output which is a genbank file compiling all the information on the insert sequences included in the ResFinderFG v2.0 construction process. 
- prokka.gff which is the output file of prokka annotation process on all the insert sequences included in ResFinderFG v2.0 construction process. 
- DNA_insert_seq_cdhit.fasta which is a fasta file with all the insert sequences included in the ResFinderFG v2.0 construction process after a first deduplication step using cdhit.

**SCRIPT** you can find the scripts needed for ARG candidates selection.
Each step is described in the script. 

**OUTPUT** contains the output generated using the script and the final ARG candidates database : ARGs_candidates.fasta

**These ARGs need to be confirmed in further cloning experiment**
