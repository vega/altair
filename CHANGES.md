# Altair Change Log

## Version 2.0.0:

Complete rewrite of Altair, focused on supporting Vega-Lite 2.X

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
