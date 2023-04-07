class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


info = Comment("user1", "I like this book")
print(info.username)
print(info.content)
print(info.likes)
