from pymongo import MongoClient
from werkzeug.security import generate_password_hash

from user import User

client = MongoClient("mongodb+srv://test:<password>@chatapp.rzcpb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users")


def save_user(username, email, password,):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})

def challenge_keys(keys):
    users_collection.insert_one({'keys': thekey})

def historic_flags(bank_intervention, by_whom, overriden_by_bank,overriden_when,reason,risk_score,support_key_used):
    users_collection.insert_one({'b_intervention': bank_intervention, 'username': by_whom, 'overidenbybank': overriden_by_bank,"overriddenwhen":overriden_when,"riskscore": risk_score,"supportkeyused":support_key_used})

def risk_intelligence(average_risk_score, current_risk_score, flags):
    users_collection.insert_one({'averageriskscore': average_risk_score, 'currentriskscore': current_risk_score, 'historicflags': flags})

def secret_keys(secretkeys):
    users_collection.insert_one({'secret-keys': secretkeys})

def existinglogin(account_number, behaviour_analysis, customer_id,challenge_keys):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})

def get_user(username):
    user_data = users_collection.find_one({'_id': username})
    return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None


