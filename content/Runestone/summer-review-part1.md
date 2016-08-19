Title: Runestone Summer Review Part I
Date: 2016-09-19
Slug: runestone-summer-review-part-i
Tags: Python, Runestone
Link:
Description: A look back at a very productive Summer

With just about 10 days until classes start, my focus must switch to prep, teaching, and the inevitable committee and faculty meetings.  But I wanted to take some time to document a few highlights of the summer.  One of the biggest highlights is a redesigned instructor interface for Runestone, that is so big that I'm going to save that one for Part II.  In the meantime it is in beta and I encourage you to take a look.

If you are new to the Runestone Interactive project you might want to watch this podcast I did with my colleague Philip Guo at the University of San Diego.  [PG Podcast - Episode 11](http://pgbovine.net/PG-Podcast-11-Brad-Miller.htm)

## New Books in Runestone by people I didn't know

Ok, it is happening!  Other people outside of a very small circle are starting to write new chapters for *How to Think* and even their own books using the Runestone components!  This is what I had hoped for all along, and it is starting to happen.  All of the authors would say that these are "works in progress"  and I think that is a sign of whats good about the interactive textbook approach.  You can write a book as you are teaching the course.
Here are some examples:

1. [Learn WebGL](http://learnwebgl.brown37.net/) Dr. C Wayne Brown of the Air Force Academy has published this very cool book on learning computer graphics with WebGL.  We talked one day about some contributions he had for improving the How to think book and told me about this!  Wow!
2. [Transforming Data with ClojureScript](https://yardsale8.github.io/stat110_book/)  Yeah, you read that right, not only did J. David Eisenberg of Evergreen Valley College write this book, but also integrated ClojureScript as a new language into the Runestone Components.  He also wrote this cool [Regular Expressions in Python](http://evc-cit.info/comsc020/python-regex-tutorial/)
3. [Intro to stats](https://yardsale8.github.io/stat110_book/)  This one, by Dr. Todd Iverson of St. Mary's University is not even a computer science book, its a statistics textbook.  I'm really looking forward to seeing how this progresses as I think it will give us lots of ideas for new components.
4. There are also a few other instructors out there who are writing their own custom chapters for their books.  They are using them in their own classes and are not quite ready to share them with the world yet.  If you fall into that camp yourself, read on...

The full library of books (that I know about) written using the Runestone Tools is [In our Library](http://runestoneinteractive.org/library.html)   

If you have written something, please let me know!

## Jenkins Integration

With more people writing more books that we want to make available on Runestone.  Not to mention the instructors who are testing new modules in their own courses, I set up a Jenkins CI server.  If you have a project like this that you would like to publish on Runestone let me know.  As long as you have your content set up as a Runestone project on a github repository, I can set up a task on Jenkins to monitor your repository and automatically rebuild and deploy your book whenever you push a change to github.

I'm excited about what I've learned here, and I'm hoping to use what I've learned to make the book building and hosting process better going forward.


## Numbered Sections

Well this may seem trivial, but it took a few years before it dawned on me how to make it happen. It is also a feature that many people have asked for for a long time! I won't go into the gory details here but you can see it on github in the source or [read this summary](https://github.com/RunestoneInteractive/RunestoneComponents/issues/238)

## Unit Tests

It is really easy now to add unit testing to problems in the textbook.  These unit test allow your students to try their solutions and get immediate feedback based on test cases you have created.  I really like this, as I think it is quite motivating for the students as well.  We added a bunch of these to the thinkcspy book early in the summer, and I'm going to be doing the same as I teach my data structures course this fall.

## More to Come

One sign of a good project is that the todo list never gets shorter.  Every time I cross two things off the list six more pop up.  I'm really excited about a bunch of things, especially polishing up the new instructor interface and a brand new directive that we are working on to help students better [visualize Python's evaluation process](http://inventwithpython.com/showeval/)
