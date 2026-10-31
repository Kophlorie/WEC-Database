# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#from .utils import webbrowser
import webbrowser

import os
import json


class MainInterface(object):
    """
    UI: description goes here
    """
    def __init__(self, main_creation):
        self.db_obj = main_creation
        self.interface = None

    def make_interface(self):
        app = dash.Dash(__name__)

        self.interface = app

        # Describe the layout, or the UI, of the app
        self.interface.layout = html.Div([
                                    dcc.Location(id='url', refresh=False),
                                    MainInterface.__title(),
                                    html.Div(id='page-content')
                                ])

        @app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            if pathname == '/' or pathname is None:
                return self.__home()
            elif pathname == '/ClassesAndObjects':
                return self.__class_and_object()
            elif pathname == '/ClassesAndObjects/Classes':
                return self.__classes('/ClassesAndObjects')
            elif pathname == '/Organisation':
                return self.__organisation_list('/ClassesAndObjects/Classes')
            else:
                organisation_list = [child for child in self.db_obj.getAllOrganisations().keys()]
                depth = pathname.split('/')[1:]
                if depth[0] in organisation_list:
                    organisation_wecs = self.db_obj.getOrganisationsWECs(depth[0])
                    if len(depth) == 1:
                        return self.__organisation_page(depth[0], organisation_wecs)
                    elif len(depth) == 2:
                        marker = depth[1].index('_')
                        wec = organisation_wecs.get('WECs', {}).get(depth[1][:marker])
                        print(json.dumps(wec, indent=3))
                        if wec is not None:
                            #print(json.dumps(wec, indent=3))
                            if depth[1][marker:] == '_Info':  # WEC Info
                                return self.__wec_info(wec, depth[1][:marker], depth[0])
                            elif depth[1][marker:] == '_Children':  # WEC Children List
                                return self.__wec_children(wec, depth[1][:marker], depth[0])
                    elif len(depth) == 3:
                        wec = organisation_wecs.get('WECs', {}).get(depth[1])
                        if depth[2][-4:] == 'Info':  # WEC Child Info
                                return self.__wec_child_info(wec, depth[1], depth[2][:-5], depth[0])
            return self.__no_page()

        return 1

    @staticmethod
    def __wec_child_info(wec, name, version, parent):
        print(f'{name}{version}')
        print(json.dumps(wec, indent=3))
        wec_info = wec.get(f'{name}{version}')
        content = []
        for key in wec_info:
            content += [html.H2(key)]
            content += [html.Span([html.H4(f'{el}: '), html.P(wec_info[key][el])]) for el in wec_info[key]]
        return html.Div([MainInterface.__fixed_navbar(f'/{parent}')] + content)

    @staticmethod
    def __wec_info(wec, name, parent):
        wec_info = wec.get(f'{name}0')
        content = []
        for key in wec_info:
            content += [html.Span([html.H4(f'{el}: '), html.P(wec_info[key][el])]) for el in wec_info[key]]
        return html.Div([MainInterface.__fixed_navbar(f'/{parent}')] + content)


    @staticmethod
    def __wec_children(wec, name, parent):
        wec_0 = f'{name}0'
        content = []
        for key in wec:
            if key == wec_0:
                pass
            else:
                content += [
                            html.Span([html.H4(f'{key}: '),
                                       html.A('Info', href=f'/{parent}/{name}/{key.replace(name,"")}_Info', className='button')])]

        return html.Div([MainInterface.__fixed_navbar(f'/{parent}')] + content)


    """working form here================================================================================================
    """

    @staticmethod
    def __organisation_page(organisation, children):
        div_children = [MainInterface.__fixed_navbar('/Organisation'),
                        html.H1(organisation),
                        html.P(children['organisationInfo']['comments']),
                        html.H2(f'List of WECs developed by {organisation}')]

        div_children += [MainInterface.__make_wec(organisation, wec) for wec in children['WECs']]

        return html.Div(
            id='organisations_page',
            children=div_children)

    @staticmethod
    def __make_wec(organisation, wec):
        return html.Div([
                            html.H2(wec),
                            html.A('Info', href=f'{organisation}/{wec}_Info', className='button'),
                            html.A('Children', href=f'{organisation}/{wec}_Children', className='button')
                        ])

    def run_interface(self):
        webbrowser.open('http://127.0.0.1:8050')  # Go to example.com
        # originally self.interface.run_server(debug=True)
        self.interface.run_server(debug=False, host='127.0.0.1', port=8050)

        return 1

    def __organisation_list(self, return_url):
        db_str = self.db_obj.getAllOrganisations()
        return html.Div(
            id='organisations_list',
            children=[
                         MainInterface.__fixed_navbar(return_url),
                         html.H2('List of the Organisations stored in the Data Base'),
                         ] + [
                         html.A(f'{child}...', href=f'/{child}', className='button') for child in
                         db_str.keys()
                     ])

    @staticmethod
    def __classes(return_url):
        """ This page is displayed @/ClassesAndObjects/Classes
        """
        return html.Div(
            id='classes',
            children=[
                MainInterface.__fixed_navbar(return_url),
                html.H2('Classes page'),

                html.A('Find a WEC (child) class from the Company', href='/Organisation', className='button'),
                html.A('All Classes', href='', className='button'),
                html.A('All WEC Classes', href='', className='button'),
                html.A('All WEC Child Classes', href='/', className='button'),
                html.A('Fixed Classes', href='/', className='button'),
            ])

    @staticmethod
    def __class_and_object():
        """ This page is displayed @/ClassesAndObjects
        """
        return html.Div(
            id='class_and_object',
            children=[
                MainInterface.__fixed_navbar(),
                html.H2('Class and Object page'),
                html.A('Classes Info', href='/ClassesAndObjects/Classes', className='button'),
                html.A('Objects Info', href='/ClassesAndObjects/Objects', className='button'),
            ])

    @staticmethod
    def __home():
        """ This page is displayed @/
        """
        return html.Div(
            id='home',
            children=[
                html.H2('Home page'),
                html.P('--> add a description here'),
                html.A('Classes and Objects Info', href='/ClassesAndObjects', className='button'),
                html.A('Post Processing', href='', className='button'),
            ])

    @staticmethod
    def __fixed_navbar(return_url=None):
        """ This page is displayed every time the URL is not found
        """
        if return_url is not None:
            return html.Div([
                            html.A('Back to Home', href='/', className='button'),
                            html.A('<', href=f'{return_url}', className='button')]
                            )

        return html.Div([html.A('Back to Home', href='/', className='button')])

    @staticmethod
    def __no_page():
        """ This page is displayed every time the URL is not found
        """
        return html.Div([html.P(["404 Page not found"])], className="no-page")

    @staticmethod
    def __title():
        """ This the title page
        """
        return html.Div(children='Wave Energy Converter Catalogue', className='title')

