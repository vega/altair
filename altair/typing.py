"""Public types to ease integrating with `altair`."""

from __future__ import annotations

__all__ = ["ChartType", "EncodeKwds", "is_chart_type"]

from altair.vegalite.v5.api import ChartType, is_chart_type
from altair.vegalite.v5.schema.channels import _EncodeKwds as EncodeKwds
