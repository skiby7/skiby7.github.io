---
layout: page
title: Programming 101
permalink: /course/
---

Here is the course index:

<ul>
  {% for lesson in site.course %}
    <li>
      <a href="{{ lesson.url | relative_url }}">{{ lesson.title }}</a>
    </li>
  {% endfor %}
</ul>
