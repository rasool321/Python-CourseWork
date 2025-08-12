class Login:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private
        self._otp = 1234  # protected

    # Getter for private password
    def getpassword(self):
        return self.__password

    # Setter for private password
    def updatePassword(self, new_pwd):
        self.__password = new_pwd

    # OTP getter
    @property
    def publicotp(self):
        return self._otp

    # OTP setter
    @publicotp.setter
    def publicotp(self, value):
        self._otp = value


# Create object
vikash = Login("vikash", "vk@123")

# Public variable
print("#public")
print("Username:", vikash.username)

# Private variable
print("\n#private")
print("Password:", vikash.getpassword())

# Protected variable via property
print("\n#protected")
print("OTP:", vikash.publicotp)

# Updating public
vikash.username = "_vikash_"
print("\nUpdated username:", vikash.username)

# Updating private
vikash.updatePassword("Vk@18")
print("Updated password:", vikash.getpassword())

# Updating protected via property
vikash.publicotp = 1111
print("Updated OTP:", vikash.publicotp)
