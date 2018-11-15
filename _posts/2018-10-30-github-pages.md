---
layout: post
title: "Github Pages with Jekyll Notes"
date: 2018-11-05
excerpt: "Setting up Github Pages and quick rundown of Jekyll"
tags: [thought]
comments: true
---
# Let's Create a Personal Website on Github
Most professionals have a personal website. It showcases your CV, portfolio, hobbies and personality. It's a more intimate presentation of yourself to prospective employers, rather than submitting flavourless cover letter and resumes. 

There are numerous web hosts. A popular one is Github for personal websites. The default domain name is `$githubaccount/github.io` so it is easy to remember. This is just a web server so don't try to use it to host a web app that connects to DB or as an application server. 

Github Pages comes with support for Jekyll. This is a framework which makes it simple to reuse common HTML elements such as header and navbars across different pages of your website.
It comes with simple themes and you can use Markdown instead of HTML.

---

## Installation
1. Have MinGW installed along with MSYS and the base packages
2. Make sure `C:\MinGW` and `C:\MinGW\1.0` are added to PATH environment variable. 
3. Install Ruby v2.4.0 or higher (the developer edition)
4. Run the command `>>gem install jekyll bundler`
5. Create a repo `$domain_name.github.io` in Github
6. That URL should work now
7. There is a `\_config.yml` file which has line theme: $var
8. Look for the Jekyll theme you like and set that to $var
9. Gem file is Ruby's equivalent to package.json in npm. It indicates project dependencies.
10. If it isn't there, create one. Make sure you use char ending UTF-8. Copy this into the file.
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
Then add gem "$JEKYLL THEME$ to the last line.
11. Run command `>>bundle install` to install it locally
12. Run command `>>bundle exec jekyll serve` to host locally
13. It will be on **http://localhost:4000**

Here are some themes I found.
1. [Minimal](https://github.com/pages-themes/minimal)
2. [Gaohaoyang](https://github.com/Gaohaoyang/gaohaoyang.github.io)
3. [Moon](https://github.com/TaylanTatli/Moon/)

---

## Making the Website
First, you need to know that Github Pages allows certain parameters and locks others in the `\_config.yml` from being modified. It is specified [here](https://help.github.com/articles/configuring-jekyll/).

---

## Liquid
**Objects** - where to output content
~~~ html
{%raw%}{{ page.title }}{%endraw%}
~~~

**Tags** - logic and control flow
~~~ html
{%raw%}{٪ if page.show_sidebar ٪}
...
{٪ endif ٪}{%endraw%}
~~~

**Filters** - modifies output of Objects
~~~ html
{%raw%}{{ "hi" | capitalize }}{%endraw%}
~~~

---

## Front Matter
This is YAML snippet enclosed between triple dashes at top of file.
It is used to set variables for page.
~~~
---
{%raw%}var: 5 {%endraw%}
---
~~~

Front matter variables can be referenced by `page.var`.

---

## Layout
These are templates that wrap around your content. You call them to avoid repeating yourself.
They are in directory `\_layouts`. To determine where it wraps the body, 
wrap `{%raw%}{{content}}{%endraw%}`. Then assign value of layout in front matter to file name of layout.

~~~ html
{%raw%}layout: default
title: Home
---
{{ "hello world" | upcase }}{%endraw%}
~~~

To use markdown, create a file with extension *.md*

---

## Includes
We don't want to repeat ourselves. Code we refer is inside the `\_includes` directory.
Html or Markdown can be used from **includes** by `{٪include navigation.html}`
One of Jekyll's useful *variables* is page.url where you can check if each link is the current page.

---

## Data File
Jekyll supports loading CVS, JSON, YAML files inside the `\_data` directory.
YAML is used to store array of navigation items.

~~~ yaml
{%raw%}- name: Home
- title: Home
- name: About
  link: /about.html
  link: /
{{ "hello world" | upcase }}{%endraw%}
~~~

You can refer to **data files** by `site.data.navigation`

{% highlight html %} {% raw %}<nav>
{٪ for item in site.data.navigation ٪}
  a href="{{ item.link }}" {٪ if page.url == item.link ٪} 
  style="color: red;"{٪ endif ٪}>
  {{ item.name }}
  a>
{٪ endfor ٪}
</nav>{% endraw %} {% endhighlight %}

---

## Assets
CSS, JS, images and other asset are often placed in the **asset** directory. 
Inline styling is not best practice so we use CSS. 
Let's create a SASS file at `/assets/css/styles.scss`.
~~~
---
---
@import "@main";
~~~

This tells it to look for `_sass\main.scss`. Within your layout, create a tag element that loads your SASS file.
~~~ html
<link rel="stylesheet" href="{{ site.url }}/assets/css/main.css">
~~~

### Blogging
Jekyll stores blog posts in folder **\_posts**. These are .md and accessed by **site.posts**.
There is layout and author values.  The post layout outputs title, date, author and content body.
This is then wrapped by the default layout. Create `blog.html` in your root folder.

The filename must be in format `2018-08-21-apples.md`.
~~~
---
layout: post
title: "Github Pages with Jekyll Notes"
date: 2018-11-05
excerpt: "Setting up Github Pages and quick rundown of Jekyll"
tags: [thought]
comments: true
---
~~~

Remember to add this to main navigation in `/_data/navigation.yml`
~~~
- name: Blog
  link: /blog.html
~~~