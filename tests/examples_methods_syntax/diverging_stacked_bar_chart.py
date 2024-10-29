"""
Diverging Stacked Bar Chart
---------------------------
This example shows a diverging stacked bar chart for sentiments towards a set of eight questions, displayed as percentages with neutral responses straddling the 0% mark.
"""
# category: bar charts
import altair as alt
import pandas as pd


source = pd.DataFrame(
    [
        {
            "question": "Question 1",
            "type": "Strongly disagree",
            "value": 24,
        },
        {
            "question": "Question 1",
            "type": "Disagree",
            "value": 294,
        },
        {
            "question": "Question 1",
            "type": "Neither agree nor disagree",
            "value": 594,
        },
        {
            "question": "Question 1",
            "type": "Agree",
            "value": 1927,
        },
        {
            "question": "Question 1",
            "type": "Strongly agree",
            "value": 376,
        },
        {
            "question": "Question 2",
            "type": "Strongly disagree",
            "value": 2,
        },
        {
            "question": "Question 2",
            "type": "Disagree",
            "value": 2,
        },
        {
            "question": "Question 2",
            "type": "Neither agree nor disagree",
            "value": 0,
        },
        {
            "question": "Question 2",
            "type": "Agree",
            "value": 7,
        },
        {
            "question": "Question 2",
            "type": "Strongly agree",
            "value": 11,
        },
        {
            "question": "Question 3",
            "type": "Strongly disagree",
            "value": 2,
        },
        {
            "question": "Question 3",
            "type": "Disagree",
            "value": 0,
        },
        {
            "question": "Question 3",
            "type": "Neither agree nor disagree",
            "value": 2,
        },
        {
            "question": "Question 3",
            "type": "Agree",
            "value": 4,
        },
        {
            "question": "Question 3",
            "type": "Strongly agree",
            "value": 2,
        },
        {
            "question": "Question 4",
            "type": "Strongly disagree",
            "value": 0,
        },
        {
            "question": "Question 4",
            "type": "Disagree",
            "value": 2,
        },
        {
            "question": "Question 4",
            "type": "Neither agree nor disagree",
            "value": 1,
        },
        {
            "question": "Question 4",
            "type": "Agree",
            "value": 7,
        },
        {
            "question": "Question 4",
            "type": "Strongly agree",
            "value": 6,
        },
        {
            "question": "Question 5",
            "type": "Strongly disagree",
            "value": 0,
        },
        {
            "question": "Question 5",
            "type": "Disagree",
            "value": 1,
        },
        {
            "question": "Question 5",
            "type": "Neither agree nor disagree",
            "value": 3,
        },
        {
            "question": "Question 5",
            "type": "Agree",
            "value": 16,
        },
        {
            "question": "Question 5",
            "type": "Strongly agree",
            "value": 4,
        },
        {
            "question": "Question 6",
            "type": "Strongly disagree",
            "value": 1,
        },
        {
            "question": "Question 6",
            "type": "Disagree",
            "value": 1,
        },
        {
            "question": "Question 6",
            "type": "Neither agree nor disagree",
            "value": 2,
        },
        {
            "question": "Question 6",
            "type": "Agree",
            "value": 9,
        },
        {
            "question": "Question 6",
            "type": "Strongly agree",
            "value": 3,
        },
        {
            "question": "Question 7",
            "type": "Strongly disagree",
            "value": 0,
        },
        {
            "question": "Question 7",
            "type": "Disagree",
            "value": 0,
        },
        {
            "question": "Question 7",
            "type": "Neither agree nor disagree",
            "value": 1,
        },
        {
            "question": "Question 7",
            "type": "Agree",
            "value": 4,
        },
        {
            "question": "Question 7",
            "type": "Strongly agree",
            "value": 0,
        },
        {
            "question": "Question 8",
            "type": "Strongly disagree",
            "value": 0,
        },
        {
            "question": "Question 8",
            "type": "Disagree",
            "value": 0,
        },
        {
            "question": "Question 8",
            "type": "Neither agree nor disagree",
            "value": 0,
        },
        {
            "question": "Question 8",
            "type": "Agree",
            "value": 0,
        },
        {
            "question": "Question 8",
            "type": "Strongly agree",
            "value": 2,
        },
    ]
)


# Add type_code that we can sort by
source["type_code"] = source["type"].map(
    {
        "Strongly disagree": -2,
        "Disagree": -1,
        "Neither agree nor disagree": 0,
        "Agree": 1,
        "Strongly agree": 2,
    }
)


def compute_percentages(
    group,
):
    # Set type_code as index and sort
    group = group.set_index("type_code").sort_index()

    # Compute percentage of value with question group
    perc = (group["value"] / group["value"].sum()) * 100
    group["percentage"] = perc

    # Compute percentage end, centered on "Neither agree nor disagree" (type_code 0)
    # Note that we access the perc series via index which is based on 'type_code'.
    group["percentage_end"] = perc.cumsum() - (perc[-2] + perc[-1] + perc[0] / 2)

    # Compute percentage start by subtracting percent
    group["percentage_start"] = group["percentage_end"] - perc

    return group


source = source.groupby("question").apply(compute_percentages).reset_index(drop=True)


color_scale = alt.Scale(
    domain=[
        "Strongly disagree",
        "Disagree",
        "Neither agree nor disagree",
        "Agree",
        "Strongly agree",
    ],
    range=["#c30d24", "#f3a583", "#cccccc", "#94c6da", "#1770ab"],
)

y_axis = alt.Axis(title="Question", offset=5, ticks=False, minExtent=60, domain=False)

alt.Chart(source).mark_bar().encode(
    x="percentage_start:Q",
    x2="percentage_end:Q",
    y=alt.Y("question:N").axis(y_axis),
    color=alt.Color("type:N").title("Response").scale(color_scale),
)
