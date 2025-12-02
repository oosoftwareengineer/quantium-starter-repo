from dash import Dash, html, dcc, ctx
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("data/sales_data.csv")

# The logic below handles data for "Total Sales Over Time"
df["date"] = pd.to_datetime(df["date"])
sales_by_year_df = df[["sales", "date"]].groupby(df['date'].dt.year)['sales'].sum().reset_index(name='total_sales')
sales_by_year_df.rename(columns={'date': 'year'}, inplace=True)
fig = px.line(sales_by_year_df, x="year", y="total_sales")

# The logic below handles data for "Total Sales By Region"
sales_by_region_df = df[["region", "sales"]].groupby("region")["sales"].count().reset_index(name='sales')
fig_2 = px.histogram(sales_by_region_df, x="sales", y="region")

# The logic below handles data for "Sales Over Time"
fig_3 = px.scatter(df, x="date", y="sales")

# fig_2 and fig_3 are not necessary. I am just satisfying my curiousity.

app.layout = html.Div(
    style={'fontFamily': 'Arial', 'backgroundColor': '#58dbcb', 'padding': '20px'}, 
    children=[

        html.Div(children=[
            html.H1(children='SoulFood', style={
                    'textAlign': 'center',
                    'color': "Black"
                }
        ),

        html.Div(children='''
            Total Sales Over Time.
        ''', style={
            'textAlign': 'center',
            'color': "Black"
            }
        ),

        html.Div([html.Label('Select Region:'),
            dcc.RadioItems(id='region-selector' , options=[
                {'label': 'North', 'value': 'north'}, 
                {'label': 'South', 'value': 'south'}, 
                {'label': 'East', 'value': 'east'}, 
                {'label': 'West', 'value': 'west'}, 
                {'label': 'All', 'value': 'all'}
            ], 
            value='all',  #id='my-input'
            labelStyle={'display': 'inline-block', 'margin-right': '15px'}
            )
        ], style={'padding': 10, 'flex': 1}),

        dcc.Graph(
            id='sales by date data',
            figure=fig
        ),
        html.Div(children='''
            Pink Morsel Total Sales by Region.
        ''', style={
            'textAlign': 'center',
            'color': "Black"
        }),

        dcc.Graph(
            id='sales by region data',
            figure=fig_2
        ),
        html.Div(children='''
            Pink Morsel Sales Over Time.
        ''', style={
            'textAlign': 'center',
            'color': "Black"
            }
        ),

        dcc.Graph(
            id='total sales by region data',
            figure=fig_3
        )
        ])
    ])

@app.callback(
    Output('sales by date data', 'figure'),
    Input('region-selector', 'value')
)

def update_line_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    sales_by_year_df = (
        filtered_df[["sales", "date"]]
        .groupby(filtered_df['date'].dt.year)['sales']
        .sum()
        .reset_index(name='total_sales')
    )
    sales_by_year_df.rename(columns={'date': 'year'}, inplace=True)

    fig = px.line(sales_by_year_df, x="year", y="total_sales", title=f"Total Sales Over Time ({selected_region.title()})")
    return fig


if __name__ == '__main__':
    app.run(debug=True)
