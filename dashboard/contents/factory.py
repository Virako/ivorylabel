from factory import Faker, LazyAttribute, SubFactory
from factory.django import DjangoModelFactory, ImageField

from contents.models import (
    Content,
    Member,
    Project,
    Service,
)


class ContentFactory(DjangoModelFactory):
    class Meta:
        model = Content

    about = Faker('paragraph', nb_sentences=5)
    recording = Faker('paragraph', nb_sentences=10)
    contact = Faker('paragraph', nb_sentences=5)


class MemberFactory(DjangoModelFactory):
    class Meta:
        model = Member

    content = SubFactory(ContentFactory)
    name = Faker('pystr', max_chars=255)
    desc = Faker('paragraph', nb_sentences=3)
    img = ImageField()


class ServiceFactory(DjangoModelFactory):
    class Meta:
        model = Service

    content = SubFactory(ContentFactory)
    name = Faker('pystr', max_chars=255)
    desc = Faker('paragraph', nb_sentences=3)
    icon = ImageField()


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project
        exclude = ('link1', 'link2', 'link3')

    link1 = Faker('url')
    link2 = Faker('url')
    link3 = Faker('url')

    content = SubFactory(ContentFactory)
    name = Faker('pystr', max_chars=255)
    slides = LazyAttribute(lambda obj: f'{obj.link1}\n{obj.link2}\n{obj.link3}')
