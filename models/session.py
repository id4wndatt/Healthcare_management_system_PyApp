class Session:
    current_user = None
    current_user_id = None

    @classmethod
    def login(cls, user):
        cls.current_user = user

    @classmethod
    def logout(cls):
        cls.current_user = None

    @classmethod
    def get_current_user(cls):
        return cls.current_user

    @classmethod
    def get_current_user_id(cls):
        return cls.current_user_id
