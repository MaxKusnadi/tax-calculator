import dash_html_components as html

annual_salary = html.Div(id="annual-salary")
taxable_salary = html.Div(id="taxable-salary")
tax_info = html.Div(id="tax-info")

result = html.Div(className="col-sm-6 text-center mt-3",
                  children=[
                      annual_salary,
                      taxable_salary,
                      tax_info
                  ])
