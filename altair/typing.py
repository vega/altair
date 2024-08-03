from __future__ import annotations

import sys
from typing import Any, Mapping, Union
from typing_extensions import TypedDict

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

ChannelType: TypeAlias = Union[str, Mapping[str, Any], Any]


class EncodeKwds(TypedDict, total=False):
    """
    Reference implementation from [comment code block](https://github.com/pola-rs/polars/pull/17995#issuecomment-2263609625).

    Aiming to define more specific `ChannelType`, without being exact.

    This would be generated alongside `tools.generate_schema_wrapper._create_encode_signature`
    """

    angle: ChannelType
    color: ChannelType
    column: ChannelType
    description: ChannelType
    detail: ChannelType | list[Any]
    facet: ChannelType
    fill: ChannelType
    fillOpacity: ChannelType
    href: ChannelType
    key: ChannelType
    latitude: ChannelType
    latitude2: ChannelType
    longitude: ChannelType
    longitude2: ChannelType
    opacity: ChannelType
    order: ChannelType | list[Any]
    radius: ChannelType
    radius2: ChannelType
    row: ChannelType
    shape: ChannelType
    size: ChannelType
    stroke: ChannelType
    strokeDash: ChannelType
    strokeOpacity: ChannelType
    strokeWidth: ChannelType
    text: ChannelType
    theta: ChannelType
    theta2: ChannelType
    tooltip: ChannelType | list[Any]
    url: ChannelType
    x: ChannelType
    x2: ChannelType
    xError: ChannelType
    xError2: ChannelType
    xOffset: ChannelType
    y: ChannelType
    y2: ChannelType
    yError: ChannelType
    yError2: ChannelType
    yOffset: ChannelType
