# -*- coding: utf-8 -*-
"""Start the original Dash catalogue directly from the repository root."""
import webbrowser
from db_interface.interface.app import app

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050')
    app.run_server(debug=False, host='127.0.0.1', port=8050)
