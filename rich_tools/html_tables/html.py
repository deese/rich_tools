from rich_tools.html_tables import HTMLExporterInterface

DEFAULT_CONFIG = {
    "css": [
        {
            "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
            "integrity":"sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        },
    ],
    "js": [
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
    ]

}

html_output = """
<html>
%(CSS)
%(JS)
<body>
	<div class="container">
        <div id="main_table">
        %(TABLE)
        </div>
    </div>
</body>
</body>
</html>
"""
class HTMLExporter(HTMLExporterInterface):
    name = "HTML exporter"
    unique_id = "html"

    def configure (self, config, extra_config=None):
        """Configure the exporter."""
        self.config = config

    def export (self, rich_table, template_file, output_file="output.html"):
        """Export a rich.Table instance to a HTML file."""
        self.vprint(f"Exporting to {output_file}.")


        html_table = "<table>\n"

        for c, i in enumerate(rich_table):
            if c == 0:
                html_table_header = "<tr>\n"
                for k in i.keys():
                    html_table_header += f"<th>{k}</th>\n"
                html_table_header += "</tr>\n"
                html_table += html_table_header
            html_table_row = "<tr>\n"
            for k, v in i.items():
                html_table_row += f"<td>{v}</td>\n"
            html_table_row += "</tr>\n"
            html_table += html_table_row

        html_table += "</table>\n"

        html_output_f = self.template_loader(template_file, { "table": html_table, "css": self.get_css(), "js": self.get_js() })

        with open(output_file, "w", encoding="utf-8") as fw:
            fw.write(html_output_f)

    def __init__ (self):
        super(HTMLExporter).__init__()
        self.config = DEFAULT_CONFIG

exporter = HTMLExporter()
