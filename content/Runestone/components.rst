Towards Web Components for Runestone
####################################

:date: 2015/03/23
:slug: Towards-Web-Components-for-Runestone
:tags: Javscript, Hacking, Development, Runestone
:link: 
:description: Having time to think about architecture and web components is nice.

One of the nice things about being in Malta for the spring is that I've been able to step back and think about `Runestone Interactive <http://runestoneinteractive.org>`_ and some of the ways it can be improved and moved forward.  One of the things that I think holds the overall goals of the project back somewhat is the initial choice of restructuredText as the main authoring language.  It was a good technical choice, but it is not nearly as popular as some other alternatives.  

Recent developments in the world of web development have lead me to believe that a new approach would make a lot of sense. 

So I’ve been messing around with `this new idea <https://github.com/bnmnetp/newactivecode>`_

The idea is to create a standard intermediate html format that sits between the `restructuredText  <http://docutils.sourceforge.net/docs/>`_ of `Sphinx <http://sphinx.pocoo.org>`_ and what gets rendered in the browser.  All of the hard work is done by javascript that takes the html and turns it into one of the Runestone components.

Why do this you may ask?  

* Well, for one reason, the code for the directives is getting increasingly unwieldy and very difficult to maintain.  Too many cooks, too little standardization.  Some of it is a real mess.  My javascript skills are much better than when I wrote the first implementation of activecode.

* But more importantly this has the benefit of making runestone available to virtually anyone you would not need to write in RST at all, you could write in plain html if you wanted to.  Or any other markup language that let you insert html.  Or if you were a clever hacker you could write your own macros for whatever system you use that generates the html.

* Finally I think this is a move in the direction that the web is headed over the next few years which is custom tags.  Imagine if we could just have an ``<activecode>`` tag?

So, rather than learning restructuredText and installing Sphinx you could include a few javascript files in your page and then write html that looked like this:

.. code-block:: html

   <body>
   <pre data-component="activecode" data-lang="python" id="test1">
   def foo():
       print 'hello world'

   foo()
   </pre>

   <pre data-component="activecode" data-lang="python" id="test2" data-include="test1 test2">
   def main():
       print 'goodbye girl'

   main()
   ====
   print "This is hidden suffix code you don't see it in the editor"
   </pre>

   </body>
   
and get a page that looked like this:

.. image:: https://www.dropbox.com/s/fqvakeftnfa75gp/Screenshot%202015-03-23%2018.45.58.png?raw=1

Anyway, I am looking at this as an excuse to learn about `Polymer <https://www.polymer-project.org/>`_, `AngularJS <http://www.angularjs.org>`_ and `Polyfills <http://stackoverflow.com/questions/7087331/what-is-the-meaning-of-polyfills-in-html5>`_ and `web components <http://webcomponents.org>`_ in general.  The repo I linked to above has got activecode working very nicely, and I like this implementation.  It is Much cleaner.  There is no reliance on creating special xxx_code, xxx_edit, xxx_output id values for different div elements, no need to mix and match a bunch of template code in the directive implementation.  Take a look and let me know what you think.  

I would be especially happy to have you look at the code on github and send me any comments about the current implementation, or pointers on how to convert that into a web component.  Someday there will be an ``<activecode>`` tag.

