from django.db import models
from viewflow.models import Process, Task
from multiselectfield import MultiSelectField

LEAVE_TYPES = (('annual', 'Annual'), ('excused', 'Excused'), ('other', 'Other'))
JOB_TITLES = (('developer', 'Developer'), ('manager', 'Manager'))
PROGRAMMING_LANGUAGE = (
    ('go', 'Golang'), ('python', 'Python'), ('java', 'Java'))
MANAGER_ITEMS = (('house', 'House'), ('car', 'Car'))


class Leave(models.Model):
    leave_type = models.CharField(choices=LEAVE_TYPES, blank=True,
                                  max_length=250)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    description = models.CharField(max_length=500, default="")
    person = models.ForeignKey("Person", null=True, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    surname = models.CharField(max_length=100)
    job_title = models.CharField(choices=JOB_TITLES, blank=True, max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} {self.surname}"


class Manager(Person):
    manager_items = MultiSelectField(choices=MANAGER_ITEMS)

    class Meta:
        permissions = [
            ('can_approve_leave', 'Can approve leave form'),
            ('can_create_leave', 'Can create leave form'),

        ]


class Developer(Person):
    programming_language = models.CharField(choices=PROGRAMMING_LANGUAGE,
                                            blank=True, max_length=250)
    manager = models.ForeignKey("Manager", null=True, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('can_create_leave', 'Can create leave form'),
        ]


class Ceo(Person):
    class Meta:
        permissions = [
            ('can_approve_leave', 'Can approve leave form'),
        ]


class LeaveProcess(Process):
    leave = models.ForeignKey("Leave", blank=True, null=True,
                              on_delete=models.CASCADE)

    # def need_extra_insurance(self):
    #     try:
    #         return self.shipment.need_insurance
    #     except Shipment.DoesNotExist:
    #         return None

    class Meta:
        verbose_name_plural = 'Leave process list'


class LeaveTask(Task):
    class Meta:
        proxy = True
