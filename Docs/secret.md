# Protocol Documentation

<a name="top"></a>

## Table of Contents

- [secret.proto](#secret-proto)

  - [SecretName](#secret-SecretName)
  - [SecretValue](#secret-SecretValue)

  - [SecretStore](#secret-SecretStore)

- [Scalar Value Types](#scalar-value-types)

<a name="secret-proto"></a>

<p align="right"><a href="#top">Top</a></p>

## secret.proto

<a name="secret-SecretName"></a>

### SecretName

| Field | Type              | Label | Description        |
| ----- | ----------------- | ----- | ------------------ |
| name  | [string](#string) |       | Name of the secret |

<a name="secret-SecretValue"></a>

### SecretValue

| Field | Type              | Label | Description         |
| ----- | ----------------- | ----- | ------------------- |
| value | [string](#string) |       | Value of the secret |

<a name="secret-SecretStore"></a>

### SecretStore

| Method Name | Request Type                     | Response Type                      | Description                           |
| ----------- | -------------------------------- | ---------------------------------- | ------------------------------------- |
| GetSecret   | [SecretName](#secret-SecretName) | [SecretValue](#secret-SecretValue) | Get secret value based on secret name |
