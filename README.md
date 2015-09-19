# Altair

High-level declarative visualization library for Python.

This package exposes a Python API for building statistical visualizations in a
declarative manner. This API contains no actual visualization rendering code, but instead
just emits JSON data that follows the [vega-lite](https://github.com/vega/vega-lite)
specification.

Actual plotting code is done by renderers that are provided by other plotting libraries.
For the purpose or prototyping, we are shipping a Matplotlib rendered in Altair.

## Testing

We are writing tests using [py.test](http://pytest.org/latest/). The run the Altair test suite, run:

	py.test altair

## Notes on vega-lite

This section contains some notes about our experience in using the `vega-lite` JSON
specification:

* It is odd that the `bin` property can either be a `bool` or an object with a single
  `maxbins` attribute. Would make more sense to have a `bins` attribute that is an integer
  that is `0` when no binning should be used and an integer to set the bins.
* There is a good amount of complexity implicit in the vega-lite spec that is difficult
  to infer from the JSON spec itself. A main example is the subtle interplay between
  aggregation and binning.
