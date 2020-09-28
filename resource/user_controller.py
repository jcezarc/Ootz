import hashlib

def users():
    return [
        '0be4dcf35d0b5ecba3f98af6ecd2aa87',
        'c9bd6f90ca8e3f91163623fe243907e9',
    ]

def encode_user(user, password):
    hash_object = hashlib.md5(
        f'{user}:{password}'.encode()
    )
    return hash_object.hexdigest()

def valid_user(user, password):
    #------- initial examples --------
    #       valid_user('Klaus Sandrini', 'OperaDeArame')
    #       valid_user('Julio Cascalles', 'novoFuncionario')
    #---------------------------------
    user_id = encode_user(user, password)
    found = user_id in users()
    return found, user_id
