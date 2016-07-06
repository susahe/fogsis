from django.contrib import admin

# Register your models here.
from .models import Course, CourseModule, Task, Lesson, Activity

admin.site.register(Course)
admin.site.register(CourseModule)
admin.site.register(Task)
admin.site.register(Lesson)
admin.site.register(Activity)
