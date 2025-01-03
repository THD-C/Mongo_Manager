# Protocol Documentation

<a name="top"></a>

## Table of Contents

- [password.proto](#password-proto)

  - [CheckResponse](#password-CheckResponse)
  - [PasswordMessage](#password-PasswordMessage)

  - [PasswordChecker](#password-PasswordChecker)

- [Scalar Value Types](#scalar-value-types)

<a name="password-proto"></a>

<p align="right"><a href="#top">Top</a></p>

## password.proto

<a name="password-CheckResponse"></a>

### CheckResponse

| Field    | Type          | Label | Description                                                                   |
| -------- | ------------- | ----- | ----------------------------------------------------------------------------- |
| isCommon | [bool](#bool) |       | Boolean value if password is common (True - it is common and can not be used) |

<a name="password-PasswordMessage"></a>

### PasswordMessage

| Field    | Type              | Label | Description       |
| -------- | ----------------- | ----- | ----------------- |
| password | [string](#string) |       | Password to check |

<a name="password-PasswordChecker"></a>

### PasswordChecker

| Method Name   | Request Type                                 | Response Type                            | Description                 |
| ------------- | -------------------------------------------- | ---------------------------------------- | --------------------------- |
| CheckPassword | [PasswordMessage](#password-PasswordMessage) | [CheckResponse](#password-CheckResponse) | Check if password is common |
