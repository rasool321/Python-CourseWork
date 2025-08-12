class Status2015():
    def view(self):
        print("you can view")
    def reply(self):
        print("you can reply")
    def caption(self):
        print('you can add caption')

class Status2020(Status2015):
    def uploadimg(self):
        print("you can upload img.")
    def uploadvid(self):
        print("you can upload vedio")
    def privacy(self):
        print("You can select who can see your status ")

class Status2023(Status2020):
    def ProfilePrivacy(self):
        print("You can update the profile privacy")
    def reaction(self):
        print("you can send reactions")
    def like(self):
        print("you can like the status")
    
class Status2024(Status2020):
    def statusrings(self):
        print("Color is added to the status display")
    def mute(self):
        print("you can mute the other's status")
    def filters(self):
        print("You can filters")
        

class Status2025(Status2023,Status2024):
    def music(self):
        print("you can add music")
    def mention(self):
        print('you can mention them')
    def collab(self):
        print('you can share your ststus from insta or fb')
    def voicenote(self):
        print('you can voice note')

print("\nSheshu")       
sheshu= Status2015()#can have acess only 2015
sheshu.view()
sheshu.reply()
sheshu.caption()

print("\nHemanth")
hemanth=Status2020()#can acess cls methods from 2020 and 2015
hemanth.uploadimg()
hemanth.uploadvid()
hemanth.privacy()
hemanth.view()
hemanth.reply()
hemanth.caption()

print("\nRasool")
rasool=Status2023() #can access clas methods only from 2023 ,2020 , from 2020 can acess 2015 
rasool.view()
rasool.reply()
rasool.caption()
rasool.uploadimg()
rasool.uploadvid()
rasool.privacy()
rasool.ProfilePrivacy()
rasool.reaction()
rasool.like()

print('\ntarit')
tarit=Status2024()#can access cls methods only from 2024,2020 and from 2020 can ve acess 2015
tarit.uploadimg()
tarit.uploadvid()
tarit.privacy()
tarit.view()
tarit.reply()
tarit.caption()
tarit.statusrings()
tarit.mute()
tarit.filters()

print('\nVarun')#can have acess all 
varun=Status2025()
varun.uploadimg()
varun.uploadvid()
varun.privacy()
varun.view()
varun.reply()
varun.caption()
varun.statusrings()
varun.mute()
varun.filters()
varun.ProfilePrivacy()
varun.reaction()
varun.like()