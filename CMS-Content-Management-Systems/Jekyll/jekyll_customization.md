<link rel="stylesheet" href="../style.css">


# Configure Jekyll
- https://pages.github.com/
- https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll
- https://pages.github.com/versions/
- https://jekyllrb.com/docs/themes/#overriding-theme-defaults

# jekyll theme configuration.
## minimal-mistake
- Theme minimal-mistake. https://mmistakes.github.io/minimal-mistakes/docs/configuration/
- https://mmistakes.github.io/minimal-mistakes/docs/layouts/
- https://fontawesome.com/v5/search?o=r&m=free&s=solid
- jekyll Menu. https://www.youtube.com/watch?v=6h8-uPadFug
- classes: wide

# Search config on github.io 
https://www.algolia.com/account/api-keys/all?applicationId=OC1JFMR0PU

# putting carausal.
https://jekyllcodex.org/without-plugin/slider/

# converting normal to github repo to jekyll website. 

- like: https://yourname.github.io/reponame
create gh-pages branch in your repo. Everything else is taken care by github.
- https://github.com/st4ple/solid-jekyll
- Creating project carousal.

# https://jekyll.one/pages/public/manuals/modules/carousel/

# Liquid Used Objects, tags, and filter inside template file to display.
https://shopify.github.io/liquid/filters/concat/

- object: Objects contain the content that Liquid displays on a page.
	- {{ page.title }}

- Tag: Tags create the logic and control flow for templates.
Tags can be categorized into various types:
	- Control flow
	- Iteration
	- Template
	- Variable assignment

{% if user %}
  Hello {{ user.name }}!
{% endif %}

- Filters change the output of a Liquid object or variable.
{{ "/my/fancy/url" | append: ".html" }}
{{ "adam!" | capitalize | prepend: "Hello " }}

<!-- if site.users = "Tobi", "Laura", "Tetsuro", "Adam" -->
{% for user in site.users %}
  {{ user }}
{% endfor %}


The opposite of if – executes a block of code only if a certain condition is not met.

{% unless product.title == "Awesome Shoes" %}
  These shoes are not awesome.
{% endunless %}


# https://rubygems.org/gems

# https://pages.github.com/versions/


# GitHub Pages uses plugins that are enabled by default and cannot be disabled:
```
jekyll-coffeescript
jekyll-default-layout
jekyll-gist
jekyll-github-metadata
jekyll-optional-front-matter
jekyll-paginate
jekyll-readme-index
jekyll-titles-from-headings
jekyll-relative-links
```

https://materialdesignicons.com/


# Glossary Plugin/Gem 
https://github.com/erikw/jekyll-glossary_tooltip

# Liquid Code
```
<div class="grid__wrapper">
  {% assign collection = 'resources' %}
  {% assign posts = site[collection] | reverse %}
  {% for post in posts %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
```


# How commenting works in jekyll 

_config.yml: to mention comment service provider and your id created on the provider's website.
comment.html (to write comment)
comments.html (to show exsting comments)
post.html: to show the post on the screen.
    it includes archive-single.html, 
    it calls archive.html (layout)
	   it includes page__hero.html, breakcrums.html
	   it calls default.html (layout)
	      default.html includes : 
			  header.html, 
			  footer.html, 
			  scripts.html: this includes /comments-providers/disqus.html
			  


# Jekyll template calling

# Layouts
default using head.html & head/customer.html, footer/custom.html 
archive using layout default 
	home using layout archive 
	post using layout archive 
	collection using layout archive 
	category using layout archive 
	category using layout archive 
search using layout default 
single using layout default 
archive-taxonomy using layout default 

slider-online-conferences using layout single 
slider-online-sessions using layout single 


include 
	carousel.html 
	
layouts
	slider-online-conferences.html uses layout: single 

pages
	slider-online-training.mt uses layout: slider-online-sessions

pages:
	slider-pm-selected-photos.md => /slider-pm-selected-photos
		uses layout slider-pm-select-photos_layout

	slider-pm-workshop.md => /slider-pm-workshops
		uses layout slider-pm-workshops-layout

	slider-online-sessions.md => /slider-online-sessions
		uses layout slider-pm-workshops-layout

	slider-online-sessions2.md => /slider-online-training2
		uses layout slider-online-sessions-layout2

layout:
	slider-online-conferences.html
	slider-online-sessions
	slider-online-sessions2
	slider-pm-select-photos
	slider-pm-workshops

keywords: "Online Sessions, Data Science Sessions, Machine Learning, upGrad Sessions, Data Science Coaching"