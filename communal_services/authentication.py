from users.models import User


class PersonalAccountAuthBackend(object):
    """Выполняет аутентификацию пользователя по e-mail."""

    def authenticate(self, request, personal_account=None, password=None):
        try:
            user = User.objects.get(personal_account=personal_account)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None