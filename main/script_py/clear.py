import os
def clear():
    path="/home/django6665/main/media/06/26"
    a=os.listdir(path=path)
    for i in a:
        if (i.endswith(".xlsx")
            and i!='list traid.xlsx'):
                file_and_path="\'{path}/{a1}\'".format(path=path,a1=i)
                os.system("rm {file_and_path}".format(file_and_path=file_and_path))
                print("def {file_and_path}".format(file_and_path=file_and_path))

def clear_test():
    path="/home/django6665/main/media/06/26"
    a=os.listdir(path=path)
    for i in a:
        if (not i.endswith(".py")
            and i!='list traid.xlsx'):
                file_and_path="\'{path}/{a1}\'".format(path=path,a1=i)
                print("{file_and_path}".format(file_and_path=file_and_path))


def clear_storage_test():
    path="/home/django6665/main/media/storage"
    a=os.listdir(path=path)
    for i in a:
        if (not i.endswith(".py")
            and i!='list traid.xlsx'):
                file_and_path="\'{path}/{a1}\'".format(path=path,a1=i)
                return  ("{file_and_path}".format(file_and_path=file_and_path))


