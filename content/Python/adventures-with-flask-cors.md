Title: adventures with flask-cors
Slug:  adventures-with-flask-cors
Date:  2015/05/24
Tags:  python, runestone
Link: 
Description: getting cors to work with my new architecture
Type:  text

As I am working through the new architecture for the [Runestone Interactive server][1] I wanted to make sure that I had my authentication model working right from the beginning. The goals for the architecture are as follows:
*  I want people to be able to write and host the static parts of any book on any server.  You can think of each page in a book as its own single page application.
* I want to provide back-end services so that students using any book hosted anywhere can save their programs and answers to quizzes etc.
* I want to continue to gather research data on how students learn computer science.
* I want to make the registration and login process as easy as possible.
Since the static parts can be hosted anywhere (including a site like [interactivepython.org][2])  The interactive parts are going to involve making cross-domain XMLHttpRequests (xhr).  Of course the first thing that happens when you have a page hosted on `static-site` that makes an xhr request to `ajax-server` is that you get an error.   Browsers and sites work together to disallow cross-domain requests to prevent a variety of nasty behaviors.  But, there are many times (wlike now) when you have a legitimate reason for doing this.  So, the w3c created the Cross Origin Resource Sharing (CORS) standard to help developers get around this.  Cory Dolphin has created an excellent plugin for [Flask][3] developers called [Flask-CORS][4].  The plugin is a great example of the brilliant design behind Flask and in fact the entire WSGI stack.

## The Really Simple Approach
The first thing you find when you start googling about this problem is that there is a seemingly simple solution.  If you have control over your AJAX response you simply need to add an HTTP header `Access-Control-Allow-Origin: *`  problem solved.  Now everyone in the world can make xhr requests to your server and use the results in their page.

Adding a header is pretty simple in Flask.  All you need to do is use `response.headers.add("Access-Control-Allow-Origin", "*"`   Problem solved, moving right along to the next programming challenge.

Or maybe not.   Minutes later you realize that this is not all that great because you have decorated some of your requests to require a login.  That wont be a problem if the static page is served from the same domain because you will automatically get the session cookie, and the Flask-Security extension will eat that cooking and validate things for you.  BUT if your static page is not served from the same domain you will not even get the session cookie.  Oh Bother.  But you also have a second problem.  You have probably violated the CORS specification without even meaning to.  Really, if I had to read the spec for every web standard I wanted to use I would seriously think about changing careers.  But, **here is the important part** you may not return a CORS header unless the request contains an origin header!  Chances are you tested you change with a quick `curl` call to your endpoint, saw the Access-Control header and were happy.  But you sure didn’t give it an origin header on the request when you did that.  So to summarize, we have two problems we need to solve:
1.  We want to incorporate authentication into our cross origin strategy.
2.  We want to be good citizens and follow the spec.

## The Smart Approach
The smart approach is to use a nice extension where _other_ people have figured this out, and presumably followed the specification. Enter Flask-CORS.  You can enable CORS support with a simple decorator `@cross_origin`  This will automatically add the  `Access-Control-Allow-Origin: *` to responses.  **As long as your test request includes an Origin**.  If you are like me you will forget that part, and then wonder why the extension must not be working.  So this solves problem 2.

To solve problem 1 here is a snippet of code that works just fine.

	@ajax.route('/ajax/page')
	@login_required
	@cross_origin(supports_credentials=True)
	def test():
	    return jsonify({'foo':'bar'})

The above responds to the url `/ajax/page`  I have all of my API calls in an `ajax` blueprint with ajax as part of the url.  I’m requiring that the user is logged in before I allow them to access this endpoint.  I also want it to be allowed cross origin.  This is where the parameter to the `@cross_origin` comes into play.  Supports credentials sets up the CORS response to return an additional CORS header:  `Access-Control-Allow-Credentials:  "true"`.  For one final twist, you need to know that when you have `supports_credentials=True` you may NOT set `Access-Control-Allow-Origin: *`  You need to be specific and set the origin to the origin that comes in the request headers.  To Make this work and try it out from the client side, here is a bit of HTML/Javascript.
 
	<button onclick="corsTest();">TestCORS</button>
	
	<script>
	    function corsTest() {
	        var xhr = new XMLHttpRequest();
	        xhr.withCredentials = true;
	        xhr.onload = function () {
	            alert(xhr.responseText);
	        }
	        xhr.onerror = function () {
	            alert("error");
	        }
	
	        xhr.open("GET", "http://example.com/ajax/page", true)
	        xhr.send()
	    }
	</script>

Note that you need to set `xhr.withCredentials` in order for your session cookie to be sent along.  By default cookies are NOT sent with cross origin requests.

Now, I may end up adding more to this as I discover the intricacies of so called “Non-Simple” requests.  That is requests beyond simple GET and POST, as I work on moving my API toward a RESTful API which uses PUT and others.  This will nodoubt enlighten me about preflighted requests.  Which I can only assume means something different than sitting around in an airport bar waiting for your flight to be called.

There is a lot more detail and background on using CORS at the following two sites:

* [The Mozilla Developer Network][5]
* [Flask-CORS documentation][6]




[1]:	http://github.com/bnmnetp/runestone/wiki/DevelopmentRoadmap
[2]:	interactivepython.org
[3]:	flask.pocoo.org
[4]:	http://github.com/corydolphin/flask-cors
[5]:	https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
[6]:	http://flask-cors.readthedocs.org