Runestone: a look ahead to 2015
###############################

:slug: runestone2015
:date: 2014/12/27 18:17:18 UTC
:tags: Python, Runestone
:link: 
:description: My first state of the 'stone post
:type: text

The Year in Review or "The state of the 'stone"
-----------------------------------------------

It has been an exciting year for the Runestone Interactive project.  Our Fall 2014 daily use has more than doubled that of Fall 2013, as we are serving nearly 8000 unique visitors a day on average on the `interactivepython.org <http://interactivepython.org>`__ site.  And with 132 Forks of the project on github, and anecdotal evidence of others running their own servers we could easily be serving over 10,000 users a day right now.  Over 730 'courses' have been created on `interactivepython.org` many of them  are high school courses, and many of them are from smaller colleges. We have users from over 170 countries around the world.  The United states now accounts for less than half of our traffic.

At least one of the books has been translated (`http://aliev.me/runestone/`) into Russian!  Seriously, I never would have thought this would happen.

The tools have also produced four new books this year that we are hosting.  
* One is in testing that I can't say anything about yet.
* A second is an `AP Review book for Java <http://interactivepython.org/runestone/static/JavaReview/index.html>`_, written by `Barbara Ericson <http://www.cc.gatech.edu/people/barbara-ericson>`_
* The third is `Programs Information and People <http://interactivepython.org/runestone/static/pip2/index.html>`_ by `Paul Resnick <http://presnick.people.si.umich.edu>`_.
* And finally My own project:  Fundamentals of Web Programming, worked very well for my seven week intro to web programming course.  I've been expanding it to work with my upper level web programming course and will release it for others to use soon.  

* There are also a few books published by others and hosted elsewhere around the web.

The activecode blocks now support:

* Python -- of course
* Javascript
* HTML
* Blockly

We also took two steps toward providing more server side functionality, rather than relying on everything happening in the browser with Javascript.  Those new features are attached to the activecode blocks in the form of the "Code Coach" and "Run in CodeLens" buttons.  This was a big departure for me, because I've always had a goal that the books should "just work" even if you are on an airplane without WiFi.  But both of these features need to connect to a server in real time.  However since the lack of connectivity is an increasingly rare phenomenon these days I think this is going to be a good direction.

There were also major improvements to assignments and grading.  You can now have a custom page for writing and publishing your own assignments.  You can also create assignments with due dates for your course and students can check their progress for the entire course on the progress page.

This past summer, I had a student researcher working on data analysis of all of the clickstream data we have captured over the last few years.  This was really interesting, and the results will hopefully lead to some good papers.  But, we barely scratched the surface of the analysis.  We did manage to do a good job of cleaning up the data.  If you are interested in doing analysis, let me know, and I will be happy to share the anonymized data set.  One thing we did learn, and are in the process of writing up, is that the error messages and hints that we added make a significant difference for the number of runs and amount of time it takes for students to complete homework programming exercises!


Looking Ahead
-------------

As with any successful project, one thing leads to another, and the list of things we **could** do grows ever longer than the things that **I have time to do do**.  So, what follows is my vision for where I would like to be at the end of 2015, I know I can't do this alone, but I'm hoping that by putting my vision out here I can convince some of you to join in the development.

Language Support
~~~~~~~~~~~~~~~~

I have been participating in a great discussion with Dirk Grunewald and Richard Lobb on our `google group <https://groups.google.com/forum/#!forum/runestoneinteractive>`_ about providing support for other languages.  Richard has an excellent project on github called `Jobe <https://github.com/trampgeek/jobe>`_ that provides exactly what I need on the backend to compile and run C, C++, Java, and even R programs.  With a bit of experimentation I've been able to get Jobe up and running, and the REST API seems simple enough that it would be possible to integrate into our activecode processing.  There are a number of challenges to make this a reality.

* Understand the CPU load that jobe will add.
* Understand the memory load that jobe will add.  It seems likely that this will require an upgrade or another machine since I'm close to my webfaction limit already.
* Figure out if we can use Jobe in a more stripped down/standalone mode.  Right now it requires Apache, and php, and a few other things.  Some of that is probably overkill for what we want to do.
* Modify the activecode directive and the bookfuncs.js runtime functions to use jobe in the background.

Code Coach
~~~~~~~~~~

This summer I introduced the Code Coach feature.  It has become quite popular for what it does.  Which is:

* Display the history of the development process.  Each time the student runs a program we capture the state of the source.  When the student presses the Code Coach button, he or she can browse the history and see the differences between each run.  I think this is a valuable tool for instructors to use when helping their students.  
* The second thing Code Coach does is display messages from `pylint` Pylint catches lots of mistakes that the python runtime does not.  For example, useless statements, like a function without parenthesis.

This bit of functionality was always intended to be a place holder for a much more intelligent automated tutoring system.  There are lots of people working on research related to understanding the paths that students following in solving a coding problem,  including `Elena Glassman <http://people.csail.mit.edu/elg/>`_, at MIT, who I met at the Learning@Scale conference last spring, and `Toby Dragon <http://faculty.ithaca.edu/tdragon/>`_, at Ithaca College, who is a user of the book, and `Chris Piech <http://stanford.edu/~cpiech/bio/index.html>`_ at Stanford.

The work that Elena and Chris are doing may allow us to detect that a student is headed down a path toward an unsuccessful solution.  If we can do that then perhaps we can intervene with some well timed hints, to get the student headed back in the right direction.

This is going to require a lot of computing horsepower, but with a data set of of 8 million runs of introductory CS problems to learn from, I think I have some interesting data for people to work with.

Integrated CodeLens
~~~~~~~~~~~~~~~~~~~

The CodeLens feature of the textbook is easily one of the most useful and educational elements in the Runestone arsenal.  Since the beginning I have been able to use this wonderful tool in offline mode to allow students to step through canned examples.  This summer I added a Run In CodeLens button that communicates with `Philip Guo's <http://www.pgbovine.net>`_ `Online Python Tutor <http://pythontutor.com>`_ which connects activecode examples and exercises to the live system.  This allows a student to step through almost any program she is working on.

However, this fall some huge advances were made on the `Skulpt Project <http://skulpt.org>`_ called Suspensions.  This new implementation of the runtime allows us to set breakpoints, and make the Skulpt implementation of Python truly interactive.  I believe that Suspensions will allow us to fully embed a Python Tutor like system in the textbook, thus distributing this processing to the browser as well.  

However, I recently re-watched `Bret Victor's <http://worrydream.com>`_ incredible `Inventing on Principle <http://vimeo.com/36579366>`_ video and I am convinced that with the advances in Skulpt, and Python Tutor, that we could realize this vision for an interactive editor.


Runestone Academy
~~~~~~~~~~~~~~~~~

And last, but not least Runestone Academy.  With book subjects expanding well beyond the realm of Python, the use of interactivepython.org as the main hosting site, is becoming increasingly inaccurate.  A new name for the main hosting site is in order. So, with thanks to my colleague, David Ranum, for the suggestion, watch for `runestone.academy` to launch sometime this year. However, even more important is that more and more people want the book to be integrated into a better system for managing grades, making assignments, notifying students of assignments, providing feedback, tracking progress, etc.  Although we have made some progress in these areas in the past year it has not been particularly cohesive.  There are systems out there that do some or all of this.  I am not interested in reinventing all of this stuff.   It would be a huge distraction from the central vision for the textbook authoring tools.  But, if we can leverage a tight integration with something like the edX platform, I think that would be a huge win.

So there you have it, It is a boatload of work.  My friend and colleague Paul Resnick made a comment to me last summer that has become a sort of guiding principle for my work.  That is "what thing can I work on that will add the greatest educational value for the largest number of students?"  I think all of these add a tremendous amount of value and I hope to see them all to fruition.  

Now I'm off to the Mediterranean for Spring semester with my wife and 12 Luther students.  This spring promises to push me out of my comfort zone and expose me to many new cultures and ideas.  I'll be posting on Reputable Journal often to keep friends and family apprised of our travel and adventure.   Hopefully I'll also be able to do some inspired hacking while enjoying the warmer climes. 

