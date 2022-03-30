"""
HTML Tables

    HTML tables allow web developers to arrange data into rows and columns.
    Example
    Company 	                    Contact 	            Country
    Alfreds Futterkiste 	        Maria Anders 	        Germany
    Centro comercial Moctezuma 	    Francisco Chang 	    Mexico
    Ernst Handel 	                Roland Mendel 	        Austria
    Island Trading 	                Helen Bennett 	        UK
    Laughing Bacchus Winecellars 	Yoshi Tannamuri 	    Canada
    Magazzini Alimentari Riuniti 	Giovanni Rovelli 	    Italy

Define an HTML Table

    A table in HTML consists of table cells inside rows and columns
    Example

    A simple HTML table:
    <table>
      <tr>
        <th>Company</th>
        <th>Contact</th>
        <th>Country</th>
      </tr>
      <tr>
        <td>Alfreds Futterkiste</td>
        <td>Maria Anders</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Centro comercial Moctezuma</td>
        <td>Francisco Chang</td>
        <td>Mexico</td>
      </tr>
    </table>

Table Cells

    Each table cell is defined by a <td> and a </td> tag.

    td stands for table data.

    Everything between <td> and </td> are the content of the table cell.
    Example
    <table>
      <tr>
        <td>Emil</td>
        <td>Tobias</td>
        <td>Linus</td>
      </tr>
    </table>

    Note: table data elements are the data containers of the table.
    They can contain all sorts of HTML elements; text, images, lists, other tables, etc.

Table Rows

    Each table row starts with a <tr> and end with a </tr> tag.

    tr stands for table row.
    Example
    <table>
      <tr>
        <td>Emil</td>
        <td>Tobias</td>
        <td>Linus</td>
      </tr>
      <tr>
        <td>16</td>
        <td>14</td>
        <td>10</td>
      </tr>
    </table>

    You can have as many rows as you like in a table, just make sure that the number of cells are the same in each row.

    Note: There are times where a row can have less or more cells than another. You will learn about that in a
    later chapter.

Table Headers

    Sometimes you want your cells to be headers, in those cases use the <th> tag instead of the <td> tag:
    Example

    Let the first row be table headers:
    <table>
      <tr>
        <th>Person 1</th>
        <th>Person 2</th>
        <th>Person 3</th>
      </tr>
      <tr>
        <td>Emil</td>
        <td>Tobias</td>
        <td>Linus</td>
      </tr>
      <tr>
        <td>16</td>
        <td>14</td>
        <td>10</td>
      </tr>
    </table>

    By default, the text in <th> elements are bold and centered, but you can change that with CSS.

        HTML Table Tags
        Tag 	    Description
        <table> 	Defines a table
        <th> 	    Defines a header cell in a table
        <tr> 	    Defines a row in a table
        <td> 	    Defines a cell in a table
        <caption> 	Defines a table caption
        <colgroup> 	Specifies a group of one or more columns in a table for formatting
        <col> 	    Specifies column properties for each column within a <colgroup> element
        <thead> 	Groups the header content in a table
        <tbody> 	Groups the body content in a table
        <tfoot> 	Groups the footer content in a table


HTML Table Borders

    HTML tables can have borders of different styles and shapes.

    When you add a border to a table, you also add borders around each table cell:

    To add a border, use the CSS border property on table, th, and td elements:
    Example
    table, th, td {
      border: 1px solid black;
    }

Collapsed Table Borders

    To avoid having double borders like in the example above, set the CSS border-collapse property to collapse.

    This will make the borders collapse into a single border.
    Example
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
    }

Style Table Borders

    If you set a background color of each cell, and give the border a white color
    (the same as the document background), you get the impression of an invisible border:
    Example
    table, th, td {
      border: 1px solid white;
      border-collapse: collapse;
    }
    th, td {
      background-color: #96D4D4;
    }

Round Table Borders

    With the border-radius property, the borders get rounded corners:
    Example
    table, th, td {
      border: 1px solid black;
      border-radius: 10px;
    }

    Skip the border around the table by leaving out table from the css selector:
    Example
    th, td {
      border: 1px solid black;
      border-radius: 10px;
    }

Dotted Table Borders

    With the border-style property, you can set the appereance of the border.

    The following values are allowed:

        dotted
        dashed
        solid
        double
        groove
        ridge
        inset
        outset
        none
        hidden

    Example
     th, td {
      border-style: dotted;
    }

Border Color

    With the border-color property, you can set the color of the border.
    Example
     th, td {
      border-color: #96D4D4;
    }

HTML Table Sizes

    HTML tables can have different sizes for each column, row or the entire table.

    Use the style attribute with the width or height properties to specify the size of a table, row or column.
    HTML Table Width

    To set the width of a table, add the style attribute to the <table> element:
    Example

    Set the width of the table to 100%:
    <table style="width:100%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </table>

    Note: Using a percentage as the size unit for a width means how wide will this element be compared to its
    parent element, which in this case is the <body> element.

HTML Table Column Width

    To set the size of a specific column, add the style attribute on a <th> or <td> element:
    Example

    Set the width of the first column to 70%:
    <table style="width:100%">
      <tr>
        <th style="width:70%">Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </table>

HTML Table Row Height

    To set the height of a specific row, add the style attribute on a table row element:
    Example

    Set the height of the second row to 200 pixels:
    <table style="width:100%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr style="height:200px">
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </table>
"""