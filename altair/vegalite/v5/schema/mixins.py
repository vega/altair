# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

import sys


from . import core
from altair.utils import use_signature
from altair.utils.schemapi import Undefined, UndefinedType
from typing import Any, List, Literal, Union


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class MarkMethodMixin:
    """A mixin class that defines mark methods"""

    def mark_arc(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="arc", **kwds)
        else:
            copy.mark = "arc"
        return copy

    def mark_area(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="area", **kwds)
        else:
            copy.mark = "area"
        return copy

    def mark_bar(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="bar", **kwds)
        else:
            copy.mark = "bar"
        return copy

    def mark_image(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="image", **kwds)
        else:
            copy.mark = "image"
        return copy

    def mark_line(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="line", **kwds)
        else:
            copy.mark = "line"
        return copy

    def mark_point(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="point", **kwds)
        else:
            copy.mark = "point"
        return copy

    def mark_rect(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rect", **kwds)
        else:
            copy.mark = "rect"
        return copy

    def mark_rule(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rule", **kwds)
        else:
            copy.mark = "rule"
        return copy

    def mark_text(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="text", **kwds)
        else:
            copy.mark = "text"
        return copy

    def mark_tick(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="tick", **kwds)
        else:
            copy.mark = "tick"
        return copy

    def mark_trail(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="trail", **kwds)
        else:
            copy.mark = "trail"
        return copy

    def mark_circle(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="circle", **kwds)
        else:
            copy.mark = "circle"
        return copy

    def mark_square(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="square", **kwds)
        else:
            copy.mark = "square"
        return copy

    def mark_geoshape(
        self,
        align: Union[Union[core.Align, core.ExprRef], UndefinedType] = Undefined,
        angle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        aria: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        ariaRole: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        ariaRoleDescription: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        aspect: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        bandSize: Union[float, UndefinedType] = Undefined,
        baseline: Union[
            Union[core.TextBaseline, core.ExprRef], UndefinedType
        ] = Undefined,
        binSpacing: Union[float, UndefinedType] = Undefined,
        blend: Union[Union[core.Blend, core.ExprRef], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        continuousBandSize: Union[float, UndefinedType] = Undefined,
        cornerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusBottomLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusBottomRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusEnd: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        cornerRadiusTopLeft: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cornerRadiusTopRight: Union[
            Union[float, core.ExprRef], UndefinedType
        ] = Undefined,
        cursor: Union[Union[core.Cursor, core.ExprRef], UndefinedType] = Undefined,
        description: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        dir: Union[Union[core.TextDirection, core.ExprRef], UndefinedType] = Undefined,
        discreteBandSize: Union[
            Union[float, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        dx: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        dy: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        ellipsis: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fill: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        fillOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        filled: Union[bool, UndefinedType] = Undefined,
        font: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        fontSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        fontStyle: Union[
            Union[core.FontStyle, core.ExprRef], UndefinedType
        ] = Undefined,
        fontWeight: Union[
            Union[core.FontWeight, core.ExprRef], UndefinedType
        ] = Undefined,
        height: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        href: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        innerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        interpolate: Union[
            Union[core.Interpolate, core.ExprRef], UndefinedType
        ] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        limit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        line: Union[Union[bool, core.OverlayMarkDef], UndefinedType] = Undefined,
        lineBreak: Union[Union[str, core.ExprRef], UndefinedType] = Undefined,
        lineHeight: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        minBandSize: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        opacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        order: Union[Union[None, bool], UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outerRadius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        padAngle: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        point: Union[Union[bool, core.OverlayMarkDef, str], UndefinedType] = Undefined,
        radius: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radius2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        radiusOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        shape: Union[
            Union[Union[core.SymbolShape, str], core.ExprRef], UndefinedType
        ] = Undefined,
        size: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        smooth: Union[Union[bool, core.ExprRef], UndefinedType] = Undefined,
        stroke: Union[
            Union[core.Color, core.Gradient, None, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeCap: Union[
            Union[core.StrokeCap, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeDash: Union[Union[List[float], core.ExprRef], UndefinedType] = Undefined,
        strokeDashOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeJoin: Union[
            Union[core.StrokeJoin, core.ExprRef], UndefinedType
        ] = Undefined,
        strokeMiterLimit: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeOpacity: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        strokeWidth: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        style: Union[Union[str, List[str]], UndefinedType] = Undefined,
        tension: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        text: Union[Union[core.Text, core.ExprRef], UndefinedType] = Undefined,
        theta: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        theta2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thetaOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        timeUnitBandPosition: Union[float, UndefinedType] = Undefined,
        timeUnitBandSize: Union[float, UndefinedType] = Undefined,
        tooltip: Union[
            Union[float, str, bool, core.TooltipContent, core.ExprRef, None],
            UndefinedType,
        ] = Undefined,
        url: Union[Union[core.URI, core.ExprRef], UndefinedType] = Undefined,
        width: Union[
            Union[float, core.ExprRef, core.RelativeBandSize], UndefinedType
        ] = Undefined,
        x: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        x2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        xOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        y: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2: Union[Union[float, str, core.ExprRef], UndefinedType] = Undefined,
        y2Offset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        yOffset: Union[Union[float, core.ExprRef], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="geoshape", **kwds)
        else:
            copy.mark = "geoshape"
        return copy

    def mark_boxplot(
        self,
        box: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        extent: Union[Union[str, float], UndefinedType] = Undefined,
        invalid: Union[Literal["filter", None], UndefinedType] = Undefined,
        median: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        opacity: Union[float, UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        outliers: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        rule: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        size: Union[float, UndefinedType] = Undefined,
        ticks: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.BoxPlotDef(type="boxplot", **kwds)
        else:
            copy.mark = "boxplot"
        return copy

    def mark_errorbar(
        self,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        extent: Union[
            Literal["ci", "iqr", "stderr", "stdev"], UndefinedType
        ] = Undefined,
        opacity: Union[float, UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        rule: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        size: Union[float, UndefinedType] = Undefined,
        thickness: Union[float, UndefinedType] = Undefined,
        ticks: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.ErrorBarDef(type="errorbar", **kwds)
        else:
            copy.mark = "errorbar"
        return copy

    def mark_errorband(
        self,
        band: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        borders: Union[Union[bool, core.AnyMarkConfig], UndefinedType] = Undefined,
        clip: Union[bool, UndefinedType] = Undefined,
        color: Union[
            Union[core.Color, core.Gradient, core.ExprRef], UndefinedType
        ] = Undefined,
        extent: Union[
            Literal["ci", "iqr", "stderr", "stdev"], UndefinedType
        ] = Undefined,
        interpolate: Union[
            Literal[
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
            ],
            UndefinedType,
        ] = Undefined,
        opacity: Union[float, UndefinedType] = Undefined,
        orient: Union[Literal["horizontal", "vertical"], UndefinedType] = Undefined,
        tension: Union[float, UndefinedType] = Undefined,
        **kwds
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
            **kwds
        )
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.ErrorBandDef(type="errorband", **kwds)
        else:
            copy.mark = "errorband"
        return copy


class ConfigMethodMixin:
    """A mixin class that defines config methods"""

    @use_signature(core.Config)
    def configure(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=False)
        copy.config = core.Config(*args, **kwargs)
        return copy

    @use_signature(core.RectConfig)
    def configure_arc(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["arc"] = core.RectConfig(*args, **kwargs)
        return copy

    @use_signature(core.AreaConfig)
    def configure_area(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["area"] = core.AreaConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axis(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axis"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisBand(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisBand"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisBottom(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisBottom"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisDiscrete(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisDiscrete"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisLeft(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisLeft"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisPoint(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisPoint"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisQuantitative(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisQuantitative"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisRight(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisRight"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisTemporal(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisTemporal"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisTop(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisTop"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisX(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisX"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXBand(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXBand"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXDiscrete(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXDiscrete"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXPoint(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXPoint"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXQuantitative(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXQuantitative"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisXTemporal(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisXTemporal"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisY(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisY"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYBand(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYBand"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYDiscrete(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYDiscrete"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYPoint(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYPoint"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYQuantitative(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYQuantitative"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axisYTemporal(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisYTemporal"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.BarConfig)
    def configure_bar(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["bar"] = core.BarConfig(*args, **kwargs)
        return copy

    @use_signature(core.BoxPlotConfig)
    def configure_boxplot(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["boxplot"] = core.BoxPlotConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_circle(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["circle"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.CompositionConfig)
    def configure_concat(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["concat"] = core.CompositionConfig(*args, **kwargs)
        return copy

    @use_signature(core.ErrorBandConfig)
    def configure_errorband(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["errorband"] = core.ErrorBandConfig(*args, **kwargs)
        return copy

    @use_signature(core.ErrorBarConfig)
    def configure_errorbar(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["errorbar"] = core.ErrorBarConfig(*args, **kwargs)
        return copy

    @use_signature(core.CompositionConfig)
    def configure_facet(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["facet"] = core.CompositionConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_geoshape(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["geoshape"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_header(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["header"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_headerColumn(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["headerColumn"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_headerFacet(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["headerFacet"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_headerRow(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["headerRow"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.RectConfig)
    def configure_image(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["image"] = core.RectConfig(*args, **kwargs)
        return copy

    @use_signature(core.LegendConfig)
    def configure_legend(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["legend"] = core.LegendConfig(*args, **kwargs)
        return copy

    @use_signature(core.LineConfig)
    def configure_line(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["line"] = core.LineConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_mark(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["mark"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_point(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["point"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.ProjectionConfig)
    def configure_projection(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["projection"] = core.ProjectionConfig(*args, **kwargs)
        return copy

    @use_signature(core.RangeConfig)
    def configure_range(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["range"] = core.RangeConfig(*args, **kwargs)
        return copy

    @use_signature(core.RectConfig)
    def configure_rect(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["rect"] = core.RectConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_rule(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["rule"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.ScaleConfig)
    def configure_scale(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["scale"] = core.ScaleConfig(*args, **kwargs)
        return copy

    @use_signature(core.SelectionConfig)
    def configure_selection(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["selection"] = core.SelectionConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_square(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["square"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_text(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["text"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.TickConfig)
    def configure_tick(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["tick"] = core.TickConfig(*args, **kwargs)
        return copy

    @use_signature(core.TitleConfig)
    def configure_title(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["title"] = core.TitleConfig(*args, **kwargs)
        return copy

    @use_signature(core.FormatConfig)
    def configure_tooltipFormat(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["tooltipFormat"] = core.FormatConfig(*args, **kwargs)
        return copy

    @use_signature(core.LineConfig)
    def configure_trail(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["trail"] = core.LineConfig(*args, **kwargs)
        return copy

    @use_signature(core.ViewConfig)
    def configure_view(self, *args, **kwargs) -> Self:
        copy = self.copy(deep=["config"])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["view"] = core.ViewConfig(*args, **kwargs)
        return copy
