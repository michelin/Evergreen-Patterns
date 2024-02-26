---
title: "{{ pattern_name}}"
date: {{ creation_date }}
featured_image: "/images/{{ pattern_slug }}.webp"
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

{{ page_contents }}