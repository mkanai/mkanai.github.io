---
layout: page
permalink: /publications/
title: publications
description:
years: [2021, 2020, 2019, 2018, 2017, 2016, 2015]
nav: true
---

<p>Link to 
  <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" target="_blank" rel="noopener">Google Scholar</a> | 
  <a href="https://orcid.org/{{site.orcid.id}}" target="_blank" rel="noopener">ORCID</a> | 
  <a href="{{site.pubmed_mybib}}" target="_blank" rel="noopener">PubMed</a>
</p>
<p>* denotes equal contribution</p>

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% if y == 2021 %}
    {% bibliography -f publications -q @*[year={{y}}]* --label split --label start %}
  {% else %}
    {% bibliography -f publications -q @*[year={{y}}]* --label split %}
  {% endif %}
{% endfor %}

</div>
