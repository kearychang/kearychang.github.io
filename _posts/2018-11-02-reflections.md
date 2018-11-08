---
layout: post
title: "Reflections on Lessons working with in SemanticUI, JS"
date: 2018-11-02
excerpt: "We all make mistakes. It's important to reflect to cement your understanding."
tags: [thought]
comments: true
---
I really **really** like the appearance of SemanticUI. Bootstrap is overused. You can always customize,
but they don't make it as easy to. Let's give a quick rundown of SemanticUI. 
Comparatively, SemanticUI classifies its **components** as 
* global - CSS attributes shared across all of SemanticUI, e.g. color, font size, spacing
* elements - individual UI elements, e.g. message, button, input
* collections - groups of elements, e.g. form, grid, menu, table
* views
* modules - describes how elements look and act, e.g. dropdowns, modals
* behaviors - descriptions about how page elements should act, e.g. form validation

### What I did ###

I decided to try out SemanticUI on a small website project that implements Bernstein's algorithm
for normalization of a DB schema. This is a sequence of how I built it so far
1. Wireframe and create container
2. Create a SemanticUI grid and put component inside columns
3. There are 4 sections: header, description, steps and configuration
4. Header consists of title with segment separating it from description
5. Description consists of nested grid with 2x2 resizable explanation of the algorithm
6. Steps is a row of 3 buttons where you toggle between steps, changing the view of description and configuration
7. Configuration is a series of forms (input, textarea) that users enter and view information about their schema

### My Installation of SemanticUI ###
You can download the source CSS and JS for SemanticUI directly, but if you want the extra features
such as theming, you need to get it from npm. It is recommended to also install Gulp globally.
Gulp automates part of the build process. In SemanticUI, the compiled CSS and JS is created
after factoring modifications such as overrides or changes to the source file. Gulp watches this 
and automatically compiles the final SemanticUI CSS/JS.

### Mistakes - SemanticUI ###
Grid was difficult for me to grasp the first time since I kept comparing it to Bootstrap. 
I had problems getting content to align correctly when using nested grids.
Next time, I have to remember to nest grids inside columns and avoid using containers.

Customizing elements was also a pain if you don't understanding theming. **I still don't really.***
In Bootstrap, you have *components* and *utilities* and the latter almost universally works on the former.
In SemanticUI, simple things such as color are tied only to certain components.
You have to use overrides and refer to the source files to see which variables to modify.

### Mistakes - CSS ###
When making dynamic content, a simple strategy is to display everything, then have JS hide it on initialization.
If you just use CSS's hidden attribute, the content is not visible, but still occupies space since position attribute is default static.
Therefore, you also have to change the position attribute to absolute to remove it from flow.

In SemanticUI, you can wrap it in a message element, then make its class hidden, removing the neccesity of changing attribute.

### Mistakes - JS ###
For a while, I always thought function(e) {...} and (e) => {...} was equivalent.
They aren't. It's my mistake for not reading the documentation and would have saved myself time.
In the former, **this** when called as a method in an object is the context that the function is called.
So if function is setInterval({this...},100), **this** is the global object.
If you want this to refer to the object containing the function, you must pass this through binding or call.
For the latter ES6 anonymous function, **this** is always the enclosing context.

When using loops (for/while) versus forEach(), map(), filter(), since arguments are passed to a function,
the former allows early termination of the calling function by invoking return.
In the latter, invoking return is equivalent to invoking break in the former.