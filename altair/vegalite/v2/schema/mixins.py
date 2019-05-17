# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
from . import core
from altair.utils import use_signature
from altair.utils.schemapi import Undefined


class MarkMethodMixin(object):
    """A mixin class that defines mark methods"""

    def mark_area(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                  clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                  dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                  fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                  limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined, point=Undefined,
                  radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                  strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                  strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                  theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                  xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'area'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="area", **kwds)
        else:
            copy.mark = "area"
        return copy

    def mark_bar(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                 clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                 dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                 fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                 limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined, point=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                 xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'bar'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="bar", **kwds)
        else:
            copy.mark = "bar"
        return copy

    def mark_line(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                  clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                  dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                  fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                  limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined, point=Undefined,
                  radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                  strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                  strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                  theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                  xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'line'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="line", **kwds)
        else:
            copy.mark = "line"
        return copy

    def mark_trail(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                   clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                   dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                   fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                   fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                   limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined,
                   point=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                   strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                   strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                   strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                   theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                   xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'trail'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="trail", **kwds)
        else:
            copy.mark = "trail"
        return copy

    def mark_point(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                   clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                   dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                   fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                   fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                   limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined,
                   point=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                   strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                   strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                   strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                   theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                   xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'point'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="point", **kwds)
        else:
            copy.mark = "point"
        return copy

    def mark_text(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                  clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                  dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                  fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                  limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined, point=Undefined,
                  radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                  strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                  strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                  theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                  xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'text'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="text", **kwds)
        else:
            copy.mark = "text"
        return copy

    def mark_tick(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                  clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                  dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                  fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                  limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined, point=Undefined,
                  radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                  strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                  strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                  theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                  xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'tick'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="tick", **kwds)
        else:
            copy.mark = "tick"
        return copy

    def mark_rect(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                  clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                  dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                  fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                  limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined, point=Undefined,
                  radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                  strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                  strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                  theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                  xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'rect'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rect", **kwds)
        else:
            copy.mark = "rect"
        return copy

    def mark_rule(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                  clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                  dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                  fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                  limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined, point=Undefined,
                  radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                  strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                  strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                  theta=Undefined, thickness=Undefined, tooltip=Undefined, x2Offset=Undefined,
                  xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'rule'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rule", **kwds)
        else:
            copy.mark = "rule"
        return copy

    def mark_circle(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                    clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                    dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                    fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                    fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                    limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined,
                    point=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                    stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                    strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                    strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, tension=Undefined,
                    text=Undefined, theta=Undefined, thickness=Undefined, tooltip=Undefined,
                    x2Offset=Undefined, xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'circle'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="circle", **kwds)
        else:
            copy.mark = "circle"
        return copy

    def mark_square(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                    clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                    dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                    fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                    fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                    limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined,
                    point=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                    stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                    strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                    strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, tension=Undefined,
                    text=Undefined, theta=Undefined, thickness=Undefined, tooltip=Undefined,
                    x2Offset=Undefined, xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        """Set the chart's mark to 'square'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="square", **kwds)
        else:
            copy.mark = "square"
        return copy

    def mark_geoshape(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                      clip=Undefined, color=Undefined, cornerRadius=Undefined, cursor=Undefined,
                      dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                      fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                      fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                      limit=Undefined, line=Undefined, opacity=Undefined, orient=Undefined,
                      point=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                      stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                      strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                      strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined,
                      tension=Undefined, text=Undefined, theta=Undefined, thickness=Undefined,
                      tooltip=Undefined, x2Offset=Undefined, xOffset=Undefined, y2Offset=Undefined,
                      yOffset=Undefined, **kwds):
        """Set the chart's mark to 'geoshape'
    
        For information on additional arguments, see :class:`MarkDef`
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, clip=clip,
                    color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                    ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                    interpolate=interpolate, limit=limit, line=line, opacity=opacity, orient=orient,
                    point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                    strokeCap=strokeCap, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                    strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                    strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, thickness=thickness, tooltip=tooltip, x2Offset=x2Offset,
                    xOffset=xOffset, y2Offset=y2Offset, yOffset=yOffset, **kwds)
        copy = self.copy(deep=False)
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="geoshape", **kwds)
        else:
            copy.mark = "geoshape"
        return copy


class ConfigMethodMixin(object):
    """A mixin class that defines config methods"""

    @use_signature(core.Config)
    def configure(self, *args, **kwargs):
        copy = self.copy(deep=False)
        copy.config = core.Config(*args, **kwargs)
        return copy

    @use_signature(core.AreaConfig)
    def configure_area(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["area"] = core.AreaConfig(*args, **kwargs)
        return copy

    @use_signature(core.AxisConfig)
    def configure_axis(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axis"] = core.AxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgAxisConfig)
    def configure_axisBand(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisBand"] = core.VgAxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgAxisConfig)
    def configure_axisBottom(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisBottom"] = core.VgAxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgAxisConfig)
    def configure_axisLeft(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisLeft"] = core.VgAxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgAxisConfig)
    def configure_axisRight(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisRight"] = core.VgAxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgAxisConfig)
    def configure_axisTop(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisTop"] = core.VgAxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgAxisConfig)
    def configure_axisX(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisX"] = core.VgAxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgAxisConfig)
    def configure_axisY(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["axisY"] = core.VgAxisConfig(*args, **kwargs)
        return copy

    @use_signature(core.BarConfig)
    def configure_bar(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["bar"] = core.BarConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_circle(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["circle"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_geoshape(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["geoshape"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.HeaderConfig)
    def configure_header(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["header"] = core.HeaderConfig(*args, **kwargs)
        return copy

    @use_signature(core.LegendConfig)
    def configure_legend(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["legend"] = core.LegendConfig(*args, **kwargs)
        return copy

    @use_signature(core.LineConfig)
    def configure_line(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["line"] = core.LineConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_mark(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["mark"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_point(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["point"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.ProjectionConfig)
    def configure_projection(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["projection"] = core.ProjectionConfig(*args, **kwargs)
        return copy

    @use_signature(core.RangeConfig)
    def configure_range(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["range"] = core.RangeConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_rect(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["rect"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_rule(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["rule"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.ScaleConfig)
    def configure_scale(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["scale"] = core.ScaleConfig(*args, **kwargs)
        return copy

    @use_signature(core.SelectionConfig)
    def configure_selection(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["selection"] = core.SelectionConfig(*args, **kwargs)
        return copy

    @use_signature(core.MarkConfig)
    def configure_square(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["square"] = core.MarkConfig(*args, **kwargs)
        return copy

    @use_signature(core.TextConfig)
    def configure_text(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["text"] = core.TextConfig(*args, **kwargs)
        return copy

    @use_signature(core.TickConfig)
    def configure_tick(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["tick"] = core.TickConfig(*args, **kwargs)
        return copy

    @use_signature(core.VgTitleConfig)
    def configure_title(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["title"] = core.VgTitleConfig(*args, **kwargs)
        return copy

    @use_signature(core.LineConfig)
    def configure_trail(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["trail"] = core.LineConfig(*args, **kwargs)
        return copy

    @use_signature(core.ViewConfig)
    def configure_view(self, *args, **kwargs):
        copy = self.copy(deep=['config'])
        if copy.config is Undefined:
            copy.config = core.Config()
        copy.config["view"] = core.ViewConfig(*args, **kwargs)
        return copy