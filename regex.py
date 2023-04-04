import re

# Read in the contents of the text file
with open("email_list.txt", "r") as file:
    contents = file.read()

# Define a regular expression to extract domain names
pattern = r"@([\w.]+)"

# Use regular expressions to extract domain names
matches = re.findall(pattern, contents)

# Remove duplicates by converting the list to a set
unique_domains = set(matches)

# Sort the domain names alphabetically
sorted_domains = sorted(unique_domains)

# Output the list of unique domain names
print("List of unique domain names:")
for domain in sorted_domains:
    print(domain)