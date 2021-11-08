# __main__.py
import os
import json
import multiprocessing
from multiprocessing import Pool
import sys
from datetime import datetime

# custom
from . import account_splitter, feature_splitter, arg_parser, results
from .parallelizer import command_generator

ANUBIS_ASCII = (
"""
                 ♡♡                                               
                ♡♡♡                                                 
              ♡♡ ♡♡♡♡                                               
         ♡♡♡♡♡♡♡♡♡♡♡♡                                               
                 ♡♡♡♡♡                                              
                  ♡♡♡♡♡                                             
               ♡♡♡♡♡♡♡♡♡                                            
              ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡        ♡♡♡♡♡♡                         
              ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡ ♡♡♡♡                     
              ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡                   
          ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡     ♡♡♡♡♡♡♡♡♡♡                  
♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡       ♡♡♡♡♡     ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡                 
                                                    ♡♡♡              
          POWERED BY ANUBIS                          ♡♡♡♡            
(and the power of love  Σ>―(〃°ω°〃)♡→)               ♡♡♡♡♡          
                                                      ♡♡♡♡♡         
                                                       ♡♡♡♡         
                                                        ♡♡     """
)


def main():
    width = os.get_terminal_size().columns
    try:
        print(ANUBIS_ASCII.center(width))
    except Exception as e:
        print(ANUBIS_ASCII)
    start = datetime.now()

    # parse arguments
    args = arg_parser.parse_arguments()

    # create a temp dir that will contain results and be exported
    if not os.path.isdir(args.output_dir):
        # todo - think about whether this is the responsibility of this tool
        print(f'Could not find directory for output: <{args.output_dir}>\nCreating directory <{args.output_dir}> now')
        os.mkdir(args.output_dir)
        # sys.exit(1)

    # set up the multiple processes
    multiprocessing.set_start_method('fork')
    pool = Pool(args.processes)

    # get account data available for parallel runs
    # the `accounts_data` list looks like this --> [(<run_name>, "user pass"), [<list of feature files>]]
    if args.account_file and args.account_section:
        print('\n--- PARSING ACCOUNTS')
        print(f'\tfile:    <{args.account_file}>')
        print(f'\tsection: <{args.account_section}>')
        accounts_data = account_splitter.get_accounts(args.processes, args.account_file, args.account_section)
    else:
        print('\n--- ACCOUNTS NOT SPECIFIED')
        # create dummy account data just for the purpose of naming the runs
        accounts_data = [(datetime.now().isoformat(), 'NONE NONE') for i in range(args.processes)]

    # split the features and store as list
    print('\n--- GROUPING FEATURES & ACCOUNTS')
    print(f'\tfeature dir:   <{args.feature_dir}>')
    print(f'\tincluded tags: <{",".join([t for t in args.itags]) if args.itags else "(none)"}>')
    print(f'\texcluded tags: <{",".join([t for t in args.etags]) if args.etags else "(none)"}>')
    feature_groups = feature_splitter.get_features(args, accounts_data)

    # run all the processes and save the locations of the result files
    num_groups = len(feature_groups)
    print(f'\n--- RUNNING <{num_groups} PROCESS{"ES" * int(num_groups > 1)}>')
    result_files = pool.map(command_generator, feature_groups)

    # recombine everything
    print('\n--- COMBINING RESULTS')
    try:
        results.create_aggregate(files=result_files, aggregate_out_file=args.result_file)
    except Exception as e:
        print(f'There was an error combining results\n{e}')

    end = datetime.now()

    # calculate passes/fails for quick summary
    res_string = None
    passes, failures, other = 0, 0, 0
    try:
        with open(args.result_file) as f:
            res = json.load(f)
        for feature in res:
            for scenario in feature['elements']:
                if scenario['keyword'].lower() != 'background':
                    status = scenario['status']
                    passes += 1 * int(status == 'passed')
                    failures += 1 * int(status == 'failed')
                    other += 1 * int(status != 'passed' and status != 'failed')
        res_string = f'{passes / (passes + failures) * 100:.2f}%'
    except Exception as e:
        # I know that this is a terrible anti-pattern, but there's really nothing to do for an exception
        print(f"\tThere was an error calculating overall results, but it's likely not fatal.\n\t{e}")

    # <editor-fold desc="extremely basic summary">
    print('\n=======================================\n\t\tSUMMARY\n=======================================')
    print(f'Env(s):    <{",".join(args.env)}>')
    print(f'Browser:   <{args.browser}>')
    print(f'Results:   <{args.result_file}>')
    print(f'Pass Rate: <{res_string if res_string else "could not calculate"}>')
    print(f'Run Time:  <{(end - start)}>')
    print('=======================================')
    # </editor-fold>


if __name__ == '__main__':
    # run everything
    main()
    sys.exit(0)
