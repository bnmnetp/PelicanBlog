On the Denial of Service Attack
###############################

:slug: on-the-denial-of-service
:date: 2014/07/21 21:55:17 UTC
:tags:
:link:
:description:
:type: text

Well its been an interesting week. My daughter is married, and I've been caught in the crossfire of a Distributed Denial of Service (DDoS) attack on Webfaction, my hosting provider. I'm quite sure the two are unrelated.

For those of you who have been frustrated in your attempts to access any of the books on interactivepython.org, I'm sorry. We were not the target of the attack, but we were in the same subdomain and got blasted. I can't believe that it took over four days to clear up the mess. But thats about what happened. This is a new one for me. I've never considered that an open source textbook project would have to worry about something like this. At one point Webfaction said they were getting 4Gbps (yes, 4 gigabits per second) of malicious traffic affecting about a dozen machines.

I've been so frustrated with Webfaction's response that I've been thinking about moving to a different hosting service. But I'm left with the following questions:

1. Could Webfaction done better? The only thing I'm qualified to say here is that they could have done way better in communicating with those of us affected. Here was the initial response I got from tech support:

  > There is no ETA as to when this issue will be fully resolved as only the attacker(s) can determine that. At times the target against a server can be large enough that our hardware mitigation system can not handle the volume. Please let us know if you need anything else.

Ok, maybe dealing with a DDoS is a really hard problem, but as a frustrated owner of the site here is what I heard. "Sorry, nothing we can do. You will just have to wait until the bad guys get tired and go away." In addition, it was maddeningly long between their status updates. You can see their updates here As a site owner, all I want to do is get my site back up and running. In order to make good decisions about what to do I need timely information, not vague intermittent messages.

2.  What are standard practices in building web applications to protect against an attack like this?

3.  How do you know whether one hosting provider is going to be any better than another in dealing with an attack like this? Is paying for AWS or Google compute engine the only way to know you are getting a provider with the resources to take on a big attack?
If you have answers to these questions, please leave a comment.
