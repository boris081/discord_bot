import sqlite3

class DBHepler:
    def __init__(self, database_path):
      try:
        self.conn   = sqlite3.connect(database_path)
        self.cursor  = self.conn.cursor()
      except sqlite3.Error as e:
        print("Error connecting to database!")

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        self.close()

    def execute(self, query, new_data):
      """execute a row of data to current cursor"""
      self.cur.execute(query, new_data)
      self.connection.commit()
      return self.cur

    def get(self,table,columns,limit=None):
        query = "SELECT {0} from {1}".format(columns,table)
        self.cursor.execute(query)
        # fetch data
        rows = self.cursor.fetchall()
        return rows[len(rows)-limit if limit else 0:]

    def write(self,table,columns,data):
        print(type(data))
        query = "INSERT INTO {0} VALUES (?,?,?,?)".format(table)
          # query = ("INSERT INTO {0} ({1}) VALUES (?,?,?,?)".format(table,columns),i)
        print(query)
        self.cursor.execute(query,data)   

    def query(self,sql):
        self.cursor.execute(sql)    

#   搜尋
    def select_point_by_id(self,userid):
      try:
        query = "SELECT point from GAME WHERE user_id=?"
        self.cursor.execute(query, (userid,))
        rows = self.cursor.fetchone()
        if rows == None:
          return "None"
        i = 0
        for r in rows:
          i = int(r)
        return i
      except sqlite3.Error as e:
        print("Update Error : " + str(e))

#   更新
    def update_point_by_id(self, userid:int, point:int):
      query = "UPDATE GAME SET point={0} WHERE user_id={1}".format(point,userid)
      self.cursor.execute(query)

        
# 寫入新成員
    def insert_new(self,data):
        query = "INSERT INTO GAME (user_id,username,server_id,point) VALUES (?,?,?,?)"
        self.cursor.execute(query,data) 

#   新增
    # def create_new(self,table,columns,data):
    #     query = "Create TABLE {0} ({1}) VALUES ({2});".format(table,columns,data)
    #     self.cursor.execute(query)   




