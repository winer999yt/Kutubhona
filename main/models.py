from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=255)
    kurs = models.IntegerField()
    kitob_soni = models.IntegerField()

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10)
    tugilgan_sana = models.DateField()
    kitob_soni = models.IntegerField()
    tirik = models.BooleanField()

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255)
    sahifa = models.IntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.ism

class  Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateField(blank=True, null=True)
    qaytarish_sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.talaba} - {self.kitob} ({self.olingan_sana})"



