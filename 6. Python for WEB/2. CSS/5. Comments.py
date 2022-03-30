"""
CSS comments are not displayed in the browser, but they can help document your source code.

CSS Comments

    Comments are used to explain the code, and may help when you edit the source code at a later date.

    Comments are ignored by browsers.

    A CSS comment is placed inside the <style> element, and starts with /* and ends with */:
    Example
    /* This is a single-line comment */
    p {
      color: red;
    }

    You can add comments wherever you want in the code:
    Example
    p {
      color: red;  /* Set text color to red */
    }

    Comments can also span multiple lines:
    Example
    /* This is
    a multi-line
    comment */

    p {
      color: red;
    }

HTML and CSS Comments

    From the HTML tutorial, you learned that you can add comments to your HTML source by using the <!--...--> syntax.

    In the following example, we use a combination of HTML and CSS comments:
    Example
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    p {
      color: red; /* Set text color to red */
    }
    </style>
    </head>
    <body>

    <h2>My Heading</h2>

    <!-- These paragraphs will be red -->
    <p>Hello World!</p>
    <p>This paragraph is styled with CSS.</p>
    <p>CSS comments are not shown in the output.</p>

    </body>
    </html>
"""