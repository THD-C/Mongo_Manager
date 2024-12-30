from blog.blog_pb2_grpc import BlogServicer
from blog.blog_pb2 import FilterBlogMessage, BlogContent, BlogList

from src.Mongo.BlogCollection import BlogCollection, BlogSearch, Blog


class BlogService(BlogServicer):

    def GetBlogs(self, request: FilterBlogMessage, context):
        search = BlogSearch(
            path=request.path,
            language=request.language,
            title=request.title,
        )
        blog_list: list[Blog] = BlogCollection.get_blog(search)

        return BlogList(Blogs=[BlogContent(**b.model_dump()) for b in blog_list])

    def AddBlog(self, request: BlogContent, context):
        blog_entry = Blog(
            language=request.language,
            title=request.title,
            content=request.content,
        )
        result = BlogCollection.add_blog(blog_entry)
        if not result:
            return BlogContent()
        return BlogContent(**result.model_dump())

    def DeleteBlog(self, request: FilterBlogMessage, context):
        search = BlogSearch(
            path=request.path,
            language=request.language,
        )
        result = BlogCollection.delete_blog(search)
        if not result:
            return BlogContent()
        return BlogContent(**result.model_dump())

    def UpdateBlog(self, request: BlogContent, context):
        blog_entry = Blog(
            path=request.path,
            language=request.language,
            title=request.title,
            content=request.content,
        )
        result = BlogCollection.update_blog(blog_entry)
        if not result:
            return BlogContent()
        return BlogContent(**result.model_dump())
