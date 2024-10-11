from fasthtml.common import *

flex_css = Link(
    rel="stylesheet",
    href="https://cdnjs.cloudflare.com/ajax/libs/flexboxgrid/"
    + "6.3.1/flexboxgrid.min.css",
    type="text/css",
)
custom_css = Link(rel="stylesheet", href="custom.css", type="text/css")

hdrs = (MarkdownJS(), flex_css, custom_css)

app, rt = fast_app(hdrs=hdrs, live=False)


def read_markdown(name):
    return open(name + ".md").read()


intro = read_markdown("intro")
download = read_markdown("download")
download_url = "https://github.com/watertap-org/watertap-ui/releases/download"
funding_ack = (
    "WaterTAP is funded by the US Department of Energy, Office of Energy "
    "Efficiency and Renewable Energy (EERE) under Funding Opportunity "
    "Announcement DE-FOA-0002336 (R&D for Advanced Water Resource Recovery)"
)

nawi_ack = (
    "The National Alliance for Water Innovation (NAWI) Energy-Water "
    "Desalination Hub is funded by the U.S. Department of Energy, Energy "
    "Efficiency and Renewable Energy Office, Advanced Manufacturing "
    "Office under Funding Opportunity Announcement DE-FOA-0001905"
)

win, mac = "Windows", "Mac OSX ARM64"

####################
# Download links   #
####################
download_version_tag = {
    "1.1.0": {
        win: "24.10.11/WaterTAP-UI_24.10.11_win64.exe",
        mac: "24.10.11/WaterTAP-UI-24.10.11-arm64.dmg",
    },
    "1.0.0": {
        win: "24.08.13/WaterTAP-UI_24.08.15_win64.exe",
        mac: "24.08.13/WaterTAP-UI-24.8.15-arm64.dmg",
    },
    "0.12.0": {
        win: "0.12.0/WaterTAP-UI-24.03.29-win64.exe",
        mac: "0.12.0/WaterTAP-UI-24.03.29-arm64.dmg"},
    "0.11.0": {
        win: "0.11.0/WaterTAP-UI_24.01.26_win64.exe",
        mac: "0.11.0/WaterTAP-UI-24.1.26-arm64.dmg"},
}

ver_flex_cls = "box col-xs-12 col-sm-12 col-md-12 col-lg-2"
a_flex_cls = "col-xs-12 col-sm-6 col-md-4 col-lg-3"
btn_flex_cls = "box outline"
btn_flex_high_cls = "box outline"

download_links = []
for key, value in download_version_tag.items():
    btn_cls = btn_flex_cls
    ver_cls = ver_flex_cls
    if key == "1.0.0":
        btn_cls += " contrast"
        ver_cls += " contrast"
    download_links.append(Div(
        Button(f"Version {key}", cls=ver_cls),
        A(
            Button(win, cls=btn_cls),
            cls=a_flex_cls,
            href=f"{download_url}/{value[win]}",
        ),
        A(
            Button(mac, cls=btn_cls),
            cls=a_flex_cls,
            href=f"{download_url}/{value[mac]}",
        ),
        cls="row",
    ))


screenshots = [Img(src=f"wt{i}.png", width="800px") for i in range(1, 4)]

@rt("/")
def get(req):
    return Body(
        Header(
            Img(src="wt-logo.webp", width="100px", style="margin: 0 1em 1em 0;"),
            H1("Get Started with the WaterTAP UI", style="display: inline;"),
        ),
        Main(
            Div(intro, cls="marked"),
            Card(Grid(*screenshots), header=Div(H3("Screenshots"), P("Input, Output, and Comparison screens"))),
            Div(download, cls="marked"),
            Div(*download_links),
        ),
        Footer(
            H2("Acknowledgements"),
            P(Em(funding_ack)),
            P(Em(nawi_ack))
        ),
        cls="container",
    )


serve(host="127.0.0.1", port=55000, reload=False)
