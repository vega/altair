.. currentmodule:: altair

.. _user-guide-image-marks:

Image
~~~~~~

Image marks allow external images, such as icons or photographs, to be included in Altair visualizations. Image files such as PNG or JPG images are loaded from provided URLs.

Image Mark Properties
^^^^^^^^^^^^^^^^^^^^^
An ``image`` mark can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: url aspect align baseline

Scatter Plot with Image Marks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame.from_records(
        [
            {
                "x": 0.5,
                "y": 0.5,
                "img": "https://vega.github.io/vega-datasets/data/ffox.png",
            },
            {
                "x": 1.5,
                "y": 1.5,
                "img": "https://vega.github.io/vega-datasets/data/gimp.png",
            },
            {
                "x": 2.5,
                "y": 2.5,
                "img": "https://vega.github.io/vega-datasets/data/7zip.png",
            },
        ]
    )

    alt.Chart(source).mark_image(width=50, height=50).encode(x="x", y="y", url="img")

Show Image Marks with Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example demonstrates how to display image marks with drag selection. We create two charts:
one with point marks and the other with image marks, applying the selection filter only to the latter.
By combining these two charts, we can achieve the desired result.

.. altair-plot::

    import altair as alt
    import pandas as pd

    source = pd.DataFrame.from_records(
        [{'a': 1, 'b': 1, 'image': 'https://altair-viz.github.io/_static/altair-logo-light.png'},
        {'a': 2, 'b': 2, 'image': 'https://avatars.githubusercontent.com/u/11796929?s=200&v=4'}]
    )

    brush = alt.selection_interval()
    point = alt.Chart(source).mark_circle(size=100).encode(
        x='a',
        y='b',
    ).add_params(
        brush
    )

    img = alt.Chart(source).mark_image(width=50, height=75).encode(
        x='a',
        y='b',
        url='image'
    ).transform_filter(
        brush
    )

    point + img

In the layered chart, images may overlap one other. 
An alternative is to use a faceted image chart beside the original chart:

.. altair-plot::

    img_faceted = alt.Chart(source, width=50, height=75).mark_image().encode(
        url='image'
    ).facet(
        alt.Facet('image', title='', header=alt.Header(labelFontSize=0))
    ).transform_filter(
        brush
    )

    point | img_faceted

If we want the images to not be visible in the initial chart
we could add ``empty=False`` to the interval selection.
However,
Altair will not automatically resize the chart area to include the faceted chart
when a selection is made,
which means it seems like the selection has no effect.
In order to resize the chart automatically,
we need to explicitly set the ``autosize`` option in the ``configure`` method.

.. altair-plot::

    brush = alt.selection_interval(empty=False)
    point = alt.Chart(source).mark_circle(size=100).encode(
        x='a',
        y='b',
    ).add_params(
        brush
    )
    img_faceted = alt.Chart(source, width=50, height=75).mark_image().encode(
        url='image'
    ).facet(
        alt.Facet('image', title='', header=alt.Header(labelFontSize=0))
    ).transform_filter(
        brush
    )

    (point | img_faceted).configure(
        autosize=alt.AutoSizeParams(resize=True)
    )


Use Local Images as Image Marks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We could also show local images by first converting them to base64-encoded_ strings.
In the example below,
we load two images saved in the Altair repo;
you can replace the image paths below with the location of the desired images on your machine.
This approach also works with images stored as Numpy Arrays
as can be seen in the tutorial :ref:`Displaying Numpy Images in Tooltips <numpy-tooltip-imgs>`.

.. altair-plot::

    import base64
    import altair as alt
    import pandas as pd

    from io import BytesIO
    from PIL import Image


    image_paths = ["doc/_static/gray-square.png","doc/_static/altair-logo-light.png"]
    base64_images = []

    for image_path in image_paths:
        pil_image = Image.open(image_path)
        output = BytesIO()
        pil_image.save(output, format='PNG')
        base64_images.append(
            "data:image/png;base64," + base64.b64encode(output.getvalue()).decode()
        )

    source = pd.DataFrame({"x": [1, 2], "y": [1, 2], "image": base64_images})
    alt.Chart(source).mark_image(
        width=50,
        height=50
    ).encode(
        x='x',
        y='y',
        url='image'
    )

Image Tooltip
^^^^^^^^^^^^^
This example shows how to render images in tooltips.
Either URLs or local file paths can be used to reference the images.
To render the image, you must use the special column name "image" in your data 
and pass it as a list to the tooltip encoding.

.. altair-plot::

    import altair as alt
    import pandas as pd

    source = pd.DataFrame.from_records(
        [{'a': 1, 'b': 1, 'image': 'https://altair-viz.github.io/_static/altair-logo-light.png'},
         {'a': 2, 'b': 2, 'image': 'https://avatars.githubusercontent.com/u/11796929?s=200&v=4'}]
    )

    alt.Chart(source).mark_circle(size=200).encode(
        x='a',
        y='b',
        tooltip=['image']  # Must be a list containing a field called "image"
    )


.. _base64-encoded: https://en.wikipedia.org/wiki/Binary-to-text_encoding
