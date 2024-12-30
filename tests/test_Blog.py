import pytest
import src.Service as Service
from blog.blog_pb2 import FilterBlogMessage, BlogContent, BlogList

from src.Mongo.connection import DATABASE_NAME, client
from src.Mongo.BlogCollection import BlogCollection

BLOG_1 = BlogContent(
    language="pl",
    title="jak stac sie bogatym",
    content="Trzeba zarabiac",
)

BLOG_2 = BlogContent(
    language="pl",
    title="jak gotowac",
    content="Trzeba gotowac",
)

BLOG_3 = BlogContent(
    language="en",
    title="Test Blog Entry",
    content="Test entry",
)


@pytest.fixture(autouse=True)
def setup():
    client.get_database(DATABASE_NAME).drop_collection("Blog")
    BlogCollection.create_collection_if_not_exists()


def test_get_blog_empty_db_success():
    s = Service.BlogService()
    request = FilterBlogMessage()
    resp = s.GetBlogs(request, None)

    assert len(resp.Blogs) == 0


def test_add_blog_success():
    s = Service.BlogService()
    resp = s.AddBlog(BLOG_1, None)

    assert resp.path == BLOG_1.title.lower().replace(" ", "-")
    assert resp.language == BLOG_1.language
    assert resp.title == BLOG_1.title
    assert resp.content == BLOG_1.content


def test_add_same_blog_more_than_once_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)

    resp = s.AddBlog(BLOG_1, None)

    assert resp.path == f"{BLOG_1.title.lower().replace(" ", "-")}-1"
    assert resp.language == BLOG_1.language
    assert resp.title == BLOG_1.title
    assert resp.content == BLOG_1.content


def test_get_blog_language_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = FilterBlogMessage(language="pl")
    resp = s.GetBlogs(request, None)

    assert len(resp.Blogs) == 2


def test_get_blog_title_wildcard_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = FilterBlogMessage(title="jak*")
    resp = s.GetBlogs(request, None)

    assert len(resp.Blogs) == 2


def test_get_blog_title_exact_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = FilterBlogMessage(title=BLOG_2.title)
    resp = s.GetBlogs(request, None)

    assert len(resp.Blogs) == 1
    assert resp.Blogs[0].title == BLOG_2.title
    assert resp.Blogs[0].content == BLOG_2.content
    assert resp.Blogs[0].language == BLOG_2.language


def test_get_blog_path_wildcard_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = FilterBlogMessage(path="jak-*")
    resp = s.GetBlogs(request, None)

    assert len(resp.Blogs) == 2


def test_get_blog_path_exact_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = FilterBlogMessage(path=BLOG_3.title.lower().replace(" ", "-"))
    resp = s.GetBlogs(request, None)

    assert len(resp.Blogs) == 1
    assert resp.Blogs[0].title == BLOG_3.title
    assert resp.Blogs[0].content == BLOG_3.content
    assert resp.Blogs[0].language == BLOG_3.language


def test_update_blog_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = BlogContent(
        path=BLOG_3.title.lower().replace(" ", "-"),
        language=BLOG_3.language,
        title="Updated Title",
        content="Updated Content",
    )

    resp = s.UpdateBlog(request, None)

    assert resp.title == request.title
    assert resp.content == request.content
    assert resp.language == request.language


def test_update_blog_fail():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = BlogContent(
        path=f"{BLOG_3.title.lower().replace(" ", "-")}-1",
        language=BLOG_3.language,
        title="Updated Title",
        content="Updated Content",
    )

    resp = s.UpdateBlog(request, None)

    assert resp.title == ""
    assert resp.content == ""
    assert resp.language == ""


def test_delete_blog_success():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = FilterBlogMessage(
        path=BLOG_3.title.lower().replace(" ", "-"),
        language=BLOG_3.language,
        title=BLOG_3.title,
    )
    resp = s.DeleteBlog(request, None)
    assert resp.title == BLOG_3.title
    assert resp.content == BLOG_3.content
    assert resp.language == BLOG_3.language


def test_delete_blog_fail():
    s = Service.BlogService()
    _ = s.AddBlog(BLOG_1, None)
    _ = s.AddBlog(BLOG_2, None)
    _ = s.AddBlog(BLOG_3, None)

    request = FilterBlogMessage(
        path=f"{BLOG_3.title.lower().replace(" ", "-")}-1",
        language=BLOG_3.language,
    )
    resp = s.DeleteBlog(request, None)
    assert resp.title == ""
    assert resp.content == ""
    assert resp.language == ""
