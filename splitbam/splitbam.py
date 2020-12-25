#===============================================================================
# splitbam.py
#===============================================================================

"""Split a BAM file into two subsamples"""

import pysam
import subprocess
import tempfile

from argparse import ArgumentParser


# Functions ====================================================================

def parse_arguments():
    parser = ArgumentParser(description='Split a BAM file into two subsamples')
    parser.add_argument(
        'input',
        metavar='<path/to/input.bam>',
        help='path to input BAM file'
    )
    parser.add_argument(
        'output',
        metavar=('<path/to/output1.bam>', '<path/to/output2.bam>'),
        nargs=2,
        help='paths to output BAM files'
    )
    parser.add_argument(
        '--tmp-dir',
        metavar='<path/to/tmp/dir>',
        help='directory for temporary files'
    )

def main():
    with tempfile.TemporaryDirectory(dir) as temp_dir:

    
    