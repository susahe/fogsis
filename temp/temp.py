class CourseGroup(models.Model):
    course = models.ForeignKey(Course)
    code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=128)
    student = models.ManyToManyField(User, related_name="student")
    teacher = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Teachers_Diary(models.Model):
    activity = models.ForeignKey(Activity)
    coursegroup = models.ForeignKey(CourseGroup)
    completed = models.BooleanField()
    tobecompleted = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Theory_Lesson_Schedule(models.Model):
    activity = models.ForeignKey(Activity)
    tobecompleted = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coursegroup = models.ForeignKey(CourseGroup)

    def __str__(self):
        return self.activity


class Practical_Lesson_Schedule(models.Model):
    activity = models.ForeignKey(Activity)
    tobecompleted = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coursegroup = models.ForeignKey(CourseGroup)

    def __str__(self):
        return self.activity


class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.calendar = Calendar()

    def is_available(self, slot):
        return self.calendar.is_available(slot)

    def make_appointment(self, slot, record):
        self.calendar.add_entry(slot, record)

    def get_public_record(self):
        return {
            'name': self.full_name,
            'booking_class': self.__class__.__name__
        }


class Student(Person):
    def __init__(self, first_name, last_name, ssn):
        super(Student, self).__init__(first_name, last_name)
        self.ssn = ssn
        self.student_id = self.first_name[:1] + self.last_name + ssn


class Teacher(Person):
    def __init__(self, first_name, last_name, speciality):
        super(Teacher, self).__init__(first_name, last_name)
        self.speciality = speciality

    def get_public_record(self):
        record = super(Teacher, self).get_public_record()
        record['specialty'] = self.speciality
        return record


class Calendar(object):
    def __init__(self):
        self.entries = {}

    def is_available(self, slot):
        return slot not in self.entries
