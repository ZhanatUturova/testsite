from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = 'Новости'    # меняем название для админки с названия модели на свое
