import psycopg

class UserConnection():

    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fast_api_postgre=juan password=juanito123 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    #Destructor
    def __def__(self):
        self.conn.close()