# Protocol Documentation

<a name="top"></a>

## Table of Contents

- [blog.proto](#blog-proto)

  - [BlogContent](#blog-BlogContent)
  - [BlogList](#blog-BlogList)
  - [FilterBlogMessage](#blog-FilterBlogMessage)

  - [Blog](#blog-Blog)

- [Scalar Value Types](#scalar-value-types)

<a name="blog-proto"></a>

<p align="right"><a href="#top">Top</a></p>

## blog.proto

<a name="blog-BlogContent"></a>

### BlogContent

Represent single blog

| Field    | Type              | Label | Description          |
| -------- | ----------------- | ----- | -------------------- |
| title    | [string](#string) |       | Title of the blog    |
| language | [string](#string) |       | Language of the blog |
| path     | [string](#string) |       | Path of the blog     |
| content  | [string](#string) |       | Content of the blog  |

<a name="blog-BlogList"></a>

### BlogList

| Field | Type                             | Label    | Description   |
| ----- | -------------------------------- | -------- | ------------- |
| Blogs | [BlogContent](#blog-BlogContent) | repeated | List of blogs |

<a name="blog-FilterBlogMessage"></a>

### FilterBlogMessage

Can filter blogs with parameters combined. If _ is used, the search is done with &#34;_&lt;provided_value&gt;\*&#34;

| Field    | Type              | Label | Description          |
| -------- | ----------------- | ----- | -------------------- |
| title    | [string](#string) |       | Title of the blog    |
| language | [string](#string) |       | Language of the blog |
| path     | [string](#string) |       | Path of the blog     |

<a name="blog-Blog"></a>

### Blog

| Method Name | Request Type                                 | Response Type                    | Description                                        |
| ----------- | -------------------------------------------- | -------------------------------- | -------------------------------------------------- |
| GetBlogs    | [FilterBlogMessage](#blog-FilterBlogMessage) | [BlogList](#blog-BlogList)       | If message is empty returns all blogs              |
| UpdateBlog  | [BlogContent](#blog-BlogContent)             | [BlogContent](#blog-BlogContent) | Request message contains updated content of a blog |
| DeleteBlog  | [FilterBlogMessage](#blog-FilterBlogMessage) | [BlogContent](#blog-BlogContent) | If path passed, blog is deleted                    |
| AddBlog     | [BlogContent](#blog-BlogContent)             | [BlogContent](#blog-BlogContent) | path is not mandatory                              |
