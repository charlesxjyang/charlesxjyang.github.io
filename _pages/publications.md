---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
## Public Policy

I published a data brief in collaboration with some folks at [CSET@Georgetown](https://cset.georgetown.edu/) on how [AI is changing the way we do science](https://cset.georgetown.edu/publication/machine-intelligence-for-scientific-discovery-and-engineering-invention/).

I also published a policy proposal with the [DayOneProject](https://www.dayoneproject.org/) outlining [how the Biden Administration can modernize and decarbonize our power grid](https://www.dayoneproject.org/post/building-back-with-a-cleaner-power-grid-for-america). 

## Academic Publications


You can find a complete list of my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=BYOREdwAAAAJ&hl=en)

This is a curated list of my publications:

{% include base_path %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
