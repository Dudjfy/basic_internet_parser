"""A program which parses INIT College's website for teacher names,
and returns a picture och chosen teacher"""


import urllib
import requests as req
from bs4 import BeautifulSoup
from PIL import Image


class Teacher:
    """A teacher class with name:str and src:str variables"""
    def __init__(self, name, src):
        self.name = name
        self.src = src

    def __str__(self):
        return self.name

    def get_src(self):
        """Returns src"""
        return self.src


def get_teachers(imgs, alpha_sorted=True):
    """Revives imgs tags and optional sorted for alphabetically sorted list.
    Returns teachers list with teacher objects."""
    teacher_list = []
    for img in imgs:
        if len(img.attrs) == 3 and "title" in img.attrs and "src" in img.attrs:
            teacher_list.append(Teacher(img["title"], img["src"]))
    if alpha_sorted:
        teacher_list.sort(key=lambda x: x.name)
    return teacher_list


def print_teachers_names(teacher_list):
    """Receives optional parameter sorted for alphabetically sorted list.
    Returns teacher's names with normal indexes from teachers list."""

    teacher_names = [teacher.name for teacher in teacher_list]

    for i, name in enumerate(teacher_names):
        print(f"{str(i + 1) + '.':<3} {name:<40}")


def get_teacher_from_imp():
    """Returns teacher's index in the teacher list"""
    return int(input("Chose teacher by entering their position in the list above: ").strip()) - 1


def get_teacher_img(teacher):
    """Receives a teacher object, returns teacher's img object"""
    urllib.request.urlretrieve(teacher.src, "teacher.jpg")
    return Image.open("teacher.jpg")


url = req.get("https://initcollege.se/kontakt/")
soup = BeautifulSoup(url.text, "html.parser")

teacher_imgs_tags = soup.find_all("img")
teachers = get_teachers(teacher_imgs_tags)
print_teachers_names(teachers)

teacher_displayed = teachers[get_teacher_from_imp()]
teacher_img = get_teacher_img(teacher_displayed)
teacher_img.show()
