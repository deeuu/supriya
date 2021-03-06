import collections

from supriya import CalculationRate
from supriya.typing import UGenInputMap
from supriya.ugens.InfoUGenBase import InfoUGenBase


class BlockSize(InfoUGenBase):
    """
    A block size info unit generator.

    ::

        >>> supriya.ugens.BlockSize.ir()
        BlockSize.ir()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = "Info UGens"

    _ordered_input_names: UGenInputMap = collections.OrderedDict([])

    _valid_calculation_rates = (CalculationRate.SCALAR,)
