Development Tips
################

:slug: development-tips
:date: 2014/05/06 11:14:28
:tags: 
:link: 
:description: 
:type: text

Development Tips
================

I have been writing programs since I was in 9th grade, that would be 
35 years (Yikes!)  I have more than put in my 10,000 hours to attain 
some level of mastery, but I like to think of it as wisdom.  Studies 
have shown that there can be huge differences in the ability level of 
even the most experienced coders.  More than a factor of 20, in some 
cases! I think beginning and intermediate CS students really struggle 
with this.  They see some of their classmates streaking on ahead of 
them effortlessly writing lines and lines of code.  But for them its 
a constant struggle.  I've watched some of my students really struggling 
with the latest homework assignment, and I felt compelled to write down 
some "words of wisdom" to try and help them through the rest of the semester.


I have been lucky enough to work with some of the best developers in the world
during my career.   Here is a summary of  some tips and things that I have
observed.  I practice all of these things in my own development work, and you
should too.  In my opinion there is no more valuable advice than the 
first section on Incremental Development. But, I would love to hear 
from friends, and former students.  What tips would you give beginning 
to intermediate students on writing software?

.. TEASER_END

Incremental Development
~~~~~~~~~~~~~~~~~~~~~~~

#. **Think before you code**.  Before you sit down and start coding, try
   drawing a picture that illustrates your objects, and the
   relationships between those objects.  Its important to understand not
   only the basic functionality of each object, but how they interact.
#. **Make a plan**.  After you have an idea of the big picture now make
   a plan for what you want to do first, second, etc.  Nothing is more
   satisfying than knowing you have been productive.  I have known CEOs
   of companies that delight in creating a hand-written todo list each
   morning, for no other reason than crossing something off the list
   gives them a little boost of joy and keeps them going through the
   day.  Everyone likes that feeling of being productive.  Making
   progress on your plan makes you feel productive, and motivates you to
   keep going.
#. **Start Small**.  Start with a small class, for example die, and
   write a little test program to make sure that the die class is
   working properly.  
#. **Test as you go**.  Nothing frees you up to work on the next thing,
   like knowing you can build on something you have already completed.
    Doing a good job of testing is what gives you that freedom.  I know,
   it is tempting, to look at a small class and read the code and simply
   assume that it works.  Most of the time this is a bad assumption,
   even in simple examples.
#. **Use Stubs.**  Even in a relatively small class it is tempting to
   try to implement all of the methods and then compile.  This may not
   be a very good idea.   What you can do is write a stub for each
   class.  For example if you have a method for your cup called shake,
   and you are not ready to write everything in shake just make a
   function called shake with an empty body.  This will compile fine,
   but it won't do anything.  If your method is supposed to return a
   value, you may need to have it return some bogus value for the time
   being.
#. **Build on success**.  Once you have one class working then go on to
   the next.  Test that class, and test its interaction with the class
   or classes that came before it.
#. If you still have classes to write GOTO 3
#. Integrate your classes and write your main, but again, **start
   small**.  Don't try to add everything at once.  For example in the
   Yahtzee command line game, start with the roll command and make sure
   you can roll all of your dice.  Then add each command one at a time.
#. **Always keep a working program working.**  Notice that if you use
   this approach you always have something that compiles and runs that
   you can hand in.  Even a simple example program of a die class with a
   die that you can roll is worth more points that nothing at all, or a
   program that simply does not compile.

Use The Tools
~~~~~~~~~~~~~

#. Early on in the development, you should create a directory for this
   project.  This keeps everything together and reduces the clutter.
#. Use git.  -- Start right away with a git init in your directory, and
   commit your changes often.   This always gives you a road back.
#. Use a Makefile
#. When debugging, make sure you sprinkle in plenty of cout statements.
    If you are getting unexpected seg faults, use gdb to find out where
   the program is crashing.
#. For goodness sake, use the internet.  Stackoverflow is your friend.
   cplusplus.com is your friend,  You should **not** feel like you ought
   to have command of everything off the top of your head.  Maybe after
   several years of C++ programming you will have all of the options
   memorized, but until then, use the documentation.  Even googling
   large parts of a compiler error message may lead you to a solution.


Debugging
~~~~~~~~~

#. **Talk it out.**  Either to yourself, or even better, to someone else
   The number of times that I sit in my office and simply ask a student
   to explain their code to me is amazing.  Very often, while that 
   explanation is in progress a lightbulb goes on, and the student
   sees the problem.  I wish it was because of my mystical professorial
   powers, but more often than not it is by telling someone else that
   we are forced to...
#. **Confront your assumptions.**   Way too often we are conviced our
   code is correct because we don't see what we actually wrote.  In most
   cases we see what we think we wrote.  By explaining to someone else
   we are forced to see what we actually put in the file.  In some 
   extreme cases I find that students are convinced that there must 
   be some other evil force in the universe that is causing their 
   program to fail, becuase they have done everything right.  This 
   has never been the case yet.  The programs that we write for class
   are not going to be the programs that find new bugs in the C++ compiler
   or the Python programming language.
#. Sometimes you just can't beat good old fashioned **pen and paper style
   tracing.** In this world of fast turnarounds, instant compiles, and fancy IDE's
   we too often get caught up in making quick changes to the program just
   to see if that fixes the problem.  Usually this is just masking some
   logic error or assumption we are making.  Pen and paper style tracing
   is another way to force our minds into focusing on what is there 
   instead of what we assume is there.

Those Pesky Compiler Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Yes, C++ error messages are voluminous, cryptic, and downright
   frustrating in many cases!!  There's nothing you can do about that.
   except:
#. Did I mention you should start small.  If you write your code in
   small chunks, and compile frequently this will reduce the number of
   compiler errors, and will help you focus on where the error is likely
   to be.. *Hint*:  in the new stuff you have just written.
#. **Be systematic.**  If the code compiled two minutes ago, and you have
   just added three new lines of code, and now it does not compile you
   should have a pretty good idea of where the error was introduced.
#. **Start with the first error!!**   Its tempting to look at the error
   message at the end of the list. because thats what you see as soon as
   the compiler is done.  But, scroll back and start with the first one.
    Many of the errors later on are the result of an error at the start.
    If you focus on fixing the wrong error, you are likely wasting your
   time.
#. **Pay attention to the parameters and their Types**.   Very often the
   questions I get boil down to the fact that someone is trying to call
   a function but is passing a parameter of the wrong type.  Some words
   and phrases to pay attention to that may help you identify these
   errors:   "candidate function not viable" ,  "no known conversion
   from  XXXX to YYY"
#. **Use redirection!**  Sometimes its hard to find the first error.
    You can change your compile command, or run it manually and send the
   output to a file.  For example: g++ -c cup.cpp > compile.out 2>&1
#. Sometimes the best way back is to comment some things out.  If you
   have followed the **start small** philosophy this should not be an
   issue.  But maybe you didn't and now you have a big pile of code that
   doesn't compile.  Once again you need to break it up some how.
    Sometimes the way to do this is to comment out a big chunk of your
   code and see if the error goes away.

Dealing with Complexity
~~~~~~~~~~~~~~~~~~~~~~~

#. There is no doubt that the programs we write in this class are more
   complicated than any you have ever written.  Often by an order of
   magnitude or two.  This can feel overwhelming, and is yet another
   reason for you to go back and reread the first section of this
   document again.
#. **Embrace Abstraction.** At the time you are creating a die class you
   may feel its a waste of time.  Why not just a variable that we assign
   a random number to?  Or the cup class, why not just use a vector?
    But as the project progresses you will see that using the
   abstraction has some  huge benefits:

   #. It makes the interesting parts of your code much more readable.
   #. It reduces the amount of repetition you need to do.
   #. If you follow good practice, it gives you confidence that the
      little things in your program are working correctly.

#. Learn and embrace the KISS (keep it simple stupid) principle.  Too 
   often I see people making things way harder than they need to be.
   You don't have to reinvent the wheel for every assignment.  Learn 
   to reuse code from previous assignments.
#. Part of dealing with complexity is having some confidence that what
   you have done is correct.  Working in small chunks, and testing in
   small chunks helps you develop that confidence.
#. The tools we have talked about in this class are there to help you
   deal with complexity.  Make, gdb, grep, and others are there to make
   your life better.
#. Don't worry if you feel like you don't know everything.  having
   knowledge available to you comes after time, and frequent practice.
    You are not going to be there after one semester.


