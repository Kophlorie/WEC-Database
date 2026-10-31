# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from .utils.organization import database_scan
# 2026 AI-assisted extension: redirect the legacy catalogue reader to generated source.
# The original database_scan import and every historical line are retained above/below.
from .utils.dynamic_catalogue import load_catalogue, generated_paths
database_scan = generated_paths  # The legacy '../Database/' argument is ignored.
from urllib.parse import quote, unquote
import dash_table as dt
import numpy as np
import pandas as pd
import json
import os
import base64

from pathlib import Path


# Original external jQuery dependency disabled in 2026.
# The current interface does not require this script.
external_scripts = [
    # 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js',
]

app = dash.Dash(__name__,
                external_scripts=external_scripts)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


paths = database_scan('../Database/')
print(json.dumps(paths, indent=2))

for chl in paths['children']:
    print(chl['name'])

def title():
    return html.Div(children='Wave Energy Converter Catalogue', className='title')


def company(company_name, id):

    description = '404: file not found'
    for ii in range(len(paths['children'][id]['children'])):
        if paths['children'][id]['children'][ii]['type'] == 'file':

            description = os.path.join(os.path.dirname(os.getcwd()), 'Database', company_name, paths['children'][id]['children'][ii]['name'])
            try:
                with open(description, 'r') as fid:
                    description = ''.join(fid.readlines())
                    print(description)
            except:
                print(f'404: cannot open the file \n{description}')



    return html.Div(
            id='company',
            children=[
                html.H1(company_name),
                html.Iframe(srcDoc=description),
                html.A('Back to Home', href='/', className='button'),
                html.A('Previous Page', href='/companies', className='button'),
            ])


# 2026 AI-assisted extension: these pages are built solely from DynamicFunctions/*.py.
# Francesco's original company(), navigation tabs and comments above/below are retained.
def generated_info(value):
    # Original version
    #return html.Pre(json.dumps(value, indent=2, ensure_ascii=False),
    #                style={'whiteSpace': 'pre-wrap', 'overflowWrap': 'anywhere'})
     # 2026 AI-assisted display formatting.
    # Information comes exclusively from DynamicFunctions.

    def format_value(item):
        if isinstance(item, dict):
            return html.Div([
                html.Div([
                    html.Strong(str(key).replace('_', ' ') + ': '),
                    format_value(entry)
                ], style={'marginBottom': '8px'})
                for key, entry in item.items()
            ])

        if isinstance(item, (list, tuple)):
            if not item:
                return html.Span('—')

            return html.Div([
                html.Div(format_value(entry))
                for entry in item
            ], style={'marginLeft': '14px'})

        return html.Span(str(item).strip() or '—')

    return html.Div(format_value(value), style={
        'backgroundColor': '#FFFFFF',
        'border': '1px solid #CCCCCC',
        'padding': '14px',
        'margin': '10px 0 18px',
        'maxWidth': '900px',
        'boxSizing': 'border-box',
        'whiteSpace': 'pre-wrap',
        'overflowWrap': 'break-word'
    })


def generated_link(label, path):
    return html.A(label, href=path, className='button',
    style={'display': 'inline-block', 'margin': '5px 8px 5px 0'}) # Added line to the original version


def generated_page(pathname):
    """Handle generated company / WEC / child routes, or defer to legacy routing."""
    if not pathname:
        return None
    data = load_catalogue()  # Re-read local generated files on every page request.
    organisations = data['organisations']

    if pathname.endswith('_info') and pathname.startswith('/'):
        name = unquote(pathname[1:-5])
        org = organisations.get(name)
        if org is not None:
            wec_links = [generated_link(name_wec, '/wec/' + quote(name, safe='')
                                        + '/' + quote(name_wec, safe=''))
                         for name_wec in org['wecs']]
            return html.Div(id='company', children=[
                html.H1(name), generated_info(org['information']),
                html.H2('WECs associated with this organisation'),
                html.Div(wec_links) if wec_links else html.P('No generated WEC classes.'),
                generated_link('Back to Home', '/'),
                generated_link('Previous Page', '/companies')])

    if pathname.startswith('/wec/'):
        parts = [unquote(part) for part in pathname[len('/wec/'):].split('/')]
        if len(parts) not in (2, 3):
            return noPage
        org_name, mother = parts[:2]
        org = organisations.get(org_name)
        if not org or mother not in org['wecs']:
            return noPage
        info = org['wecs'][mother]
        mother_path = '/wec/' + quote(org_name, safe='') + '/' + quote(mother, safe='')
        if len(parts) == 2:
            links = [generated_link(child_name, mother_path + '/' + quote(child_name, safe=''))
                     for child_name in info['children']]
            return html.Div(id='wec', children=[
                html.H1(mother), generated_info(info['details']),
                html.H2('Associated WEC child classes'),
                html.Div(links) if links else html.P('No generated child classes.'),
                generated_link('Back to ' + org_name, '/' + quote(org_name, safe='') + '_info'),
                generated_link('Back to Home', '/')])
        child_name = parts[2]
        child_info = info['children'].get(child_name)
        if child_info is None:
            return noPage
        objects = [(obj_name, obj) for obj_name, obj in data['objects'].items()
                   if obj['class'] == child_name]
        object_cards = [html.Div([html.H3(obj_name), generated_info(obj['attributes'])])
                        for obj_name, obj in objects]
        return html.Div(id='wec_child', children=[
            html.H1(child_name), generated_info(child_info),
            html.H2('Generated WEC objects'),
            html.Div(object_cards) if object_cards else html.P('No objects found in MainCreation.'),
            generated_link('Previous Page', mother_path),
            generated_link('Back to Home', '/')])
    return None

def company_list():
    return html.Div(
        id='class_and_object',
        children=[
            html.H2('Class and Object page'),
            html.A('Back to Home', href='/', className='button')] + [
                html.A(f'{child["name"]} Info', href=f'/{child["name"]}_info', className='button') for child in paths['children']
            ])

def class_list():
    return html.Div(
        id='class_and_object',
        children=[
            html.H2('Class and Object page'),
            html.A('Back to Home', href='/', className='button'),
            html.A('Company Info', href='/companies', className='button'),
            html.A('Objects Info', href='', className='button'),
        ])


def class_and_object():
    return html.Div(
        id='class_and_object',
        children=[
            html.H2('Class and Object page'),
            html.A('Back to Home', href='/', className='button'),
            html.A('Classes Info', href='/companies', className='button'),
            html.A('Objects Info', href='', className='button'),
        ])


def home():
    return html.Div(
        id='home',
        children=[
            html.H2('Home page'),
            html.A('Path and Info', href='/path-and-info', className='button'),
            html.A('X', href='', className='button'),
        ])


noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")


# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    title(),
    html.Div(id='page-content')
])


@app.callback(
              Output('page-content', 'children'),
              [Input('url', 'pathname')]
              )
def display_page(pathname):
    # 2026 addition: reflect the current generated source, not a startup snapshot.
    global paths
    paths = database_scan('../Database/')
    if pathname == '/':
        return home()
    elif pathname == '/path-and-info':
        return class_and_object()
    elif pathname == '/classes':
        return class_list()
    elif pathname == '/companies':
        return company_list()
    else:
        # 2026 addition: generated pages, while keeping Francesco's original fall-through.
        page = generated_page(pathname)
        if page is not None:
            return page
        if pathname and pathname.endswith('_info'):
            return noPage  # No fallback to the old Database/ file reader.
        for id_child, child in enumerate(paths['children']):
            if pathname == f'/{child["name"]}_info':
                return company(child["name"], id_child)
        return noPage


if __name__ == '__main__':
    # Originally: app.run_server(debug=True)
    app.run_server(debug=False, host='127.0.0.1', port=8050)