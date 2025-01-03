# Mongo_Manager

This Python microservice enables interaction with a MongoDB database, focusing on the Blog collection and providing additional utility functions. Key features include:

- CRUD Operations: Offers a comprehensive set of functions to perform CRUD operations on the Blog collection, along with retrieval functions for secrets, currency, and password.
- MongoDB Integration: Uses the `pymongo` library for efficient communication with the MongoDB database.
- `Distributed Tracing`: Integrated with OpenTelemetry to capture and send trace data to Grafana Tempo (host: `Tempo`, port: `4317`), a scalable, open-source distributed tracing backend.
- `Prometheus Metrics`: Exposes Prometheus-compatible metrics on port `8111` for real-time monitoring and performance tracking.
- `gRPC Server`: Operates a gRPC server on port `50051` for fast and reliable client-server communication.

This microservice is designed for modern application needs, combining database interaction, observability, and scalability in one solution.

# gRPC Services

## Blog

| Method Name | Request Type                                         | Response Type                            | Description                                          |
| ----------- | ---------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------- |
| GetBlogs    | [FilterBlogMessage](/Docs/blog.md#filterblogmessage) | [BlogList](/Docs/blog.md#bloglist)       | Get Blogs according to provided Filter.              |
| AddBlog     | [BlogContent](/Docs/blog.md#blogcontent)             | [BlogContent](/Docs/blog.md#blogcontent) | Insert new blog.                                     |
| UpdateBlog  | [BlogContent](/Docs/blog.md#blogcontent)             | [BlogContent](/Docs/blog.md#blogcontent) | Update existing Blog based on provided blog content. |
| DeleteBlog  | [FilterBlogMessage](/Docs/blog.md#filterblogmessage) | [BlogContent](/Docs/blog.md#blogcontent) | Delete Blog from DB.                                 |

## Currency

| Method Name            | Request Type                                         | Response Type                                        | Description                                 |
| ---------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------- |
| GetCurrencyType        | [CurrencyDetails](/Docs/currency.md#currencydetails) | [CurrencyTypeMsg](/Docs/currency.md#currencytypemsg) | Returns type of provided currency.          |
| GetSupportedCurrencies | [CurrencyTypeMsg](/Docs/currency.md#currencytypemsg) | [CurrencyList](/Docs/currency.md#currencylist)       | Returns list of currencies in a given type. |

## PasswordChecker

| Method Name   | Request Type                                         | Response Type                                    | Description                  |
| ------------- | ---------------------------------------------------- | ------------------------------------------------ | ---------------------------- |
| CheckPassword | [PasswordMessage](/Docs/password.md#passwordmessage) | [CheckResponse](/Docs/password.md#checkresponse) | Check if password is common. |

### SecretStore

| Method Name | Request Type                               | Response Type                                | Description                            |
| ----------- | ------------------------------------------ | -------------------------------------------- | -------------------------------------- |
| GetSecret   | [SecretName](/Docs/password.md#secretname) | [SecretValue](/Docs/password.md#secretvalue) | Get secret value based on secret name. |
