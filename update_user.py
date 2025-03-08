from db import db_session
from models import User

user = User.query.last()
print(user)
user.salary = 2345
db_session.commit()