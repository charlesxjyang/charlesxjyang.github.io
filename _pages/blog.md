---
layout: archive
permalink: /blog/
title: "Blog posts"
author_profile: true
redirect_from:
  - /wordpress/blog-posts/
---

<iframe src="https://charlesyang.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no">
</iframe>

I also occasionally write on [Medium](https://medium.com/@charlesyang_32909). Here are some of my best articles:
 - [Deep Learning in Science](https://towardsdatascience.com/deep-learning-in-science-fd614bb3f3ce)
 - [AI is a Cybersecurity Threat](https://medium.com/@charlesyang_32909/ai-is-a-cybersecurity-threat-516e58e6e4df)
 - [Interviewing OpenAI's GPT-2](https://towardsdatascience.com/interviewing-the-1-5b-gpt-2-model-by-openai-b7f30fbbb8a6)
 - [An introduction to metal organic frameworks](https://medium.com/@charlesyang_32909/metal-organic-frameworks-a-brief-intro-9f8ced9500bb)

<!--
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
-->
