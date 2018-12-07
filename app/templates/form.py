import dash_html_components as html
import dash_core_components as dcc

monthly_salary = html.Div(className="row mt-1",
                          children=[
                              html.Div(className="col-sm-4 mr-1",
                                       children=["Monthly Salary (S$)"]),
                              dcc.Input(id="monthly-salary",
                                        className="col-sm-2",
                                        type="number",
                                        value=0,
                                        min=0,
                                        pattern="[0-9]+")

                          ])

bonus = html.Div(className="row mt-1",
                 children=[
                     html.Div(className="col-sm-4 mr-1",
                              children=["Annual Bonus (S$)"]),
                     dcc.Input(id="annual-bonus",
                               className="col-sm-2",
                               type="number",
                               value=0,
                               min=0,
                               pattern="[0-9]+")

                 ])

rebates = html.Div(className="row mt-1",
                   children=[
                       html.Div(className="col-sm-4 mr-1",
                                children=["Total Tax Rebates (S$)"]),
                       dcc.Input(id="tax-rebates",
                                 className="col-sm-2",
                                 type="number",
                                 value=0,
                                 min=0,
                                 pattern="[0-9]+")

                   ])

donation = html.Div(className="mt-1",
                    children=[
                        html.Div(className="row",
                                 children=[
                                     html.Div(className="col-sm-4 mr-1",
                                              children=["Donation: "]),
                                     dcc.Input(className="col-sm-2",
                                               type='number',
                                               min=0,
                                               value=0,
                                               id="current-donation"),
                                 ]),
                        html.Div(className="col-sm-6 ml-1 mt-2",
                                 children=[dcc.Slider(
                                     id='donation',
                                     min=0,
                                     step=10,
                                     value=0,
                                     updatemode='drag'
                                 )])

                    ])

form = html.Div(className="col-sm-6 text-center mt-3",
                children=[
                    monthly_salary,
                    bonus,
                    rebates,
                    donation
                ])
