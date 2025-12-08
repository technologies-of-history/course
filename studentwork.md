---
layout: page
title: Student Work
---

<div class="posts" id="top">
  {% for post in site.posts %}
    <article class="post">
      <header class="post-header">
      <h2 class="post-title"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
      <h4>By {{ post.author }} on {{ post.date | date: "%B %e, %Y" }}</h4>
      </header>

      <div class="entry">
        {{ post.excerpt }}
      </div>

      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
    </article>
  {% endfor %}

  <div class="breadcrumbs">
    <a href="#top">Return to the top</a>
  </div>
</div>