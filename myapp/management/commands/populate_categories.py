
from myapp.models import Categories
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):

    help = "To populate the data for post"

    def handle(self, *args: Any, **kwargs: Any):

        # delete existing data
        Categories.objects.all().delete()

        categories = [
            "Technology",
            "Environment",
            "Workplace",
            "Science",
            "Energy",
            "AI",
            "Economy",
            "Finance",
            "Marketing",
            "Healthcare",
            "Space",
            "Psychology",
            "Social Media",
            "Cooking",
            "Diversity",
            "Sustainability",
            "Globalization",
            "Mindfulness",
            "Education",
            "Art & Technology"
        ]

        # for i in range(len(titles)):
        #     post.objects.create(
        #         title=titles[i],
        #         content=contents[i],
        #         image_url=img_urls[i]
        #     )

        for name in categories:
            Categories.objects.create(
                name=name
            )

        self.stdout.write(self.style.SUCCESS("Data populated successfully!"))