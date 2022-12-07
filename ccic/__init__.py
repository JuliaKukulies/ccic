"""
ccic
====

The 'ccic' Python package implements the Chalmers Cloud-Ice Climatology.
"""
from numcodecs.registry import register_codec

from ccic.codecs import LogBins

# Register filter used to encode water content data.
register_codec(LogBins)
