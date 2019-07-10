"""
For the last few days you have been using the newest text editor - which you also wrote yourself!

Unfortunately, you did not notice a nasty bug that crept in.
Instead of appending new changes to the end of the currently opened file,
it just saved them into a random file somewhere in the /root/devops/ directory (or one of its subdirectories).

It is too late to fix it in the text editor now since you have already written a lot of content that is due tomorrow.
Your only hope is to recreate the original text from all the random chunks produced by the buggy editor.

Given the different files stored in the /root/devops/ folder and its subfolders,
write a script that reconstructs the original text from their content and outputs it.

You can assume that all the files represent disjointed chunks of the text,
that they were all created at different times, and that they were not modified after their creation.

It is guaranteed that there is at least one file.

Example

Consider the following files on your computer:

/root/devops/a.txt
/root/devops/b
/root/devops/c/d
/root/devops/a.txt, created on 2017-01-16 09:15, contains the following information:

very important
/root/devops/b, created on 2017-01-17 11:11, contains the following information:

 text!
/root/devops/c/d, created on 2017-01-16 09:00, contains the following information:

This is
The output for this test should be as follows:

This is very important text!
"""

import os

x = {}
y = ''

for r, d, c in os.walk('/root/devops/'):
    for f in c:
        p = r + '/' + f
        x[os.stat(p)[8]] = open(p).read()

for i in sorted(x):
    y += x[i]

print (y)
