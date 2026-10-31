# -*- coding: utf-8 -*-

from interface.app import app
#from interface.utils import webbrowser
import webbrowser

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:8050')  # Go to example.com

    # Initially possessing only debug=True.
    app.run_server(debug=False, host='127.0.0.1', port=8050)
