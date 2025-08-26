class Instagram:
    def __init__(self, username):
        self.username = username
        self.posts = []   # list to store posts

    def addUsername(self):
        print(f"{self.username} is added to Instagram!")

    def uploadPost(self, posturl):
        self.posts.append(posturl)
        print(f"{self.username} uploaded a post: {posturl}")

    def viewPosts(self):
        print(f"--- Posts of {self.username} ---")
        for post in self.posts:
            print(post)


# creating users
taruni = Instagram("Taruni")
sirisha = Instagram("Sirisha")
sheshu = Instagram("Sheshu")

# add usernames
taruni.addUsername()
sirisha.addUsername()
sheshu.addUsername()

# uploading posts
taruni.uploadPost("dsgshshj.png")
sirisha.uploadPost("hguigigig.png")
sheshu.uploadPost("uiihihuv.png")

# view posts
taruni.viewPosts()
sirisha.viewPosts()
