#!/usr/bin/env python

__author__="pharno"
__date__ ="$26.03.2011 23:00:00$"


import subprocess

# Directly taken from Py3k (and modified a bit:
def check_output(*popenargs, **kwargs):
    """Run command with arguments and return its output as a byte string.

    If the exit code was non-zero it raises a CalledProcessError.  The
    CalledProcessError object will have the return code in the returncode
    attribute and output in the output attribute.

    The arguments are the same as for the Popen constructor.  Example:

    >>> check_output(["ls", "-l", "/dev/null"])
    'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

    The stdout argument is not allowed as it is used internally.
    To capture standard error in the result, use stderr=subprocess.STDOUT.

    >>> check_output(["/bin/sh", "-c",
                      "ls -l non_existent_file ; exit 0"],
                     stderr=subprocess.STDOUT)
    'ls: non_existent_file: No such file or directory\n'
    """
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(*popenargs, stdout=subprocess.PIPE, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = subprocess.popenargs[0]
        raise subprocess.CalledProcessError(retcode, cmd, output=output)
    return output
