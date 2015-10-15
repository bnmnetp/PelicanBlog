Organizing your Runestone Course
################################

:date: 2015/08/14
:slug: Organizing-your-Runestone-Course
:tags: Python, Runestone
:link: 
:description: Editing your table of contents lets you provide a syllabus all in one place

With the latest release of the Runestone Tools for this Fall I added a feature that will allow you to edit the table of contents file for your course.  This lets you do two really nice things:

1.  You can move chapters around and/or remove sections that you are not going to cover.
2.  You can provide a Syllabus and assignment notices right on the index page for your course.

To do this you need to click on one of the two links provided in the instructors dashboard.  Your two options are:

* Customize Chapter Order (thinkcspy only) If you have a course created before July 21 2015 and want this feature contact me.
* Customize Title Page and Order (all others)

The first link is for any course based on How to Think Like a Computer Scientist. This book has its own link because the initial page of that book has the swirly turtle program on it, and the table of contents is in a different file.

The second option is for all other books which have their table of contents in the usual `index` file.   If you are using the How to Think book this link will let you edit the page that has the swirly turtle program on it.

Clicking on either of these links will bring you to a little text editing window where you can edit the restructuredText for the appropriate page.  Yeah, this is a little like coding, there is no WYSWIG version of this, just a nice simple markup language.   So, to add a Syllabus or a Weekly assignments section to this page you can add something like this:

.. code-block:: rst

   ---------------------
   Readings and Homework
   ---------------------
 
   Week of Sept 3
   ~~~~~~~~~~~~~~
 
   * **Friday:**  :doc:`WWW/intro`, `exercise 1 <HTML/exercises.html#ex_html_1>`_  and 2
   * **Saturday:** sleep in
 
   Week of Sept 8
   ~~~~~~~~~~~~~~
 
   * **Monday:** Read :doc:`HTML/intro` and :doc:`HTML/basic`

If you are completely unfamiliar with markup languages like Markdown and restructuredText you may want to check out this `restructuredText Primer <http://sphinx-doc.org/rest.html>`_.  

There are a couple of nice things to point out.  The `:doc:\`foo/bar\`` syntax allows you to create a link directly to the page you want your students to read.  Its pretty friendly because all you have to do is look at the table of contents (in the file you are editing) and copy/paste what you want them to read.  Note that you do need to remove the `.rst` suffix.

You can also link directly to any exercise in the book using the following syntax:  `\`Some Title <Chapter/exercises.html#id_of_exercise> \``

You will find id of each exercise in parenthesis in the caption of each exercise at the end of the chapter.  In fact this will work for any *activecode* in the book not just in the exercises sections.

If you don't want the assignments to clutter up your table of contents page you can modify the above example to something like this:

.. code-block:: rst

   .. reveal:: syllabusreveal
      :showtitle: Show Syllabus
      
      * Week of Sept 3
        
        * **Friday:**  :doc:`WWW/intro`, `exercise 1 <HTML/exercises.html#ex_html_1>`_  and 2
        * **Saturday** Sleep in
        

This will hide the syllabus until they click on the button.

If you want to add your own custom problems you can do that by clicking on the "Edit my Assignments" link.   I'm seriously considering renaming that link to Edit my Homework Problems.  The identifiers that you give your exercises in that document can be linked to just like the exercises anywhere else in the book.

Don't forget that once you have edited any of these files you need to click on the rebuild link to get a new version of the book posted on line.

Any Questions?


**UPDATE**

With an hour or so of hacking I have fixed the runestone directives so that you can now reference an active code much more simply.  the above example can now be

.. code-block:: rst

   Do :ref:`Exercise 1 <ex_html_1>`   
   
All of the identifiers you use, and can see in the captions can now be cross referenced by providing a label, and then using  the identifier of the activecode inside the < and >.
