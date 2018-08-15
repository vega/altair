# Altair Change Log

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
