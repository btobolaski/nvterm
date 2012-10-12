This is like [nvalt][1], except:

- It runs from the terminal
- It should run on any system that python works on(hopefully)

Right now, it is only a command that you run at the command line. 
	
	nvterm.py [options] search_string

Options:

	-d, --directory	the notes directory(defaults to ~/Dropbox/Notes)
	-e, --editor	the editor that you would like to use to open up the matching notes(defaults to gvim)

I plan on making an interface similar to [nvalt][1] that works in the terminal in the future. Right now, nvterm searches through all of the files in the directory each time you run the command. I&rsquo;m looking to cache the files in a database to speed up the search, although the search is lightning quick for me, but I don&rsquo;t have that much to search through right now.

If you feel like contributing and are looking for ideas on what to help with, take a look at the todo.taskpaper document(if it exists), it will contain everything that I think needs to be implemented.
If you have an idea for something else, great, go ahead and do it.

This software is under the BSD License.
Look at license.txt for the text of the license.
If you have a particular need of this software under a differenct license, contact me and we will work something out.

[1]:https://github.com/ttscoff/nv