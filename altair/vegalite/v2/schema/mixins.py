# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
# 2018-02-27 12:09

from altair.utils.schemapi import Undefined
from . import core

class MarkMethodMixin(object):
    """A mixin that defines mark methods"""

    def mark_area(self, align=Undefined, angle=Undefined, baseline=Undefined,
                  clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                  dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                  filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                  interpolate=Undefined, limit=Undefined, opacity=Undefined,
                  orient=Undefined, radius=Undefined, shape=Undefined,
                  size=Undefined, stroke=Undefined, strokeDash=Undefined,
                  strokeDashOffset=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined,
                  text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'area'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="area", **kwds)
        else:
            copy.mark = "area"
        return copy

    def mark_bar(self, align=Undefined, angle=Undefined, baseline=Undefined,
                 clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                 dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                 interpolate=Undefined, limit=Undefined, opacity=Undefined,
                 orient=Undefined, radius=Undefined, shape=Undefined,
                 size=Undefined, stroke=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, style=Undefined, tension=Undefined,
                 text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'bar'
    
        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="bar", **kwds)
        else:
            copy.mark = "bar"
        return copy

    def mark_line(self, align=Undefined, angle=Undefined, baseline=Undefined,
                  clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                  dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                  filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                  interpolate=Undefined, limit=Undefined, opacity=Undefined,
                  orient=Undefined, radius=Undefined, shape=Undefined,
                  size=Undefined, stroke=Undefined, strokeDash=Undefined,
                  strokeDashOffset=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined,
                  text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'line'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="line", **kwds)
        else:
            copy.mark = "line"
        return copy

    def mark_point(self, align=Undefined, angle=Undefined, baseline=Undefined,
                   clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                   dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                   filled=Undefined, font=Undefined, fontSize=Undefined,
                   fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                   interpolate=Undefined, limit=Undefined, opacity=Undefined,
                   orient=Undefined, radius=Undefined, shape=Undefined,
                   size=Undefined, stroke=Undefined, strokeDash=Undefined,
                   strokeDashOffset=Undefined, strokeOpacity=Undefined,
                   strokeWidth=Undefined, style=Undefined, tension=Undefined,
                   text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'point'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="point", **kwds)
        else:
            copy.mark = "point"
        return copy

    def mark_text(self, align=Undefined, angle=Undefined, baseline=Undefined,
                  clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                  dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                  filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                  interpolate=Undefined, limit=Undefined, opacity=Undefined,
                  orient=Undefined, radius=Undefined, shape=Undefined,
                  size=Undefined, stroke=Undefined, strokeDash=Undefined,
                  strokeDashOffset=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined,
                  text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'text'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="text", **kwds)
        else:
            copy.mark = "text"
        return copy

    def mark_tick(self, align=Undefined, angle=Undefined, baseline=Undefined,
                  clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                  dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                  filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                  interpolate=Undefined, limit=Undefined, opacity=Undefined,
                  orient=Undefined, radius=Undefined, shape=Undefined,
                  size=Undefined, stroke=Undefined, strokeDash=Undefined,
                  strokeDashOffset=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined,
                  text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'tick'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="tick", **kwds)
        else:
            copy.mark = "tick"
        return copy

    def mark_rect(self, align=Undefined, angle=Undefined, baseline=Undefined,
                  clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                  dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                  filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                  interpolate=Undefined, limit=Undefined, opacity=Undefined,
                  orient=Undefined, radius=Undefined, shape=Undefined,
                  size=Undefined, stroke=Undefined, strokeDash=Undefined,
                  strokeDashOffset=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined,
                  text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'rect'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rect", **kwds)
        else:
            copy.mark = "rect"
        return copy

    def mark_rule(self, align=Undefined, angle=Undefined, baseline=Undefined,
                  clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                  dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                  filled=Undefined, font=Undefined, fontSize=Undefined,
                  fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                  interpolate=Undefined, limit=Undefined, opacity=Undefined,
                  orient=Undefined, radius=Undefined, shape=Undefined,
                  size=Undefined, stroke=Undefined, strokeDash=Undefined,
                  strokeDashOffset=Undefined, strokeOpacity=Undefined,
                  strokeWidth=Undefined, style=Undefined, tension=Undefined,
                  text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'rule'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="rule", **kwds)
        else:
            copy.mark = "rule"
        return copy

    def mark_circle(self, align=Undefined, angle=Undefined, baseline=Undefined,
                    clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                    dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                    filled=Undefined, font=Undefined, fontSize=Undefined,
                    fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                    interpolate=Undefined, limit=Undefined, opacity=Undefined,
                    orient=Undefined, radius=Undefined, shape=Undefined,
                    size=Undefined, stroke=Undefined, strokeDash=Undefined,
                    strokeDashOffset=Undefined, strokeOpacity=Undefined,
                    strokeWidth=Undefined, style=Undefined, tension=Undefined,
                    text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'circle'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="circle", **kwds)
        else:
            copy.mark = "circle"
        return copy

    def mark_square(self, align=Undefined, angle=Undefined, baseline=Undefined,
                    clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined,
                    dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                    filled=Undefined, font=Undefined, fontSize=Undefined,
                    fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                    interpolate=Undefined, limit=Undefined, opacity=Undefined,
                    orient=Undefined, radius=Undefined, shape=Undefined,
                    size=Undefined, stroke=Undefined, strokeDash=Undefined,
                    strokeDashOffset=Undefined, strokeOpacity=Undefined,
                    strokeWidth=Undefined, style=Undefined, tension=Undefined,
                    text=Undefined, theta=Undefined, **kwds):
        """Set the chart's mark to 'square'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="square", **kwds)
        else:
            copy.mark = "square"
        return copy

    def mark_geoshape(self, align=Undefined, angle=Undefined, baseline=Undefined,
                      clip=Undefined, color=Undefined, cursor=Undefined,
                      dx=Undefined, dy=Undefined, fill=Undefined,
                      fillOpacity=Undefined, filled=Undefined, font=Undefined,
                      fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined,
                      href=Undefined, interpolate=Undefined, limit=Undefined,
                      opacity=Undefined, orient=Undefined, radius=Undefined,
                      shape=Undefined, size=Undefined, stroke=Undefined,
                      strokeDash=Undefined, strokeDashOffset=Undefined,
                      strokeOpacity=Undefined, strokeWidth=Undefined,
                      style=Undefined, tension=Undefined, text=Undefined,
                      theta=Undefined, **kwds):
        """Set the chart's mark to 'geoshape'

        For information on additional arguments, see ``alt.MarkDef``
        """
        kwds = dict(align=align, angle=angle, baseline=baseline, clip=clip,
                    color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                    fillOpacity=fillOpacity, filled=filled, font=font,
                    fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                    href=href, interpolate=interpolate, limit=limit,
                    opacity=opacity, orient=orient, radius=radius, shape=shape,
                    size=size, stroke=stroke, strokeDash=strokeDash,
                    strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                    strokeWidth=strokeWidth, style=style, tension=tension,
                    text=text, theta=theta, **kwds)
        copy = self.copy(deep=True, ignore=['data'])
        if any(val is not Undefined for val in kwds.values()):
            copy.mark = core.MarkDef(type="geoshape", **kwds)
        else:
            copy.mark = "geoshape"
        return copy
