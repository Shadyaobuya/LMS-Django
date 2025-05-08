from django.db import models
from lms_auth.models import ModificationTrackingModel, CustomUser as User


class Course(ModificationTrackingModel):
    name = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        help_text="Enter the name of the course",
    )

    code = models.CharField(
        max_length=20,
        null=True,
        help_text="Enter the course code. Maximum 20 characters.",
    )

    lecturer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lecturer_courses",
        null=False,
        blank=False,
        help_text="Select the lecturer responsible for the course.",
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text="Provide a brief description of the course.",
    )

    class Meta:
        db_table = "course"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "lecturer"], name="unique-course-lecturer"
            )
        ]

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


class CourseEnrollment(ModificationTrackingModel):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrolled_courses",
        null=False,
        blank=False,
        help_text="Select the student enrolling in the course.",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrolled_students",
        null=False,
        blank=False,
        help_text="Select the course for enrollment.",
    )
    date_enrolled = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the student enrolled in the course.",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("active", "Active"),
            ("completed", "Completed"),
            ("dropped", "Dropped"),
        ],
        default="active",
        help_text="Enrollment status of the student in the course.",
    )
    grade = models.IntegerField(
        null=True,
        blank=True,
        help_text="Grade obtained by the student in the course.",
    )

    class Meta:
        db_table = "course_enrollment"
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"], name="unique-student-course-enrollment"
            )
        ]

    def __str__(self):
        return f"{self.__class__.__name__} : {self.student.username}-{self.course.name}"


class Topic(ModificationTrackingModel):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Name of the topic.",
    )
    description = models.TextField(
        null=False,
        blank=False,
        help_text="Short summary of the topic.",
    )
    video_url = models.URLField(
        null=True, blank=True, help_text="The link to the topic"
    )
    document = models.FileField(
        upload_to="topics/",
        null=True,
        blank=True,
        help_text="Upload the topic file. Allowed formats: PDF, DOCX.",
    )
    course = models.ForeignKey(
        Course, related_name="topics", on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        db_table = "topic"
        constraints = [
            models.UniqueConstraint(
                fields=["course", "name"], name="unique-topic-course"
            )
        ]

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


class Assignment(ModificationTrackingModel):
    name = models.CharField(
        max_length=30,
        default="",
        null=False,
        blank=False,
        help_text="Enter the name of the assignment. Maximum 30 characters.",
    )
    assignment_topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="assignment_topics",
        null=False,
        blank=False,
        help_text="topic tied to assignment",
    )

    document = models.FileField(
        upload_to="assignments",
        null=True,
        blank=True,
        help_text="Upload the assignment document. Allowed formats: PDF, DOCX.",
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text="Provide a brief description of the assignment.",
    )

    class Meta:
        db_table = "assignment_course"

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"
