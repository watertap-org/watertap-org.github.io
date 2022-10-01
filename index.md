---
layout: default
modified: 1 October 2022
---

<span style="font-size: 80%; color: grey;">Last modified on {{ page.modified }}</span>

# Overview

Welcome to the WaterTAP graphical user interface (GUI) software download page.

WaterTAP is part of the National Alliance for Water Innovation (NAWI).

<img alt="NAWI logo" src="nawi-transp.webp" width="150px">
<img alt="WaterTAP logo" src="watertap-transp.webp" width="150px">

# Downloads

Download installer and open on your desktop to install the software.

| Download | Version | OS |
|:---------|:--------|:---|
{% for release in site.data.releases -%}
| <a href="{{ release.url }}">{{ release.url }}</a> | {{release.version}} | {{ release.os }} |
{% endfor %}

# More information

* (https://github.com/watertap-org/watertap)[Github]
* (https://www.nawihub.org/knowledge/watertap/)[WaterTAP page on NAWI website]
* (https://www.nawihub.org/)[NAWI website]

## Acknowledgements

> WaterTAP is funded by the US Department of Energy, Office of Energy Efficiency and Renewable Energy (EERE) under Funding Opportunity Announcement DE-FOA-0002336 (R&D for Advanced Water Resource Recovery)

> The National Alliance for Water Innovation (NAWI) Energy-Water Desalination Hub is funded by the U.S. Department of Energy, Energy Efficiency and Renewable Energy Office, Advanced Manufacturing Office under Funding Opportunity Announcement DE-FOA-0001905