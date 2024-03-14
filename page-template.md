---
title: "{{ pattern_name}}"
date: {{ creation_date }}
draft: false
status: {{ status }}
model: {{ model }}
categories: 
 - {{ family }}
tags: 
{% for tag in tags %}
 - {{ tag }} 
{% endfor %}
description: "{{ short_description }}"
---

![Card for {{ pattern_name}}.](/cards/{{ pattern_slug }}.png)
![{{ short_description }}](/images/{{ pattern_slug }}.webp)

{{ page_contents }}