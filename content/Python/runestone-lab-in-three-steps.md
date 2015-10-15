Title: writing a runestone lab the easy way
Date: 2015/05/06
Slug: how-to-make-a-lab-in-three-easy-steps
Tags: python, runestone, tutorial
Link: 
Description: new packaging and a new command should make this easy

## Background

As part of the grand reorganization of the various tools and software associated with the [Runestone Interactive][1] project I am planning to also write a series of tutorials to help people get started.  The major aspects of this reorganization are discussed in detail in the [Project Roadmap][2], but for the sake of some context I can summarize the major efforts as follows:

1.  Separate the distribution and development of writing tools from the server.
	1.  Make a pip installable runestone package.
	2. Remove the interconnectedness between the components and Sphinx.  In other words support the user of runestone tools in environments like Markdown, and even wysiwyg html editors.

2. Re-architect the server side focusing on services for the writing tools
	1.    Create an authentication service that supports CORS for cross domain AJAX use.
	2.    Create a standard REST API for logging and storing student data

3.  Create a web application (or integrate with another) for grading

Since I just completed Part 1.1 I thought it was a good time to talk about how easy it is for you to now use the runestone tools for creating a lab for your students, or lecture notes and presentation materials for your class.

## Getting Started

The major steps in getting started are 

* Installing Python
* Installing the runestone tools
* Building your first lab

### Install Python

1.  If you are on a Mac you are already done with this step.
2.  If you are on Windows you will need to go to [Python.org][3] and download Python3.x.   The windows installer is a typical installer and you can just click your way through it.

If you are an advanced Python user you may want to may want to create a `virtualenvironment` for this project but it is not a requirement.

If you are on Windows you may want to edit your PATH environment variable following the instructions [here][4].  Again, mac users can ignore this.

### Installing the Runestone Components

You are going to need to use the command line for the rest of this tutorial, so start up a [Terminal][5]   (/Applications/Utilities on a Mac  or run [PowerShell][6] or cmd.exe on Windows)  I will repeat myself here.  These commands need to be run from the command line, **not** from the Python shell.

Run the `pip` command

	$ pip install runestone

Or on Windows if you have not modified  your PATH try:

	C:\\Python34\Scripts\pip.exe install runestone

From now on I'm only going to give the Mac way of running the commands.  If you are on windows you will need to add `C:\\Python34\Scripts` to the beginning of the command and add `.exe` to the end.

You can watch as a lot of text goes scrolling by.  But as long as you don't get any errors you should be good to go.  You only need to do these first two steps once.  Once you have installed Python and runestone you will not have to do it again.

### Starting your first Runestone Project

Here is a session of me on my computer creating a simple project.

	$ mkdir mynewproject
	$ cd mynewproject
	$ runestone init
	
	This will create a new Runestone project in your current directory.
	Do you want to proceed?  [Y/n]: y
	Next we need to gather a few pieces of information to create your configuration files
	Project name: (one word, no spaces): myhello
	path to build dir  [./build]:
	require login   [false]:
	URL for ajax server  [http://127.0.0.1:8000]:
	Your Name  [bmiller]: Brad Miller
	Title for this project  [Runestone Default]: My Hello World
	Log student actions?  [True]: False
	Done.  Type runestone build to build your project

At this point you will have the following files and folders:

	mynewproject/
	        _static/
	        _sources    
	        _templates  
	        conf.py
	        pavement.py

* The `_static` folder is for things like images or javscript files.
* The `_sources` folder is where you will put your own writing.  To start with there are a couple of examples files for you.
* The `_templates` folder is for styling.  There is a default set of templates that match the runestone interactive look and feel.  That is a good thing to start with.  Once you become more familiar with the system you may want to customize the templates or even make your own.
* The `conf.py` file is used by Sphinx, and contains information from some of the questions you answered when you initialized your project.
* The `pavement.py` file is used for building and setting build parameters.

All of these files are important, and you should not delete any of them.

Next run `runestone build`  This command will create a build/mynewproject folder with an index.html file in it.  If you want you can now run `runestone serve` and then go to your browser and open up the following URL  `http://localhost:8000/index.html`   Yay!  You have a webpage.  Feel free to explore a bit to get an idea about some of the components you can use in your lab.

### Writing your Own Lab

OK, lets edit  `_sources/index.rst`   Initially it looks like this:

	=====================
	This Is A New Project
	=====================
	
	
	SECTION 1: Introduction
	:::::::::::::::::::::::
	
	Congratulations!   If you can see this file you have probably successfully run the ``runestone init`` command.  If you are looking at this as a source file you should now run ``runestone build``  to generate html files.   Once you have run the build command you can run ``runestone serve`` and then view this in your browser at ``http://localhost:8000``
	
	This is just a sample of what you can do.  The index.rst file is the table of contents for your entire project.  You can put all of your writing in the index, or as you will see in the following section you can include additional rst files.  those files may even be in subdirectories that you can reference using a relative path.
	
	The overview section, which follows is an ideal section to look at both online and at the source.  It is pretty easy to see how to write using any of the interactive features just by looking at the examples in ``overview.rst``
	
	
	SECTION 2: An Overview of the extensions
	::::::::::::::::::::::::::::::::::::::::
	
	.. toctree::
	   :maxdepth: 2
	
	   overview.rst
	
	
	SECTION 2: Add more stuff here
	::::::::::::::::::::::::::::::
	
	You can add more stuff here.
  

If you are not familiar with markup languages, this file should still be quite readable to you, and you can probably easily guess what most things do.  Runestone uses a markup language called restructuredText.  There is a very nice, short tutorial [here][7].  

To give you an idea of what you see in the example above,  the section that starts with `.. toctree::` is called a directive and it creates a table of contents for you.  the `maxdepth` part sets the table of contents to show sections and subsections.  And the line with `overview.rst` indicates that it is a file that should be included in the overall  web page.  More on all of this later. Our first task is simply going to be to wipe everything out, and start over.   Using a plain text editor change index.rst to look like this:

	=============
	My Sample Lab
	=============
	
	Part 1: Turtle Graphics
	=======================
	
	In this section we will do the following:
	
	* Create a turtle
	* Make the turtle draw a box
	
	.. activecode:: turtle1
	
	   import turtle
	
	   timmy = turtle.Turtle()
	   for i in range(4):
	       timmy.forward(100)
	       timmy.right(90)
	
	
	Now it is your turn.  Can you modify the program to make timmy draw an octagon instead of a square?

Now save the file and rerun the `runestone build` command.  Everything should build without a problem and you can now run `runestone serve` and open up `http://localhost:8000` from your browser.  Notice that you can change the program and rerun it right from your browser. 

It is probably obvious that you can create headings and subheadings.  Unordered lists are created using `*` and the runnable code examples are created by the `.. activecode::`  directive. The name turtle1 must be unique on the webpage, other than that it is not used for too much at this point.  The rest of the activecode directive contains plain old python code, but it must be indented to line up with the `a` in `activecode.`  All indented lines are included as the body of the activecode directive, regular text processing starts at the first unindented line.

There you have it.  You have created a very nice little lesson without a lot of hassle.  The Runestone and Sphinx tools take care of all of the formatting for you!

## Giving Students Browser Access to the Lab

If you have your own webpage hosted on a school server that you normally use for class you can make your Lab available to the students by simply taking the folder `mynewproject` inside the `build` folder and putting that on your website.  The folder is self contained and can be hosted on any web server.  

If you know the IP Address of your own computer and you simply want to give let students bring up the webpage from your computer you can do that too.  For example, lets suppose you know that your IP address is `10.0.0.23`  Your students can get everything they need from `http://10.0.0.23:8000/index.html`

### Coming Soon

There are many free web hosting solutions out there and you can also choose one of them and upload your project folder for hosting there.  I'll cover at least one of them in another tutorial.  In fact I think I see a whole series of tutorials in the future on topics such as:

* Making an online quiz for class
* Making a lecture or presentation 
* Hosting your lab or quiz on **github pages** or another online service
* Using your lab with runestone services


[1]:	http://runestoneinteractive.org
[2]:	https://github.com/bnmnetp/runestone/wiki/DevelopmentRoadmap
[3]:	http://python.org
[4]:	https://docs.python.org/3.4/using/windows.html
[5]:	http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line
[6]:	http://www.tomshardware.co.uk/faq/id-1656450/windows-powershell-feature.html
[7]:	http://getnikola.com/quickstart.html