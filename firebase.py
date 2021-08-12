from google.cloud import firestore

def get_user(user):
    """Retrieves a user by email

    Args:
        user (dict): {
            email: (string) email address
            first_name: (string) first name
            last_name: (string) last name
        }
    """
    try:
        print (f'Retrieving user: {user}')
        db = firestore.Client()

        docs = db.collection(u'users').where(u'email', '==', user['email']).get()

        if len(docs) == 0:
            # create user if doesn't exist
            return insert_user(user)

        for doc in docs:
            id = doc.id
            user = doc.to_dict()
            user['id'] = id
            return user
            
    except Exception as e:
        raise e

def insert_user(user):
    """Inserts a user by email

    Args:
        user (dict): {
            email: (string) email address
            first_name: (string) first name
            last_name: (string) last name
        }
    
    Returns:
        id: (string) document Id
    """
    try:
        print (f'Inserting user: {user}')
        db = firestore.Client()
        doc = db.collection(u'users').add(user)
        return doc[1].id
    except Exception as e:
        raise e
