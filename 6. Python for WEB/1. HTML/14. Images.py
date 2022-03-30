"""
HTML Images

    Images can improve the design and the appearance of a web page.
    Example
    <img src="pic_trulli.jpg" alt="Italian Trulli">
    Example
    <img src="img_girl.jpg" alt="Girl in a jacket">
    Example
    <img src="img_chania.jpg" alt="Flowers in Chania">

HTML Images Syntax

    The HTML <img> tag is used to embed an image in a web page.

    Images are not technically inserted into a web page; images are linked to web pages.
    The <img> tag creates a holding space for the referenced image.

    The <img> tag is empty, it contains attributes only, and does not have a closing tag.

    The <img> tag has two required attributes:

        src - Specifies the path to the image
        alt - Specifies an alternate text for the image

    Syntax
    <img src="url" alt="alternatetext">

The src Attribute

    The required src attribute specifies the path (URL) to the image.

    Note: When a web page loads, it is the browser, at that moment, that gets the image from a web server and inserts
    it into the page. Therefore, make sure that the image actually stays in the same spot in relation to the web page,
    otherwise your visitors will get a broken link icon. The broken link icon and the alt text are shown if the browser
    cannot find the image.
    Example
    <img src="img_chania.jpg" alt="Flowers in Chania">
    The alt Attribute

    The required alt attribute provides an alternate text for an image, if the user for some reason cannot view it
    (because of slow connection, an error in the src attribute, or if the user uses a screen reader).

    The value of the alt attribute should describe the image:
    Example
    <img src="img_chania.jpg" alt="Flowers in Chania">

    If a browser cannot find an image, it will display the value of the alt attribute:
    Example
    <img src="wrongname.gif" alt="Flowers in Chania">

    Tip: A screen reader is a software program that reads the HTML code, and allows the user to "listen" to the content.
    Screen readers are useful for people who are visually impaired or learning disabled.

Image Size - Width and Height

    You can use the style attribute to specify the width and height of an image.
    Example
    <img src="img_girl.jpg" alt="Girl in a jacket" style="width:500px;height:600px;">

    Alternatively, you can use the width and height attributes:
    Example
    <img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">

    The width and height attributes always define the width and height of the image in pixels.

    Note: Always specify the width and height of an image. If width and height are not specified, the web page might
    flicker while the image loads.

Width and Height, or Style?

    The width, height, and style attributes are all valid in HTML.

    However, we suggest using the style attribute. It prevents styles sheets from changing the size of images:
    Example
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    img {
      width: 100%;
    }
    </style>
    </head>
    <body>

    <img src="html5.gif" alt="HTML5 Icon" width="128" height="128">

    <img src="html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">

    </body>
    </html>

Images in Another Folder

    If you have your images in a sub-folder, you must include the folder name in the src attribute:
    Example
    <img src="/images/html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">

Images on Another Server/Website

    Some web sites point to an image on another server.

    To point to an image on another server, you must specify an absolute (full) URL in the src attribute:
    Example
    <img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com">

    Notes on external images: External images might be under copyright. If you do not get permission to use it,
    you may be in violation of copyright laws. In addition, you cannot control external images; it can suddenly be
    removed or changed.

Animated Images

    HTML allows animated GIFs:
    Example
    <img src="programming.gif" alt="Computer Man" style="width:48px;height:48px;">

Image as a Link

    To use an image as a link, put the <img> tag inside the <a> tag:
    Example
    <a href="default.asp">
      <img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;">
    </a>

Image Floating

    Use the CSS float property to let the image float to the right or to the left of a text:
    Example
    <p><img src="smiley.gif" alt="Smiley face" style="float:right;width:42px;height:42px;">
    The image will float to the right of the text.</p>

    <p><img src="smiley.gif" alt="Smiley face" style="float:left;width:42px;height:42px;">
    The image will float to the left of the text.</p>

    Tip: To learn more about CSS Float, read our CSS Float Tutorial.

Common Image Formats

Here are the most common image file types, which are supported in all browsers (Chrome, Edge, Firefox, Safari, Opera):
Abbreviation 	File Format 	                        File Extension
APNG 	        Animated Portable Network Graphics 	    .apng
GIF 	        Graphics Interchange Format 	        .gif
ICO 	        Microsoft Icon 	                        .ico, .cur
JPEG 	        Joint Photographic Expert Group image 	.jpg, .jpeg, .jfif, .pjpeg, .pjp
PNG 	        Portable Network Graphics 	            .png
SVG 	        Scalable Vector Graphics 	            .svg



HTML Image Maps

    With HTML image maps, you can create clickable areas on an image.

    The HTML <map> tag defines an image map. An image map is an image with clickable areas. The areas are defined
    with one or more <area> tags.

    How Does it Work?

    The idea behind an image map is that you should be able to perform different actions depending on where in the
    image you click.

    To create an image map you need an image, and some HTML code that describes the clickable areas.

    The Image

        The image is inserted using the <img> tag. The only difference from other images is that you must add a
        usemap attribute:
        <img src="workplace.jpg" alt="Workplace" usemap="#workmap">

        The usemap value starts with a hash tag # followed by the name of the image map, and is used to create a
        relationship between the image and the image map.

        Tip: You can use any image as an image map!

    Create Image Map

        Then, add a <map> element.

        The <map> element is used to create an image map, and is linked to the image by using the required name attribute:
        <map name="workmap">

        The name attribute must have the same value as the <img>'s usemap attribute .

    The Areas

        Then, add the clickable areas.

        A clickable area is defined using an <area> element.

    Shape

    You must define the shape of the clickable area, and you can choose one of these values:

        rect - defines a rectangular region
        circle - defines a circular region
        poly - defines a polygonal region
        default - defines the entire region

    You must also define some coordinates to be able to place the clickable area onto the image.

    Shape="rect"

    The coordinates for shape="rect" come in pairs, one for the x-axis and one for the y-axis.

    So, the coordinates 34,44 is located 34 pixels from the left margin and 44 pixels from the top:

    The coordinates 270,350 is located 270 pixels from the left margin and 350 pixels from the top:

    Now we have enough data to create a clickable rectangular area:
    Example
    <area shape="rect" coords="34, 44, 270, 350" href="computer.htm">

    This is the area that becomes clickable and will send the user to the page "computer.htm":

    Shape="circle"

    To add a circle area, first locate the coordinates of the center of the circle:

    337,300

    Then specify the radius of the circle:

    44 pixels

    Now you have enough data to create a clickable circular area:
    Example
    <area shape="circle" coords="337, 300, 44" href="coffee.htm">

    This is the area that becomes clickable and will send the user to the page "coffee.htm":

    Shape="poly"

    The shape="poly" contains several coordinate points, which creates a shape formed with straight lines (a polygon).

    This can be used to create any shape.

    Like maybe a croissant shape!

    How can we make the croissant in the image below become a clickable link?

    We have to find the x and y coordinates for all edges of the croissant:

    The coordinates come in pairs, one for the x-axis and one for the y-axis:
    Example
    <area shape="poly" coords="140,121,181,116,204,160,204,222,191,270,140,
                               329,85,355,58,352,37,322,40,259,103,161,128,147" href="croissant.htm">

    This is the area that becomes clickable and will send the user to the page "croissant.htm":

Image Map and JavaScript

    A clickable area can also trigger a JavaScript function.

    Add a click event to the <area> element to execute a JavaScript function:
    Example

    Here, we use the onclick attribute to execute a JavaScript function when the area is clicked:
    <map name="workmap">
      <area shape="circle" coords="337,300,44" href="coffee.htm" onclick="myFunction()">
    </map>

    <script>
    function myFunction() {
      alert("You clicked the coffee cup!");
    }
    </script>

HTML Background Images

    A background image can be specified for almost any HTML element.

    To add a background image on an HTML element, use the HTML style attribute and the CSS background-image property:
    Example

    Add a background image on a HTML element:
    <div style="background-image: url('img_girl.jpg');">

    You can also specify the background image in the <style> element, in the <head> section:
    Example

    Specify the background image in the <style> element:
    <style>
    div {
      background-image: url('img_girl.jpg');
    }
    </style>

Background Image on a Page

    If you want the entire page to have a background image, you must specify the background image on the <body> element:
    Example

    Add a background image for the entire page:
    <style>
    body {
      background-image: url('img_girl.jpg');
    }
    </style>
    Background Repeat

    If the background image is smaller than the element, the image will repeat itself, horizontally and vertically,
    until it reaches the end of the element:
    Example
    <style>
    body {
      background-image: url('example_img_girl.jpg');
    }
    </style>

    To avoid the background image from repeating itself, set the background-repeat property to no-repeat.
    Example
    <style>
    body {
      background-image: url('example_img_girl.jpg');
      background-repeat: no-repeat;
    }
    </style>

Background Cover

    If you want the background image to cover the entire element, you can set the background-size property to cover.

    Also, to make sure the entire element is always covered, set the background-attachment property to fixed:

    This way, the background image will cover the entire element, with no stretching (the image will keep its original
    proportions):
    Example
    <style>
    body {
      background-image: url('img_girl.jpg');
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-size: cover;
    }
    </style>

Background Stretch

    If you want the background image to stretch to fit the entire element, you can set the background-size
    property to 100% 100%:

    Try resizing the browser window, and you will see that the image will stretch, but always cover the entire element.
    Example
    <style>
    body {
      background-image: url('img_girl.jpg');
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-size: 100% 100%;
    }
    </style>


HTML <picture> Element

    The HTML <picture> element allows you to display different pictures for different devices or screen sizes.

    The HTML <picture> element gives web developers more flexibility in specifying image resources.

    The <picture> element contains one or more <source> elements, each referring to different images through the
    srcset attribute. This way the browser can choose the image that best fits the current view and/or device.

    Each <source> element has a media attribute that defines when the image is the most suitable.
    Example

    Show different images for different screen sizes:
    <picture>
      <source media="(min-width: 650px)" srcset="img_food.jpg">
      <source media="(min-width: 465px)" srcset="img_car.jpg">
      <img src="img_girl.jpg">
    </picture>

    Note: Always specify an <img> element as the last child element of the <picture> element.
    The <img> element is used by browsers that do not support the <picture> element, or if none
    of the <source> tags match.

When to use the Picture Element

    There are two main purposes for the <picture> element:

    1. Bandwidth

    If you have a small screen or device, it is not necessary to load a large image file. The browser will use the
    first <source> element with matching attribute values, and ignore any of the following elements.

    2. Format Support

    Some browsers or devices may not support all image formats. By using the <picture> element, you can add
    images of all formats, and the browser will use the first format it recognizes, and ignore any of the
    following elements.

    Example

    The browser will use the first image format it recognizes:
    <picture>
      <source srcset="img_avatar.png">
      <source srcset="img_girl.jpg">
      <img src="img_beatles.gif" alt="Beatles" style="width:auto;">
    </picture>
"""