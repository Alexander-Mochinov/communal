from django.db import models
from django.forms import model_to_dict
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as Manager


class UserManager(Manager):

    def create_user(self, personal_account, password=None, is_admin=False, is_staff=False, is_active=True):
        if not personal_account:
            raise ValueError("User must have an personal_account")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            personal_account=personal_account
        )
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, personal_account, password=None, **extra_fields):
        if not personal_account:
            raise ValueError("User must have an personal_account")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            personal_account=personal_account,
        )
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Расширенный пользователь"""

    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format."
    )
    username = None
    email = models.EmailField(verbose_name="Email", unique=True, null=True, blank=True)
    first_name = models.CharField(verbose_name="Имя", max_length=25, unique=True, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Статус активности", default=True)
    second_name = models.CharField(verbose_name="Фамилия", max_length=25, unique=True, null=True, blank=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=25, unique=True, null=True, blank=True)
    personal_account = models.CharField(verbose_name="Лицевой счёт", max_length=25, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name="Дата регистрации", auto_now_add=True)
    hide_personal_data = models.BooleanField(verbose_name="Скрыть персональные данные:", default=False, blank=True)
    user_photo = models.ImageField(verbose_name="Фото профиля", upload_to="users/personal-img/", null=True, blank=True)
    phone = models.CharField(verbose_name="Мобильный номер телефона", validators=[phone_regex], max_length=17, blank=True)
    address = models.ForeignKey("users.Address", on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(verbose_name="Является ли сотрудником", default=False)
    is_supervisor = models.BooleanField(verbose_name="Является ли руководителем", default=False)
    objects = UserManager()

    def save(self, *args, **kwargs):
        from users.models import Address

        self.address = Address.objects.create()
        super(User, self).save(*args, **kwargs)

    USERNAME_FIELD = "personal_account"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.personal_account

    def to_json(self):
        return model_to_dict(self)

    def has_permission(self, perm):
        """Проверка прав пользователя на совершения действия"""

        if self.is_active and self.is_superuser:
            return True

        return perm in self.user_permissions.all()
        
    __repr__ = __str__

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
