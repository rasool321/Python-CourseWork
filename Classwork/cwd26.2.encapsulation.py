class Instagram:
    def __init__(self, username, password):
        print("Welcome to Instagram")
        self.__bio = ''  # private variable
        self.posts = []
        self.followers = []
        self.following = []
        self.username = username
        self.__password = password  # private variable
        print(f'Hello {self.username} login successful')
    
    # Getter for bio
    @property
    def bio(self):
        return self.__bio
    
    # Setter for bio
    @bio.setter
    def bio(self, upd_bio):
        self.__bio = upd_bio

    # Getter for password
    def showPassword(self):
        return self.__password
    
    # Setter for password
    def updatePassword(self, new_pwd):
        self.__password = new_pwd
        return "Password updated successfully"
        

# Create object
mani = Instagram('manikanta', 'mani@123')

# Public variables
print("Bio:", mani.bio)
print('Posts:', mani.posts)
print('Followers:', mani.followers)
print('Following:', mani.following)
print('Username:', mani.username)

# Modify public variables
mani.bio = 'sigma'
mani.posts.append('Pyth.png')
mani.followers.extend(['ras', 'varun', 'tarit'])
mani.following.extend(['ntr', 'rajini', 'kohli'])
mani.username = 'mani_09'

# After updating
print("Bio:", mani.bio)
print('Posts:', mani.posts)
print('Followers:', mani.followers)
print('Following:', mani.following)
print('Username:', mani.username)

# Private variables (through methods)
print("Old Password:", mani.showPassword())
print(mani.updatePassword('sada'))
print("New Password:", mani.showPassword())
