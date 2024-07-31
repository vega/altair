Versioning
==========
Vega-Altair has historically released major versions that coincide with those of Vega-Lite_.

As the projects have matured, and major versions become less frequent, there has been a growing need to introduce breaking changes between these major versions.
Such changes would allow Vega-Altair to address technical debt and improve upon API ergonomics.

To ensure future releases clearly communicate changes, Vega-Altair will be working towards adopting SemVer_.

Public API
----------
Functionality documented in :ref:`api` defines the Vega-Altair public API.

Version numbers
---------------

A Vega-Altair release number is composed of ``MAJOR.MINOR.PATCH``.

* Backward incompatible API changes increment **MAJOR** version (``4.2.2`` - ``5.0.0``)
* New backward compatible functionality increment **MINOR** version (``5.2.0`` - ``5.3.0``)
* Backward compatible bug fixes increment **PATCH** version (``5.1.1`` - ``5.1.2``)

**MAJOR** versions will *likely* continue to increase with a **MAJOR** increment to Vega-Lite_.

Deprecation
-----------
Deprecation warnings may be introduced in **MAJOR** and **MINOR** versions, 
but the removal of deprecated functionality will not occur until *at least* the next **MAJOR** version.

For upstream breaking changes that trigger a **MAJOR** version, 
we *may* provide a deprecation warning if we consider the change especially disruptive.

Starting in version ``5.4.0``, all deprecation warnings *must* specify:

* the version number they were introduced

Where possible, deprecation warnings *may* specify:

* an alternative function/method/parameter/class to use instead
* an explanation for why this change had to be made

Deprecated functionality *may* be removed from the Vega-Altair documentation, if there is a 
suitable replacement and we believe inclusion of both could confuse new users.

.. _Vega-Lite: https://github.com/vega/vega-lite
.. _SemVer: https://semver.org/