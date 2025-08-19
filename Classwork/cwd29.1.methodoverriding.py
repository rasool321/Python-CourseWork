class NormalUser():
    def __init__(self,username):
        self.username=username
        print(f'\nWelcome to youtube "{self.username}". explore our content..')

    def playvedio(self):
        print('Ads  Included')
        print('No Background Play')
        print('Download with Low Quality')
        print('No yt music')
    def profile(self):
        print('You can upload your profile')
    def MultipleDevice(self):
        print('you can login with different devices')
    def shorts(self):
        print('You can see the yt shorts')
    def likecommentshare(self):
        print('You can like share and comment')

class PremiumUser(NormalUser):
    def __init__(self,username):
        super().__init__(username)

    def playvedio(self):
        print('Ads Free')
        print('You can play on Background')
        print('Exclusive content')
        print('Download with hign Quality')
        print('YT music is available')

hemanth=NormalUser('hemanth')
hemanth.playvedio()
hemanth.profile()
hemanth.shorts()
hemanth.MultipleDevice()
hemanth.likecommentshare()

shesu=PremiumUser('Sheshu')
shesu.playvedio()
shesu.profile()
shesu.shorts()
shesu.MultipleDevice()
shesu.likecommentshare()