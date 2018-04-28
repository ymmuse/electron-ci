#!/usr/bin/env python

import argparse
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
ELECTRON_ROOT = os.path.join(ROOT, 'electron')
LIBCC_DIR = os.path.join(ELECTRON_ROOT, 'vendor', 'libchromiumcontent')
def main():
    os.chdir(LIBCC_DIR)

    args = parse_args()

    script_dir = os.path.join(LIBCC_DIR, 'script')
    update = os.path.join(script_dir, 'update')
    
    execute_script([sys.executable, update, '-t', args.target_arch])
    
    os.chdir(ROOT)
    # call apply-patches
    # call electron/script/bootstrap.py -v --build_release_libcc

def execute_script(argv, env=os.environ, cwd=None):
    print ' '.join(argv)
    try:
        output = subprocess.check_output(argv, stderr=subprocess.STDOUT, env=env, cwd=cwd)
        print output
        return output
    except subprocess.CalledProcessError as e:
        print e.output
    raise e
    
def parse_args():
  parser = argparse.ArgumentParser(description='build electron.')

  parser.add_argument('-t', '--target-arch', default='x64',
                      help='Target architecture')

  return parser.parse_args()

if __name__ == '__main__':
    sys.exit(main())