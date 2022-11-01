---
modified: 1 October 2022
---
<link rel="stylesheet" href="style.css">
<span style="font-size: 80%; color: grey;">Last modified on {{ page.modified }}</span>

## Contents

  * <a href="#download">Download</a>
  * <a href="#screenshots">Screenshots</a>
  * <a href="#windows-warnings">Windows warnings</a>
  * <a href="#about-watertap">About WaterTAP</a>
  * <a href="#acknowlegements">Acknowledgements</a>

## Download

Choose a version (latest first) and click on the link corresponding to your operating system.
This will download an installation file.
Open the installation file to install the software.

{% assign ver = "-" -%}
{% assign rel_by_ver = site.data.releases | sort: "key" | reverse -%}
{% for release in rel_by_ver -%}
{% if ver != release.version -%}
<span class="wt-ver">Version {{ release.version }}</span><span class="wt-date">{{ release.date }}</span>
{% endif %}
<a href="{{ release.url }}" class="wt-link">{{ release.os }}</a>{% assign ver = release.version -%}
{% endfor %}

## Screenshots

Version: 0.6.0

***List of models***

<img width="855" alt="image" src="https://user-images.githubusercontent.com/420923/199105451-b34da5fd-6ef9-4220-a3dd-b3c6c5068558.png">

***Set model parameters***

<img width="855" alt="image" src="https://user-images.githubusercontent.com/420923/199105605-6e0866c8-0b19-46c2-b92e-ef8fc8d85fdd.png">

***Show results***

<img width="855" alt="image" src="https://user-images.githubusercontent.com/420923/199105704-4e59fda8-e4e6-4738-b55e-9b11fb0eaa8f.png">


## Windows warnings

Due to security procedures by Microsoft, you may see warnings and need to take additional steps to download the `.exe` file for the Windows installer.
**The executable has been verified to be safe,** but due to the small number of people who have downloaded and installed it, Microsoft still regards it as an untrusted resource. Below are details on how to tell Windows to install the software anyways.

### Windows Protector warning screens

The most common form of this warning comes from Windows Protector. You will see an initial screen that looks like this (red annotation added):

<img width="300px" src="assets/img/windows-protect-1.webp" alt="Windows Protector window 1">

As the annotation indicates, you should click on the "More info" link. This will result in a second screen that looks like this:

<img width="300px" src="assets/img/windows-protect-2.webp" alt="Windows Protector window 2">

In this screen, click on the "Run anyway" button to begin the installation process.

### Microsoft Edge warnings

If you use the Microsoft Edge browser, you may encounter a second form of this process.
When you perform the download, the browser will show a message that looks like this:

<img width="300px" src="assets/img/windows-edge-1.webp" alt="Windows Edge browser 1">

Select the three dots next to this message and select "Keep", as indicated in the following screenshot (red annotation added):

<img width="300px" src="assets/img/windows-edge-2.webp" alt="Windows Edge browser 2">

This will bring up another window, where you need to first select "Show more" and then select the "Keep anyway" option that appears, as indicated in this screenshot (red annotation added):

<img width="300px" src="assets/img/windows-edge-3.webp" alt="Windows Edge browser 3">


## About WaterTAP

* WaterTAP is part of the [National Alliance for Water Innovation (NAWI)](https://www.nawihub.org).
* [WaterTAP on Github](https://github.com/watertap-org/)
* [WaterTAP page on NAWI website](https://www.nawihub.org/knowledge/watertap/)

## Acknowledgements

> WaterTAP is funded by the US Department of Energy, Office of Energy Efficiency and Renewable Energy (EERE) under Funding Opportunity Announcement DE-FOA-0002336 (R&D for Advanced Water Resource Recovery)

> The National Alliance for Water Innovation (NAWI) Energy-Water Desalination Hub is funded by the U.S. Department of Energy, Energy Efficiency and Renewable Energy Office, Advanced Manufacturing Office under Funding Opportunity Announcement DE-FOA-0001905
