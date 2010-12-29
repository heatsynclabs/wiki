You can format your text using wiki markup. This consists of normal characters like asterisks, single quotes or equal signs which have a special function in the wiki, sometimes depending on their position. For example, to format a word in *italic*, you include it in two pairs of single quotes like `''this''`.

## Text formatting markup

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th><p>Description</p></th>
<th width="40%"><p>You type</p></th>
<th width="40%"><p>You get</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="background:#ABE"><p>character (inline) formatting – <em>applies anywhere</em></p></td>
</tr>
<tr>
<td><p>Italic text</p></td>
<td><pre><code>&#39;&#39;italic&#39;&#39;</code></pre></td>
<td><p><em>italic</em></p></td>
</tr>
<tr>
<td><p>Bold text</p></td>
<td><pre><code>&#39;&#39;&#39;bold&#39;&#39;&#39;</code></pre></td>
<td><p><strong>bold</strong></p></td>
</tr>
<tr>
<td><p>Bold and italic</p></td>
<td><pre><code>&#39;&#39;&#39;&#39;&#39;bold &amp; italic&#39;&#39;&#39;&#39;&#39;</code></pre></td>
<td><p><strong><em>bold &amp; italic</em></strong></p></td>
</tr>
<tr>
<td><p>Escape wiki markup</p></td>
<td><pre><code>&amp;lt;nowiki&gt;no &#39;&#39;markup&#39;&#39;&lt;/nowiki&amp;gt;</code></pre></td>
<td><p>no ''markup''</p></td>
</tr>
<tr>
<td colspan="3" style="background:#ABE"><p>section formatting – <em>only at the beginning of the line</em></p></td>
</tr>
<tr>
<td><p>Headings of different levels</p></td>
<td><pre><code>= Level 1 =
== Level 2 ==
=== Level 3 ===
==== Level 4 ====
===== Level 5 =====
====== Level 6 ======</code></pre>
<hr />
<p><em>Note:</em> An article with 4 or more headings automatically creates a <a href="https://en.wikipedia.org/wiki/Wikipedia:Section">table of contents</a>.</p></td>
<td><h1 id="level_1">Level 1</h1>
<h2 id="level_2">Level 2</h2>
<h3 id="level_3">Level 3</h3>
<h4 id="level_4">Level 4</h4>
<h5 id="level_5">Level 5</h5>
<h6 id="level_6">Level 6</h6></td>
</tr>
<tr>
<td><p>Horizontal rule</p></td>
<td><pre><code>Text above
----
Text below</code></pre></td>
<td><p>Text above</p>
<hr />
<p>Text below</p></td>
</tr>
<tr>
<td><p>Bullet list</p></td>
<td><pre><code>* Start each line
* with an [[Wikipedia:asterisk|asterisk]] (*).
** More asterisks gives deeper
*** and deeper levels.
* Line breaks&lt;br /&gt;don&#39;t break levels.
*** But jumping levels creates empty space.
Any other first character ends the list.</code></pre></td>
<td><ul>
<li>Start each line</li>
<li>with an <a href="https://en.wikipedia.org/wiki/asterisk">asterisk</a> (*).
<ul>
<li>More asterisks gives deeper
<ul>
<li>and deeper levels.</li>
</ul></li>
</ul></li>
<li>Line breaks<br />
don't break levels.
<ul>
<li><ul>
<li>But jumping levels creates empty space.</li>
</ul></li>
</ul></li>
</ul>
<p>Any other first character ends the list.</p></td>
</tr>
<tr>
<td><p>Numbered list</p></td>
<td><pre><code># Start each line
# with a [[Wikipedia:Number_sign|number sign]] (#).
## More number signs gives deeper
### and deeper
### levels.
# Line breaks&lt;br /&gt;don&#39;t break levels.
### But jumping levels creates empty space.
# Blank lines
&#10;# end the list and start another.
Any other first character also
ends the list.</code></pre></td>
<td><ol>
<li>Start each line</li>
<li>with a <a href="https://en.wikipedia.org/wiki/Number_sign">number sign</a> (#).
<ol>
<li>More number signs gives deeper
<ol>
<li>and deeper</li>
<li>levels.</li>
</ol></li>
</ol></li>
<li>Line breaks<br />
don't break levels.
<ol>
<li><ol>
<li>But jumping levels creates empty space.</li>
</ol></li>
</ol></li>
<li>Blank lines</li>
</ol>
<ol>
<li>end the list and start another.</li>
</ol>
<p>Any other first character also ends the list.</p></td>
</tr>
<tr>
<td><p>Definition list</p></td>
<td><pre><code>;item 1
: definition 1
;item 2
: definition 2-1
: definition 2-2</code></pre></td>
<td><dl>
<dt>item 1</dt>
<dd>
definition 1
</dd>
<dt>item 2</dt>
<dd>
definition 2-1
</dd>
<dd>
definition 2-2
</dd>
</dl></td>
</tr>
<tr>
<td><p>Adopting definition list to indent text</p></td>
<td><pre><code>: Single indent
:: Double indent
::::: Multiple indent</code></pre>
<hr />
<p><em>Note:</em> This workaround may be controversial from the viewpoint of accessibility.</p></td>
<td><dl>
<dt></dt>
<dd>
Single indent
<dl>
<dt></dt>
<dd>
Double indent
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
Multiple indent
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl></td>
</tr>
<tr>
<td><p>Mixture of different types of list</p></td>
<td><pre><code># one
# two
#* two point one
#* two point two
# three
#; three item one
#: three def one
# four
#: four def one
#: this looks like a continuation
#: and is often used
#: instead&lt;br /&gt;of &amp;lt;nowiki&gt;&lt;br /&gt;&amp;lt;/nowiki&gt;
# five
## five sub 1
### five sub 1 sub 1
## five sub 2</code></pre>
<hr />
<p><em>Note:</em> The usage of <code>#:</code> and <code>*:</code> for breaking a line within an item may also be controversial.</p></td>
<td><ol>
<li>one</li>
<li>two
<ul>
<li>two point one</li>
<li>two point two</li>
</ul></li>
<li>three
<dl>
<dt>three item one</dt>
<dd>
three def one
</dd>
</dl></li>
<li>four
<dl>
<dt></dt>
<dd>
four def one
</dd>
<dd>
this looks like a continuation
</dd>
<dd>
and is often used
</dd>
<dd>
instead<br />
of &lt;br /&gt;
</dd>
</dl></li>
<li>five
<ol>
<li>five sub 1
<ol>
<li>five sub 1 sub 1</li>
</ol></li>
<li>five sub 2</li>
</ol></li>
</ol></td>
</tr>
<tr>
<td><p>Preformatted text</p></td>
<td><pre><code> Start each line with a space.
 Text is &#39;&#39;&#39;preformatted&#39;&#39;&#39; and
 &#39;&#39;markups&#39;&#39; &#39;&#39;&#39;&#39;&#39;can&#39;&#39;&#39;&#39;&#39; be done</code></pre>
<hr />
<p><em>Note:</em> This way of preformatting only applies to section formatting. Character formatting markups are still effective.</p></td>
<td><p><code>Start each line with a space.</code><br />
<code>Text is </code><strong><code>preformatted</code></strong><code> and</code><br />
<em><code>markups</code></em><code> </code><strong><em><code>can</code></em></strong><code> be done</code></p></td>
</tr>
</tbody>
</table>

## Paragraphs

MediaWiki ignores single line breaks. To start a new paragraph, leave an empty line. You can force a line break within a paragraph with the HTML tags `<br />`.

## HTML tags

Some [HTML](https://en.wikipedia.org/wiki/HTML) tags are allowed in MediaWiki, for example `<code>`, `<div>`, `<span>` and `<font>`. These apply anywhere you insert them.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th><p>Description</p></th>
<th width="40%"><p>You type</p></th>
<th width="40%"><p>You get</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Underline</p></td>
<td><pre><code>&lt;u&gt;Underline&lt;/u&gt;</code></pre></td>
<td><p><u>Underline</u></p></td>
</tr>
<tr>
<td><p>Strikethrough</p></td>
<td><pre><code>&lt;del&gt;Strikethrough&lt;/del&gt;
&#10;or
&#10;&lt;s&gt;Strikethrough&lt;/s&gt;</code></pre></td>
<td><p><del>Strikethrough</del></p>
<p>or</p>
<p><s>Strikethrough</s></p></td>
</tr>
<tr>
<td><p>Fixed width text</p></td>
<td><pre><code>&lt;code&gt;Source code&lt;/code&gt;
&#10;or
&#10;&lt;tt&gt;Fixed width text&lt;/tt&gt;</code></pre></td>
<td><p><code>Source code</code></p>
<p>or</p>
<p><code>Fixed width text</code></p></td>
</tr>
<tr>
<td><p>Blockquotes</p></td>
<td><pre><code>text above
text above
&lt;blockquote&gt;blockquote&lt;/blockquote&gt;
text below
text below</code></pre></td>
<td><p>text above text above</p>
<blockquote>
<p>blockquote</p>
</blockquote>
<p>text below text below</p></td>
</tr>
<tr>
<td><p>Comment</p></td>
<td><pre><code>&lt;!-- This is a comment --&gt;
Comments are only visible
in the edit window.</code></pre></td>
<td><p>Comments are only visible in the edit window.</p></td>
</tr>
<tr>
<td><p>Completely preformatted text</p></td>
<td><pre><code>&lt;pre&gt; Text is &#39;&#39;&#39;preformatted&#39;&#39;&#39; and
&#39;&#39;markups&#39;&#39; &#39;&#39;&#39;&#39;&#39;cannot&#39;&#39;&#39;&#39;&#39; be done&amp;lt;/pre&gt;</code></pre>
<hr />
<p><em>Note:</em> For marking up of preformatted text, check the "Preformatted text" entry at the bottom of the previous table.</p></td>
<td><pre><code> Text is &#39;&#39;&#39;preformatted&#39;&#39;&#39; and
&#39;&#39;markups&#39;&#39; &#39;&#39;&#39;&#39;&#39;cannot&#39;&#39;&#39;&#39;&#39; be done</code></pre>
</pre></td>
</tr>
<tr>
<td><p><strong>Customized</strong> preformatted text</p></td>
<td><pre><code>&lt;pre style=&quot;color:red&quot;&gt;
Text is &#39;&#39;&#39;preformatted&#39;&#39;&#39;
with a style and
&#39;&#39;markups&#39;&#39; &#39;&#39;&#39;&#39;&#39;cannot&#39;&#39;&#39;&#39;&#39; be done
&amp;lt;/pre&gt;</code></pre>
<hr />
<p><em>Note:</em> A CSS style can be named within the <code>style</code> property.</p></td>
<td><pre><code>Text is &#39;&#39;&#39;preformatted&#39;&#39;&#39;
with a style and
&#39;&#39;markups&#39;&#39; &#39;&#39;&#39;&#39;&#39;cannot&#39;&#39;&#39;&#39;&#39; be done</code></pre></td>
</tr>
</tbody>
</table>

## HTML symbols

An HTML symbol entity is a sequence of characters that produces one particular character. For example, `&rarr;` produces a right arrow "`→`" and `&mdash;` produces an em dash "`—`". HTML symbol entities are allowed in MediaWiki and are sometimes used in advanced editing for two main reasons: to insert characters not normally available on keyboards:

  
`&copy;` → **©**

`&delta;` → **δ**

and to prevent the parser from interpreting and displaying HTML tags and symbols:

  
`&amp;euro;` → **`&euro;`**

`&euro;` → **€**

<!-- -->

  
`&lt;span style="color:green;">Green&lt;/span>` → **`<span style="color:green;">Green</span>`**

`<span style="color:green;">Green</span>` → **<span style="color:green;">Green</span>**

The following is a list of characters that can be produced using HTML symbols. Hover any character to find out the symbol that produces it. Some symbols not available in the current font will appear as empty squares.

<table>
<thead>
<tr>
<th colspan="32">HTML Symbol Entities</th>
</tr>
</thead>
<tbody>
<tr>
<td><span title="&amp;Aacute;">Á</span></td>
<td><span title="&amp;aacute;">á</span></td>
<td><span title="&amp;Acirc;">Â</span></td>
<td><span title="&amp;acirc;">â</span></td>
<td><span title="&amp;acute;">´</span></td>
<td><span title="&amp;AElig;">Æ</span></td>
<td><span title="&amp;aelig;">æ</span></td>
<td><span title="&amp;Agrave;">À</span></td>
<td><span title="&amp;agrave;">à</span></td>
<td><span title="&amp;alefsym;">ℵ</span></td>
<td><span title="&amp;Alpha;">Α</span></td>
<td><span title="&amp;alpha;">α</span></td>
<td><span title="&amp;amp;">&amp;</span></td>
<td><span title="&amp;and;">∧</span></td>
<td><span title="&amp;ang;">∠</span></td>
<td><span title="&amp;Aring;">Å</span></td>
<td><span title="&amp;aring;">å</span></td>
<td><span title="&amp;asymp;">≈</span></td>
<td><span title="&amp;Atilde;">Ã</span></td>
<td><span title="&amp;atilde;">ã</span></td>
<td><span title="&amp;Auml;">Ä</span></td>
<td><span title="&amp;auml;">ä</span></td>
<td><span title="&amp;bdquo;">„</span></td>
<td><span title="&amp;Beta;">Β</span></td>
<td><span title="&amp;beta;">β</span></td>
<td><span title="&amp;brvbar;">¦</span></td>
<td><span title="&amp;bull;">•</span></td>
<td><span title="&amp;cap;">∩</span></td>
<td><span title="&amp;Ccedil;">Ç</span></td>
<td><span title="&amp;ccedil;">ç</span></td>
<td><span title="&amp;cedil;">¸</span></td>
<td><span title="&amp;cent;">¢</span></td>
</tr>
<tr>
<td><span title="&amp;Chi;">Χ</span></td>
<td><span title="&amp;chi;">χ</span></td>
<td><span title="&amp;circ;">ˆ</span></td>
<td><span title="&amp;clubs;">♣</span></td>
<td><span title="&amp;cong;">≅</span></td>
<td><span title="&amp;copy;">©</span></td>
<td><span title="&amp;crarr;">↵</span></td>
<td><span title="&amp;cup;">∪</span></td>
<td><span title="&amp;curren;">¤</span></td>
<td><span title="&amp;dagger;">†</span></td>
<td><span title="&amp;Dagger;">‡</span></td>
<td><span title="&amp;darr;">↓</span></td>
<td><span title="&amp;dArr;">⇓</span></td>
<td><span title="&amp;deg;">°</span></td>
<td><span title="&amp;Delta;">Δ</span></td>
<td><span title="&amp;delta;">δ</span></td>
<td><span title="&amp;diams;">♦</span></td>
<td><span title="&amp;divide;">÷</span></td>
<td><span title="&amp;Eacute;">É</span></td>
<td><span title="&amp;eacute;">é</span></td>
<td><span title="&amp;Ecirc;">Ê</span></td>
<td><span title="&amp;ecirc;">ê</span></td>
<td><span title="&amp;Egrave;">È</span></td>
<td><span title="&amp;egrave;">è</span></td>
<td><span title="&amp;empty;">∅</span></td>
<td><span title="&amp;emsp;"> </span></td>
<td><span title="&amp;ensp;"> </span></td>
<td><span title="&amp;Epsilon;">Ε</span></td>
<td><span title="&amp;epsilon;">ε</span></td>
<td><span title="&amp;equiv;">≡</span></td>
<td><span title="&amp;Eta;">Η</span></td>
<td><span title="&amp;eta;">η</span></td>
</tr>
<tr>
<td><span title="&amp;ETH;">Ð</span></td>
<td><span title="&amp;eth;">ð</span></td>
<td><span title="&amp;Euml;">Ë</span></td>
<td><span title="&amp;euml;">ë</span></td>
<td><span title="&amp;euro;">€</span></td>
<td><span title="&amp;exist;">∃</span></td>
<td><span title="&amp;fnof;">ƒ</span></td>
<td><span title="&amp;forall;">∀</span></td>
<td><span title="&amp;frac12;">½</span></td>
<td><span title="&amp;frac14;">¼</span></td>
<td><span title="&amp;frac34;">¾</span></td>
<td><span title="&amp;frasl;">⁄</span></td>
<td><span title="&amp;Gamma;">Γ</span></td>
<td><span title="&amp;gamma;">γ</span></td>
<td><span title="&amp;ge;">≥</span></td>
<td><span title="&amp;gt;">&gt;</span></td>
<td><span title="&amp;harr;">↔︎</span></td>
<td><span title="&amp;hArr;">⇔</span></td>
<td><span title="&amp;hearts;">♥</span></td>
<td><span title="&amp;hellip;">…</span></td>
<td><span title="&amp;Iacute;">Í</span></td>
<td><span title="&amp;iacute;">í</span></td>
<td><span title="&amp;Icirc;">Î</span></td>
<td><span title="&amp;icirc;">î</span></td>
<td><span title="&amp;iexcl;">¡</span></td>
<td><span title="&amp;Igrave;">Ì</span></td>
<td><span title="&amp;igrave;">ì</span></td>
<td><span title="&amp;image;">ℑ</span></td>
<td><span title="&amp;infin;">∞</span></td>
<td><span title="&amp;int;">∫</span></td>
<td><span title="&amp;Iota;">Ι</span></td>
<td><span title="&amp;iota;">ι</span></td>
</tr>
<tr>
<td><span title="&amp;iquest;">¿</span></td>
<td><span title="&amp;isin;">∈</span></td>
<td><span title="&amp;Iuml;">Ï</span></td>
<td><span title="&amp;iuml;">ï</span></td>
<td><span title="&amp;Kappa;">Κ</span></td>
<td><span title="&amp;kappa;">κ</span></td>
<td><span title="&amp;Lambda;">Λ</span></td>
<td><span title="&amp;lambda;">λ</span></td>
<td><span title="&amp;lang;">⟨</span></td>
<td><span title="&amp;laquo;">«</span></td>
<td><span title="&amp;larr;">←</span></td>
<td><span title="&amp;lArr;">⇐</span></td>
<td><span title="&amp;lceil;">⌈</span></td>
<td><span title="&amp;ldquo;">“</span></td>
<td><span title="&amp;le;">≤</span></td>
<td><span title="&amp;lfloor;">⌊</span></td>
<td><span title="&amp;lowast;">∗</span></td>
<td><span title="&amp;loz;">◊</span></td>
<td><span title="&amp;lrm;">‎</span></td>
<td><span title="&amp;lsaquo;">‹</span></td>
<td><span title="&amp;lsquo;">‘</span></td>
<td><span title="&amp;lt;">&lt;</span></td>
<td><span title="&amp;macr;">¯</span></td>
<td><span title="&amp;mdash;">—</span></td>
<td><span title="&amp;micro;">µ</span></td>
<td><span title="&amp;middot;">·</span></td>
<td><span title="&amp;minus;">−</span></td>
<td><span title="&amp;Mu;">Μ</span></td>
<td><span title="&amp;mu;">μ</span></td>
<td><span title="&amp;nabla;">∇</span></td>
<td><span title="&amp;nbsp;"> </span></td>
<td><span title="&amp;ndash;">–</span></td>
</tr>
<tr>
<td><span title="&amp;ne;">≠</span></td>
<td><span title="&amp;ni;">∋</span></td>
<td><span title="&amp;not;">¬</span></td>
<td><span title="&amp;notin;">∉</span></td>
<td><span title="&amp;nsub;">⊄</span></td>
<td><span title="&amp;Ntilde;">Ñ</span></td>
<td><span title="&amp;ntilde;">ñ</span></td>
<td><span title="&amp;Nu;">Ν</span></td>
<td><span title="&amp;nu;">ν</span></td>
<td><span title="&amp;Oacute;">Ó</span></td>
<td><span title="&amp;oacute;">ó</span></td>
<td><span title="&amp;Ocirc;">Ô</span></td>
<td><span title="&amp;ocirc;">ô</span></td>
<td><span title="&amp;OElig;">Œ</span></td>
<td><span title="&amp;oelig;">œ</span></td>
<td><span title="&amp;Ograve;">Ò</span></td>
<td><span title="&amp;ograve;">ò</span></td>
<td><span title="&amp;oline;">‾</span></td>
<td><span title="&amp;Omega;">Ω</span></td>
<td><span title="&amp;omega;">ω</span></td>
<td><span title="&amp;Omicron;">Ο</span></td>
<td><span title="&amp;omicron;">ο</span></td>
<td><span title="&amp;oplus;">⊕</span></td>
<td><span title="&amp;or;">∨</span></td>
<td><span title="&amp;ordf;">ª</span></td>
<td><span title="&amp;ordm;">º</span></td>
<td><span title="&amp;Oslash;">Ø</span></td>
<td><span title="&amp;oslash;">ø</span></td>
<td><span title="&amp;Otilde;">Õ</span></td>
<td><span title="&amp;otilde;">õ</span></td>
<td><span title="&amp;otimes;">⊗</span></td>
<td><span title="&amp;Ouml;">Ö</span></td>
</tr>
<tr>
<td><span title="&amp;ouml;">ö</span></td>
<td><span title="&amp;para;">¶</span></td>
<td><span title="&amp;part;">∂</span></td>
<td><span title="&amp;permil;">‰</span></td>
<td><span title="&amp;perp;">⊥</span></td>
<td><span title="&amp;Phi;">Φ</span></td>
<td><span title="&amp;phi;">φ</span></td>
<td><span title="&amp;Pi;">Π</span></td>
<td><span title="&amp;pi;">π</span></td>
<td><span title="&amp;piv;">ϖ</span></td>
<td><span title="&amp;plusmn;">±</span></td>
<td><span title="&amp;pound;">£</span></td>
<td><span title="&amp;prime;">′</span></td>
<td><span title="&amp;Prime;">″</span></td>
<td><span title="&amp;prod;">∏</span></td>
<td><span title="&amp;prop;">∝</span></td>
<td><span title="&amp;Psi;">Ψ</span></td>
<td><span title="&amp;psi;">ψ</span></td>
<td><span title="&amp;quot;">"</span></td>
<td><span title="&amp;radic;">√</span></td>
<td><span title="&amp;rang;">⟩</span></td>
<td><span title="&amp;raquo;">»</span></td>
<td><span title="&amp;rarr;">→</span></td>
<td><span title="&amp;rArr;">⇒</span></td>
<td><span title="&amp;rceil;">⌉</span></td>
<td><span title="&amp;rdquo;">”</span></td>
<td><span title="&amp;real;">ℜ</span></td>
<td><span title="&amp;reg;">®</span></td>
<td><span title="&amp;rfloor;">⌋</span></td>
<td><span title="&amp;Rho;">Ρ</span></td>
<td><span title="&amp;rho;">ρ</span></td>
<td><span title="&amp;rlm;">‏</span></td>
</tr>
<tr>
<td><span title="&amp;rsaquo;">›</span></td>
<td><span title="&amp;rsquo;">’</span></td>
<td><span title="&amp;sbquo;">‚</span></td>
<td><span title="&amp;Scaron;">Š</span></td>
<td><span title="&amp;scaron;">š</span></td>
<td><span title="&amp;sdot;">⋅</span></td>
<td><span title="&amp;sect;">§</span></td>
<td><span title="&amp;shy;">­</span></td>
<td><span title="&amp;Sigma;">Σ</span></td>
<td><span title="&amp;sigma;">σ</span></td>
<td><span title="&amp;sigmaf;">ς</span></td>
<td><span title="&amp;sim;">∼</span></td>
<td><span title="&amp;spades;">♠</span></td>
<td><span title="&amp;sub;">⊂</span></td>
<td><span title="&amp;sube;">⊆</span></td>
<td><span title="&amp;sum;">∑</span></td>
<td><span title="&amp;sup;">⊃</span></td>
<td><span title="&amp;sup1;">¹</span></td>
<td><span title="&amp;sup2;">²</span></td>
<td><span title="&amp;sup3;">³</span></td>
<td><span title="&amp;supe;">⊇</span></td>
<td><span title="&amp;szlig;">ß</span></td>
<td><span title="&amp;Tau;">Τ</span></td>
<td><span title="&amp;tau;">τ</span></td>
<td><span title="&amp;there4;">∴</span></td>
<td><span title="&amp;Theta;">Θ</span></td>
<td><span title="&amp;theta;">θ</span></td>
<td><span title="&amp;thetasym;">ϑ</span></td>
<td><span title="&amp;thinsp;"> </span></td>
<td><span title="&amp;THORN;">Þ</span></td>
<td><span title="&amp;thorn;">þ</span></td>
<td><span title="&amp;tilde;">˜</span></td>
</tr>
<tr>
<td><span title="&amp;times;">×</span></td>
<td><span title="&amp;trade;">™</span></td>
<td><span title="&amp;Uacute;">Ú</span></td>
<td><span title="&amp;uacute;">ú</span></td>
<td><span title="&amp;uarr;">↑</span></td>
<td><span title="&amp;uArr;">⇑</span></td>
<td><span title="&amp;Ucirc;">Û</span></td>
<td><span title="&amp;ucirc;">û</span></td>
<td><span title="&amp;Ugrave;">Ù</span></td>
<td><span title="&amp;ugrave;">ù</span></td>
<td><span title="&amp;uml;">¨</span></td>
<td><span title="&amp;upsih;">ϒ</span></td>
<td><span title="&amp;Upsilon;">Υ</span></td>
<td><span title="&amp;upsilon;">υ</span></td>
<td><span title="&amp;Uuml;">Ü</span></td>
<td><span title="&amp;uuml;">ü</span></td>
<td><span title="&amp;weierp;">℘</span></td>
<td><span title="&amp;Xi;">Ξ</span></td>
<td><span title="&amp;xi;">ξ</span></td>
<td><span title="&amp;Yacute;">Ý</span></td>
<td><span title="&amp;yacute;">ý</span></td>
<td><span title="&amp;yen;">¥</span></td>
<td><span title="&amp;yuml;">ÿ</span></td>
<td><span title="&amp;Yuml;">Ÿ</span></td>
<td><span title="&amp;Zeta;">Ζ</span></td>
<td><span title="&amp;zeta;">ζ</span></td>
<td><span title="&amp;zwj;">‍</span></td>
<td><span title="&amp;zwnj;">‌</span></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Other formatting

Beyond the text formatting markup shown above, here are some other formatting references:

- [Links](Help-Links)
- [Images](Help-Images)
- [Tables](Help-Tables)

---
*Categories: [Help](Category-Help)*
