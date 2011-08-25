# Developing Maintainable Software

This page is a place holder for a future Thursday Night Presentation.

**You really shouldn't read this, yet.**

Here are some initial ideas for topics:

- Finding defects early means less overall effort
  - language selection (e.g. c++ vs objective-C, scripted languages vs compiled languages)
  - compiler options (strong typing, ZERO warnings, etc)
    - examples: SQLite
    - anecdote: turning on warnings and forcing errors: found latent defects, forced co-workers to write better (i.e. NON sloppy) code
- style
  - pretty printers
  - stupid IDEs (e.g. tabs, line endings, etc)
- \#defines vs inlines and debugging
- [Hungarian Notation](http://en.wikipedia.org/wiki/Hungarian_notation#Disadvantages)
- parent keyword for classes
- pass by reference vs pass by address, const references
- use const!
- stdint.h
- boost libraries
- stl
- consistency of style (again? so soon?)
- modularize, make code manageable. There should be a limit to the number of lines in a given file.
- function size: fit on a screen.
- document / doxygen is it.
- let the compiler find problems:
  - typing
  - avoid setting default values, have the compiler tell you when a garbage value might get used (this is a defect)
  - avoid default in switches
