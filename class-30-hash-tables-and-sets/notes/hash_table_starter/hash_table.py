class HashTable():
    """
    Implements a HashTable using a Dictionary at the moment.
    Your task is to remove use of Dictionary but maintain the api.
    You'll need a hashing function and handle collisions
    """

    def __init__(self):
        self._dict = {}

    def __repr__(self):
        return "<HashTable: {}>".format('coming soon')

    def __len__(self):
        return len(self._dict)

    def _hash_key(self, key):
        return 'replace me'

    def get(self, key):
        return self._dict[key]

    def set(self, key, value):
        self._dict[key] = value

    