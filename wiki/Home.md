/\* Main page hacks. Remove default "Main Page" header \*/ var mpTitle = ""; var isMainPage = (document.title.substr(0, document.title.lastIndexOf(" - ")) == mpTitle); var isDiff = (document.location.search && (document.location.search.indexOf("diff=") != -1 \|\| document.location.search.indexOf("oldid=") != -1));

if (isMainPage && !isDiff) { document.write('\<style type="text/css"\>/\*\<\![CDATA\[\*/ \#siteSub, \#contentSub, h1.firstHeading { display: none !important; } /\*\]\]\>\*/\</style\>'); }

<big>**MediaWiki has been successfully installed.**</big>

Consult the [User's Guide](http://meta.wikimedia.org/wiki/Help:Contents) for information on using the wiki software.

## Getting started

- [Configuration settings list](http://www.mediawiki.org/wiki/Manual:Configuration_settings)
- [MediaWiki FAQ](http://www.mediawiki.org/wiki/Manual:FAQ)
- [MediaWiki release mailing list](https://lists.wikimedia.org/mailman/listinfo/mediawiki-announce)
