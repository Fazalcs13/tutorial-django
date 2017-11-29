from django.db import models


class User(models.Model):
    UserName = models.TextField()
    Password = models.TextField()

    def __str__(self):
        return  self.UserName

class CoursesModel1(models.Model):

    MICROSOFT = 'MOS'
    GRAPHIC = 'GD'
    SOUND = 'SM'
    WEBSITE = 'WD'
    ANIMATION = 'AP'
    VIDEO = 'VE'

    course_thumbanilImage = models.ImageField()
    course_title = models.TextField()
    course_subTitle = models.TextField()
    course_author_image = models.ImageField()
    course_author_name = models.TextField()
    course_date = models.TextField()
    course_duration = models.TextField()
    COURSE_CATEGORY_CHOICES = (
        (MICROSOFT, 'Microsoft Office Suite'),
        (GRAPHIC, 'Graphic Design'),
        (SOUND, 'Sound & Music'),
        (WEBSITE, 'Web Site Development'),
        (ANIMATION, 'Animation Production'),
        (VIDEO, 'Video Editing'),
    )
    course_category = models.CharField(max_length=5,
                                      choices=COURSE_CATEGORY_CHOICES,
                                      default=MICROSOFT)

    def __str__(self):
        return self.course_title

