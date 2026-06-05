from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

# For auto seeding defualt Categories after signup
class FinanceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    def ready(self):
        import main_app.signals