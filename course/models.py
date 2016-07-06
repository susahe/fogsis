# import modules
# all models are display here
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# course model
class Course(models.Model):
    name = models.CharField(max_length=250)  # name of the course
    instructor = models.ForeignKey(User, related_name='Instructor')
    code = models.CharField(max_length=10)  # course code
    duration = models.IntegerField(default=0)  # course duration
    fees = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    course_logo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class CourseModule(models.Model):
    course = models.ForeignKey(Course)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    fees = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    theory_hrs = models.IntegerField(default=0)
    practical_hrs = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(CourseModule, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Task(models.Model):
    course_module = models.ForeignKey(CourseModule)
    code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=128)
    fees = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    theory_hrs = models.IntegerField(default=0)
    practical_hrs = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    topic = models.ForeignKey(Task)
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=128)
    fees = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Activity(models.Model):
    GENRE_CHOICES1 = (
        ('de', 'Demostration'),
        ('pr', 'Presentation'),
        ('ex', 'Exercise'),
        ('as', 'Assignment'),
        ('pr', 'Project'),
        ('db', 'Debate'),
        ('qu', 'Questining'),
    )
    GENRE_CHOICES2 = (('t', 'Theory'), ('p', 'Practical'), ('l', 'Lab'),)
    leson = models.ForeignKey(Lesson)
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=128)
    fees = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    duration = models.IntegerField(default=0)
    activity_type = models.CharField(max_length=15, choices=GENRE_CHOICES1)
    session = models.CharField(max_length=15, choices=GENRE_CHOICES2)
    iscompleted = models.BooleanField()

    def __str__(self):
        return self.name

# class CourseGroup(modles.Model):
