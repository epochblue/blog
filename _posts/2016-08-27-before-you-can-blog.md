## Behind the Blog

Like any good software developer, before I started this blog I wasted an enormous amount of time writing the [engine behind it](https://github.com/epochblue/nanogen).
Well, not an _enormous_ amount of time, but more than the zero minutes I should have wasted given that blogging is a solved problem.
So why did I do it?

I have a number of reasons, but when you get right down to it, I did it because I could and because I wanted to.
I don't use a lot of software I write myself.
Most of what I write is written for `$EMPLOYER`, and used somewhat sparingly in my personal life.
This was an opportunity to write a simple bit of software and then actually _use it_ regularly.


Ironically, given how simple the project is now, the hardest part of the project for me was keeping it simple.
My first attempt was an engine that was little more than a worse version of [Jekyll](http://jekyllrb.com).
It had the YAML front-matter, and the templates, and the themes, and it supported posts as well and pages, and it was much more than what I wanted or needed.
I was letting my ideas that other people would want to use this get in the way of building the thing _I_ wanted.
So I dialed it back as much as I could: no themes or configuration, minimal templates, and no YAML front-matter.
All the engine really does is process Markdown files into HTML and throw that content into a few templates it expects to find in specific places.
It doesn't ship with a theme, and it doesn't even support pages that aren't blog posts.
This scratched an itch for me, and it was fun.
And that's enough.

I call my engine [`nanogen`](https://github.com/epochblue/nanogen).
Feel free to use it if you'd like.

