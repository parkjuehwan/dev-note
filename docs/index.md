---
layout: default
title: Welcome to My Dev Blog
---

<h1>{{ page.title }}</h1>

<ul>
  {%- assign uncategorized_posts = site.posts | where_exp:"post","post.categories == empty" -%}

  {%- comment -%}
    1. 카테고리 있는 글들을 카테고리별로 묶어서 출력
  {%- endcomment -%}
  {% for category in site.categories %}
    <li>
      📂 <strong>{{ category[0] }}</strong>
      <ul>
        {% for post in category[1] %}
          <li>📄 <a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date: "%Y-%m-%d" }})</li>
        {% endfor %}
      </ul>
    </li>
  {% endfor %}

  {%- comment -%}
    2. 카테고리 없는 글은 바로 파일처럼 출력
  {%- endcomment -%}
  {% for post in uncategorized_posts %}
    <li>📄 <a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date: "%Y-%m-%d" }})</li>
  {% endfor %}
</ul>
