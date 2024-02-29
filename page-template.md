---
title: "{{ pattern_name}}"
date: {{ creation_date }}
draft: false
status: {{ status }}
model: {{ model }}
categories: 
 - {{ category }}
tags:[] 
{% for tag in tags %}
    {{ tag }}, 
{% endfor %}
description: "{{ short_description }}"
---

![{{ short_description }}](/images/{{ pattern_slug }}.webp)

{{ page_contents }}