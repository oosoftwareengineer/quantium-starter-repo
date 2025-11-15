from dash import Dash, html, dcc
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

app.layout = html.Div(children=[
    html.H1(children='SoulFood', style={
            'textAlign': 'center',
            'color': "Black"
        }),

    html.Div(children='''
        Total Sales Over Time.
    ''', style={
        'textAlign': 'center',
        'color': "Black"
    }),

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
    }),

    dcc.Graph(
        id='total sales by region data',
        figure=fig_3
    )
])

if __name__ == '__main__':
    app.run(debug=True)
