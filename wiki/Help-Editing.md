**Copied from <http://meta.wikimedia.org/wiki/Help:Editing>**

**Editing** refers to the changing of a page by a Wikimedia user. Unless certain restrictions are in effect, such as [protection](Protection), all pages are editable, by everyone. This is a brief overview of that process. The editing table of contents to the right contains more information on editing functions.

## Most frequent Wiki markup explained

Here are the most frequently used types of wiki markup. If you need more help see [Wikitext examples](Help-Wikitext-examples).

\
{\| class="wikitable" ! style="width: 50%" \| What it looks like ! style="width: 50%" \| What you type \|- \| You can *italicize text* by putting 2 apostrophes on each side.

3 apostrophes will embolden **the text**.

5 apostrophes will embolden and italicize ***the text***.

(4 apostrophes don't do anything special -- there's just **'one left over**'.) \|

    You can ''italicize text'' by putting 2 
    apostrophes on each side. 

    3 apostrophes will embolden '''the text'''. 

    5 apostrophes will embolden and italicize 
    '''''the text'''''.

    (4 apostrophes don't do anything
    special -- there's just ''''one left
    over''''.)

\|- \| You should "sign" your comments on talk pages:

- Three tildes give your user name: [Example](User-Example) ([talk](User-talk-Example))\
- Four tildes give your user name plus date/time: [Example](User-Example) ([talk](User-talk-Example)) 07:46, 27 November 2005 (UTC)
- Five tildes give the date/time alone: 07:46, 27 November 2005 (UTC)

\|

    You should "sign" your comments 
    on talk pages:
    * Three tildes give your user
    name: ~~~
    * Four tildes give your user 
    name plus date/time: ~~~~
    * Five tildes give the 
    date/time alone: ~~~~~

\|- \| colspan=2 \|

### Section headings

\|- ! style="width: 50%" \| What it looks like ! style="width: 50%" \| What you type \|- \|

<div style="font-size:150%;border-bottom:1px solid rgb(170,170,170);">

Section headings

</div>

*Headings* organize your writing into sections. The Wiki software can automatically generate a [table of contents](Help-Section) from them.

<div style="font-size:132%;font-weight:bold;">

Subsection

</div>

Using more equals signs creates a subsection.

<div style="font-size:116%;font-weight:bold;">

A smaller subsection

</div>

Don't skip levels, like from two to four equals signs.

Start with 2 equals signs not 1 because 1 creates H1 tags which should be reserved for page title. \|

    == Section headings ==

    ''Headings'' organize your writing into sections.
    The Wiki software can automatically generate
    a table of contents from them.

    === Subsection ===

    Using more equals signs creates a subsection.

    ==== A smaller subsection ====
    Don't skip levels, 
    like from two to four equals signs.

    Start with 2 equals signs not 1 
    because 1 creates H1 tags
    which should be reserved for page title.

\|- \| colspan=2 \|

### Lists and indents

\|- ! style="width: 50%" \| What it looks like ! style="width: 50%" \| What you type \|- \|

- *Unordered [lists](Help-List)* are easy to do:
  - Start every line with a star.
    - More stars indicate a deeper level.
- Previous item continues.
  - A new line
- in a list

marks the end of the list.

- Of course you can start again.

\|

    * ''Unordered lists'' are easy to do:
    ** Start every line with a star.
    *** More stars indicate a deeper level.
    * Previous item continues.
    ** A new line
    * in a list  
    marks the end of the list.
    * Of course you can start again.

\|- \|

1.  *Numbered lists* are:
    1.  Very organized
    2.  Easy to follow
2.  Previous item continues

A new line marks the end of the list.

1.  New numbering starts with 1.

\|

    # ''Numbered lists'' are:
    ## Very organized
    ## Easy to follow
    # Previous item continues
    A new line marks the end of the list.
    # New numbering starts with 1.

\|- \|

  
A colon (:) indents a line or paragraph.

A newline starts a new paragraph.\
Often used for discussion on [talk pages](Talk-pages).

  
We use 1 colon to indent once.

  
We use 2 colons to indent twice.

  
3 colons to indent 3 times, and so on.

\|

    : A colon (:) indents a line or paragraph.
    A newline starts a new paragraph. <br>
    Often used for discussion on talk pages.
    : We use 1 colon to indent once.
    :: We use 2 colons to indent twice.
    ::: 3 colons to indent 3 times, and so on.

\|- \| colspan=2 \|

### Links

\|- ! style="width: 50%" \| What it looks like ! style="width: 50%" \| What you type \|- \| Here's a link to the [Main page](Home).

But be careful - capitalization counts! \|

    Here's a link to the [[Main page]].

\|- \| [Intentionally permanent red link](Intentionally-permanent-red-link) is a page that doesn't exist yet. You could create it by clicking on the link. \|

    [[Intentionally permanent red link]] is 
    a page that doesn't exist
    yet. You could create it by 
    clicking on the link.

\|- \| You can link to a page section by placing a "#" before its title:

- [Help:Contents#For editors](Help-Contents#for-editors).

If multiple sections have the same title, add a number. [\#Example section 3](#example-section-3) goes to the third section named "Example section". \|

    You can link to a page section by its title:

    * [[Help:Contents#For editors]].

    If multiple sections have the same title, add
    a number. [[#Example section 3]] goes to the
    third section named "Example section".

\|}

### Formatting

\|- \|

    Preformatted text

\|

    &lt;pre&gt;Preformatted text&lt;/pre&gt;

\|}

## Restrictions

Some pages cannot be edited by everyone. A special function known as [protection](Protection) can be applied to a page by [administrators](Administrator), making the said page uneditable to certain classes of users. There are several degrees of protection:

- If a page is semiprotected, it can be edited by everyone except IPs and accounts that have not yet been [confirmed](Autoconfirmation).
- If a page is fully protected, only other admins can make edits to the page.
- A page can also be protected so that it cannot be [moved](Move).
- In some cases, an admin might see fit to protect a page from being created.
- For very rare pages, such as the Main Page, "cascading" protection is applied, wherein every page that is [transcluded](Transcluded) onto a page is protected too.

There are various reasons why a page might be protected. Vandalism and spam can lead to semiprotection, while content wars and other severe cases can lead to full protection. There are other times where [Office actions](Office-actions) come into play. For the most part, protection is temporary and editing privileges are then restored. In any case, everyone can [view the source](View-source) of any page, irrespective of its level of protection.

## Further reading

### Editing help

- [Help:Editing FAQ](Help-Editing-FAQ)
- [Help:Editing toolbar](Help-Editing-toolbar)
- [Help:Minor edit](Help-Minor-edit)

### Wiki markups and codes

- [Help:Wikitext examples](Help-Wikitext-examples)
- [Help:Reference card](Help-Reference-card): a one-page summary of important commands, to be printed out and used next to the computer
- [Help:HTML in wikitext](Help-HTML-in-wikitext)
- [Help:Comment tags](Help-Comment-tags)
- [HTML elements](https://en.wikipedia.org/wiki/HTML_element): introduction to HTML
- [Help:Redirect](Help-Redirect) - Setting up a Redirect Page within Wiki

### Page management

- [Help:Starting a new page](Help-Starting-a-new-page)
- 
- 
- 

### [Additional Editing Tools](http://en.wikipedia.org/wiki/Wikipedia_tools)
