# import dash
# import dash_table
# import dash_html_components as html
# import dash_core_components as dcc
# import pandas as pd
# import numpy as np
#
#
# def create_dashboard(server):
#     """Create a Dash app."""
#     external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#     dash_app = dash.Dash(server=server,
#                          routes_pathname_prefix='/dashapp/',
#                          external_stylesheets=external_stylesheets
#                          )
#
#
#     df = pd.read_csv()
#
#     dash_app.layout = html.Div(children=[
#     html.H4(children='US Agriculture Exports (2011)'),
#     create_data_table(df)
#     ])
#     return dash_app.server
#
#
# def create_data_table(df):
#     table = dash_table.DataTable(
#         id='database-table',
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict('records'),
#         sort_action="native",
#         sort_mode='native',
#         page_size=300
#     )
#     return table