from django.core.management import BaseCommand
from wagtail_wordpress_importer.utils import spinner


class BaseProcessCommand(BaseCommand):

    def output_start(self, message, newline=''):
        self.stdout.write(message, ending=newline)

    def output_message_success(self, message, newline=''):
        self.stdout.write(self.style.SUCCESS(message), ending=newline)

    def output_message_warning(self, message, newline=''):
        self.stdout.write(self.style.WARNING(message), ending=newline)

    def output_message_end(self, message, newline='\n', symbol='tick'):
        SYMBOLS = {
            'tick': ' ✅',
            'wait': ' ⌛️',
            'boom': ' 💥',
            'popper': ' 🎉',
            'flag': ' 🏁'
        }
        self.stdout.write(message + SYMBOLS[symbol], ending=newline)

    def output_spinner(self):
        self.stdout.write(next(spinner), ending='\b')
