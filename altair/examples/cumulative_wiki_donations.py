"""
Cumulative Wikipedia Donations
==============================

This chart shows cumulative donations to Wikipedia over the past 10 years. Inspired by this `Reddit post <https://www.reddit.com/r/dataisbeautiful/comments/7guwd0/cumulative_wikimedia_donations_over_the_past_10/>`_ but using lines instead of areas.
"""
# category: case studies
import altair as alt

source = "https://frdata.wikimedia.org/donationdata-vs-day.csv"

alt.Chart(source).mark_line().encode(
    alt.X('monthdate(date):T', axis=alt.Axis(format='%B', title='Month')),
    alt.Y(
        'max(ytdsum):Q', stack=None,
        axis=alt.Axis(title='Cumulative Donations')
    ),
    alt.Color('year(date):O', legend=alt.Legend(title='Year')),
    alt.Order('year(data):O')
)
