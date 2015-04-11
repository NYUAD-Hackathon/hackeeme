#outputs 1 point into the server graph

import plotly.plotly as py
from plotly.graph_objs import *
# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py

# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots
from plotly.graph_objs import *

import numpy as np  # (*) numpy for math functions and arrays


stream_id = 'h4647cu2nm'

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(token=stream_id)
)

data = Data([trace1])
py.plot(data)
s = py.Stream(stream_id)
s.open()
s.write(dict(x=1, y=2))
s.close()
