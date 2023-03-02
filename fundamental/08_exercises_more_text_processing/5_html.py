article_title = input()
article_content = input()

print(f"<h1>\n    {article_title}\n</h1>")
print(f"<article>\n    {article_content}\n</article>")

while True:
    comment = input()
    if comment == "end of comments":
        break
    print(f"<div>\n    {comment}\n</div>")
