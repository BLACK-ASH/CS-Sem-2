<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/bookstore">
        <html>
            <head>
                <style>
                    table {
                    width: 400px;
                    border-collapse: collapse;
                    }
                    th{
                    background:teal;
                    }
                    td,th{
                    text-align: left;
                    border: 1px solid black;
                    font:bolder;
                    padding:10px;
                    }
                </style>
            </head>
            <body>
                <h1>MY FIRST CODE IN XML AND XSLT</h1>
                <table>
                    <tr>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Year</th>
                        <th>Price</th>
                    </tr>
                    <xsl:for-each select="book">
                        <tr>
                            <td>
                                <xsl:value-of select="title" />
                            </td>
                            <td>
                                <xsl:value-of select="author" />
                            </td>
                            <td>
                                <xsl:value-of select="year" />
                            </td>
                            <td>
                                <xsl:value-of select="price" />
                            </td>
                        </tr>
                    </xsl:for-each>

                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>