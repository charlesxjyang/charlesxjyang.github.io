---
layout: archive
permalink: /blog/
title: "Blog posts"
author_profile: true
redirect_from:
  - /wordpress/blog-posts/
---
<!--
I write on <a href="https://medium.com/@charlesyang_32909" target="_blank">Medium</a> occasionally. Here are some of my top posts:

I write about <a href="https://ml4sci.substack.com/" target="_blank">Machine Learning for Scientific Applications at ML4Sci</a>!

<iframe src="https://ml4sci.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no">
</iframe>
-->

I write on [Medium](https://medium.com/@charlesyang_32909)

I also write about machine learning for scientific applications at [ML4Sci](https://ml4sci.substack.com/)

<iframe src="https://ml4sci.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no">
</iframe>


{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}
