#Create a class with the name "Comment". The __init__ method should accept 3 parameters:
# username
# content
# likes (optional, 0 by default)
#Use the exact names for your variables
#Note: there is no input/output for this problem. Test the class yourself and submit only the class


class Coment:
    def __init__(self, name, content, likes = 0):
        self.name = name
        self.content = content
        self.likes = likes

coment = Coment("user1", "I like this book")
print(coment.name)
print(coment.content)
print(coment.likes)