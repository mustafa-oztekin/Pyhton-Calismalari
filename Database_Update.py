import psycopg2
import pandas as pd
df = pd.read_excel("rvm_db.xlsx")


con = psycopg2.connect(
                        host = "localhost",
                        database = "my_database",
                        user = "postgres",
                        password = "1234")

cur = con.cursor()

for i in range(len(df)):
    cur.execute("insert into rvm (kod, isim, cinsi) values (%s, %s, %s)",
                (int(df.iloc[i,0]), df.iloc[i,1], df.iloc[i,3]))
    
cur.execute("select * from rvm")
rows = cur.fetchall()
con.commit()
print(rows)
cur.close()
con.close()