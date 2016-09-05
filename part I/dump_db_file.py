from make_db_file import loadDbase
import update_db_file
db = loadDbase()
print(db.values())
for key in db:
    print(key, '=>\n ', db[key])
print(db)
