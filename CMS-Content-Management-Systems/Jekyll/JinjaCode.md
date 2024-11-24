#Jinga Coding #JingaCode #Jekyll #DasarpAI #blog


---
layout: archive
permalink: /WoC/
title: "Winter of Code"
author_profile: true
header:
  image: "/assets/images/ai1.png"
---


<div class="grid__wrapper">
  {% assign collection = 'woc' %}
  {% assign posts = site[collection] | reverse %}
  {% for post in posts %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>


{% if post.header.teaser %}
  {% capture teaser %}{{ post.header.teaser }}{% endcapture %}
{% else %}
  {% assign teaser = site.teaser %}
{% endif %}



