from utils.mysql_connection import MysqlConnection
from utils.security import get_password_hash, verify_password

class User(MysqlConnection):
    def all(self) -> list:
        self.cursor.execute("SELECT * from users")
        users = self.cursor.fetchall()

        return users

    def create(self, user_info: list) -> bool:
        email = user_info["email"]
        password = get_password_hash(user_info["password"])
        role_id = 3 if "role_id" not in user_info else user_info["role_id"]
        self.cursor.execute("INSERT INTO \
            `ness_project`.`users` (`email`, `password`, `role_id`) \
            VALUES ('%s', '%s', '%s');" % (email, password, role_id))
        self.connection.commit()

        try:
            self.cursor.execute("INSERT INTO \
            `ness_project`.`users` (`email`, `password`, `role_id`) \
            VALUES ('%s', '%s', '%s');" % (email, password, role_id))
            self.connection.commit()
        except:
            return False
        if self.cursor.rowcount > 0:
            return True
        return False

    def delete(self, email: str) -> bool:
        if not self.get(email):
            return False
        self.cursor.execute("DELETE FROM users WHERE email = '%s'" % email)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def edit(self, user_info: list) -> list:
        user = self.get(user_info['email'])
        same_password = verify_password(user_info['password'], user['password']) \
            if 'password' in user_info else True

        user["password"] = get_password_hash(user_info['password']) \
            if not same_password else user['password']
        user["role_id"] = user_info['role_id'] \
            if 'role_id' in user_info else user['role_id']        

        self.cursor.execute("UPDATE `ness_project`.`users` SET \
            `password`='%s', \
            `role_id`='%s' WHERE `email`='%s';" % (user["password"], user["role_id"], user['email']))
        user["password"] = ""
        return user

    def get(self, email: str) -> list:
        self.cursor.execute("SELECT * from users WHERE email = '%s'" % email)
        user = self.cursor.fetchall()
        if not user:
            return {}
        user_dict = {
            "id": user[0][0],
            "email": user[0][1],
            "password": user[0][2],
            "role_id": user[0][3]
        }
        return user_dict

    def destroy(self):
        self.connection.close()