What is HTML
HyperText Markup Language. Tags text files to achieve a font, color, graphic, or hyperlink effect on a world wide web page.
HTML describes the structure of a webpage using markup. HTML elements are building blocks of a HTML page.
HTML tags are labled with a class like heading, paragraph, table, etc.
Browsers do not display tags but use them to render content.

How to create an HTML page
<!DOCTYPE html>
<html>
</html>

What is a markup language
A system for annotating a document from text. It comes from marking up paper manuscripts to a digital media.


What is the DOM
DOM is Document Object Model. It is like a tree for HTML and XML and represents the elements as nodes or objects. Webpages are documents.

What is an element / tag
An element in HTML is some sort of structure or sematic that has a tag like <p>. Tags like <footer> are used to mark the start and end of an element.

What is an attribute
Attributes are properties for an element and have a attribute-value pair. They appear in an elemet's start tag and can contain any number of attributes.

The most popular misuse of the term tag is when alt attributes are references as alt tags. Alt is an attribute, not a tag.

How does the browser load a webpage
A request is made when a link is clicked. The page and its resources are downloaded.
The web browser uses the page resources to build the page and the page is then rendered to the user. So request, response, build, and render.

What is CSS
Cascading Style Sheets. It describes how HTML elements are displayed on the screen. CSS saves a lot of work and controls the layout of multiple web pages.

How to add style to an element
selector {declaration of a property and value}

What is a class
A class attribute is used by designers to identify different sections that can be styled in CSS. This helps differentiate different styles for the same HTML elements on a web page in different sections.

What is a selector
The element selector selects elements based on the element name. You can select all p elements like so: p {stuff}

How to compute CSS Specificity Value
If multiple CSS selectors are targeting the same element and the CSS selectors are trying to assign the same properties to the HTML element, then the selector with the highest specificity value will win.
The most specific selector gets assigned to the HTML element. Here is an example of specificity values, p is 1. div#warning p is 22. div#caution p is 102. body#home .container p is 112.

Calculating the specificity requires looking into 4 colums. In-line styling adds 1 point to columb a. For each ID value, add 1 point to column B. For each class value, add 1 to column c. And for each element reference add 1 to column d. We can read these values like 1,0,0,0 or 1000.

\* has no specificity value (0,0,0,0).

What are Box properties in CSS
Box sizing property defines how the width and height of an element are calculated. There is padding, borders, margins, and box stuff.



HTML will always represent content, and CSS will always represent the appearance of that content.

Tags are the use of > and <. Opening tag and closing tag. Content is between the 2.

All HTML documents have a required structure that includes the following declaration and elements: <!DOCTYPE html>, <html>, <head>, and <body>.

Some elements do not need a closing tag and are self-closing elements like meta, br, img, wbr, embed, input, param, hr, link, source.

Selectors, property, values.

Type selectors would be something like div {} or p {}. It targets all the elements of that type.

Class selectors choose based on class. Classes have a leading period.

ID selectors only target one unique element. They should be reserved for significant elements. They have a leading #.

There are more advanced selectors.

Default styles are just browsers imposing their own preferred CSS to those elements. CSS resets help cross browser compatibility.
Lots of popular resets exists. Eric Meyer and Nicolas Gallagher have popular ones.

Different browsers render elements differently. Div is short for division and span is span. Both are for styling purposes and they have no semantic value.

Div and span are just containers. Read above. Block elements start on a new line and stack on each other and can only take up an appropriate width. Large things are usually clocks. Inline elements follow the normal flow of a doc and they line up from end to end and only maintain the width of their content.

Text is the kind of media and content. Headings come in h1 to h6 rankings. Strong vs b. Strong is to give importance and is usually more popular while bold is to make it look different. Italicize with em which stresses the emphasis and i is used to for an alternative tone like if we wanted to use quotes.

For the longest time we used only divs to divide sections of a webpage but now in HTML5 we finally have new divisions.
Say hello to the new structural elements: header, nav, article, section, aside, and footer.

The header is for the top of a page or article or section. It can even be a nav bar. Nav is used for a section with tons of navigational links. Article is for identifying sections of self contained content that can be reused or distributed. A good rule of thumb for using an article, if we remove this, will the work still make sense? Section is identifying a group of content that generally has a heading and the content inside can be generic.

If someone needs to decide on article, section, or div elements, depends on the content. Both article and section help outline a document and if we need content purely styled then use div. If the content can be redistributed, make it an article. If the content is part of the web page and essential, make it a section.

Aside is an element that holds content like a sidebar, insert, or brief explanation. If an aside is in an article, then it may identify content related to the author of the article. 

Footer identifies the closing or end of a page or element. It is found at the bottom. Content inside should be relative info and not diverge.

Use hyperlinks to navigate between web pages or websites.
