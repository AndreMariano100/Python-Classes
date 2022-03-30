"""
HTML attributes provide additional information about HTML elements.

HTML Attributes

    All HTML elements can have attributes
    Attributes provide additional information about elements
    Attributes are always specified in the start tag
    Attributes usually come in name/value pairs like: name="value"


The href Attribute

    The <a> tag defines a hyperlink. The href attribute specifies the URL of the page the link goes to:
    Example
    <a href="https://www.w3schools.com">Visit W3Schools</a>

The src Attribute

    The <img> tag is used to embed an image in an HTML page. The src attribute specifies the path to the
    image to be displayed:
    Example
    <img src="img_girl.jpg">

The width and height Attributes

    The <img> tag should also contain the width and height attributes, which specifies the width and height
    of the image (in pixels):
    Example
    <img src="img_girl.jpg" width="500" height="600">

The alt Attribute

    The required alt attribute for the <img> tag specifies an alternate text for an image, if the image for some
    reason cannot be displayed. This can be due to slow connection, or an error in the src attribute, or if the user
    uses a screen reader.
    Example
    <img src="img_girl.jpg" alt="Girl with a jacket">

The style Attribute

    The style attribute is used to add styles to an element, such as color, font, size, and more.
    Example
    <p style="color:red;">This is a red paragraph.</p>

The lang Attribute

    You should always include the lang attribute inside the <html> tag, to declare the language of the Web page.
    This is meant to assist search engines and browsers.

    The following example specifies English as the language:
        <!DOCTYPE html>
        <html lang="en">
        <body>
        ...
        </body>
        </html>

The title Attribute

    The title attribute defines some extra information about an element.

    The value of the title attribute will be displayed as a tooltip when you mouse over the element:
    Example
    <p title="I'm a tooltip">This is a paragraph.</p>


"""