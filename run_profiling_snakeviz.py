"""
    File: tests_profiles.py
    Description: Run application and display performance report in browser.
    Date: 27/03/2019

    Run: profiling <name_file>.py
    View Profile through the terminal.
"""

import os
import pathlib

#import deepnlpf.modules.notifications.toast import Toast

tool_name = 'stanford_corenlp'
tool_file= 'stanford_corenlp.py'
corpus_size = 'corpus1000sentences'
analysis = '_experience_1_analise_sintatica_stanford_corenlp.prof'


path_root = str(pathlib.Path.cwd())
path_out = '/data/out/'+corpus_size+'/'+tool_name+'/'
path_filerun = 'scripts/'+tool_file
file_out = ''+corpus_size+analysis
path_full = path_root + path_out + file_out

try:
    #Toast().send_notification('success', "Success", "Start! Profiling Snakeviz.")

    # run create analysis profile file: .prof
    os.system('python -m cProfile -o ' + path_full + ' ' + path_filerun)

    #Toast().send_notification('success', "Success", "Success! Profiling Snakeviz.")

    # run browse result analysis profile.
    os.system('cd ' + path_root + path_out + ' && snakeviz ' + file_out)
except Exception as err:
    #Toast().send_notification('error', "Err", "Err! Profiling Snakeviz.")
    print(err)
