Title: hosting a web2py app in the cloud
Date: 2012/01/26
Slug: hosting-a-web2py-app-in-the-cloud
Tags: python
Link: 
Description: 


<p>I consider myself pretty up to speed on web development.</p>&#13;
<p>I’ve spent the last two days trying to find a hosting solution for the data structures eBook…. I looked at too many of the following:</p>&#13;
<ul><li>Google App Engine — I’m a long time GAE user, but the setup I have uses sphinx to generate content on the fly which it wants to store in pickle files on the local file system.  This doesn’t work with a GAE and some other systems that treat the file system as read only and expect any writing you do to go to a database.</li>&#13;
<li>heroku — seems very promising, but I’m not sure how to configure web2py so it doesn’t need any local file system write access.  The lack of ssh access is a bit disconcerting.</li>&#13;
<li>dotcloud — seems promising but the app kept hanging for no discernible reason.  I fought with it for the better part of the afternoon before deciding to move on.</li>&#13;
<li>fluxflex — easy to get web2py installed, (1 minute)  but a real pain to try to work with a real app.  I’m not going to use the web interface for all my editing.  I want to git push and/or git pull to deploy and update the app.  It doesn’t seem possible to get both ease of installation and robust configuration management.</li>&#13;
<li>pythonanywhere - non-starter</li>&#13;
<li>webfaction — Its not free, but at least it has a command line I can work with and I’ve got the whole thing running.  The only confusing thing about webfaction is that they don’t list web2py as a supported framework, but when you type it in under other it magically works for  you….  The other annoying thing that I <em><strong>just</strong></em> discovered is that the 256MB limit is way too low for the default configuration.  I just now got a helpful email saying a support ticket had been opened for me because I was using too much memory.  This was like 15 minutes after I finally got my app running and I’d made about 5 page requests.</li>&#13;
</ul> 
