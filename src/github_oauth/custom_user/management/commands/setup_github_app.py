import os
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Set up github oauth from environment vars (.env)"

    def handle(self, *args, **options):
        github_client_id = os.getenv("GITHUB_CLIENTID")
        github_secret = os.getenv("GITHUB_SECRET")

        if github_client_id and github_secret:

            # set default site to localhost
            Site.objects.filter(domain="example.com").update(
                domain="127.0.0.1", name="localhost"
            )

            if not SocialApp.objects.exists():
                obj = SocialApp.objects.create(
                    provider="github",
                    name="Github Example",
                    client_id=github_client_id,
                    secret=github_secret,
                )
                obj.sites.add(Site.objects.first())
                print(f"Created: {obj}")
        else:
            raise CommandError(
                "GITHUB_CLIENTID and GITHUB_SECRET must be defined in .env (or environment)"
            )
