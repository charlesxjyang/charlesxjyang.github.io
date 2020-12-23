---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can find a complete list of my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=BYOREdwAAAAJ&hl=en)
{% include base_path %}

<!--{% if author.googlescholar %}-->

<!--{% endif %}-->


{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
