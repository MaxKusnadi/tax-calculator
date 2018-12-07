import dash_html_components as html

title = html.Div(id="title",
                 className="text-center col-sm-12 bg-primary pt-3 pb-3",
                 children=[
                     html.H1(className="text-white font-weight-bold",
                             children=["Easy Tax Calculator"])
                 ])
