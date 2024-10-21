from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    humidity = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"Weather in {self.city} on {self.date_time.strftime('%Y-%m-%d %H:%M:%S')}"
