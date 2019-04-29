# Copyright (c) 2019 Santosh Philip
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from six import StringIO
from witheppy.eppyhelpers import idfsequence


def test_simpleidfread():
    """py.test for simpleidfread"""
    tdata = (("version, 9.0.1;", {"VERSION":[1]}), # fstring, expected
    )
    for fstring, expected in tdata:
        fhandle = StringIO(fstring)
        result = idfsequence.simpleidfread(fhandle)
        assert result == None
        # assert result == expected