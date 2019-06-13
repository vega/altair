# Altair Change Log

## Version 3.2.0 (unreleased)
### Enhancements
### Bug Fixes
### Backward-Incompatible Changes

## Version 3.1.0  (Released June 6, 2019)

Update includes full compatibility with version 3.3 of Vega-Lite.

### Enhancements

- Added support for [vega themes](https://github.com/vega/vega-themes) via
  ``alt.themes.enable(theme_name)`` (#1539)

- Added an ``alt.renderers.disable_max_rows()`` method for disabling the
  maximum rows check (#1538)

- Improved user-facing warnings/errors around layering and faceting (#1535).

- ``data`` argument is now properly handled by  ``Chart.properties`` (#1525)

- Compound charts (layer, concat, hconcat, vconcat) now move data to the top
  level by default. In particular, this means that the ``facet()`` method
  can now be called directly on a layered chart without having to change
  how data is specified. (#1521)

- ``alt.LayerChart`` now supports ``mark_*()`` methods. If a layer specifies a
  mark at the top level, all child charts will inherit it (unless they override
  it explicitly).

- ``alt.Chart.facet()`` now handles wrapped facets; for example:
  ```python
  chart.facet('column_name', columns=5)
  ```
  See ``altair/examples/us_population_over_time_facet.py`` for a more
  complete example.

### Bug fixes

- Make ``chart.serve()`` and ``chart.save()`` respect the data transformer
  setting (#1538)

- Fixed a deserialization bug for certain chart specs in schemapi (#1543)

### Backward-Incompatible Changes

- ``alt.Chart.facet()`` now accepts a wrapped facet encoding as a first positional
   argument, rather than a row encoding. The following are examples of old invocations,
   and the equivalent new invocations:

   - ``chart.facet(row='col1', column='col2')``: unchanged
   - ``chart.facet('col1', 'col2')``: change to ``chart.facet(row='col1', column='col2')``
   - ``chart.facet('col1')``: change to ``chart.facet(row='col1')``

   In each case, the new invocations are compatible back to Altair 2.X.

- Several of the encoding channels added in 3.0 have had their capitalization
  corrected to better match the names used in the schema:

  - ``alt.Fillopacity`` -> ``alt.FillOpacity``
  - ``alt.Strokeopacity`` -> ``alt.StrokeOpacity``
  - ``alt.Strokewidth`` -> ``alt.StrokeWidth``
  - ``alt.Xerror`` -> ``alt.XError``
  - ``alt.Xerror2`` -> ``alt.XError2``
  - ``alt.Yerror`` -> ``alt.YError``
  - ``alt.Yerror2`` -> ``alt.YError2``

## Version 3.0.1 (Released May 1, 2019)

Fix version info bug for HTML output and Colab & Kaggle renderers.

## Version 3.0.0 (Released April 26, 2019)

Update to Vega-Lite 3.2 and Vega 5.3 & support all new features. See
https://github.com/vega/vega-lite/releases/tag/v3.0.0 for Vega-Lite
feature lists.

### Highlights:

- new compound marks: ``mark_boxplot()``, ``mark_errorband()``, ``mark_errorbar()``
- new transforms: ``transform_impute()``, ``transform_joinaggregate()``, ``transform_flatten()``
  ``transform_fold()``, ``transform_sample()``, ``transform_stack()``
- new ``facet`` encoding that is similar to the ``row`` and ``column`` encoding, but
  allows for wrapped facets
- new ``alt.concat()`` function that is similar to ``alt.hconcat`` and ``alt.vconcat``,
  but allows for more general wrapped concatenation
- new ``columns`` keyword that allows wrapped faceting, repeating, and concatenation.
- many, many bug fixes
- tooltips can now be automatically populated using the ``tooltip`` mark configuration.
- ability to specify initial condisions for selections

## Version 2.4.1 (Released February 21, 2019)

### Enhancements

- Several documentation cleanups & new examples

### Bug Fixes

- Fix incompatibility with pandas version 0.24 (#1315)

## Version 2.3.0 (Released December 7, 2018)

Includes many reworked examples in the example gallery.

### Enhancements

- Better errors for non-string column names, as well as automatic conversion
  of ``pandas.RangeIndex`` columns to strings (#1107)

- Renderers now have set_embed_options() method (#1203)

- Added kaggle renderer & more HTML output options (#1123)

### Backward-incompatible changes

### Maintenance

- fix typing requirement in Python 3.6+ (#1185)

- Added support & CI testing for Python 3.7 (#1008)

### Bug fixes

- Selection predicates now recognize all valid entries (#1143)
- Python 2 support for `chart.save()` (#1134)

## Version 2.2.2 (Released August 17, 2018)

### Bug Fixes

- fix missing JSON resource in ``altair.vega.v4`` (#1097)

## Version 2.2.1 (Released August 15, 2018)

### Bug Fixes

- appropriate handling of InlineData in dataset consolidation (#1092)

- fix admonition formatting in documentation page (#1094)

## Version 2.2.0 (Released August 14, 2018):

### Enhancements

- better handling of datetimes and timezones (#1053)

- all inline datasets are now converted to named datasets and stored at the
  top level of the chart. This behavior can be disabled by setting
  ``alt.data_transformers.consolidate_datasets = False`` (#951 & #1046)

- more streamlined shorthand syntax for window transforms (#957)

### Maintenance

- update from Vega-Lite 2.4.3 to Vega-Lite 2.6.0; see vega-lite change-logs [2.5.0](https://github.com/vega/vega-lite/releases/tag/v2.5.0) [2.5.1](https://github.com/vega/vega-lite/releases/tag/v2.5.1) [2.5.2](https://github.com/vega/vega-lite/releases/tag/v2.5.2) [2.6.0](https://github.com/vega/vega-lite/releases/tag/v2.6.0)

### Backward-incompatible changes

- ``alt.SortField`` renamed to ``alt.EncodingSortField`` and
  ``alt.WindowSortField`` renamed to ``alt.SortField`` (#3741)

### Bug Fixes

- Fixed serialization of logical operands on selections within
  ``transform_filter()``: (#1075)

- Fixed sphinx issue which embedded chart specs twice (#1088)

- Avoid Selenium import until it is actually needed (#982)

## Version 2.1.0 (Released June 6, 2018):

### Enhancements

- add a ``scale_factor`` argument to ``chart.save()`` to allow the
  size/resolution of saved figures to be adjusted. (#918)

- add an ``add_selection()`` method to add selections to charts (#832)

- add ``chart.serve()`` and ``chart.display()`` methods for more flexibility
  in displaying charts (#831)

- allow multiple fields to be passed to encodings such as ``tooltip``
  and ``detail`` (#830)

- make ``timeUnit`` specifications more succinct, by parsing them in a manner
  similar to aggregates (#866)

- make ``to_json()`` and ``to_csv()`` have deterministic filenames, so in json
  mode a single datasets will lead to a single on-disk serialization (#862)

### Breaking Changes

- make ``data`` the first argument for all compound chart types to match the
  semantics of ``alt.Chart`` (this includes ``alt.FacetChart``,
  ``alt.LayerChart``, ``alt.RepeatChart``, ``alt.VConcatChart``, and
  ``alt.HConcatChart``) (#895).

- update vega-lite to version 2.4.3 (#836)

  - Only API change is internal: ``alt.MarkProperties`` is now ``alt.MarkConfig``

### Maintenance

- update vega to v3.3 & vega-embed to v3.11 in html output & colab renderer (#838)


## Version 2.0.0: May 2, 2018

- Complete rewrite of Altair, focused on supporting Vega-Lite 2.X

## Version 1.2.1: October 29, 2017

This version of Altair is based on Vega-Lite 1.2.1.

### Major additions

- Support for JupyterLab/nteract through MIME based rendering. Enable this by calling
  `enable_mime_rendering()` before rendering visualizations
  ([#216](https://github.com/altair-viz/altair/pull/216)).

- Change default import in all code and docs to `import altair as alt`

- Check for missing and misspelled column names upon exporting or rendering,
  and raise `FieldError` ([#399](https://github.com/altair-viz/altair/pull/399))
  if any problems are found. This can be disabled by setting `Chart.validated_columns=False`.

- Raise `MaxRowsExceeded`  if the number of rows in the dataset is larger than `Chart.max_rows`
  to guard against sending large datasets to the browser.

- Move the Vega-Lite 1.x api into `altair.v1` to make it easier for us to migrate to Vega-Lite
  2.x and continue to support 1.x. No import change are needed as `altair.v1` is aliased to
  `altair` in this release`altair.v1` ([#377](https://github.com/altair-viz/altair/pull/377)).

- Moved the example notebooks into a separate repository (https://github.com/altair-viz/altair_notebooks) that has Binder support
  ([#391](https://github.com/altair-viz/altair/pull/391)).

- Add `$schema` to top-level JSON spec ([#370](https://github.com/altair-viz/altair/issues/370)).

- Minor documentation revisions.

### Bug fixes

- Make sure default mark is a point ([#344](https://github.com/altair-viz/altair/pull/344)).

## Version 1.2: Nov 7, 2016

### Major additions

- Update to Vega-Lite 1.2 and make all its enhancements available to Altair

- Add ``Chart.serve`` method
  ([#197](https://github.com/altair-viz/altair/pull/197))

- Add ``altair.expr`` machinery to specify transformations and filterings
  ([#215](https://github.com/altair-viz/altair/pull/215))

- Add ``Chart.savechart`` method, which can output JSON, HTML, and (if Node
  is installed) PNG and SVG. See https://altair-viz.github.io/documentation/displaying.html ([#213](https://github.com/altair-viz/altair/pull/213))

### Bug fixes

- Countless minor bug fixes

### maintenance:

- Update to Vega-Lite 1.2.1 and add its supported features

- Create website: http://altair-viz.github.io/

- Set up Travis to run conda & pip; and to build documentation


## Version 1.0: July 11, 2016

- Initial release of Altair
