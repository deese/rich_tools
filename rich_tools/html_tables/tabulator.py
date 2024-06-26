from rich_tools.html_tables import HTMLExporterInterface
import json



DEFAULT_CONFIG = {
    "css": [
        {
            "href": "https://cdnjs.cloudflare.com/ajax/libs/tabulator/6.2.1/css/tabulator_bootstrap5.min.css",
            "integrity": "sha512-qDEgvDbdp7tq+ytU/OgCzWfvbfdEe3pv0yEOMz/gurMcR0BWNgIF6I4VKeoACEj5E5PFf1uo3Vzuwk/ga9zeUg=="
        },
    ],
    "js": [
        "https://unpkg.com/tabulator-tables/dist/js/tabulator.min.js"
    ]

}

class TabulatorExporter(HTMLExporterInterface):
    name = "Tabulator exporter"
    unique_id = "tabulator"
    config = {}

    def export (self, rich_table, template_file, output_file="output.html"):
        """Export a rich.Table instance to a HTML file."""
        self.vprint(f"Exporting to {output_file}.")

        #html_output_f = html_output.replace("%(TABLEDATA)", )
        #html_output_f = html_output_f.replace("%(CSS)", self.get_css())
        #html_output_f = html_output_f.replace("%(JS)", self.get_js())
        #headerFilter:true
        columns = []

        for f in rich_table:
            if columns:
                break
            for k in f.keys():
                #"field": k.replace(" ", "").lower(),
                columns.append({"title": k,  "field": k, "headerFilter": True})

        html_output_f = self.template_loader(template_file, { "tabledata": json.dumps([f for f in rich_table], indent=4), "columns": json.dumps(columns, indent=4), "css": self.get_css(), "js": self.get_js() })

        with open(output_file, "w", encoding="utf-8") as fw:
            fw.write(html_output_f)

    def __init__ (self):
        super(TabulatorExporter).__init__()
        self.config = DEFAULT_CONFIG

exporter = TabulatorExporter()
