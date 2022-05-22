from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'plotly_dark'

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    
    CommonPairings = pd.read_csv('CommonPairings.csv')
    pairings = px.bar(CommonPairings, x = 'Messages', y = 'Pair', orientation = 'h', width=1600, height=400)
    
    graphJSON = json.dumps(pairings, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(pairings, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON = graphJSON, graphJSON1 = graphJSON1)