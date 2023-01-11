# This is the Database Config Class
import psycopg2


# Configure Database Connection
class ImageDB:
    # Connection
    @staticmethod
    def img_db_conn():
        try:
            conn = psycopg2.connect(
                database="image_data",
                user="postgres",
                password="v1s10n",
                port="5432"
            )
            return conn
        finally:
            return False
