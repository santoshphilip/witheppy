# Copyright (c) 2019 Santosh Philip
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================
"""try to retain the original sequence of the idf objects in the idf file"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def removecomment(astr, cphrase):
    """
    the comment is similar to that in python.
    any charachter after the # is treated as a comment
    until the end of the line
    astr is the string to be de-commented
    cphrase is the comment phrase"""
    # linesep = mylib3.getlinesep(astr)
    alist = astr.splitlines()
    for i in range(len(alist)):
        alist1 = alist[i].split(cphrase)
        alist[i] = alist1[0]

    # return string.join(alist, linesep)
    return '\n'.join(alist)

def simpleidfread(fhandle):
    """read the idf file by usning string functions to get the data out."""
    astr = fhandle.read()
    nocom = removecomment(astr, '!')
    idfst = nocom
    alist = idfst.split(';')
    lss = []
    for element in alist:
        lst = element.split(',')
        lss.append(lst)

    for i in range(0, len(lss)):
        for j in range(0, len(lss[i])):
            lss[i][j] = lss[i][j].strip()

    dt = {}
    dtls = []
    for element in lss:
        if element[0] == '':
            continue
        dt[element[0].upper()] = []
        dtls.append(element[0].upper())

    return dt, dtls

