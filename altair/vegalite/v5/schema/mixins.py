# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Literal, Sequence

from altair.utils import use_signature
from altair.utils.schemapi import Undefined

from . import core

if TYPE_CHECKING:
    from altair import Parameter, SchemaBase

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


# ruff: noqa: F405
if TYPE_CHECKING:
    from altair.typing import Optional

    from ._typing import *  # noqa: F403


class MarkMethodMixin:
    """A mixin class that defines mark methods."""

    def mark_arc(
        self,
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'arc' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'area' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'bar' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'image' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'line' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'point' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'rect' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'rule' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'text' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'tick' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'trail' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'circle' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'square' (see :class:`MarkDef`)."""
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
        align: Optional[Parameter | SchemaBase | Map | Align_T] = Undefined,
        angle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        aria: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        ariaRole: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        ariaRoleDescription: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        aspect: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        bandSize: Optional[float] = Undefined,
        baseline: Optional[Parameter | SchemaBase | Map | TextBaseline_T] = Undefined,
        binSpacing: Optional[float] = Undefined,
        blend: Optional[Parameter | SchemaBase | Map | Blend_T] = Undefined,
        clip: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        continuousBandSize: Optional[float] = Undefined,
        cornerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusBottomLeft: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusBottomRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cornerRadiusEnd: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopLeft: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        cornerRadiusTopRight: Optional[
            float | Parameter | SchemaBase | Map
        ] = Undefined,
        cursor: Optional[Parameter | SchemaBase | Map | Cursor_T] = Undefined,
        description: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        dir: Optional[Parameter | SchemaBase | Map | TextDirection_T] = Undefined,
        discreteBandSize: Optional[float | SchemaBase | Map] = Undefined,
        dx: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        dy: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        ellipsis: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fill: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        fillOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        filled: Optional[bool] = Undefined,
        font: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        fontStyle: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        fontWeight: Optional[Parameter | SchemaBase | Map | FontWeight_T] = Undefined,
        height: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        href: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        innerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        interpolate: Optional[Parameter | SchemaBase | Map | Interpolate_T] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        limit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        line: Optional[bool | SchemaBase | Map] = Undefined,
        lineBreak: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        lineHeight: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        minBandSize: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        opacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        order: Optional[bool | None] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outerRadius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        padAngle: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        point: Optional[bool | SchemaBase | Literal["transparent"] | Map] = Undefined,
        radius: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radius2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        radiusOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        shape: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        size: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        smooth: Optional[bool | Parameter | SchemaBase | Map] = Undefined,
        stroke: Optional[
            str | None | Parameter | SchemaBase | Map | ColorName_T
        ] = Undefined,
        strokeCap: Optional[Parameter | SchemaBase | Map | StrokeCap_T] = Undefined,
        strokeDash: Optional[
            Parameter | SchemaBase | Sequence[float] | Map
        ] = Undefined,
        strokeDashOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeJoin: Optional[Parameter | SchemaBase | Map | StrokeJoin_T] = Undefined,
        strokeMiterLimit: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeOpacity: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        strokeWidth: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        style: Optional[str | Sequence[str]] = Undefined,
        tension: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        text: Optional[str | Parameter | SchemaBase | Sequence[str] | Map] = Undefined,
        theta: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        theta2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thetaOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        thickness: Optional[float] = Undefined,
        timeUnitBandPosition: Optional[float] = Undefined,
        timeUnitBandSize: Optional[float] = Undefined,
        tooltip: Optional[
            str | bool | None | float | Parameter | SchemaBase | Map
        ] = Undefined,
        url: Optional[str | Parameter | SchemaBase | Map] = Undefined,
        width: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        x: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2: Optional[
            float | Parameter | SchemaBase | Literal["width"] | Map
        ] = Undefined,
        x2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        xOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        y: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2: Optional[
            float | Parameter | SchemaBase | Literal["height"] | Map
        ] = Undefined,
        y2Offset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        yOffset: Optional[float | Parameter | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'geoshape' (see :class:`MarkDef`)."""
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
        box: Optional[bool | SchemaBase | Map] = Undefined,
        clip: Optional[bool] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        extent: Optional[float | Literal["min-max"]] = Undefined,
        invalid: Optional[None | SchemaBase | MarkInvalidDataMode_T] = Undefined,
        median: Optional[bool | SchemaBase | Map] = Undefined,
        opacity: Optional[float] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        outliers: Optional[bool | SchemaBase | Map] = Undefined,
        rule: Optional[bool | SchemaBase | Map] = Undefined,
        size: Optional[float] = Undefined,
        ticks: Optional[bool | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'boxplot' (see :class:`BoxPlotDef`)."""
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
        clip: Optional[bool] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        extent: Optional[SchemaBase | ErrorBarExtent_T] = Undefined,
        opacity: Optional[float] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        rule: Optional[bool | SchemaBase | Map] = Undefined,
        size: Optional[float] = Undefined,
        thickness: Optional[float] = Undefined,
        ticks: Optional[bool | SchemaBase | Map] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'errorbar' (see :class:`ErrorBarDef`)."""
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
        band: Optional[bool | SchemaBase | Map] = Undefined,
        borders: Optional[bool | SchemaBase | Map] = Undefined,
        clip: Optional[bool] = Undefined,
        color: Optional[str | Parameter | SchemaBase | Map | ColorName_T] = Undefined,
        extent: Optional[SchemaBase | ErrorBarExtent_T] = Undefined,
        interpolate: Optional[SchemaBase | Interpolate_T] = Undefined,
        opacity: Optional[float] = Undefined,
        orient: Optional[SchemaBase | Orientation_T] = Undefined,
        tension: Optional[float] = Undefined,
        **kwds,
    ) -> Self:
        """Set the chart's mark to 'errorband' (see :class:`ErrorBandDef`)."""
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
    """A mixin class that defines config methods."""

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
