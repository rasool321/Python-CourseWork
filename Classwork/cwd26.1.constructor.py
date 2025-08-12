class Instagram:
    def __init__(self, username, password):
        print("Welcome to the Instagram")
        self.bio=''
        self.posts=[]
        self.followers={}
        self.following={}
        self.username=username
        self.password=password
        print(f'Hello {self.username} login successful')

mani = Instagram('manikanta','mani@123')