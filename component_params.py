"""
component_params.py

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

## TODO: here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
                'chimeric_junction' : '__REQUIRED__', # --chimeric_junction or -J
                'ref_gtf_file' : None, # --ref_GTF or -G
                'ref_cdna_file' : None, # --ref_cdna or -C
                }

## TODO: here goes the list of the output files.
output_files = {
                'output_prefix' : None, # --out_prefix or -O
                'tmp_out_dir' : None, # --tmpdir
                }

## TODO: here goes the list of the input parameters excluding input/output files.
input_params = {
                'aggregate_novel_junction_dist': None, # --aggregate_novel_junction_dist
                'e_value_threshold' : None, # -E
                'max_promiscuity' : None, # --max_promiscuity
                'min_alt_pct_junction' : None, #--min_alt_pct_junction
                'min_junction_reads' : None, #--min_junction_reads
                'min_novel_junction_support' : None, # --min_novel_junction_support
                'min_sum_frags' : None, # --min_sum_frags
                'no_blast_filter' : None, # --no_filter
                'verbose_level' : None, # --verbose_level
                }

## TODO: here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
