# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from __future__ import annotations

import sys


from . import core
from altair.utils import use_signature
from altair.utils.schemapi import Undefined, UndefinedType
from typing import Sequence, Literal


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class MarkMethodMixin:
    """A mixin class that defines mark methods"""

    def mark_arc(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'arc' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="arc", **kwds)
        else:
            copy.mark = "arc"
        return copy

    def mark_area(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'area' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="area", **kwds)
        else:
            copy.mark = "area"
        return copy

    def mark_bar(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'bar' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="bar", **kwds)
        else:
            copy.mark = "bar"
        return copy

    def mark_image(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'image' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="image", **kwds)
        else:
            copy.mark = "image"
        return copy

    def mark_line(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'line' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="line", **kwds)
        else:
            copy.mark = "line"
        return copy

    def mark_point(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'point' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="point", **kwds)
        else:
            copy.mark = "point"
        return copy

    def mark_rect(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'rect' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rect", **kwds)
        else:
            copy.mark = "rect"
        return copy

    def mark_rule(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'rule' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rule", **kwds)
        else:
            copy.mark = "rule"
        return copy

    def mark_text(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'text' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="text", **kwds)
        else:
            copy.mark = "text"
        return copy

    def mark_tick(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'tick' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="tick", **kwds)
        else:
            copy.mark = "tick"
        return copy

    def mark_trail(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'trail' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="trail", **kwds)
        else:
            copy.mark = "trail"
        return copy

    def mark_circle(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'circle' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="circle", **kwds)
        else:
            copy.mark = "circle"
        return copy

    def mark_square(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'square' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="square", **kwds)
        else:
            copy.mark = "square"
        return copy

    def mark_geoshape(
        self,
        align: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["left", "center", "right"]
        | UndefinedType = Undefined,
        angle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aria: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRole: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ariaRoleDescription: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        aspect: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        bandSize: float | UndefinedType = Undefined,
        baseline: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal["top", "middle", "bottom"]
        | UndefinedType = Undefined,
        binSpacing: float | UndefinedType = Undefined,
        blend: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            None,
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ]
        | UndefinedType = Undefined,
        clip: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        continuousBandSize: float | UndefinedType = Undefined,
        cornerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusBottomRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusEnd: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopLeft: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cornerRadiusTopRight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        cursor: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "auto",
            "default",
            "none",
            "context-menu",
            "help",
            "pointer",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "move",
            "no-drop",
            "not-allowed",
            "e-resize",
            "n-resize",
            "ne-resize",
            "nw-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "w-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "col-resize",
            "row-resize",
            "all-scroll",
            "zoom-in",
            "zoom-out",
            "grab",
            "grabbing",
        ]
        | UndefinedType = Undefined,
        description: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dir: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["ltr", "rtl"]
        | UndefinedType = Undefined,
        discreteBandSize: dict | float | core.SchemaBase | UndefinedType = Undefined,
        dx: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        dy: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        ellipsis: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fill: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        fillOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        filled: bool | UndefinedType = Undefined,
        font: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontStyle: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        fontWeight: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "normal",
            "bold",
            "lighter",
            "bolder",
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900,
        ]
        | UndefinedType = Undefined,
        height: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        href: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        innerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        interpolate: dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        limit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        line: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        lineBreak: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        lineHeight: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        minBandSize: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        opacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        order: bool | None | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outerRadius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        padAngle: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        point: str | bool | dict | core.SchemaBase | UndefinedType = Undefined,
        radius: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radius2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        radiusOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        shape: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        size: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        smooth: bool
        | dict
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        stroke: str
        | dict
        | None
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        strokeCap: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["butt", "round", "square"]
        | UndefinedType = Undefined,
        strokeDash: dict
        | core._Parameter
        | core.SchemaBase
        | Sequence[float]
        | UndefinedType = Undefined,
        strokeDashOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeJoin: dict
        | core._Parameter
        | core.SchemaBase
        | Literal["miter", "round", "bevel"]
        | UndefinedType = Undefined,
        strokeMiterLimit: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeOpacity: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        strokeWidth: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        style: str | Sequence[str] | UndefinedType = Undefined,
        tension: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        text: str
        | dict
        | Sequence[str]
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        theta2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thetaOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        timeUnitBandPosition: float | UndefinedType = Undefined,
        timeUnitBandSize: float | UndefinedType = Undefined,
        tooltip: str
        | bool
        | dict
        | None
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        url: str | dict | core._Parameter | core.SchemaBase | UndefinedType = Undefined,
        width: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        x2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        xOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2: str
        | dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        y2Offset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        yOffset: dict
        | float
        | core._Parameter
        | core.SchemaBase
        | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'geoshape' (see :class:`MarkDef`)"""
        kwds = dict(
            align=align,
            angle=angle,
            aria=aria,
            ariaRole=ariaRole,
            ariaRoleDescription=ariaRoleDescription,
            aspect=aspect,
            bandSize=bandSize,
            baseline=baseline,
            binSpacing=binSpacing,
            blend=blend,
            clip=clip,
            color=color,
            continuousBandSize=continuousBandSize,
            cornerRadius=cornerRadius,
            cornerRadiusBottomLeft=cornerRadiusBottomLeft,
            cornerRadiusBottomRight=cornerRadiusBottomRight,
            cornerRadiusEnd=cornerRadiusEnd,
            cornerRadiusTopLeft=cornerRadiusTopLeft,
            cornerRadiusTopRight=cornerRadiusTopRight,
            cursor=cursor,
            description=description,
            dir=dir,
            discreteBandSize=discreteBandSize,
            dx=dx,
            dy=dy,
            ellipsis=ellipsis,
            fill=fill,
            fillOpacity=fillOpacity,
            filled=filled,
            font=font,
            fontSize=fontSize,
            fontStyle=fontStyle,
            fontWeight=fontWeight,
            height=height,
            href=href,
            innerRadius=innerRadius,
            interpolate=interpolate,
            invalid=invalid,
            limit=limit,
            line=line,
            lineBreak=lineBreak,
            lineHeight=lineHeight,
            minBandSize=minBandSize,
            opacity=opacity,
            order=order,
            orient=orient,
            outerRadius=outerRadius,
            padAngle=padAngle,
            point=point,
            radius=radius,
            radius2=radius2,
            radius2Offset=radius2Offset,
            radiusOffset=radiusOffset,
            shape=shape,
            size=size,
            smooth=smooth,
            stroke=stroke,
            strokeCap=strokeCap,
            strokeDash=strokeDash,
            strokeDashOffset=strokeDashOffset,
            strokeJoin=strokeJoin,
            strokeMiterLimit=strokeMiterLimit,
            strokeOffset=strokeOffset,
            strokeOpacity=strokeOpacity,
            strokeWidth=strokeWidth,
            style=style,
            tension=tension,
            text=text,
            theta=theta,
            theta2=theta2,
            theta2Offset=theta2Offset,
            thetaOffset=thetaOffset,
            thickness=thickness,
            timeUnitBandPosition=timeUnitBandPosition,
            timeUnitBandSize=timeUnitBandSize,
            tooltip=tooltip,
            url=url,
            width=width,
            x=x,
            x2=x2,
            x2Offset=x2Offset,
            xOffset=xOffset,
            y=y,
            y2=y2,
            y2Offset=y2Offset,
            yOffset=yOffset,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="geoshape", **kwds)
        else:
            copy.mark = "geoshape"
        return copy

    def mark_boxplot(
        self,
        box: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        clip: bool | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        extent: str | float | UndefinedType = Undefined,
        invalid: Literal["filter", None] | UndefinedType = Undefined,
        median: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        opacity: float | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        outliers: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        rule: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        size: float | UndefinedType = Undefined,
        ticks: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'boxplot' (see :class:`BoxPlotDef`)"""
        kwds = dict(
            box=box,
            clip=clip,
            color=color,
            extent=extent,
            invalid=invalid,
            median=median,
            opacity=opacity,
            orient=orient,
            outliers=outliers,
            rule=rule,
            size=size,
            ticks=ticks,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.BoxPlotDef(type="boxplot", **kwds)
        else:
            copy.mark = "boxplot"
        return copy

    def mark_errorbar(
        self,
        clip: bool | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        extent: core.SchemaBase
        | Literal["ci", "iqr", "stderr", "stdev"]
        | UndefinedType = Undefined,
        opacity: float | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        rule: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        size: float | UndefinedType = Undefined,
        thickness: float | UndefinedType = Undefined,
        ticks: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'errorbar' (see :class:`ErrorBarDef`)"""
        kwds = dict(
            clip=clip,
            color=color,
            extent=extent,
            opacity=opacity,
            orient=orient,
            rule=rule,
            size=size,
            thickness=thickness,
            ticks=ticks,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.ErrorBarDef(type="errorbar", **kwds)
        else:
            copy.mark = "errorbar"
        return copy

    def mark_errorband(
        self,
        band: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        borders: bool | dict | core.SchemaBase | UndefinedType = Undefined,
        clip: bool | UndefinedType = Undefined,
        color: str
        | dict
        | core._Parameter
        | core.SchemaBase
        | Literal[
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
            "orange",
            "aliceblue",
            "antiquewhite",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "blanchedalmond",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkgrey",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkslategrey",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dimgrey",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "greenyellow",
            "grey",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightgrey",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightslategrey",
            "lightsteelblue",
            "lightyellow",
            "limegreen",
            "linen",
            "magenta",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "oldlace",
            "olivedrab",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "skyblue",
            "slateblue",
            "slategray",
            "slategrey",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "whitesmoke",
            "yellowgreen",
            "rebeccapurple",
        ]
        | UndefinedType = Undefined,
        extent: core.SchemaBase
        | Literal["ci", "iqr", "stderr", "stdev"]
        | UndefinedType = Undefined,
        interpolate: core.SchemaBase
        | Literal[
            "basis",
            "basis-open",
            "basis-closed",
            "bundle",
            "cardinal",
            "cardinal-open",
            "cardinal-closed",
            "catmull-rom",
            "linear",
            "linear-closed",
            "monotone",
            "natural",
            "step",
            "step-before",
            "step-after",
        ]
        | UndefinedType = Undefined,
        opacity: float | UndefinedType = Undefined,
        orient: core.SchemaBase
        | Literal["horizontal", "vertical"]
        | UndefinedType = Undefined,
        tension: float | UndefinedType = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'errorband' (see :class:`ErrorBandDef`)"""
        kwds = dict(
            band=band,
            borders=borders,
            clip=clip,
            color=color,
            extent=extent,
            interpolate=interpolate,
            opacity=opacity,
            orient=orient,
            tension=tension,
            **kwds,
        )
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.ErrorBandDef(type="errorband", **kwds)
        else:
            copy.mark = "errorband"
        return copy


class ConfigMethodMixin:
    """A mixin class that defines config methods"""

    @use_signature(core.Config)
    def configure(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=False)  # type: ignore[attr-defined]
        copy.config = core.Config(*args, **kwargs)
        return copy

    @use_signature(core.RectConfig)
    def configure_arc(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["arc"] = core.RectConfig(*args, **kwargs)
        return copy

    @use_signature(core.AreaConfig)
    def configure_area(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["area"] = core.AreaConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axis(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axis"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisBand(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisBand"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisBottom(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisBottom"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisDiscrete(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisDiscrete"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisLeft(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisLeft"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisPoint(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisPoint"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisQuantitative(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisQuantitative"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisRight(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisRight"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisTemporal(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisTemporal"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisTop(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisTop"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisX(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisX"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXBand(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXBand"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXDiscrete(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXDiscrete"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXPoint(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXPoint"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXQuantitative(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXQuantitative"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXTemporal(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXTemporal"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisY(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisY"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYBand(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYBand"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYDiscrete(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYDiscrete"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYPoint(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYPoint"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYQuantitative(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYQuantitative"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYTemporal(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYTemporal"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.BarConfig)
    def configure_bar(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["bar"] = core.BarConfig(*args, **kwargs)
        return copy

    @use_signature(core.BoxPlotConfig)
    def configure_boxplot(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["boxplot"] = core.BoxPlotConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_circle(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["circle"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.CompositionConfig)
    def configure_concat(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["concat"] = core.CompositionConfig(*args, **kwargs)
        return copy

    @use_signature(core.ErrorBandConfig)
    def configure_errorband(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["errorband"] = core.ErrorBandConfig(*args, **kwargs)
        return copy

    @use_signature(core.ErrorBarConfig)
    def configure_errorbar(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["errorbar"] = core.ErrorBarConfig(*args, **kwargs)
        return copy

    @use_signature(core.CompositionConfig)
    def configure_facet(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["facet"] = core.CompositionConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_geoshape(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["geoshape"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_header(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["header"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_headerColumn(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["headerColumn"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_headerFacet(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["headerFacet"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_headerRow(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["headerRow"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.RectConfig)
    def configure_image(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["image"] = core.RectConfig(*args, **kwargs)
        return copy

    @use_signature(core.LegendConfig)
    def configure_legend(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["legend"] = core.LegendConfig(*args, **kwargs)
        return copy

    @use_signature(core.LineConfig)
    def configure_line(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["line"] = core.LineConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_mark(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["mark"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_point(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["point"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.ProjectionConfig)
    def configure_projection(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["projection"] = core.ProjectionConfig(*args, **kwargs)
        return copy

    @use_signature(core.RangeConfig)
    def configure_range(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["range"] = core.RangeConfig(*args, **kwargs)
        return copy

    @use_signature(core.RectConfig)
    def configure_rect(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["rect"] = core.RectConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_rule(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["rule"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.ScaleConfig)
    def configure_scale(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["scale"] = core.ScaleConfig(*args, **kwargs)
        return copy

    @use_signature(core.SelectionConfig)
    def configure_selection(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["selection"] = core.SelectionConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_square(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["square"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_text(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["text"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.TickConfig)
    def configure_tick(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["tick"] = core.TickConfig(*args, **kwargs)
        return copy

    @use_signature(core.TitleConfig)
    def configure_title(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["title"] = core.TitleConfig(*args, **kwargs)
        return copy

    @use_signature(core.FormatConfig)
    def configure_tooltipFormat(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["tooltipFormat"] = core.FormatConfig(*args, **kwargs)
        return copy

    @use_signature(core.LineConfig)
    def configure_trail(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["trail"] = core.LineConfig(*args, **kwargs)
        return copy

    @use_signature(core.ViewConfig)
    def configure_view(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])  # type: ignore[attr-defined]
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["view"] = core.ViewConfig(*args, **kwargs)
        return copy
