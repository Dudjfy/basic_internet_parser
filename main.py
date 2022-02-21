import urllib

import requests
from bs4 import BeautifulSoup
from PIL import Image


class Teacher:
    """A teacher class with name:str and src:str variables"""
    def __init__(self, name, src):
        self.name = name
        self.src = src

    def __str__(self):
        return self.name


def get_teachers(imgs):
    """Revives imgs tags. Returns teachers list with teacher objects."""
    teachers = []
    for img in imgs:
        if len(img.attrs) == 3 and "title" in img.attrs and "src" in img.attrs:
            teachers.append(Teacher(img["title"], img["src"]))
    return teachers


def print_teachers_names(teachers, sorted=True):
    """Receives optional parameter sorted for sorted list.
    Returns teacher's names with normal indexes from teachers list."""

    teacher_names = [teacher.name for teacher in teachers]
    if sorted:
        teacher_names.sort()

    [print(f"{str(i + 1) + '.':<3} {name:<40}") for i, name in enumerate(teacher_names)]


def get_teacher_from_imp():
    """Returns teacher's index in the teacher list"""
    return int(input("Chose teacher by entering their position in the list above: ").strip()) - 1


def get_teacher_img(teacher):
    """Receives a teacher object, returns teacher's img object"""
    urllib.request.urlretrieve(teacher.src, "teacher.jpg")
    return Image.open("teacher.jpg")


r = requests.get("https://initcollege.se/kontakt/")
soup = BeautifulSoup(r.text, "html.parser")

imgs = soup.find_all("img")
teachers = get_teachers(imgs)
print_teachers_names(teachers)

teacher = teachers[get_teacher_from_imp()]
teacher_img = get_teacher_img(teacher)
teacher_img.show()
