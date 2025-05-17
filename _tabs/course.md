---
layout: page
title: Programming pills
icon: fas fa-laptop
order: 4
permalink: /course/
---

This "course" is a collections of programming pills collected over the years. I'm publishing them here in case someone finds these concepts somewhat useful. Here's the index:

<ul>
  {% for lesson in site.course %}
    <li>
      <a href="{{ lesson.url | relative_url }}">{{ lesson.title }}</a>
    </li>
  {% endfor %}
</ul>
