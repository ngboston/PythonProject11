import zipfile

class Archive:
    def __init__(self, path, description):
        self.path = path
        self.description = description
        self.password = None

    def getinfo(self):
        print(f"Path: {self.path}\nDescription: {self.description}\nPassword: {self.password}")

class Brutforse:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def hack(self, archive):
        zip_file = zipfile.ZipFile(archive)
        password = None
        f = open(self.dictionary, 'r')
        for line in f.readlines():
            password = line.strip('\n')
            try:
                zip_file.extractall(pwd=password.encode())
                print("------------------")
                print(f"RESULT: {password}")
                f.close()
                return  (True, password)
            except:
                print(password)
        f.close()
        return(False, None)
class Library:
    def __init__(self, bruteforce):
        self.bruteforce = bruteforce
        self.archive = []

    def showarchive(self):
        for archive in self.archive:
            archive.getinfo()
            print("")

    def hackall(self):
        for archive in self.archive:
            if archive.password == None:
                res = self.bruteforce.hack(archive.path)
                if res[0] == True:
                    archive.password = res[1]

def main():
    library = Library(Brutforse("dictionary.txt"))
    library.archive.append(Archive("test.zip", "Test"))
    library.showarchive()
    library.hackall()
    library.showarchive()

if __name__ == '__main__':
    main()
