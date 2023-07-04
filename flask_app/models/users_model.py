from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex
import datetime

db = 'users'

class User:
    def __init__(self, data):
        #follow database table fields plus any other attribute you want to create
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Get all users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        user_list = []
        for user in results:
            new_user = cls(user)
            user['created_at'] = user['created_at'].strftime('%y/%m/%d %I:%M %p') # convert to readable date and time
            user['updated_at'] = user['updated_at'].strftime('%y/%m/%d %I:%M %p') # convert to readable date and time
            user_list.append(user)
        return user_list
    
    # Get one user
    @classmethod
    def get_one(cls, user_id):
        data = {
            'id': user_id
        }
        query = "SELECT * FROM users where id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        results[0]['created_at'] = results[0]['created_at'].strftime('%b %d %Y %I:%M %p') # convert to readable date and time
        results[0]['updated_at'] = results[0]['updated_at'].strftime('%b %d %Y %I:%M %p') # convert to readable date and time
        print(results)
        
        return results
    
    # Add one user
    @classmethod
    def insert_user(cls, form_data):
        query = '''insert into users (first_name, last_name, email) 
                values (%(first_name)s, %(last_name)s, %(email)s)
                '''
        results = connectToMySQL(db).query_db(query, form_data)
        print(results)
        return results
    
    # Update one user
    @classmethod
    def edit_one(cls, form_data):
        query = '''update users
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s
                where id = %(id)s;
                '''
        results = connectToMySQL(db).query_db(query, form_data)
        return results
    
    # Delete one user
    @classmethod
    def delete_user(cls, user_id):
        print(user_id)
        query = '''DELETE FROM users WHERE id = %(id)s;
                '''
        results = connectToMySQL(db).query_db(query, user_id)
        print(results)
        return results