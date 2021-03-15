from django.apps import AppConfig


class NampConfig(AppConfig):
    name = 'namp'

    def ready(self):
    	import namp.signals
