"""
Given a sentence in English, your mission is to find all the misspell words and put them
in the list ordered by their positions in the sentence. No grammar check needed. Just spelling.

Example
For str = "Mispell is the correct spelling", the output should be

misspell(str) = ["Mispell"].
"""

# solution by miguel_r35

import os
misspell = lambda s: [i[:-1] for i in os.popen("echo %s | aspell list" % s)]
