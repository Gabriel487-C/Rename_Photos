import os

def rename_folder(folder_photos, rename):
   
    #verifica se o caminho da pasta Realmente Existe:

    if not os.path.isdir(folder_photos):
        return f"error, {folder_photos} not found!"
   

    photos = []
    
    
    for file in os.listdir(folder_photos):
         if os.path.splitext(file)[1].lower() in ['.jpeg','.jpg','.png']:
             path = os.path.join(folder_photos, file)
             photos.append(path)  
    
    
    count=0
    for file in photos:
        if os.path.splitext(file)[1].lower() == '.jpeg':
         new = rename + '_' + str(count) + '.jpeg'
        elif os.path.splitext(file)[1].lower() == '.jpg':
         new = rename + '_' + str(count) + '.jpg'
        else:
         new = rename + '_' + str(count) + '.png'      
        new_path = os.path.join(folder_photos, new) 
        os.rename(file ,new_path)
        count+=1
    
    print("Folder Found!")

#----------------------------------------------------------------------------


folder = str(input("Enter the folder name:\n"))  

prefix = str(input("Enter the name you want to use to rename the photos:\n"))
rename_folder(folder, prefix)