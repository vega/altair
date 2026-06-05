.. currentmodule:: altair

.. _user-guide-encoding-channel-options:

Channel Options
---------------

Some encoding channels allow for additional options to be expressed.
These can control things like axis properties, scale properties, headers and
titles, binning parameters, aggregation, sorting, and many more.

The section titles below refer to the channels introduced in :ref:`user-guide-encoding-channels`
and show the accepted options for these channels.


X and Y
~~~~~~~

The :class:`X` and :class:`Y` encodings accept the following options:

.. altair-object-table:: altair.PositionFieldDef

Color, Fill, and Stroke
~~~~~~~~~~~~~~~~~~~~~~~

The :class:`Color`, :class:`Fill`, and :class:`Stroke`  encodings accept the following options:

.. altair-object-table:: altair.FieldOrDatumDefWithConditionMarkPropFieldDefGradientstringnull

Shape
~~~~~

The :class:`Shape` encoding accepts the following options:

.. altair-object-table:: altair.FieldOrDatumDefWithConditionMarkPropFieldDefTypeForShapestringnull

Order
~~~~~

The :class:`Order` encoding accepts the following options:

.. altair-object-table:: altair.OrderFieldDef

Angle, FillOpacity, Opacity, Size, StrokeOpacity, and StrokeWidth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`Angle`, :class:`FillOpacity`, :class:`Opacity`, :class:`Size`, :class:`StrokeOpacity`,
and :class:`StrokeWidth` encodings accept the following options:

.. altair-object-table:: altair.FieldOrDatumDefWithConditionMarkPropFieldDefnumber

StrokeDash
~~~~~~~~~~

The :class:`StrokeDash` encoding accepts the following options:

.. altair-object-table:: altair.FieldOrDatumDefWithConditionMarkPropFieldDefnumberArray

Row and Column
~~~~~~~~~~~~~~

The :class:`Row` and :class:`Column`, and :class:`Facet` encodings accept the following options:

.. altair-object-table:: altair.RowColumnEncodingFieldDef

Facet
~~~~~

The :class:`Facet` encoding accepts the following options:

.. altair-object-table:: altair.FacetEncodingFieldDef

Text
~~~~

The :class:`Text` encoding accepts the following options:

.. altair-object-table:: altair.FieldOrDatumDefWithConditionStringFieldDefText

Href, Tooltip, Url
~~~~~~~~~~~~~~~~~~

The :class:`Href`, :class:`Tooltip`, and :class:`Url` encodings accept the following options:

.. altair-object-table:: altair.StringFieldDefWithCondition

Detail
~~~~~~

The :class:`Detail` encoding accepts the following options:

.. altair-object-table:: altair.FieldDefWithoutScale

Latitude and Longitude
~~~~~~~~~~~~~~~~~~~~~~

The :class:`Latitude` and :class:`Longitude` encodings accept the following options:

.. altair-object-table:: altair.LatLongFieldDef

Radius and Theta
~~~~~~~~~~~~~~~~

The :class:`Radius` and :class:`Theta` encodings accept the following options:

.. altair-object-table:: altair.PositionFieldDefBase

Latitude2, Longitude2, Radius2, Theta2, X2, Y2, XError, YError, XError2, and YError2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`Latitude2`, :class:`Longitude2`, :class:`Radius2`, :class:`Theta2`, :class:`X2`, :class:`Y2`, :class:`XError`, :class:`YError`, :class:`XError2`, and :class:`YError2` encodings accept the following options:

.. altair-object-table:: altair.SecondaryFieldDef

