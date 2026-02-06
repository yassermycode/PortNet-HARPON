from app.db.session import engine
from sqlalchemy import inspect

inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables créées :", tables)
print(f"Total : {len(tables)} tables")
