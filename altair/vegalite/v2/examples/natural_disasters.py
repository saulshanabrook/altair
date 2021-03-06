"""
Natural Disasters
-----------------
This example shows a visualization of global deaths from natural disasters.
"""

import altair as alt
from altair.expr import datum
from vega_datasets import data

source = data.disasters.url

alt.Chart(source).mark_circle(
    opacity=0.8,
    stroke='black',
    strokeWidth=1
).encode(
    alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
    alt.Y('Entity:N'),
    alt.Size('Deaths:Q',
        scale=alt.Scale(range=[0, 5000]),
        legend=alt.Legend(title='Annual Global Deaths')
    ),
    alt.Color('Entity:N', legend=None)
).properties(
    width=480,
    height=350
).transform_filter(
    datum.Entity != 'All natural disasters'
)
