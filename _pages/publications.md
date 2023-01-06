---
layout: page
permalink: /publications/
title: Publications
description:
years: ["Preprints", 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
nav: true
redirect_from:
  - /ja/publications/
---

<p>Selected publications are listed <a href="/">here</a>.</p>
<p>Link to 
    <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" target="_blank" rel="noopener"><i class="ai ai-google-scholar"></i> Google Scholar</a> | 
    <a href="https://orcid.org/{{site.orcid_id}}" target="_blank" rel="noopener"><i class="ai ai-orcid"></i> ORCID</a> | 
    <a href="{{site.pubmed_mybib}}" target="_blank" rel="noopener"><i class="ai ai-pubmed"></i> PubMed</a>
</p>
<p>* denotes equal contribution</p>

<div class="publications">
<p>
    Jump to {% for y in page.years %}
    <a href="#{{y}}">{{y}}</a> |
    {% endfor %}
</p>

{% for y in page.years %}
  <h2 class="year" id="{{y}}">{{y}}</h2>
  {% if y == "Preprints" %}
    {% bibliography -f publications -q @*[journal~=Rxiv$] --label reset %}
  {% else %}
    {% bibliography -f publications -q @*[year={{y}} && journal!~Rxiv$] %}
  {% endif %}
{% endfor %}

</div>
