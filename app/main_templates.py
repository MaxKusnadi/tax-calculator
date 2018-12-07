import dash_html_components as html

from app import app
from app.templates.title import title
from app.templates.form import form
from app.templates.result import result

app.layout = html.Div([
    title,
    html.Div(id="main",
             className="row",
             children=[
                 form,
                 result
             ]),
])
