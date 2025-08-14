class Status:
    def __init__(self,caption):
        self.caption=caption
        
    def display(self):
        print(f"'{self.caption}' is added")
class StatusV1(Status):
    def __init__(self, url ,caption):
        super().__init__(caption)
        self.url=url
        
    def display(self):
        super().display()
        print(f'{self.url} is uploaded')

sheshu = Status('Python weekly test')
vikash=StatusV1('Assignment','ass-img')
vikash.display()