# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc

import logging
import os
import datetime

database_address = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'Database')


def create_folder(test, version, device, company):
    company_dir = os.path.join(database_address, company)
    if not os.path.exists(company_dir):
        os.makedirs(company_dir)
        description_file_template = os.path.join(company_dir, f'{company}_description.txt')
        with open(description_file_template, 'w') as fid:
            fid.write('OrganizationObject\n')
            fid.write('===========\n')
            fid.write('add a company description\n')
            fid.write('===========\n')
            today = datetime.date.today()
            fid.write(f'ID: {company}{today:%Y%m%d%H%M%S}\n')


    device_dir = os.path.join(company_dir, device)
    if not os.path.exists(device_dir):
        os.makedirs(device_dir)
        description_file_template = os.path.join(device_dir, f'{device}_description.txt')
        with open(description_file_template, 'w') as fid:
            fid.write('WEC\n')
            fid.write('===========\n')
            fid.write('add a mother class description\n')
            fid.write('===========\n')
            fid.write('p1: arm_length  (m) (add more if need, one parameter per line with increasing number)\n')


    version_dir = os.path.join(device_dir, f'{device}_{version}')
    if not os.path.exists(version_dir):
        os.makedirs(version_dir)

    tests_list = os.listdir(version_dir)
    test_dir = os.path.join(version_dir, test)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)




def menu():

    return html.Div(
        html.Div(
            [
                html.Div(
                    [
                        # modal header
                        html.Div(
                            [
                                html.Span(
                                    "Create new DB entries",
                                    style={
                                        "color": "#506784",
                                        "fontWeight": "bold",
                                        "fontSize": "20",
                                    },
                                ),
                            ],
                            className="row",
                            style={"borderBottom": "1px solid #C8D4E3"},
                        ),

                        # modal form
                        html.Div(
                            [

                                # left Div
                                html.Div(
                                    [
                                        html.P(
                                            "Organization Name",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="organization-name",
                                            placeholder="Name of the company that develop the machine",
                                            type="text",
                                            value='',
                                            style={"width": "100%"},
                                        ),
                                        html.P(
                                            "",
                                            id="organization-name-out",
                                            style={
                                                "textAlign": "left",
                                                "text-color":"red",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),

                                        html.P(
                                            "device name",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="device-name",
                                            placeholder="Name of the device",
                                            type="text",
                                            value='',
                                            style={"width": "100%"},
                                        ),
                                        html.P(
                                            "",
                                            id="device-name-out",
                                            style={
                                                "textAlign": "left",
                                                "text-color":"red",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                    ],
                                    className="six columns",
                                    style={"paddingRight": "15"},
                                ),


                                # right Div
                                html.Div(
                                    [
                                        html.P(
                                            "device version",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="device-version",
                                            placeholder="ID or str identificative of the current version of the device",
                                            type="text",
                                            value='',
                                            style={"width": "100%"},
                                        ),
                                        html.P(
                                            "",
                                            id="device-version-out",
                                            style={
                                                "textAlign": "left",
                                                "text-color": "red",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),

                                        html.P(
                                            "Test Type",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id='test-type',
                                            options=[
                                                {'label': 'Dry Test', 'value': 'DT'},
                                                {'label': 'Wave Basin Test', 'value': 'WBT'},
                                                {'label': 'Open Water Test', 'value': 'OWT'}
                                            ],
                                            placeholder="Select a test type",
                                        ),
                                        html.P(
                                            "",
                                            id="test-type-out",
                                            style={
                                                "textAlign": "left",
                                                "text-color": "red",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),

                                    ],
                                    className="six columns",
                                    style={"paddingLeft": "15"},
                                ),
                            ],
                            style={"marginTop": "10", "textAlign": "center"},
                            className="row",
                        ),

                        # submit button
                        html.Span(
                            "Start",
                            id="submit_new_case",
                            n_clicks=0,
                            className="button button--primary add",
                            style={"margin-top":"10px"},
                        ),
                        html.P(
                            "",
                            id="submit_new_case-out",
                            style={
                                "textAlign": "left",
                                "text-color": "red",
                                "marginBottom": "2",
                                "marginTop": "4",
                            },
                        ),

                    ],
                    className="modal-content",
                    style={"textAlign": "center", "border": "1px solid #C8D4E3"},
                )
            ],
            className="modal",
        ),
        id="cases_modal",
        style={"display": "block"},
    )

def main():
    # Disable Flask's get/post console logs
    log = logging.getLogger('werkzeug')
    #log.disabled = True

    app = dash.Dash()
    app.config['suppress_callback_exceptions']=True
    app.scripts.config.serve_locally = True

    app.layout = html.Div(children=[
        menu(),
    ])

    ###########################
    ###### MODAL CONTROL ######
    ###########################

    @app.callback(
        [Output('submit_new_case-out', 'children'),
         Output('test-type-out', 'children'),
         Output('device-version-out', 'children'),
         Output('device-name-out', 'children'),
         Output('organization-name-out', 'children')],
        [Input('submit_new_case', 'n_clicks')],
        [State('test-type','value'),
         State('device-version','value'),
         State('device-name','value'),
         State('organization-name','value')]
    )
    def submit_newcase(nc,tt,dv,dn,on):
        out1 = ''
        out2 = ''
        out3 = ''
        out4 = ''
        out5 = ''
        flg = 0

        if nc > 0:
            out1 = 'some field are missing'
            if tt == '':
                out2 = 'missing test type'
                flg=1
            if dv == '':
                out3 = 'missing device version'
                flg = 1
            if dn == '':
                out4 = 'missing device name'
                flg = 1
            if on == '':
                out5 = 'missing company name'
                flg = 1

            if flg == 0:
                try:
                    out1 = 'folder created'
                    create_folder(tt, dv, dn, on)
                except:
                    out1 = 'something went wrong in the creation of the folders'

        return out1, out2, out3, out4, out5


    external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                    "https://fonts.googleapis.com/css?family=Raleway:400,400i,700,700i",
                    "https://codepen.io/cryptocss/pen/geyPdg.css",
                    "https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i",]

    for css in external_css:
        app.css.append_css({"external_url": css})

    # Originally: app.run_server(debug=True)
    app.run_server(debug=False, host='127.0.0.1', port=8050)

if __name__ == '__main__':
    main()