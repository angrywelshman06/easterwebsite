#!/usr/bin/env python3

import cgi
import cgitb
from datetime import date

cgitb.enable()

def calculate_easter(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)

def format_date(date_obj, format_type):
    day = date_obj.day
    month = date_obj.strftime("%B")
    year = date_obj.year
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    numeric_format = date_obj.strftime("%d/%m/%Y")
    verbose_format = f"{day}{suffix} {month} {year}"
    if format_type == "numeric":
        return numeric_format
    elif format_type == "verbose":
        return verbose_format
    elif format_type == "both":
        return f"{numeric_format} ({verbose_format})"

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
year = int(form.getvalue("year"))
format_type = form.getvalue("format")

easter_date = calculate_easter(year)
formatted_date = format_date(easter_date, format_type)

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Easter Date Result</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <h1>Easter Date Result</h1>
    <p>The date of Easter in {year} is: {formatted_date}</p>
</body>
</html>
""")