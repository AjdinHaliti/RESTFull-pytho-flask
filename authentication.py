from werkzeug.security import safe_str_cmp
from resources.user import UserModel

#para se mos kriju db kt e kam prdorur
# users = [
#     User(1, 'Ajdin', 'password', 'ah27098@seeu.edu.mk'),
#     User(2, 'Ajdin1', 'password', 'ah1234@seeu.edu.mk'),
# ]
#
# username_table = {u.username: u for u in users}#do ti krkoje userat nprmjet username
# userid_table = {u.id: u for u in users}#nprmjet id
# useremail_table = {u.email: u for u in users }

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

#kjo osht unique pr flask jwt, kjo mer si parametr payload, payload osht ajo vlera mbrenda jwt tokenit
def identity(payload): #payload vajn pi ne request
    user_id = payload['identity'] # ne identity ruhet id
    return UserModel.find_by_id(user_id)

def retrievUserByemail(email):
    user_email = UserModel.useremail_table.get(email, None)
    return UserModel.find_by_email(user_email)
