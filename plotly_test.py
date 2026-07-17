import numpy as np
import plotly.graph_objects as go
import streamlit as st

x = np.linspace(-1.0, 8.0, 300)
mean = np.sin(x)
std = 0.2 + 0.05 * np.abs(x - 3.5)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x,
        y=mean + 1.96 * std,
        mode="lines",
        line={"width": 0},
        hoverinfo="skip",
        showlegend=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=x,
        y=mean - 1.96 * std,
        mode="lines",
        line={"width": 0},
        fill="tonexty",
        name="95% interval",
        hoverinfo="skip",
    )
)

fig.add_trace(
    go.Scatter(
        x=x,
        y=mean,
        mode="lines",
        name="Mean",
    )
)

st.plotly_chart(fig, width="stretch")