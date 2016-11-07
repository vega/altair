# Altair Change Log


## Version 1.2: Nov 7, 2016

### Major additions

- Add ``Chart.serve`` method
  ([#197](https://github.com/altair-viz/altair/pull/197))

- Add ``altair.expr`` machinery to specify transformations and filterings
  ([#213](https://github.com/altair-viz/altair/pull/213))

- Add ``Chart.savechart`` method, which can output JSON, HTML, and (if Node
  is installed) PNG and SVG. See https://altair-viz.github.io/documentation/displaying.html

### Bug Fixes

- Countless minor bug fixes

### Maintenance:

- Update to Vega-Lite 1.2.1 and add its supported features

- Create website: http://altair-viz.github.io/

- Set up Travis to run conda & pip; and to build documentation


## Version 1.0: July 11, 2016

- Initial release of Altair