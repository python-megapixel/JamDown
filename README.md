# What's a Jamstack?
The fundemental idea of a Jamstack is that it doesn't rely on the web server generating a web page in real time in response to each request. Instead, content is pre-built into static pages, which are generated at the time the site is deployed rather than when it is requested. For simple sites, this can be faster and more secure, and is far lighter on webserver resources which means companies like [Netlify](www.netlify.com) offer pretty generous hosting of Jamstack sites for free or at low cost.

# What does JamDown do?
JamDown is a simple tool to harness one of the most important advantages of real-time page generation - standardised templates across the entire site. The problem with manually building each page of your site individually is that if you want to edit something that applies to multiple pages then you must edit all of those pages one-by-one.

What JamDown does is takes the actual content of a page, incorporates it into a template as specified by various configuration files, and adds styling information, producing a single HTML file. This process is hereafter referrred to as "building". It can do this for an unlimited number of pages very quickly, to create an entire Jamstack site, usually in a very short amount of time. If you need to change something across the entire site, it's a matter of just editing one file, building the site again, and you're done.

JamDown is designed to operate in a very simple, but very configurable, manner.

# Do I need technical knowledge?
Yes, but not much. You should be able to get a reasonably good site working using the setup tutorials provided here (which involve deploying your site to Netlify) if you...

+ have a basic knowledge of HTML and CSS
+ feel comfortable navigating Github
+ feel comfortable with the idea of configuration carried out by editing files (rather than some graphical thingamajig)
+ are able to write content in Markdown (and if you don't, don't worry, it's the simplest thing ever, [this short page probably contains all you need](https://www.markdownguide.org/cheat-sheet/))

# How can I get started?
Head over to [this project's wiki](https://github.com/python-megapixel/JamDown/wiki) and follow the instructions. Don't worry, it's very simple.

# Can I use this to build my own site?
Yes.
*__Note:__ A credit and link back to this page somewhere on the site would be appreciated, but is not required.*

# Can I do [something else]?
Maybe. Please check [license.txt](https://github.com/python-megapixel/JamDown/blob/master/license.txt).
This project is licensed under the GNU Affero GPL 3.0.
