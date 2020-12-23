---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can find a complete list of my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=BYOREdwAAAAJ&hl=en)

This is a curated list of my publications:

{% include base_path %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
