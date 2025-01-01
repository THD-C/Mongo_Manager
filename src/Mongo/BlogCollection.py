from pymongo.errors import CollectionInvalid
from pydantic import BaseModel, Field, field_validator
import string

from src.Mongo.connection import client, DATABASE_NAME

PATH_ALLOWED_CHARS = string.ascii_lowercase + string.digits + "-"


class Blog(BaseModel):
    path: str = Field(init=True, default=None)
    language: str = Field(init=True)
    title: str = Field(init=True)
    content: str = Field(init=True)

    @field_validator("path")
    def path_validator(cls, value: str):
        return path_post_init(cls, value)

    @field_validator("language")
    def language_validator(cls, value: str):
        return language_post_init(cls, value)

    def __eq__(self, other):
        if not isinstance(other, Blog):
            return False

        if self.path != other.path:
            return False

        if self.language != other.language:
            return False

        if self.title != other.title:
            return False

        if self.content != other.content:
            return False

        return True

    def generate_path(self):
        if self.path is not None:
            return
        prohibited_chars = set()
        for char in self.title.lower():
            if char not in PATH_ALLOWED_CHARS:
                prohibited_chars.add(char.lower())

        self.path = self.title.lower().replace(" ", "-")
        for char in prohibited_chars:
            self.path = self.path.replace(char, "")


class BlogSearch(BaseModel):
    path: str = Field(init=True, default="*")
    language: str = Field(init=True, default="*")
    title: str = Field(init=True, default="*")

    @field_validator("path")
    def path_validator(cls, value: str):
        if value is None:
            return value
        return path_post_init(cls, value)

    @field_validator("language")
    def language_validator(cls, value: str):
        return language_post_init(cls, value)

    @field_validator("title")
    def title_validator(cls, value: str):
        if value == "":
            return "*"
        return value

    def get_mongo_filter(
        self, allow_regex: bool = True, exclude_title: bool = False
    ) -> dict:
        result: dict[str, str] = {
            k: v for k, v in self.model_dump().items() if v is not None
        }
        if exclude_title:
            result.pop("title")

        if allow_regex:
            for key, value in result.items():
                if "*" in value:
                    result[key] = {"$regex": value.replace("*", ""), "$options": "i"}

        return result


def path_post_init(cls, value: str):
    if value == "":
        return "*"
    value = value.lower()
    allowed_chars = PATH_ALLOWED_CHARS
    if cls is BlogSearch:
        allowed_chars += "*"
    for char in value:
        if char not in allowed_chars:
            raise ValueError(f"Invalid character in path: {char}")
    return value


def language_post_init(cls, value: str):
    if value == "":
        return "*"
    return value.lower()


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
    def get_blog(filter: BlogSearch, exclude_title_check: bool = False) -> list[Blog]:

        try:
            return [
                Blog(**item)
                for item in (
                    client.get_database(DATABASE_NAME)
                    .get_collection(BlogCollection.__collection)
                    .find(filter.get_mongo_filter(exclude_title=exclude_title_check))
                )
            ]
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def add_blog(blog_entry: Blog) -> Blog:
        blog_entry.generate_path()
        counter = 1
        requested_path = blog_entry.path

        while True:
            search = BlogSearch(**blog_entry.model_dump())
            if not BlogCollection.get_blog(search, exclude_title_check=True):
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

        blog_list: list[Blog] = BlogCollection.get_blog(
            search, exclude_title_check=True
        )

        if not blog_list or len(blog_list) != 1:
            return None

        blog_entry: Blog = blog_list[0]

        try:
            client.get_database(DATABASE_NAME).get_collection(
                BlogCollection.__collection
            ).delete_one(blog_entry.model_dump())
        except Exception as e:
            print(e)
            return None

        blog_list: list[Blog] = BlogCollection.get_blog(
            search, exclude_title_check=True
        )

        if blog_list or len(blog_list) != 0:
            return None

        return blog_entry

    @staticmethod
    def update_blog(blog_entry: Blog) -> Blog:

        search = BlogSearch(**blog_entry.model_dump())

        blog_list: list[Blog] = BlogCollection.get_blog(
            search, exclude_title_check=True
        )

        if not blog_list or len(blog_list) != 1:
            return None

        try:
            client.get_database(DATABASE_NAME).get_collection(
                BlogCollection.__collection
            ).update_one(
                search.get_mongo_filter(exclude_title=True),
                {"$set": blog_entry.model_dump()},
            )
        except Exception as e:
            print(e)
            return None

        blog_list: list[Blog] = BlogCollection.get_blog(
            search, exclude_title_check=True
        )

        if not blog_list[0] == blog_entry:
            return None

        return blog_list[0]


BlogCollection.create_collection_if_not_exists()
