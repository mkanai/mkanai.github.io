---
layout: page
permalink: /publications/
title: Publications
description:
years: ["Preprints", 2026, 2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
nav: true
redirect_from:
  - /ja/publications/
---

<div class="row">
  <div class="col-sm-9">
    <ul class="list-unstyled mb-0">
      <li><p>Selected publications are listed <a href="/">here</a>. <b>*</b> denotes equal contribution</p></li>
      <li>Link to
        <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" target="_blank" rel="noopener"><i class="ai ai-google-scholar"></i> Google Scholar</a> | 
        <a href="https://orcid.org/{{site.orcid_id}}" target="_blank" rel="noopener"><i class="ai ai-orcid"></i> ORCID</a> | 
        <a href="{{site.pubmed_mybib}}" target="_blank" rel="noopener"><i class="ai ai-pubmed"></i> PubMed</a>
      </li>
      <li>Jump to
      {% for y in page.years %}
        <a href="#{{y}}">{{y}}</a> |
      {% endfor %}
      </li>
    </ul>
  </div>
  <div class="col-sm-3 mt-auto pt-3">
    <input type="text" class="form-control" id="search-input" placeholder="Search...">
  </div>
</div>

<div class="publications">

{% for y in page.years %}
  <h2 class="year" id="{{y}}">{{y}}</h2>
  {% if y == "Preprints" %}
    {% bibliography -f publications -q @*[journal~=Rxiv$ || journal=Research Square] --label reset %}
  {% else %}
    {% bibliography -f publications -q @*[year={{y}} && journal!~Rxiv$ && journal!=Research Square] %}
  {% endif %}
{% endfor %}

</div>
