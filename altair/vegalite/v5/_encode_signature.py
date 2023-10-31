# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

# ruff: noqa: F403, F405
from typing import Union
from .schema import *

# Type alias for value and datum dictionaries.
# They are mainly used to make the type hints
# more readable when they show up in IDEs. We can't type these more accurately
# as TypedDict do not accept arbitrary extra keys where as alt.value and alt.datum
# do. Also see https://github.com/python/mypy/issues/4617#issuecomment-367647383
# We can't split it into two separate type aliases as IDEs such as VS Code
# simply show the first one in the signature if they refer to the same type.
ValueOrDatum = dict


def _encode_signature(
    self,
    angle: Union[
        str, Angle, ValueOrDatum, AngleDatum, AngleValue, UndefinedType
    ] = Undefined,
    color: Union[
        str, Color, ValueOrDatum, ColorDatum, ColorValue, UndefinedType
    ] = Undefined,
    column: Union[str, Column, ValueOrDatum, UndefinedType] = Undefined,
    description: Union[
        str, Description, ValueOrDatum, DescriptionValue, UndefinedType
    ] = Undefined,
    detail: Union[str, Detail, ValueOrDatum, UndefinedType] = Undefined,
    facet: Union[str, Facet, ValueOrDatum, UndefinedType] = Undefined,
    fill: Union[
        str, Fill, ValueOrDatum, FillDatum, FillValue, UndefinedType
    ] = Undefined,
    fillOpacity: Union[
        str,
        FillOpacity,
        ValueOrDatum,
        FillOpacityDatum,
        FillOpacityValue,
        UndefinedType,
    ] = Undefined,
    href: Union[str, Href, ValueOrDatum, HrefValue, UndefinedType] = Undefined,
    key: Union[str, Key, ValueOrDatum, UndefinedType] = Undefined,
    latitude: Union[
        str, Latitude, ValueOrDatum, LatitudeDatum, UndefinedType
    ] = Undefined,
    latitude2: Union[
        str, Latitude2, ValueOrDatum, Latitude2Datum, Latitude2Value, UndefinedType
    ] = Undefined,
    longitude: Union[
        str, Longitude, ValueOrDatum, LongitudeDatum, UndefinedType
    ] = Undefined,
    longitude2: Union[
        str, Longitude2, ValueOrDatum, Longitude2Datum, Longitude2Value, UndefinedType
    ] = Undefined,
    opacity: Union[
        str, Opacity, ValueOrDatum, OpacityDatum, OpacityValue, UndefinedType
    ] = Undefined,
    order: Union[str, Order, ValueOrDatum, OrderValue, UndefinedType] = Undefined,
    radius: Union[
        str, Radius, ValueOrDatum, RadiusDatum, RadiusValue, UndefinedType
    ] = Undefined,
    radius2: Union[
        str, Radius2, ValueOrDatum, Radius2Datum, Radius2Value, UndefinedType
    ] = Undefined,
    row: Union[str, Row, ValueOrDatum, UndefinedType] = Undefined,
    shape: Union[
        str, Shape, ValueOrDatum, ShapeDatum, ShapeValue, UndefinedType
    ] = Undefined,
    size: Union[
        str, Size, ValueOrDatum, SizeDatum, SizeValue, UndefinedType
    ] = Undefined,
    stroke: Union[
        str, Stroke, ValueOrDatum, StrokeDatum, StrokeValue, UndefinedType
    ] = Undefined,
    strokeDash: Union[
        str, StrokeDash, ValueOrDatum, StrokeDashDatum, StrokeDashValue, UndefinedType
    ] = Undefined,
    strokeOpacity: Union[
        str,
        StrokeOpacity,
        ValueOrDatum,
        StrokeOpacityDatum,
        StrokeOpacityValue,
        UndefinedType,
    ] = Undefined,
    strokeWidth: Union[
        str,
        StrokeWidth,
        ValueOrDatum,
        StrokeWidthDatum,
        StrokeWidthValue,
        UndefinedType,
    ] = Undefined,
    text: Union[
        str, Text, ValueOrDatum, TextDatum, TextValue, UndefinedType
    ] = Undefined,
    theta: Union[
        str, Theta, ValueOrDatum, ThetaDatum, ThetaValue, UndefinedType
    ] = Undefined,
    theta2: Union[
        str, Theta2, ValueOrDatum, Theta2Datum, Theta2Value, UndefinedType
    ] = Undefined,
    tooltip: Union[str, Tooltip, ValueOrDatum, TooltipValue, UndefinedType] = Undefined,
    url: Union[str, Url, ValueOrDatum, UrlValue, UndefinedType] = Undefined,
    x: Union[str, X, ValueOrDatum, XDatum, XValue, UndefinedType] = Undefined,
    x2: Union[str, X2, ValueOrDatum, X2Datum, X2Value, UndefinedType] = Undefined,
    xError: Union[str, XError, ValueOrDatum, XErrorValue, UndefinedType] = Undefined,
    xError2: Union[str, XError2, ValueOrDatum, XError2Value, UndefinedType] = Undefined,
    xOffset: Union[
        str, XOffset, ValueOrDatum, XOffsetDatum, XOffsetValue, UndefinedType
    ] = Undefined,
    y: Union[str, Y, ValueOrDatum, YDatum, YValue, UndefinedType] = Undefined,
    y2: Union[str, Y2, ValueOrDatum, Y2Datum, Y2Value, UndefinedType] = Undefined,
    yError: Union[str, YError, ValueOrDatum, YErrorValue, UndefinedType] = Undefined,
    yError2: Union[str, YError2, ValueOrDatum, YError2Value, UndefinedType] = Undefined,
    yOffset: Union[
        str, YOffset, ValueOrDatum, YOffsetDatum, YOffsetValue, UndefinedType
    ] = Undefined,
):
    ...
