Versioning
==========
Vega-Altair has historically released major versions that coincide with those of Vega-Lite_.

As the projects have matured, and major versions become less frequent, there has been a growing need to introduce breaking changes between these major versions.
Such changes would allow Vega-Altair to address technical debt and improve upon API ergonomics.

To ensure future releases clearly communicate changes, Vega-Altair will be working towards adopting SemVer_.

Version numbers
---------------

A Vega-Altair release number is composed of ``MAJOR.MINOR.PATCH``.

* Backward incompatible API changes increment **MAJOR** version (``4.2.2`` - ``5.0.0``)
* New backward compatible functionality increment **MINOR** version (``5.2.0`` - ``5.3.0``)
* Backward compatible bug fixes increment **PATCH** version (``5.1.1`` - ``5.1.2``)

**MAJOR** versions will *likely* continue to increase with a **MAJOR** increment to Vega-Lite_.

.. _Vega-Lite: https://github.com/vega/vega-lite
.. _SemVer: https://semver.org/