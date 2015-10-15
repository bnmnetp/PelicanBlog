Title: runestone interactive announces new editions of interactive textbooks
Date: 2013/08/14
Slug: runestone-interactive-announces-new-editions-of-interactive-textbooks
Tags: python
Link: 
Description: 


<p>Today I'm really pleased to announce that  have launched version 2.0 of our interactive computer science  textbooks:</p>
<ul>
<li><a href="http://interactivepython.org/runestone/static/thinkcspy/index.html">How to Think Like a Computer Scientist:  Interactive Edition 2.0</a>  (CS 1)</li>
<li><a href="http://interactivepython.org/runestone/static/pythonds/index.html">Problem Solving with Algorithms and Data Structures using Python</a>  (CS 2)</li>
</ul>
<p>We first launched these books on our <a href="http://interactivepython.org">interactivepython.org</a> website in May of 2012, after around a year of private testing in the classroom.  Since then we have had 1.3 million page views by a quarter of a million unique visitors.  Daily, we get around 2,000 unique visitors.  Not bad for a site with zero dollars for an advertising budget.</p>
<h2>What Makes these Books Unique?</h2>
<p>These books are unique because they are interactive.  We have developed a set of authoring tools that make it really easy to write an interactive textbook with many interactive features.  We call these the Runestone tools.  Some of the interactive features that are possible include:</p>
<ul>
<li><strong>Activecode</strong>:  Using a <a href="http://skulpt.org">Javascript implementation</a> of Python you can run and modify the examples in the textbook right in the book.  No server connection is required since it is based on javascript and runs right in the browser.</li>
<li><strong>Codelens</strong>:  Using the amazing power of the <a href="http://www.pythontutor.com">pythontutor.com</a>  tools you can step through examples one line at a time, forward and backward.  While you are stepping through the code you can see variables and other data structures change values.</li>
<li><strong>Parsons Problems: </strong> For beginning programmers Parson's problems are like refrigerator magnet poetry.  You can provide your students with the statements needed to write a program, but they must put the statements in the correct order.</li>
<li><strong>Inline Quizzes: </strong>Each section of the book contains some inline quizzes that allow students to check their understanding of the material.  The quizzes have different feedback for each correct or incorrect answer that try to point students in the right direction. </li>
<li><strong>Online Homework:</strong>   At the end of each chapter are programming assignments.  In this new edition we have provided the answers to the odd numbered questions, and discussion forums for students to exchange ideas or ask questions about the homework problems.  As an instructor, you can grade your students programs on one convenient page.</li>
<li><strong>Highlighting</strong>  This is another much requested new feature.  Students can highlight text using the mouse and the highlights magically reappear on any supported browser.  In addition we will remember the students last location in the book and offer to return them to that position when they return.</li>
<li>There are many other features but the best way to understand what we are doing is to actually have a look at our <a href="http://interactivepython.org/runestone/static/overview/overview.html">overview page</a>, which shows everything I have mentioned here and a lot more in action.</li>
</ul>
<p>Over this past year we have discovered that we serve two different audiences with these books.</p>
<ul>
<li>Instructors looking for a textbook to use in their own course</li>
<li>People who are interested in teaching themselves some computer science and have found our books through google search, the Python wiki, or some other word of mouth source.</li>
</ul>
<h2>Textbooks as a Service</h2>
<p>When we launched the site last year we decided to not only provide the books free and open for anyone who wanted to read them, but also as a service for instructors who wanted to have their own custom copy of the book where they could track their students progress, review their answers to quizzes, and grade their students homework.   If you want to use our books in your class you are welcome to do so.  You have two options:</p>
<ol>
<li>You can use a copy of either book as is with the order of the chapters just as they are on the books linked to above.</li>
<li>You can try our custom interface where you can mix and match chapters from both books to create your own custom textbook.</li>
</ol>
<p>Once you have created your own course then you will be able to see the assignments your students have completed right in the textbook.  I find this to be very valuable as an instructor.  For example if I have assigned the students to read and do the quizzes for a particular section, I can simply go to the quiz question and click on the 'Compare Me' button.  As an instructor I will see a summary of the answers my students gave, as well as the details of the answers that each student tried.</p>
<h2>Supporting the Independent Learner</h2>
<p>Perhaps the biggest surprise of this project is the number of people that have found one of the books through google, and are simply teaching themselves to program.  We are hopeful that some of the new features we have added will help foster a  community of learners so that people just learning to program can talk to others in the same situation.  Some things we hope are particularly helpful include:</p>
<ul>
<li><strong>Answers to odd numbered questions</strong>.  This was probably the number one request I got through email all last year.  How do I know if I did it right?  We decided to risk it and provide the answers, but only to the odd numbered problems.  In addition a student must try to answer the problem at least once before the answer becomes "unlocked"</li>
<li><strong>Discussion threads</strong> for homework problems.  Again this may seem like a risky move where students can just publish their answer and others can copy.  But, what we are hoping for is that students will see that there are many ways to get to the "right answer"  There are different approaches and programming styles that can be used to solve the same problem.</li>
<li><strong>Compare Me</strong>  Although we aren't sure about the title on the button, the idea is that after answering one of the quiz questions a learner can check on their overall 'grade' for all quiz questions, and see how their answer compared to all the other learners.  We haven't gone so far as to give out badges, but we think this is a nice intermediate approach.</li>
</ul>
<h2>The Runestone Tools</h2>
<p>The books above were built using our <a href="http://runestoneinteractive.org">Runestone Interactive</a> toolkit.  These tools are freely available on <a href="http://github.com/bnmnetp/runestone">github</a>.  If you want to write your own interactive book, or even just use the tools to create some interactive labs for your students you are welcome to do so.  You can write your materials in an easy to use markup language called restructuredText and add examples or quizzes using very simple tags.  Complete documentation for our extensions to restructuredText is provided on the website.  In addition to our own books, the team at Harvey Mudd College has published <a href="http://www.cs.hmc.edu/csforall">CS for All</a>  another introductory textbook using our tools.  I know of at least two other books in progress!  </p>
<p>If you are interested in following our development or getting involved You can do so in several ways:</p>
<ul>
<li>Twitter, follow <a href="http://twitter.com/iRunestone">iRunestone</a></li>
<li>Facebook, <a href="https://www.facebook.com/RunestoneInteractive">facebook.com/RunestoneInteractive</a></li>
<li>Google <a href="https://groups.google.com/forum/#!forum/runestoneinteractive">Groups</a>  </li>
</ul>
<h2>Acknowledgements</h2>
<p>I am grateful to the many people who have provided us with feedback over the last year.  And I am especially grateful to the ACM SIGCSE social projects committee for providing me with a special projects grant that allowed me to work with a student (Isaac Dontje Lindell) this summer.  He did a ton of work and will be graduating next year.  You should hire him.  In addition this project relies on many open source components which I will mention and link to below.</p>
<ul>
<li>The original text for<em> How to Think Like a Computer Scientist</em> comes from Allen Downey, Jeff Elkner and Chris Meyers.  We have modified it a lot, but without a starting point for us to experiment with our interactive ideas this project never would have taken off.</li>
<li>The <em>Problem Solving with Algorithms and Data Structures</em> text is published as a paper textbook by Franklin Beedle and Associates.  Without the forward thinking of Jim Leisy this book would be stuck.  Thankfully Jim freed us to use the text in an interactive form online.</li>
<li>Mark Guzdial, Barbara Ericson and the rest of the <a href="http://home.cc.gatech.edu/csl/CSLearning4U">CSLearning4U</a> research group at Georgia Tech have provided questions, assessments,  and many other features and ideas.</li>
<li>The <strong>Activecode</strong> examples are made possible by <a href="http://skulpt.org">skulpt</a></li>
<li>The <strong>Codelens</strong> examples are made possible by Philip Guo and his <a href="http://www.pythontutor.com">pythontutor.com</a></li>
<li>The look and feel of the book is based on the <a href="http://getbootstrap.com/">bootstrap</a> templates</li>
<li>The system that builds the website from source is called <a href="http://sphinx-doc.org">Sphinx</a> and is really the backbone of the system that allows us to write our interactive extensions.</li>
<li><a href="https://github.com/vkaravir">Ville Karavirta</a> wrote the original js-parsons library and Mike Hewner integrated it into the Runestone Tools.</li>
</ul>
