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
    tdata = (
    ("version, 9.0.1;", {"VERSION":[0]}), # fstring, expected
    ("""Timestep,4;
    version, 9.0.1;""", 
    {"VERSION":[1], "TIMESTEP":[0]}), # fstring, expected
    ("""version, 9.0.1;
    Timestep,4;
    Timestep,5;
    """, 
    {"VERSION":[0], "TIMESTEP":[1, 2]}), # fstring, expected
    ("""Timestep,5;
    version, 9.0.1;
    Timestep,4;
    """, 
    {"VERSION":[1], "TIMESTEP":[0, 2]}), # fstring, expected
    )
    for fstring, expected in tdata:
        fhandle = StringIO(fstring)
        result = idfsequence.simpleidfread(fhandle)
        assert result == expected
