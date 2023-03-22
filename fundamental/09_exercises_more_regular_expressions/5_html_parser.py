import re

program_input_str = input()

pattern_title = r"<title>(.+)<\/title>"
pattern_content = r"<body>(.+)<\/body>"

match_title = re.findall(pattern_title, program_input_str)
match_content = re.findall(pattern_content, program_input_str)

extracted_title = "".join(match_title)
extracted_content = "".join(match_content)

# Handling the <body> text , step by step.

# First remove all <Text>
extracted_content_filter_one = re.sub(r"(<.*?>)", " ", extracted_content)
# Second remove all \n+Text
extracted_content_filter_two = re.sub(r"(\\n*)", " ", extracted_content_filter_one)
# Third fix the white_spaces (double or more ) in the text
extracted_content_filter_three = re.sub(r"(\s{2,})", " ", extracted_content_filter_two)
# Final fix the white_spaces
extracted_content_stripped_text = extracted_content_filter_three.strip()

print(f"Title: {extracted_title}")
print(f"Content: {extracted_content_stripped_text}")
