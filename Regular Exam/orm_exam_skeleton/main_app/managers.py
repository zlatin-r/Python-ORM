from django.db import models


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return self.annotate(count_missions=models.Count('missions')).order_by('-count_missions', 'phone_number')
