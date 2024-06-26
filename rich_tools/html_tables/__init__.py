from os.path import dirname, basename, isfile, join
from importlib import import_module
import glob
import re

try:
    from jinja2 import Environment, FileSystemLoader, ChoiceLoader
    HAS_JINJA2 = True
except ImportError:
    HAS_JINJA2 = False

modules = glob.glob(join(dirname(__file__), "*.py"))
exporter_names = [ basename(f)[:-3] for f in modules if isfile(f) and not ( f.endswith('__init__.py') or f.endswith('interface.py'))]

DEFAULT_CONFIG = {}

class HTMLExporterInterface:
    """Interface class for exporting rich.Table instances to HTML files."""

    name = "Interface HTML exporter"
    unique_id = "interface"
    verbose = False

    def vprint(self, data):
        """ Print data if verbose is True. """
        if self.verbose:
            print(f"[{self.unique_id}] {data}")

    def export (self, rich_table, template_file, output_file="output.html"):
        """Export a rich.Table instance to a HTML file."""
        print(f"Exporting to {output_file}.")
        print("Done.")

    def configure (self, config=None, extra_config=None):
        """Add extra configs to the exporter."""
        if config:
            self.config.update(config)

        if extra_config:
            for cfg in [ "css", "js"]:
                if cfg in extra_config:
                    self.config[cfg]  += extra_config[cfg]

    def __init__(self) -> None:
        self.config = DEFAULT_CONFIG

    def get_js(self) -> str:
        """Get the JS."""
        js = ""
        for i in self.config.get("js", []):
            js += f'<script src="{i}"></script>\n'
        return js

    def get_css(self) -> str:
        """Get the CSS."""
        css = ""
        for i in self.config.get("css", []):
            if "integrity" in i:
                css += f'<link rel="stylesheet" href="{i["href"]}" integrity="{i["integrity"]}" crossorigin="anonymous">\n'
            else:
                css += f'<link rel="stylesheet" href="{i["href"]}">\n'
        return css

    def template_loader(self, template_file, data):
        """ Load the template file and replace the data. """
        if not HAS_JINJA2:
            return self.simple_loader(template_file, data)
        else:
            environment = Environment(loader=ChoiceLoader([ FileSystemLoader("templates/"), FileSystemLoader(".") ]))
            template = environment.get_template(template_file)
            return template.render(**data)

    def simple_loader(self, template_file, data):
        """ Load the template file and replace the data. """
        with open(template_file, "r", encoding="utf-8")  as f:
            template = f.read()

        for k, v in data.items():
            template = re.sub(r"{{{{\s+{}\s+}}}}".format(k), v, template)
        return template % data

exporters = {}
for i in exporter_names:
    exporters[i] = import_module(f"rich_tools.html_tables.{i}").exporter