project = 'IDA Launcher'
html_title = 'IDA Launcher Docs'

extensions = ['sphinx_tabs.tabs', 'myst_parser']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'furo'
html_static_path = ['_static']
sphinx_tabs_disable_tab_closing = True

def setup(app):
    app.add_css_file('main.css')
