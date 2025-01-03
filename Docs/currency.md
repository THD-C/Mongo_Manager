# Protocol Documentation

<a name="top"></a>

## Table of Contents

- [currency.proto](#currency-proto)

  - [CurrencyDetails](#currency-CurrencyDetails)
  - [CurrencyList](#currency-CurrencyList)
  - [CurrencyTypeMsg](#currency-CurrencyTypeMsg)

  - [Currency](#currency-Currency)

- [currency_type.proto](#currency_type-proto)
  - [CurrencyType](#currency-CurrencyType)
- [Scalar Value Types](#scalar-value-types)

<a name="currency-proto"></a>

<p align="right"><a href="#top">Top</a></p>

## currency.proto

<a name="currency-CurrencyDetails"></a>

### CurrencyDetails

Contains name of currency which needs to be checked for type.

| Field         | Type              | Label | Description          |
| ------------- | ----------------- | ----- | -------------------- |
| currency_name | [string](#string) |       | Name of the currency |

<a name="currency-CurrencyList"></a>

### CurrencyList

Represents a currency list

| Field      | Type                                         | Label    | Description        |
| ---------- | -------------------------------------------- | -------- | ------------------ |
| currencies | [CurrencyDetails](#currency-CurrencyDetails) | repeated | List of currencies |

<a name="currency-CurrencyTypeMsg"></a>

### CurrencyTypeMsg

Contains a type of crypto sent for check.

| Field | Type                                   | Label | Description |
| ----- | -------------------------------------- | ----- | ----------- |
| type  | [CurrencyType](#currency-CurrencyType) |       |             |

<a name="currency-Currency"></a>

### Currency

| Method Name            | Request Type                                 | Response Type                                | Description                                 |
| ---------------------- | -------------------------------------------- | -------------------------------------------- | ------------------------------------------- |
| GetCurrencyType        | [CurrencyDetails](#currency-CurrencyDetails) | [CurrencyTypeMsg](#currency-CurrencyTypeMsg) | Returns type of provided currency.          |
| GetSupportedCurrencies | [CurrencyTypeMsg](#currency-CurrencyTypeMsg) | [CurrencyList](#currency-CurrencyList)       | Returns list of currencies in a given type. |

<a name="currency_type-proto"></a>

<p align="right"><a href="#top">Top</a></p>

## currency_type.proto

<a name="currency-CurrencyType"></a>

### CurrencyType

| Name                        | Number | Description                              |
| --------------------------- | ------ | ---------------------------------------- |
| CURRENCY_TYPE_NOT_SUPPORTED | 0      | Platform does not support this currency. |
| CURRENCY_TYPE_FIAT          | 1      | Currency is FIAT.                        |
| CURRENCY_TYPE_CRYPTO        | 2      | Currency is crypto.                      |
