<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <!-- The template that matches the root of the XML document -->
    <xsl:template match="/">
        <html>
            <body>
                <h1>Book Details</h1>
                <table border="1" >
                    <tr bgcolor="#FFFF00">
                        <th>BOOK ID</th>
                        <th>BOOK NAME</th>
                        <th>AUTHOR</th>
                        <th>PUBLISHER</th>
                        <th>PRICE</th>
                    </tr>
                    <xsl:for-each select="class/book">
                        <tr bgcolor="slate">
                            <td>
                                <xsl:value-of select="@bid"/>
                            </td>
                            <td>
                                <xsl:value-of select="bname"/>
                            </td>
                            <td>
                                <xsl:value-of select="author"/>
                            </td>
                            <td>
                                <xsl:value-of select="publisher"/>
                            </td>
                            <td>
                                <xsl:value-of select="price"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
