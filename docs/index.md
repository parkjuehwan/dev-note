---
layout: default
title: Welcome to My Dev Blog
---

<h1>{{ page.title }}</h1>

<ul>
  {%- assign uncategorized_posts = site.posts | where_exp:"post","post.categories == empty" -%}

  {% for category in site.categories %}
    <li>
      📂 <strong>{{ category[0] }}</strong>
      <ul>
        {% for post in category[1] %}
          <li>📄 <a href="{{ post.url | relative_url }}">{{ post.title }}</a> ({{ post.date | date: "%Y-%m-%d" }})</li>
        {% endfor %}
      </ul>
    </li>
  {% endfor %}

  {% for post in uncategorized_posts %}
    <li>📄 <a href="{{ post.url | relative_url }}">{{ post.title }}</a> ({{ post.date | date: "%Y-%m-%d" }})</li>
  {% endfor %}
</ul>
