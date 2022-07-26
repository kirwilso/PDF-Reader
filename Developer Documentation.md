# Developer's for PDF File Reader 

External documentation (i.e. the developer's guide)

I realize that for some of you, the question who is the user and who is the developer may not be clear cut, e.g. your actual user could always be another developer. In this case, the rule is: put simple stuff in your user's guide and complex stuff in this programmer's guide. Obviously you can point across documents if needed. Or maybe your dev guide holds everything and your user's guide just pulls out the most important parts. Point is, that the user's guide ReadMe.md  will be your "portal" to your project to get started, but for more complex stuff, just point to the separate dev guide.
This programmer's guide should go over all the big picture software stuff of your project. Think of it as the doc that a new developer, who is tasked to take over your project, will read to get up to speed.

The structure of your guide doc obviously depends on the complexity and nature of your project but here are some suggestions:
Overview (in which you can re-use material from your sketch or the user's guide)
Condensed version of the final(!) planning specs, i.e. which parts of the initial specs are actually currently implemented. 

Install/deployment/admin issues:
Assume that the developer has already read your user's guide, knows how to run your app and has your project installed. If there are additional things that the dev (but not the user) needs to do or know (e.g. to run as admin, configure something first, install other stuff, deploy the server in a specific way, watch out for that) - this is the place to mention them!  

(End) User interaction and flow through your code ("walkthrough")
Start be a brief(!) recap of what the flow of the user interaction is. If you didn't talk about the UX aspects earlier, mention them here. This should include screenshots where needed.
Now, think about what happens at each step of the flow in your code. Describe, which classes, functions, etc. are involved. You can be as specific as you like here, but assume that the dev is also looking at your code while reading this, so no need to literally "cite" code, unless you think it's a vital snippet.
However, should certainly mention the names of classes, functions (and in which module they can be found) and any hierarchies that are put  into (class inheritance, multi-level modules (packages), etc.)
It maybe be useful to use graphics to illustrate some aspects of your explanation. This could be something like class diagrams or flow diagrams or even just simple tables.

Known Issues: You should mention any issues you know about (or suspect)
Minor: anything that's a minor bug (non-breaking) that could easily be fixed given some time
Major: anything that will break, how to possible work around it and maybe how to fix it
(These could also come up in a user-centric, UX, UI context!)
Optional: Mention any known or suspected computational inefficiencies. This could be something that worked OK for your (small) data set but would be impractically slow or memory-hungry if deployed in the real-world. Or something you used a pure Python solution for but that could be done better with a C-wrapper that's using the GPU instead.

Future work:
Here you can offer some insights into how your project could be expanded. Maybe there were some points in your initial spec that you didn't get to. Or maybe, during development, you found that you could also do something cool ... but didn't have the time or resources to do it.
Optional: if you talked about inefficiencies, speculate how you could potentially solve them, given more time and money.