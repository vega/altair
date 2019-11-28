from ...utils.deprecation import _deprecated
from . import channels

# Deprecated classes (see https://github.com/altair-viz/altair/issues/1474).
# TODO: Remove these in Altair 3.2.
Fillopacity = _deprecated(channels.FillOpacity, 'Fillopacity')
FillopacityValue = _deprecated(channels.FillOpacityValue, 'FillopacityValue')
Strokeopacity = _deprecated(channels.StrokeOpacity, 'Strokeopacity')
StrokeopacityValue = _deprecated(channels.StrokeOpacityValue, 'StrokeopacityValue')
Strokewidth = _deprecated(channels.StrokeWidth, 'Strokewidth')
StrokewidthValue = _deprecated(channels.StrokeWidthValue, 'StrokewidthValue')
Xerror = _deprecated(channels.XError, 'Xerror')
XerrorValue = _deprecated(channels.XErrorValue, 'XerrorValue')
Xerror2 = _deprecated(channels.XError2, 'Xerror2')
Xerror2Value = _deprecated(channels.XError2Value, 'Xerror2Value')
Yerror = _deprecated(channels.YError, 'Yerror')
YerrorValue = _deprecated(channels.YErrorValue, 'YerrorValue')
Yerror2 = _deprecated(channels.YError2, 'Yerror2')
Yerror2Value = _deprecated(channels.YError2Value, 'Yerror2Value')
