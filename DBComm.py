# This is the Database Communications Class
from ImageDB import ImageDB


# Handles Database Communications
class DBComm:
    # Save Classification
    @staticmethod
    def save_classification(img_key, img_quad, img_classification):
        # Connect to Database
        db_conn = ImageDB.img_db_conn()
        # Database Cursor
        cur = db_conn.cursor()
        # Write Classification
        cur.execute("INSERT INTO parsed_img_classifications (img_keys, img_quad, img_classification)"
                    "VALUES (%s, %s, %s)",
                    (img_key, img_quad, img_classification))
        # Commit Changes
        db_conn.commit()
        # Close Communications
        cur.close()
        db_conn.close()

    # Save Image Path Data
    @staticmethod
    def save_img_paths(img_key, img_save_path, img_index):
        # Connect to Database
        db_conn = ImageDB.img_db_conn()
        # Database Cursor
        cur = db_conn.cursor()
        # Insert into Database
        cur.execute("INSERT INTO parsed_img_paths (img_keys, img_paths, img_quad) "
                    "VALUES (%s, %s, %s)",
                    (img_key, img_save_path, img_index))
        # Commit Changes
        db_conn.commit()
        # Close Communications
        cur.close()
        db_conn.close()

    # Get Image Path Data
    @staticmethod
    def get_rand_img_path():
        # Connect to Database
        db_conn = ImageDB.img_db_conn()
        # Database Cursor
        cur = db_conn.cursor()
        # Return Random Image Set
        return cur.execute("SELECT img_paths, img_quad "
                           "FROM parsed_img_paths "
                           "WHERE img_keys IN (SELECT img_keys  FROM parsed_img_paths ORDER BY random() LIMIT 1)")

