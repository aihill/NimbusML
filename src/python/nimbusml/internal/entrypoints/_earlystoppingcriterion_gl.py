# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
GL
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def gl(
        threshold=0.01,
        **params):
    """
    **Description**
        Stop in case of loss of generality.

    :param threshold: Threshold in range [0,1]. (settings).
    """

    entrypoint_name = 'GL'
    settings = {}

    if threshold is not None:
        settings['Threshold'] = try_set(
            obj=threshold,
            none_acceptable=True,
            is_of_type=numbers.Real,
            valid_range={
                'Max': 1.0,
                'Min': 0.0})

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='EarlyStoppingCriterion')
    return component