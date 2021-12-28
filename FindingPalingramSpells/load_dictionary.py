"""Load a text file as a list.
Arguments:
text
file name (and directory path, if needed)
Exceptions:
IOError
if filename not found.
Returns:
A
list of all words in a text file in lower case.
Requiresimport
sys
"""

import sys

def load(file):
    """Open a text firle & return a lsit of lwercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt=[x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}{file}. Terminating program",file=sys.stderr)
        sys.exit(1)