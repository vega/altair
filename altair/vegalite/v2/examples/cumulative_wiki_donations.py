"""
Cumulative Wikipedia Donations
==============================

This chart shows cumulative donations to Wikipedia over the past 10 years. This chart was inspired by https://www.reddit.com/r/dataisbeautiful/comments/7guwd0/cumulative_wikimedia_donations_over_the_past_10/ but using lines instead of areas.
Data comes from https://frdata.wikimedia.org/.
"""

import altair as alt

data = "https://frdata.wikimedia.org/donationdata-vs-day.csv"

chart = alt.Chart(data).mark_line().encode(
    alt.X(
        'date:T', timeUnit='monthdate',
        axis=alt.Axis(format='%B', title='Month')
    ),
    alt.Y(
        'max(ytdsum):Q', stack=None,
        axis=alt.Axis(title='Cumulative Donations')
    ),
    alt.Color('date:O', timeUnit='year', legend=alt.Legend(title='Year')),
    alt.Order('data:O', timeUnit='year')
)
