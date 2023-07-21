# ChartWidget
This directory contains the JavaScript portion of the Altair `ChartWidget` Jupyter Widget. The `ChartWidget` is based on the [AnyWidget](https://anywidget.dev/) project.

# ChartWidget development instructions
First, make sure you have Node.js 18 installed.

Then build the JavaScript portion of `ChartWidget` widget in development mode:
```
cd widget/
npm install
npm run watch
```

This will write a file to `altair/widget/static/index.js`, which is specified as the `_esm` property of the `ChartWidget` Python class (located at `altair/widget/__init__.py`). Any changes to `widget/src/index.js` will automatically be recompiled as long as the `npm run watch` command is running.

# Release process
The JavaScript portion of the `ChartWidget` is automatically built in release mode when `hatch build` runs.
