Title: getting unicode right in python - nick's blog
Date: 2010/11/16
Slug: getting-unicode-right-in-python-nick-s-blog
Tags: 
Link: 
Description: 


<div class='posterous_autopost'><div class="posterous_bookmarklet_entry"> <blockquote><div>    <h3>Getting unicode right in Python</h3>  <p>  Posted by Nick Johnson    | Filed under    <a href="http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python#">python</a>,    <a href="http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python#">text</a>,    <a href="http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python#">unicode</a>,    <a href="http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python#">rant</a>      </p>  <p>Yup, I'm back from holidays! Apologies to everyone for the delayed return - it's taking me a long while to catch up on everything that built up while I was away.</p>    <p>Proper text processing - specifically, correct handling of unicode - is one of those things that consistently confounds even experienced developers. This isn't because it's difficult, but rather, I believe, because most developers carry around a few key misconceptions about what text (in the context of software) is and how it's represented. A search on StackOverflow for <a href="http://stackoverflow.com/search?q=unicodedecodeerror">UnicodeDecodeError</a> demonstrates just how prevalent these misconceptions are. These misconceptions date back to the days before unicode - longer than many developers have been in the industry, including myself - but they're still nothing if not widespread. This is in part because a number of well known and popular languages continue to, at worst, perpetuate the misunderstandings, and at best are insufficiently good at helping developers get it right.</p>    <p>We can divide languages into four categories along the axis of unicode support:</p>    <ol>  <li>Languages that were written before unicode was defined, or widespread. C and C++ fall into this category. Languages in this category tend to have unicode support that's spotty, not built into the language, or difficult to use correctly, making the path of least resistance the wrong one, more often than not.</li>  <li>Languages that should know better. These languages were written after unicode was already widespread, but managed to get things horribly wrong. They have all the weaknesses of category 1, without the excuse of age. Prime amongst these, in my experience, is PHP, though there are doubtless many more languages that do just as badly.</li>  <li>Languages that get it basically right, but have a few critical flaws. Languages in this category are 'modern' and understand unicode, but fail to make the path of least resistance for developers the correct one, which results in some serious shortfalls in unicode support for things implemented in these languages. Python 2.X, to my dismay, falls into this category - more about which, later.</li>  <li>Languages that Get It Right. They support unicode, and they make it easy to do the right thing, and hard to do the wrong thing. Java and the .NET platform both fall into this category.</li>  </ol>    <p>So what's the deal with unicode, and how are we getting it wrong? Joel's post, <a href="http://www.joelonsoftware.com/articles/Unicode.html">the absolute minimum every software developer absolutely, positively must know about unicode</a> is an excellent place to start for this, but for the sake of brevity and those who are naturally impatient, I'll summarize.</p>    <h3>Characters and bytes</h3>    <p>The essential fact that you <b>must</b> understand in order to handle text properly is the abstract concept of a character. A character is a representation of a single symbol in a piece of text - a platonic ideal, of sorts. Crucially, a character is <b>not</b> a byte. Let me repeat for emphasis: A character is <b>not, not, not</b> a byte. Furthermore, there's no single way of representing a given character as one or more bytes - as I said, a character is the platonic ideal of the smallest unit of text.</p>    <p>Unicode, then, is a way of defining a set of characters that everyone can agree on. It consists of a huge database of characters, and each one is associated with a unique number, called a code point. Thus, the english letter capital A has the codepoint U+0041. The euro symbol has codepoint U+20A0, and so forth. A text string is simply a series of these codepoints, representing the character for each element in the string.</p>    <p>Of course, sooner or later, you need a way to store and transmit your platonic unicode strings. It helps if you choose a method that other people can understand, so that you can send text to them, and they to you, in a mutually comprehensible fashion. This is where character encodings come in.</p>    <p>A character encoding defines a mapping between our platonic characters and some way of representing them as bytes. The mapping doesn't have to be complete - it may have no way to represent certain characters - and it doesn't need to use the same amount of space for each character - some characters may be encoded as a single byte, while others may require several.</p>    <p>Because there are many ways of representing the same character as bytes, this means that if you have a series of bytes, but do not know their encoding - even if you know the data is textual - the data is meaningless. You can guess, but you'd be doing just that, guessing. In short, <b>bytes are not text</b>. If you forget everything else in this article, remember that. In order to read and write text, you must first know the encoding you are using, whether from of convention, out of band information, or any other mechanism.</p>    <h3>How Python handles unicode</h3>    <p>This is where Python's unicode support comes in. In Python's type heirarchy, there are three distinct string types: 'unicode', which represents unicode strings (text strings), 'str', which represents byte strings (binary data), and 'basestring', which acts as a parent class for both of the other string types. This is where, in my opinion, Python makes its misstep in handling unicode which pushes it into category 3, instead of category 4, by my definition above.</p>    <p>As I've just spent several paragraphs belabouring, bytes and characters are fundamentally different entities, only interconvertible with the help of a character encoding. Python, unfortunately, does its best to help you forget this, with two separate missteps:</p>    <p>The first is of debatable significance: treating sequences of bytes as strings. It's arguable whether or not this is a good thing; Java and .NET support the proposition that it's not, while other languages make good arguments in the other direction. In any case, it's certainly true that certain operations you might want to preform on text strings - regular expression matching, string replacement, and so forth - don't entirely make sense on sequences of bytes. Python, though, treats bytes as just a different type of string, and allows the same set of operations on both.</p>    <p>The second misstep is the more significant one: Python's attempt at transparently converting between byte strings and character strings. In a variety of circumstances, Python will attempt to convert a byte string to a unicode string or vice-versa, when the situation warrants - for example, when attempting to concatenate a byte string and a unicode string together. Since, as we've previously detailed, conversion between the two types is meaningless without an encoding, Python relies on a 'default encoding', specified by sys.setdefaultencoding(). On most platforms, this defaults to ASCII, and it's almost certainly wrong for any given conversion. Other places this encoding is used include calls to str() or unicode() without specifying an encoding yourself, and functions that expect one type of string but are passed the other.</p>    <p>One solution to some of your unicode woes, then, would be to call sys.setdefaultencoding(), setting the default encoding to whatever you ought to be using. This only masks the root problem, though, which is your failure to handle text correctly in the first place. It may also be impractical, since many apps, particularly webapps, may have to deal with multiple different text encodings in different places.</p>    <p>The correct solution is to fix your code so that you handle text correctly. Here's the cliff's notes on what you should be doing:</p>    <ul>  <li>All text strings, everywhere should be of type unicode, not str. If you're handling text, and your variable is a str, it's a bug!</li>  <li>To decode a byte string as text, use var.decode(encoding) (eg, var.decode('utf-8'), with the correct encoding. To encode a text string as bytes, use var.encode(encoding).</li>  <li>Never ever use str() on a unicode string, or unicode() on a byte string without a second argument specifying the encoding.</li>  <li>Whenever you read data from outside your app, expect it to be bytes - eg, of type str - and call .decode() on it to interpret it as text. Likewise, always call .encode() on text you want to send to the outside world.</li>  <li>If a string literal in your code is intended to represent text, it should always be prefixed with 'u'. In fact, you probably never want to define a raw string literal in your code at all. For what it's worth, though, I'm terrible at this one, as I'm sure pretty much everyone else is, too.</li>  </ul>    <p>Python 3, by the way, fixes things, and gets unicode and string handling right, putting it solidly into category 4. See <a href="http://docs.python.org/release/3.0.1/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit">this section of the What's new page</a> for details.</p>    <p>Hopefully this made sense, and if you had any doubts about what exactly unicode is and how to handle it, they're now cleared up. Next time you get a UnicodeEncodeError or UnicodeDecodeError in your app, then, you'll know exactly what's gone wrong, and how to fix it!</p>  <p>  <span>21 July, 2010</span>  </p>    <a href="http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python#">Previous Post</a>      <a href="http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python#">Next Post</a>        <h3>Comments</h3>  <p>      <a href="http://disqus.com/forums/notdot-blog/?url=ref">View the discussion thread.</a>  <a href="http://disqus.com">blog comments powered by <span>Disqus</span></a>      		</p></div></blockquote>    <div class="posterous_quote_citation">via <a href="http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python">blog.notdot.net</a></div> <p>Good article on the issues you encounter when working with strings and unicode in Python.</p></div></div><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/2759017781463016019-8099313241295933953?l=blog.bonelakesoftware.com' alt='' /></div>