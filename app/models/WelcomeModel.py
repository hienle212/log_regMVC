from system.core.model import *
import re     
class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    def register(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
        errors = []
        if len(info['first_name']) < 2 or not info['first_name'].isalpha():
            errors.append("Invalid First Name. (Letters only, at least 2 characters.)")
        if len(info['last_name']) < 2 or not info['last_name'].isalpha():
            errors.append("Invalid Last Name. (Letters only, at least 2 characters.)")
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")    
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if info['password'] != info['confirm_password']:
            errors.append('Password and confirm password must match!')
        if PASSWORD_REGEX.match(info['confirm_password']):
            errors.append("Password requires to have at least 1 uppercase letter and 1 numeric value ")   
        if errors:
            return {"status":False, "errors":errors}            
        else:  
            query = "INSERT into users (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name,:last_name,:email,:password, NOW(),NOW())"
            data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'email' :info['email'], 'password' :info['password']}
            self.db.query_db(query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return {"status": True, "user": users[0]}
    def login(self,info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")    
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if errors:
            return {"status":False, "errors":errors}            
        else:  
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = {'email' : info['email']}
            users = self.db.query_db(query,data) 
            return {"status": True, "user": users[0]}


