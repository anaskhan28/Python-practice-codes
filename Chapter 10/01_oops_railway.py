class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train name is {self.train}")


anasApplication = RailwayForm()
anasApplication.name = "Anas Khan"
anasApplication.train = "Lokmaniya Tilak Terminus"
anasApplication.printData()