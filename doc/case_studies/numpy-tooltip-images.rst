.. _numpy-tooltip-imgs:

Displaying Numpy Images in Tooltips
-----------------------------------

In this tutorial,
you’ll learn how to display images stored as Numpy arrays
in tooltips with any Altair chart.

First,
we create some example image arrays with blobs (objects)
of different sizes and shapes (circular and square).
We measure the area of the blobs
in order to have a quantitative measurement
to compare them with in our charts.

.. altair-plot::
    :output: repr

    import numpy as np
    import pandas as pd
    from scipy import ndimage as ndi

    rng = np.random.default_rng([ord(c) for c in 'altair'])
    n_rows = 200

    def create_blobs(blob_shape, img_width=96, n_dim=2, sizes=[0.05, 0.1, 0.15]):
        """Helper function to create blobs in the images"""
        shape = tuple([img_width] * n_dim)
        mask = np.zeros(shape)
        points = (img_width * rng.random(n_dim)).astype(int)
        mask[tuple(indices for indices in points)] = 1
        if blob_shape == 'circle':
            im = ndi.gaussian_filter(mask, sigma=rng.choice(sizes) * img_width)
        elif blob_shape == 'square':
            im = ndi.uniform_filter(mask, size=rng.choice(sizes) * img_width, mode='constant') * rng.normal(4, size=(img_width, img_width))
        return im / im.max()

    df = pd.DataFrame({
        'image1': [create_blobs('circle') for _ in range(n_rows)],
        'image2': [create_blobs('square', sizes=[0.3, 0.4, 0.5]) for _ in range(n_rows)],
        'group': rng.choice(['a', 'b', 'c'], size=n_rows)
    })
    # Compute the area as the proportion of pixels above a threshold
    df[['image1_area', 'image2_area']] = df[['image1', 'image2']].map(lambda x: (x > 0.4).mean())
    df

Next, we define the function
that will convert the Numpy arrays to base64-encoded_ strings.
This is a necessary step
for the tooltip to recognize that the data
is in the form of an image and render it appropriately.


.. altair-plot::
    :output: repr

    from io import BytesIO
    from PIL import Image, ImageDraw
    import base64


    def create_tooltip_image(df_row):
        """Concatenate, rescale, and convert images to base64 strings."""
        # Concatenate images to show together in the tooltip
        # This can be skipped if only one image is to be displayed
        img_gap = np.ones([df_row['image1'].shape[0], 10])  # 10 px white gap between imgs
        img_arr = np.concatenate(
            [
                df_row['image1'],
                img_gap,
                df_row['image2']
            ],
            axis=1
        )

        # Create a PIL image from the array.
        # Multiplying by 255 and recasting as uint8 for the images to occupy the entire supported instensity space from 0-255
        img = Image.fromarray((255 * img_arr).astype('uint8'))

        # Optional: Burn in labels as pixels in the images. Can be helpful to keep track of which image is which
        ImageDraw.Draw(img).text((3, 0), 'im1', fill=255)
        ImageDraw.Draw(img).text((3 + df_row['image1'].shape[1] + img_gap.shape[1], 0), 'im2', fill=255)

        # Convert to base64 encoded image string that can be displayed in the tooltip
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"

    # The column with the base64 image string must be called "image" in order for it to trigger the image rendering in the tooltip
    df['image'] = df[['image1', 'image2']].apply(create_tooltip_image, axis=1)

    # Dropping the image arrays since they are large and no longer needed
    df_plot = df.drop(columns=['image1', 'image2'])
    df_plot

Now we are ready to create the charts that show the images as tooltips
when the dots are hovered with the mouse.
We can see that the large white blobs
correspond to the higher area measurements
as expected.

.. altair-plot::
    import altair as alt

    # The random() function is used to jitter points in the x-direction
    alt.Chart(df_plot, width=alt.Step(40)).mark_circle(xOffset=alt.expr('random() * 16 - 8')).encode(
        x='group',
        y=alt.Y(alt.repeat(), type='quantitative'),
        tooltip=['image'],
        color='group',
    ).repeat(
        ['image1_area', 'image2_area']
    ).resolve_scale(
        y='shared'
    ).properties(
        title='Comparison of blob areas'
    )

Note that when including images as part of the chart data,
the chart size often increases several-fold.
The size of the chart above would have been 19 Kb without the images,
but with the images added it is 760 Kb.
While this is a 20x size increase,
the base64 encoding is still quite storage efficient;
if we would have included the images in their original Numpy array format
the chart size would have been 35Mb!

If we want to have even more fun and get a bit more sophisticated,
we could show one chart at a time
and update what is shown on the y-axis
as well as what is shown in the image tooltip
based on a dropdown selector.
We start by defining a tooltip that only contains a single image
instead of both the images concatenated together.

.. altair-plot::
    :output: repr

    def create_tooltip_image(img_arr):
        """Rescale and convert an image to a base64 string."""
        # print(img_arr)
        # Create a PIL image from the array.
        # Multiplying by 255 and recasting as uint8 for the images to occupy the entire supported instensity space from 0-255
        img = Image.fromarray((255 * img_arr).astype('uint8'))

        # Convert to base64 encoded image string that can be displayed in the tooltip
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"

    # The column with the base64 image string must be called "image" in order for it to trigger the image rendering in the tooltip
    df[['image1_base64', 'image2_base64']] = df[['image1', 'image2']].map(create_tooltip_image)
    # Dropping the image arrays since they are large and no longer needed
    # Also drop the previous tooltip image for clarity
    df_plot = df.drop(columns=['image1', 'image2', 'image'])
    df_plot

In our chart,
we need to use a transform to update
both the y-axis column as well as the tooltip column
dynamically based on the selection in the dropdown.
The comments in the code explain more in detail what each line
in this chart specification does.

.. altair-plot::
    metric_dropdown = alt.binding_select(
        options=['image1_area', 'image2_area'],
        name='Image metric '
    )
    metric_param = alt.param(
        value='image1_area',
        bind=metric_dropdown
    )
    alt.hconcat(
        # This first chart is the axis title and is only needed because
        # Vega-Lite does not yet support passing an expression directly to the axis title
        alt.Chart().mark_text(angle=270, dx=-150, fontWeight='bold').encode(
            alt.TextValue(alt.expr(f'{metric_param.name}'))
        ),
        alt.Chart(df_plot, width=alt.Step(40)).mark_circle(xOffset=alt.expr('random() * 16 - 8')).encode(
            x='group',
            y=alt.Y('image_area:Q').title(''),
            tooltip=['image:N'],
            color='group',
        ).properties(
            title='Area of blobs'
        ).transform_calculate(
            # This first line updates the image_area which is used for the y axis
            # to correspond to the selected string in the dropdown
            image_area=f'datum[{metric_param.name}]',
            # Since altair needs the tooltip field to be called `image`, we need to dynamically
            # change what's in the `image` field depending on the selection in the dropdown
            # This is further complicated by the fact that the string in the dropdown is not
            # an exact match for the column holding the image data so we need
            # to replace part of the name to match to match the corresponding base 64 image field
            image=f'datum[replace({metric_param.name}, "_area", "_base64")]',
        )
    ).add_params(
        metric_param
    )


.. _base64-encoded: https://en.wikipedia.org/wiki/Binary-to-text_encoding
