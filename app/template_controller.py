import dash_html_components as html

from dash.dependencies import Input, Output, State

from app import app
from app.utils import Utils
from app.logic.tax_calculator import TaxCalculator

tax_calculator = TaxCalculator()


@app.callback(
    Output('annual-salary', 'children'),
    [Input('monthly-salary', 'n_submit'), Input('monthly-salary', 'n_blur')],
    [State('monthly-salary', 'value')]
)
def get_annual_salary(n_submit, n_blur, value):
    annual_salary = Utils.get_annual_income(value)
    return html.Div(className="row mt-1",
                    children=[
                        html.Div(className="col-sm-3 mr-1",
                                 children=["Annual salary: "]),
                        html.Div(className="col-sm-3",
                                 children=["S$ {0:.2f}".format(annual_salary)])
                    ])


@app.callback(
    Output('taxable-salary', 'children'),
    [Input('monthly-salary', 'n_submit'), Input('monthly-salary', 'n_blur'),
     Input('annual-bonus', 'n_submit'), Input('annual-bonus', 'n_blur'),
     Input('tax-rebates', 'n_submit'), Input('tax-rebates', 'n_blur'),
     Input('donation', 'value')],
    [State('monthly-salary', 'value'),
     State('annual-bonus', 'value'),
     State('tax-rebates', 'value')]
)
def get_taxable_salary(ns1, nb1, ns2, nb2, ns3, nb3, donation, monthly_salary, annual_bonus, tax_rebates):
    annual_salary = Utils.get_annual_income(monthly_salary)
    taxable_salary = Utils.get_taxable_income(annual_salary, annual_bonus, tax_rebates, donation)
    return html.Div(className="row mt-1",
                    children=[
                        html.Div(className="col-sm-3 mr-1",
                                 children=["Taxable salary: "]),
                        html.Div(className="col-sm-3",
                                 children=["S$ {0:.2f}".format(taxable_salary)])
                    ])


@app.callback(
    Output('donation', 'max'),
    [Input('monthly-salary', 'n_submit'), Input('monthly-salary', 'n_blur'),
     Input('annual-bonus', 'n_submit'), Input('annual-bonus', 'n_blur')],
    [State('monthly-salary', 'value'),
     State('annual-bonus', 'value')]
)
def get_maximum_donation(ns1, nb1, ns2, nb2, monthly_salary, annual_bonus):
    annual_salary = Utils.get_annual_income(monthly_salary)
    return annual_salary + annual_bonus


@app.callback(
    Output('donation', 'marks'),
    [Input('monthly-salary', 'n_submit'), Input('monthly-salary', 'n_blur'),
     Input('annual-bonus', 'n_submit'), Input('annual-bonus', 'n_blur')],
    [State('monthly-salary', 'value'),
     State('annual-bonus', 'value')]
)
def get_maximum_donation_mark(ns1, nb1, ns2, nb2, monthly_salary, annual_bonus):
    annual_salary = Utils.get_annual_income(monthly_salary)
    max_donation = annual_salary + annual_bonus
    return {
        0: 'S$ 0',
        max_donation: "{0:.2f}".format(max_donation)
    }


@app.callback(
    Output('current-donation', 'value'),
    [Input('donation', 'value')]
)
def get_maximum_donation_label(donation):
    return donation

@app.callback(
    Output('donation', 'value'),
    [Input('current-donation', 'n_submit'), Input('current-donation', 'n_blur')],
    [State('current-donation', 'value')]
)
def get_maximum_donation_label(ns, nb, donation):
    return donation


@app.callback(
    Output('tax-info', 'children'),
    [Input('monthly-salary', 'n_submit'), Input('monthly-salary', 'n_blur'),
     Input('annual-bonus', 'n_submit'), Input('annual-bonus', 'n_blur'),
     Input('tax-rebates', 'n_submit'), Input('tax-rebates', 'n_blur'),
     Input('donation', 'value')],
    [State('monthly-salary', 'value'),
     State('annual-bonus', 'value'),
     State('tax-rebates', 'value')]
)
def get_taxable_salary(ns1, nb1, ns2, nb2, ns3, nb3, donation, monthly_salary, annual_bonus, tax_rebates):
    tax_info = tax_calculator.calculate_tax(monthly_salary, annual_bonus, tax_rebates, donation)
    print(tax_info)
    return [
        html.Div(className="row mt-1",
                 children=[
                     html.Div(className="col-sm-3 mr-1",
                              children=["Total Annual Tax: "]),
                     html.Div(className="col-sm-3",
                              children=["S$ {0:.2f}".format(tax_info.total_tax)])
                 ]),
        html.Div(className="row mt-1",
                 children=[
                     html.Div(className="col-sm-3 mr-1",
                              children=["Total Monthly Tax: "]),
                     html.Div(className="col-sm-3",
                              children=["S$ {0:.2f}".format(tax_info.total_tax / 12)])
                 ]),
        html.Div(className="row mt-1",
                 children=[
                     html.Div(className="col-sm-3 mr-1",
                              children=["Tax Tier: "]),
                     html.Div(className="col-sm-3",
                              children=["{}".format(tax_info.tier_level)])
                 ]),
        html.Div(className="row mt-1",
                 children=[
                     html.Div(className="col-sm-3 mr-1",
                              children=["Tax Rate: "]),
                     html.Div(className="col-sm-3",
                              children=["{0:.2f}%".format(tax_info.tier_info['tax_rate'])])
                 ]),
        html.Div(className="row mt-1",
                 children=[
                     html.Div(className="col-sm-3 mr-1",
                              children=["Tier Upper Limit: "]),
                     html.Div(className="col-sm-3",
                              children=["S$ {}".format(tax_info.tier_info['upper_limit'])])
                 ]),
        html.Div(className="row mt-1",
                 children=[
                     html.Div(className="col-sm-3 mr-1",
                              children=["Tier Lower Limit: "]),
                     html.Div(className="col-sm-3",
                              children=["S$ {}".format(tax_info.tier_info['lower_limit'])])
                 ]),
    
    ]
