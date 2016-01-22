""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

from kronos.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    """
    TODO: add component doc here. 
    """

    def __init__(self, component_name="run_star_fusion", 
                 component_parent_dir=None, seed_dir=None):
        
        ## TODO: pass the version of the component here.
        self.version = "v0.99.0"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    ## TODO: write the focus method if the component is parallelizable.
    ## Note that it should return cmd, cmd_args.
    def focus(self, cmd, cmd_args, chunk):
        pass 
#         return cmd, cmd_args

    ## TODO: this method should make the command and command arguments 
    ## used to run the component_seed via the command line. Note that 
    ## it should return cmd, cmd_args. 
    def make_cmd(self, chunk=None):
        cmd = self.requirements['star_fusion_binary']
        cmd_args = []
        args = vars(self.args)
        
        ## component params to seed params mapping
        comp_seed_map = {
                         'aggregate_novel_junction_dist': 'aggregate_novel_junction_dist',
                         'chimeric_junction': 'chimeric_junction',
                         'e_value_threshold': 'E',
                         'max_promiscuity': 'max_promiscuity',
                         'min_alt_pct_junction': 'min_alt_pct_junction',
                         'min_junction_reads': 'min_junction_reads',
                         'min_novel_junction_support': 'min_novel_junction_support',
                         'min_sum_frags': 'min_sum_frags',
                         'no_blast_filter': 'no_filter',
                         'output_prefix': 'out_prefix',
                         'ref_cdna_file' : 'ref_cdna',
                         'ref_gtf_file': 'ref_GTF',
                         'tmp_out_dir': 'tmpdir',
                         'verbose_level' : 'verbose_level',
                        }

        for k, v in args.items():
            if v is None or v is False:
                continue

            k = comp_seed_map[k]            
            cmd_args.append('--' + k)
            
            if isinstance(v, bool):
                continue
            if isinstance(v, str):
                v = repr(v)
            if isinstance(v, (list, tuple)):
                cmd_args.extend(v)
            else:
                cmd_args.extend([v])
        
        return cmd, cmd_args


## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

