Adventures of an Expat Cord Cutter
##################################

:date: 2015/02/19
:slug: Cutting-the-Cord
:tags: Travel, Tech
:link: 
:description: 

Even thought I'm living abroad and traveling for an extended period there are a few entertaining parts of my life I'm not willing to leave behind.  Watching Arsenal, keeping up with The Big Bang Theory, The Blacklist, Food Network, and a few others.  How you do this is well covered territory.  You can probably figure it out with several google searches,  but it seems worth it to collect my own efforts into one cohesive post.  Here are the problems to solve:

1. How to stream TV shows that have geographic restrictions.  Lots of content is available only inside the borders of the USA. 

2. How to get the content off of your small screen and onto a larger screen if you are lucky enough to have one.

3.  How to optimize your WiFi and streaming throughput in the midst of an urban WiFi jungle.

Warning.  This is a geeky technical post.  You can quit here and I won't feel bad.

Streaming
---------

There are lots of options for streaming from places like Hulu, Netflix, and even the big four major networks all have apps now that let you stream more or less of their content.  When we left home, I had NBCSportsLive Extra, Netflix, HBO Go, DirectTV all installed on my iPad.  I also have iTunes, and had downloaded a few movies that I had on my list to watch.  In the United States this would be fine, but all of these apps (except iTunes) have geographic restrictions on them.  So I also had to subscribe to a Virtual Private Network (VPN) service and configure that on my iPad.

VPN
~~~

If you are not familiar with a VPN you can think of it as a bit of software that messes around with your network configuration to make the rest of your computer and the rest of the world think that you are a part of some other network.  This is often used in large organizations where you have content that you restrict to your own institutional network.  Luther does this with some resources, like our network drives.  Other services, such as O'Reilly's Safari, may check to make sure that you are coming from a particular network before you are granted access to their own content because of a corporate licensing agreement.  If you have a VPN connection back to your institutional network then it is just like you are in the office and not at home or halfway around the world.

Now the reason this is important for my entertainment is that there are many VPN services that exist partly for the purpose of making it look like you are connected to a network in the United States somewhere rather than a network in Vietnam or Malta.  I signed up with `Private Internet Access <http://www.privteinternetaccess.com>`_ These services also have the side effect that your content is encrypted from the time it leaves your computer until it leaves the VPN provider, which many people look at as a significant privacy benefit.  Using a VPN to trick NBC into thinking that I am in the united states might be considered a moral gray area, but I'm still paying my DirecTV, and Mediacom bill every month back home every month so I don't have any problem going to sleep.

The VPN solution works pretty well, except for some content providers have figured out how to identify these VPN servers, and have made moves to block the connections from known VPN providers.  I'm looking at you ABC.  

This content blocking thing is interesting, especially from companies like ABC that force you to watch commercials as part of their streamed offering.  Why wouldn't they want more eyeballs on their commercials?

To the Big Screen
-----------------

Once we got settled in our flat in Malta, I decided I wanted to upgrade the streaming experience by adding an AppleTV to the TV in our flat.  With this setup, I can use Airplay to send the content from my iPad to the larger screen we had set up in our living area.  Except that it doesn't work.  The AppleTV has no provision for joining a VPN.  There are some ugly hacks that involve jailbreaking your AppleTV but I didn't want to go there.  I'd rather install more iPad apps for streaming FoodTV, Fox Sports, and several others that I've added to the list since we arrived.

Here is our Entertainment center in our flat in Sliema.

.. image:: /images/Malta/entertain.jpg

DNS
~~~

The Domain Name Service is at the heart of the Internet.  If you haven't been subjected to my days of DNS in Networking class, you can think of it like a phone book for the entire world.  Of course its way more fun and complicated than that.

So what does DNS have to do with this particular problem?  Well, when you want to contact a website or stream some video, you need to look up the address of the server that authenticates you, **and** checks to see that that address is in the right country.  You find the address by contacting your friendly local DNS server.  You normally don't have to worry about this because your home router takes care of it.  But, it is an easy thing to customize.  It turns out that these video streaming services use one server for authentication, and a different server for video streaming.  

With me so far?  Now there are companies that provide DNS services to replace the DNS provided by your friendly neighborhood Internet Service Provider.  For example Google runs DNS servers that you can use.  They are really reliable, and of course keep track of all the addresses you look up to better inform their search algorithms I suppose.  However, if google wasn't trustworthy, you could ask them for the address of company X, and they could lie to you so you connected to company Y.  

In order to avoid a full VPN, and to make it easier for helping iPads, iPhones, and AppleTVs get around the geographical restrictions there are some companies that are running their own DNS servers that will in fact lie to you about the server you connect to for the authentication part of setting up a video stream. This little setup is actually called a **proxy.**  So when you ask for the address of the ABC authentication server you don't connect to ABC you connect to one of the servers run by `UnoTelly <http://www.unotelly.com>`_.  UnoTelly sits between you and the authentication server and passes on your information.  But since the UnoTelly server is in the United State, ABC thinks you are in the United States too.  With the authentication taken care of UnoTelly gets out of the way and allows your AppleTV to connect directly to the streaming server.  So far the UnoTelly servers remain blissfully below the radar of content providers everywhere.  Yay technology.  Also, DNS is very easy to customize even on your AppleTV.

This is a silly arms race between the VPN Providers, the DNS providers, and the content providers.  Hopefully this will sort itself out in a saner fashion sometime soon.  In the meantime its likely that every time the content providers find one way to block some clever software engineer will figure out a way around the block.  It reminds of of disk copy protection software in my younger days.  No matter what scheme a software company came up with to block copying, someone would figure out a way around it.

Optimizing your Streaming
-------------------------
Which brings us to our final problem.  How to optimize your streaming in the WiFi jungle.  The flat we live in is in a very densely populated area. My WiFi Scanner program shows between 15 and 20 different access points depending on the time of day and day of the week.  With this many access points there is a lot of interference because everyone is trying to use a rather narrow band of the radio spectrum at the same time.  Although WiFi is divided up into 11 different channels, there are really only 3 of the channels that don't overlap and interfere with nearby channels.

So the best solution is actually to use wired internet if you can.  luckily my AppleTV and my Router sit right next to each other, so its easy to plug in.  Even when I am using Airplay from my iPad to send something to the AppleTV the stream ends up coming directly through the wire rather than over WiFi.

If you can't plug in, then you might think that the thing to do is to choose a channel that isn't being used by one of your neighbors.  It turns out that most routers use channel 1 or 6 or 11 by default.  So your first thought might be to use 2 or 5.  But that will actually make the problem worse, because 1 and 2 will be unaware of each other and just make interference.  The counter intuitive solution is to pick the same channel as your neighbor with the strongest signal.  This way the normal Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) algorithm can actually do its work.  Yep, CSMA/CA is another day of networking class, but now you can throw that around like your an expert the next time someone brings up WiFi.

So with all of this, we have a pretty good setup.  I can catch up on shows on all of the major networks, I can stream English Premier League Football, and FA cup, and Champions league. I can watch FoodTV, and of course we can watch anything that is on the AppleTV.  Just last night we finally got around to watching the Theory of Everything.  Of course some times are better than others, and some providers are better than others.   AppleTV is top notch all the time.  I always get a good stream on anything I watch on any of the apps on the AppleTV.  Sadly its the sports streaming FoxGo, and NBCSports Live Extra, that seem to fall down.  I don't know if they are not built out enough to handle the worldwide demand, or what the deal is.  But there is a lot of season left, so I hope they keep on improving.

When I get back home I probably will not remain a cord cutter.  Too much content still relies on me having my DirecTV password to show that I am paying for it. To often, I have to play technical support person in the middle of a show to restart the stream.  But it does make me wonder about our lake house.  Do we really need two DirecTV subscriptions, especially for the amount of time we spend watching TV there, and with our Fiber Optic connection just around the corner, the bandwidth we'll have for streaming in the middle of Wisconsin lake country will be quite amazing.


