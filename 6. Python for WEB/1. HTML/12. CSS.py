"""
CSS stands for Cascading Style Sheets.

CSS saves a lot of work. It can control the layout of multiple web pages all at once.

What is CSS?

    Cascading Style Sheets (CSS) is used to format the layout of a webpage.

    With CSS, you can control the color, font, the size of text, the spacing between elements, how elements are
    positioned and laid out, what background images or background colors are to be used, different displays for
    different devices and screen sizes, and much more!

    Tip: The word cascading means that a style applied to a parent element will also apply to all children elements
    within the parent. So, if you set the color of the body text to "blue", all headings, paragraphs, and other text
    elements within the body will also get the same color (unless you specify something else)!

Using CSS

    CSS can be added to HTML documents in 3 ways:

        Inline - by using the style attribute inside HTML elements
        Internal - by using a <style> element in the <head> section
        External - by using a <link> element to link to an external CSS file

    The most common way to add CSS, is to keep the styles in external CSS files.

Inline CSS

    An inline CSS is used to apply a unique style to a single HTML element.

    An inline CSS uses the style attribute of an HTML element.

    The following example sets the text color of the <h1> element to blue, and the text color of the <p> element to red:
    Example
    <h1 style="color:blue;">A Blue Heading</h1>

    <p style="color:red;">A red paragraph.</p>

Internal CSS

    An internal CSS is used to define a style for a single HTML page.

    An internal CSS is defined in the <head> section of an HTML page, within a <style> element.

    The following example sets the text color of ALL the <h1> elements (on that page) to blue, and the text
    color of ALL the <p> elements to red. In addition, the page will be displayed with a "powderblue" background color:

    Example
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {background-color: powderblue;}
    h1   {color: blue;}
    p    {color: red;}
    </style>
    </head>
    <body>

    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>

External CSS

    An external style sheet is used to define the style for many HTML pages.

    To use an external style sheet, add a link to it in the <head> section of each HTML page:
    Example
    <!DOCTYPE html>
    <html>
    <head>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>

    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>

    The external style sheet can be written in any text editor.
    The file must not contain any HTML code, and must be saved with a .css extension.

    Here is what the "styles.css" file looks like:
    "styles.css":
    body {
      background-color: powderblue;
    }
    h1 {
      color: blue;
    }
    p {
      color: red;
    }

CSS Colors, Fonts and Sizes

    The CSS color property defines the text color to be used.

    The CSS font-family property defines the font to be used.

    The CSS font-size property defines the text size to be used.

    Example

    Use of CSS color, font-family and font-size properties:
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        h1 {
          color: blue;
          font-family: verdana;
          font-size: 300%;
        }
        p {
          color: red;
          font-family: courier;
          font-size: 160%;
        }
        </style>
        </head>
        <body>

        <h1>This is a heading</h1>
        <p>This is a paragraph.</p>

        </body>
        </html>

CSS Border

    The CSS border property defines a border around an HTML element.

    Tip: You can define a border for nearly all HTML elements.
    Example

    Use of CSS border property:
    p {
      border: 2px solid powderblue;
    }

CSS Padding

    The CSS padding property defines a padding (space) between the text and the border.
    Example

    Use of CSS border and padding properties:
    p {
      border: 2px solid powderblue;
      padding: 30px;
    }

CSS Margin

    The CSS margin property defines a margin (space) outside the border.
    Example

    Use of CSS border and margin properties:
    p {
      border: 2px solid powderblue;
      margin: 50px;
    }

Link to External CSS

    External style sheets can be referenced with a full URL or with a path relative to the current web page.
    Example

    This example uses a full URL to link to a style sheet:
    <link rel="stylesheet" href="https://www.w3schools.com/html/styles.css">

    Example

    This example links to a style sheet located in the html folder on the current web site:
    <link rel="stylesheet" href="/html/styles.css">

    Example

    This example links to a style sheet located in the same folder as the current page:
    <link rel="stylesheet" href="styles.css">

"""