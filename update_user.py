from db import db_session
from models import User

user = User.query.last()
print(f"My great user: {user}")
user.salary = 2345
db_session.commit()