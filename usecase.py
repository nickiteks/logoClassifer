from repository import Repository
import os
import csv

def get_photo_names():
    folder_path = 'data'
    photo_names = []

    for photo_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, photo_name)):
            photo_names.append(photo_name)

    return photo_names

class Usecase:
    def __init__(self, connection):
        self.repo = Repository(connection)

    def init_user(self, id):
        user_ids = self.repo.list_all_users()
        if id not in user_ids:
            photo_names = get_photo_names()
            self.repo.add_data(photo_names, id)
        unmarked = self.repo.list_photos(id)
        return unmarked
    
    def add_mark(self, photo_name, id, beaty_mark, noise, location, category):
        self.repo.add_mark(photo_name, id, beaty_mark, noise, location, category)
    
    def list_photo_names(self, id):
        return self.repo.list_photos(id)
    
    def get_dataset(self):
        raw_data = self.repo.list_dataset()
        file_name = "dataset.csv"
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(raw_data)
        return file_name
