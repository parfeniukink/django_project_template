from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Custom User Manager."""

    def create_user(self, email, username=None, password=None, **kwargs):
        if not email:
            raise ValueError("Email field is required.")
        if not password:
            raise TypeError("User must have a password.")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **kwargs):
        superuser_paylod = {"is_superuser": True, "is_active": True, "is_staff": True}
        return self.create_user(
            email=email, username=username, password=password, **superuser_paylod
        )
