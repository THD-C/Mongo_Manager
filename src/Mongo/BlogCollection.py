from pymongo.errors import CollectionInvalid
from src.Mongo.connection import client, DATABASE_NAME
from pydantic import BaseModel, Field


class Blog(BaseModel):
    path: str
    language: str
    title: str
    content: str

    def __init__(self, **data):
        data["path"] = data["path"].lower()
        data["language"] = data["language"].lower()

        super().__init__(**data)


class BlogSearch(BaseModel):
    path: str = Field(init=True)
    language: str = Field(init=True)

    def __init__(self, **data):
        data["path"] = data["path"].lower()
        data["language"] = data["language"].lower()

        super().__init__(**data)


class BlogCollection:

    __collection = "Blog"

    @staticmethod
    def create_collection_if_not_exists():
        db = client.get_database(DATABASE_NAME)
        try:
            db.create_collection(BlogCollection.__collection)
        except CollectionInvalid:
            print("Collection already exists")

    @staticmethod
    def get_blog(filter: BlogSearch) -> Blog:
        try:
            return Blog(
                **(
                    client.get_database(DATABASE_NAME)
                    .get_collection(BlogCollection.__collection)
                    .find_one(filter.model_dump())
                )
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def add_blog(blog_entry: Blog) -> Blog:
        counter = 1
        requested_path = blog_entry.path

        while True:
            search = BlogSearch(**blog_entry.model_dump())
            if not BlogCollection.get_blog(search):
                break
            blog_entry.path = f"{requested_path}-{counter}"
            counter += 1

        try:
            client.get_database(DATABASE_NAME).get_collection(
                BlogCollection.__collection
            ).insert_one(blog_entry.model_dump())
        except Exception as e:
            print(e)
            return None

        return blog_entry

    @staticmethod
    def delete_blog(filter: BlogSearch) -> Blog:

        search = BlogSearch(**filter.model_dump())

        blog_entry = BlogCollection.get_blog(search)

        if not blog_entry:
            return None

        try:
            client.get_database(DATABASE_NAME).get_collection(
                BlogCollection.__collection
            ).delete_one(filter.model_dump())
        except Exception as e:
            print(e)
            return None

        return blog_entry

    @staticmethod
    def update_blog(blog_entry: Blog) -> Blog:

        search = BlogSearch(**blog_entry.model_dump())

        if not BlogCollection.get_blog(search):
            return None

        try:
            client.get_database(DATABASE_NAME).get_collection(
                BlogCollection.__collection
            ).update_one(search.model_dump(), {"$set": blog_entry.model_dump()})
        except Exception as e:
            print(e)
            return None

        return blog_entry


BlogCollection.create_collection_if_not_exists()
