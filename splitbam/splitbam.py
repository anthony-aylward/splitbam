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
    return parser.parse_args()


def main():
    args = parse_arguments()
    with tempfile.TemporaryFile() as temp_file:
        temp_file_name = temp_file.name
    pysam.sort('-n', args.input, temp_file_name)
    for out in args.output:
        pysam.view('-H', args.input, out)
    with open(args.input, 'r') as f:
        with subprocess.Popen(
            ('samtools', 'view'), stdin=f, stdout=subprocess.PIPE
        ) as view:
            subprocess.run(
                ('awk', ),
                stdin=view.stdout
            )



    
    