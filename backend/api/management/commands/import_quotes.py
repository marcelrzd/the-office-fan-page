import os
import json
from django.core.management.base import BaseCommand
from ...models import Quote, Character  # Import your Quote model


class Command(BaseCommand):
    help = 'Import quotes from JSON file to database'

    def handle(self, *args, **options):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        json_file_path = os.path.join(script_directory, 'quotes.json')

        with open(json_file_path) as json_file:
            data = json.load(json_file)

            for item in data:
                quote = Quote(
                    id=item['id'],
                    character=Character.objects.filter(
                        name=item['character']).first(),
                    quote=item['quote']
                )
                quote.save()

        self.stdout.write(self.style.SUCCESS('Quotes imported successfully'))
