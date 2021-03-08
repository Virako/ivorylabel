import pytest

from contents.factory import ContentFactory
from contents.factory import ServiceFactory
from contents.factory import ProjectFactory
from contents.factory import MemberFactory
from contents.generate_json_content import generate_json_content


@pytest.mark.django_db
def test_generate_json_content_no_content():
    result = generate_json_content()
    assert result == {}


@pytest.mark.django_db
def test_generate_json_content_with_content_only():
    content = ContentFactory()
    result = generate_json_content()

    assert result.get('about') == content.about
    assert result.get('recording') == content.recording
    assert result.get('contact') == content.contact

    assert result.get('members') == []
    assert result.get('services') == []
    assert result.get('projects') == []


@pytest.mark.django_db
def test_generate_json_content_full_content():
    content = ContentFactory()
    MemberFactory.create_batch(3, content=content, img=None)
    ServiceFactory.create_batch(3, content=content, icon=None)
    ProjectFactory.create_batch(3, content=content)

    result = generate_json_content()

    assert result.get('about') == content.about
    assert result.get('recording') == content.recording
    assert result.get('contact') == content.contact

    assert len(result.get('members')) == 3
    assert 'name' in result.get('members')[0].keys()
    assert 'desc' in result.get('members')[0].keys()
    assert 'img' in result.get('members')[0].keys()

    assert len(result.get('services')) == 3
    assert 'name' in result.get('services')[0].keys()
    assert 'desc' in result.get('services')[0].keys()
    assert 'icon' in result.get('services')[0].keys()

    assert len(result.get('projects')) == 3
    assert 'name' in result.get('projects')[0].keys()
    assert 'slides' in result.get('projects')[0].keys()
