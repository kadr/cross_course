from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Currency(_message.Message):
    __slots__ = ["id", "iso", "currency_name", "is_obsolete", "superseded_by", "currency_symbol", "currency_symbol_on_right", "create_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISO_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_BY_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SYMBOL_ON_RIGHT_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    iso: str
    currency_name: str
    is_obsolete: bool
    superseded_by: str
    currency_symbol: str
    currency_symbol_on_right: bool
    create_at: float
    def __init__(self, id: _Optional[int] = ..., iso: _Optional[str] = ..., currency_name: _Optional[str] = ..., is_obsolete: bool = ..., superseded_by: _Optional[str] = ..., currency_symbol: _Optional[str] = ..., currency_symbol_on_right: bool = ..., create_at: _Optional[float] = ...) -> None: ...

class GetCurrencyRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetCurrenciesRequest(_message.Message):
    __slots__ = ["limit", "is_obsolete", "superseded_by"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    IS_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_BY_FIELD_NUMBER: _ClassVar[int]
    limit: int
    is_obsolete: bool
    superseded_by: str
    def __init__(self, limit: _Optional[int] = ..., is_obsolete: bool = ..., superseded_by: _Optional[str] = ...) -> None: ...

class AddCurrencyRequest(_message.Message):
    __slots__ = ["iso", "currency_name", "is_obsolete", "superseded_by", "currency_symbol", "currency_symbol_on_right"]
    ISO_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_BY_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SYMBOL_ON_RIGHT_FIELD_NUMBER: _ClassVar[int]
    iso: str
    currency_name: str
    is_obsolete: bool
    superseded_by: str
    currency_symbol: str
    currency_symbol_on_right: bool
    def __init__(self, iso: _Optional[str] = ..., currency_name: _Optional[str] = ..., is_obsolete: bool = ..., superseded_by: _Optional[str] = ..., currency_symbol: _Optional[str] = ..., currency_symbol_on_right: bool = ...) -> None: ...

class GetCurrencyResponse(_message.Message):
    __slots__ = ["currency"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    currency: Currency
    def __init__(self, currency: _Optional[_Union[Currency, _Mapping]] = ...) -> None: ...

class GetCurrenciesResponse(_message.Message):
    __slots__ = ["currency"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    currency: _containers.RepeatedCompositeFieldContainer[Currency]
    def __init__(self, currency: _Optional[_Iterable[_Union[Currency, _Mapping]]] = ...) -> None: ...
