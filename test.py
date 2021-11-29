import dropbox
import os
class TransferData:

    def __init__(self,access_token):
        self.access_token=access_token
        
    def upload_file(self,file_from,file_to):
        self.dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from): 
            for filename in files: 
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path) 
                with open(local_path, 'rb') as f: 
                    self.dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def readInput():
    a=input("Enter Sales For Hour 1: ")
    b=input("Enter Sales For Hour 2: ")
    c=input("Enter Sales For Hour 3: ")
    d=input("Enter Sales For Hour 4: ")
    e=input("Enter Sales For Hour 5: ")
    f=input("Enter Sales For Hour 6: ")
    g=input("Enter Sales For Hour 7: ")
    h=input("Enter Sales For Hour 8: ")
    i=input("Enter Sales For Hour 9: ")
    j=input("Enter Sales For Hour 10: ")
    k=input("Enter Sales For Hour 11: ")
    l=input("Enter Sales For Hour 12: ")
    totalFor12Hours=a+b+c+d+e+f+g+h+i+j+k+l

    l = open("test2.txt", "a")
    l.write(totalFor12Hours)
    l.close()

        
def main():
    access_token='sl.A8wGoPqOfxFuy8wGgCyj9E0gcKb66hhHQbvdUeNdXS4gOUVeWMvvrIphiT9XSj9T9EDvx62Cp13odLZt6Z5_o8b6T9uWBO3sZv1RAeH1S_VhP_xzGjLxkiOXSQ6VSD8ZzSSQhkM'
    transferData=TransferData(access_token)

    file_from="/Users/malharjoshi/Development/Projects/coding/C-102 Project"
    file_to=input("Enter The File Path To Upload")
    readInput()
    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved")
main()