#!/bin/bash
curl -s "https://www.ena.am/Info.aspx?id=5&lang=1" > output.html

# Grep for all occurrences of "Ձորաղբյուր", case-insensitive, from the HTML content
grep -iP "(<p[^>]*>.*?Ձորաղբյուր.*?</p>|<td[^>]*>.*?Ձորաղբյուր.*?</td>)" output.html > p2.html
