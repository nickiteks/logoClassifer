class Repository:
    def __init__(self, connection):
        self.db_connection = connection
    #работает
    def create_db (self):
        query = '''CREATE TABLE IF NOT EXISTS photo
                  (photo_name TEXT,
                   tg_id INTEGER,
                   beaty_mark INTEGER,
                   noise INTEGER,
                   location INTEGER,
                   category TEXT,
                   UNIQUE(photo_name, tg_id))'''
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute(query)

    #работает
    def add_mark(self, photo_name, tg_id, beaty_mark, noise, location, category):
        query = "UPDATE photo SET beaty_mark = ?, noise = ?, location = ?, category = ? WHERE photo_name = ? and tg_id = ?"
        values = (beaty_mark, noise, location, category, photo_name, tg_id,)

        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute(query, values)
    #работате
    def list_photos(self, id):
        query = "SELECT photo_name FROM photo WHERE tg_id = ? and beaty_mark is NULL"
        values = (id,)
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute(query, values)
            results = cursor.fetchall()
            image_names = [result[0] for result in results]
        return image_names
    #рвботает
    def add_data(self, photos, id):
        cursor = self.db_connection.cursor()
        for photo in photos:
            cursor.execute("INSERT INTO photo (photo_name, tg_id) VALUES (?, ?)", (photo,id,))
        self.db_connection.commit()
        cursor.close()

    #работает
    def list_all_users(self):
        query = "SELECT DISTINCT tg_id FROM photo"

        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            tg_ids = [result[0] for result in results]
        return tg_ids
    
    def list_dataset(self):
        query = "SELECT photo_name, beaty_mark, noise, location, category from photo"
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
        return results