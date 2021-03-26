import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import pickle

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)

df = pd.read_pickle("df_all_rules.pkl")

df_all_rules_group = df.groupby(['SITE_NUMBER', 'year', 'month']).mean().reset_index()

df_all_rules_group_pivot = df_all_rules_group.pivot(index = 'year', columns = 'month', values = 'TMR_SUB_18')

#df.reset_index(inplace=True)
#print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Temperatue Data Probe Dashboard", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2003", "value": 2003},
                     {"label": "2004", "value": 2004},
                     {"label": "2005", "value": 2005},
                     {"label": "2007", "value": 2006},
                     {"label": "2008", "value": 2008},
                     {"label": "2009", "value": 2009},
                     {"label": "2010", "value": 2010},
                     {"label": "2011", "value": 2011},
                     {"label": "2012", "value": 2012},
                     {"label": "2013", "value": 2013},
                     {"label": "2014", "value": 2014},
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='tdp_graph', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='tdp_graph', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df_all_rules_group_pivot.copy()
    dff = dff[dff["year"] == option_slctd]

   # dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express

dfpx = df_all_rules_group_pivot

fig = px.density_heatmap(dfpx, x="year", y="month", nbinsx=15, nbinsy=12, color_continuous_scale="Viridis")
fig.show()



    #fig = px.choropleth(
    #    data_frame=dff,
    #   locationmode='USA-states',
    #    locations='state_code',
    #    scope="usa",
    #    color='Pct of Colonies Impacted',
    #    hover_data=['State', 'Pct of Colonies Impacted'],
    #    color_continuous_scale=px.colors.sequential.YlOrRd,
    #    labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
    #    template='plotly_dark'
    # )

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

    
# https://youtu.be/hSPmj7mK6ng 