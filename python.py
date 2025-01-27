from bs4 import BeautifulSoup

# Open the HTML file
with open('p2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all text from the HTML
text = soup.get_text()

# Print the extracted text
print(text)
