# ChartWidget build instructions
First, [install node.js 18](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

Then build the JavaScript portion of `ChartWidget` widget with:
```
cd widget/
npm install
npm run build
```

This will write a file to `altair/widget/static/index.js`, which is specified as the `_esm` property of the `ChartWidget` [AnyWidget](https://anywidget.dev/).
