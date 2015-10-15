Version 3.0 of Runestone Interactive released
#############################################

:slug: runestone-interactive-3-0
:date: 2014/08/18 12:55:07 UTC
:tags: Python, Education
:link: 
:description: A new school year brings a new release of Runestone Interactive
:type: text

I'm pleased to announce that over the weekend, I updated `interactivepython.org <http://interactivepython.org>`_ to version 3.0.  This release completes another summer of hacking, and integrating contributions from colleagues around the world.

My plan in this post is to briefly summarize some of the highlights of the new release and then follow up over the course of this week with posts and screencasts about specific features. 


* **Progress tracking, and cohorts.**  This is one of the major visual changes to the books, thanks to some great work by `Vipul Thackur <http://www.ivipul.com>`_.  The "chapters" have been broken up into subchapters and you can now track your progress through each chapter/sub-chapter on the table of contents.  In addition, there is now the facility to create a study group and to negotiate reading deadlines and have discussions with members of your own cohort.

* **New and improved grading and assignments interface.**  Thanks to `Paul Resnick <http://presnick.people.si.umich.edu/>`_ and his students at the University of Michigan you can now group activities into assignments.  You can also provide comments to students on the programming problems.

* **Custom assignment page.**  As an instructor you can now easily edit an assignments page that is part of your custom course.  This page will allow you to make use of all of the features of the Runestone tools and restructured text to add your own assignments.  I think this feature has great potential to grow into additional custom content in the future so stay tuned.

* **Run in Codelens.**  Sometime earlier this summer `Philip Guo <http://www.pgbovine.net/>`_ added an iframe interface to the awesome Online Python Tutor.  This allowed me to add a button to most of the activecode examples that allow you to also run the example in the `Online Python Tutor <http://pythontutor.com>`_.  You can edit the examples and click the button to run another version.  This feature requires that you have internet access while reading, something I have resisted in the past, but it it seems increasingly difficult to be offline now anyway, so I'm not going to resist anymore.

* **Code Coach.**   Last spring at SIGCSE, Paul Resnick, David Ranum and I spent an afternoon hacking.  The idea was to provide an interface that would allow students to look at the history of any particular programming assignment, and see the differences from one try to the next.  Our hypothesis is that this would be a good teaching tool for an instructor to use with a student to review how they developed a solution and arrived at their current state.  I expanded on the concept a bit this summer by making use of pylint, which points out a number of potential problems that plague beginning programmers.  For example, pointing out "useless statements" when a student forgets their parenthesis on a function call.  My hope is that Code Coach will grow into a fully automated code tutor in the future.

* **Blockly directive.**   I think that blocks based programming languages like `Blockly <https://blockly-demo.appspot.com/static/apps/index.html>`_, and Scratch have great potential to help students develop a mental model or a picture in their mind of how various programming constructs work. So I created this new directive that will let you write blocks language examples and exercises.  My hope was to write a new introduction to How to Think Like a Computer Scientist using Blockly, but there are only so many hours in the summer.  Hopefully I'll make progress on this during the coming months.

* **Activecode support for Javascript and HTML.**  In preparation for a new course I'm teaching this fall, I wanted to be able to have students edit HTML and Javascript examples like we can do with Python.  Now you can.

* **New Book:**  `Programs, Information, People <http://interactivepython.org/runestone/static/pip/index.html>`_.  This book is a new mashup of the How to Think book that Paul Resnick uses in his course in the School of Information by the same title.  I think this is a great alternative to the How to Think book in that it avoids some of the "early math" problems and focuses on information processing using data from the internet.

* **AP Java Review:**  `This book  <http://interactivepython.org/runestone/static/JavaReview/index.html>`_ came on line last spring, but its worth mentioning in this summary.  `Barbara Ericson <http://www.cc.gatech.edu/people/barbara-ericson>`_ at Georgia Tech has put this together and although we can't run any Java examples in the browser the rest of the interactive resources are great for getting ready for the AP exam.

Well, thats the overview.  I look forward to bringing you the details over the next week.  In the meantime, you can see some of the features on the `Overview site <http://interactivepython.org/runestone/static/overview/overview.html>`_  I'm sure we will see a few glitches as these new features move out of beta testing and into general use. Please report them on our `github page <http://github.com/bnmnetp/runestone>`_ or send me an email.



