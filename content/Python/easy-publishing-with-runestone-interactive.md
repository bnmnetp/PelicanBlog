Title: easy publishing with runestone interactive
Date: 2014/03/05 08:19:04
Slug: easy-publishing-with-runestone-interactive
Tags: python, runestone
Link: 
Description: 


During my January travels, I also converted this blog from tubmlr, which had been frustrating me for a while, to Octopress, with which I have been very happy.  Nothing like hacker level control of your own blog.  But more, than just the switch in tools, the move to Octopress inspired me to make it easier for people to publish small or large works using the Runestone tools.

Yesterday, at the Learning @ Scale conference we demoed this new capability.  See [the demo here](<http://runestoneinteractive.org/LearningAtScale).  To make it super easy to publish:

* Lecture slides
* Demonstrations
* A Tutorial
* Lab Instructions
* In class exercises
* A short module on your favorite topic not covered elsewhere
* An entire book

<!-- TEASER_END -->

### Building

You can simply follow the instructions at this new repository:  [github.com/RunestoneInteractive/RunestoneTools](http://github.com/RunestoneInteractive/RunestoneTools).  In a nutshell:

1.  Install Sphinx, paver, and paverutils using pip.
2.  Clone the repository
3.  Edit the index.rst file in source, and add any additional rst files you may want, depending on how complex your project is.
4.  run ``paver build``

### Deploying

Now you have a choice.  In the build directory you have a nice self contained set of html files, these files are set up to make use of the runestone server invisibly in the background.  The static html can be served from any web server.  Just drop in the build directory and you are ready to serve.  OR, you can now host and deploy your project using **GitHub Pages**.  To host on github pages you need to do three things.

1.  Create an empty repository in your github account.
2.  run `paver setup_github_pages` and paste in the URL of the new account.
3.  run paver deploy

Now your pages will be available at:  http://youraccount.github.io/YourRepo
If you want to host these pages behind a custom domain name, you can follow the instructions on github for doing so.  Hint:  Its really easy.

I hope this new capability will inspire lots of people to give these tools a try.  I also hope that we can build a repository of resources built with the tools, so that we can all share our teaching ideas.  Stay tuned for more on that.

### Caveats

All of the features, activecode, codelens, assessment questions, parson's problems, [and more](http://interactivepython.org/overview/overview.html) work just fine.  The major thing that will not work (yet!) is the login/logout.  I need to rework our authentication system in order for this to work.  This will for sure need to happen before the end of summer.
