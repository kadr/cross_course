from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Course(_message.Message):
    __slots__ = ["id", "name", "course", "create_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    course: float
    create_at: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., course: _Optional[float] = ..., create_at: _Optional[float] = ...) -> None: ...

class GetCourseRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetCoursesRequest(_message.Message):
    __slots__ = ["limit"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class AddCourseRequest(_message.Message):
    __slots__ = ["name", "course"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    name: str
    course: float
    def __init__(self, name: _Optional[str] = ..., course: _Optional[float] = ...) -> None: ...

class CalcCourseRequest(_message.Message):
    __slots__ = ["first_currency_name", "second_currency_name"]
    FIRST_CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    SECOND_CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    first_currency_name: str
    second_currency_name: str
    def __init__(self, first_currency_name: _Optional[str] = ..., second_currency_name: _Optional[str] = ...) -> None: ...

class GetCourseResponse(_message.Message):
    __slots__ = ["course"]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: Course
    def __init__(self, course: _Optional[_Union[Course, _Mapping]] = ...) -> None: ...

class GetCoursesResponse(_message.Message):
    __slots__ = ["course"]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: _containers.RepeatedCompositeFieldContainer[Course]
    def __init__(self, course: _Optional[_Iterable[_Union[Course, _Mapping]]] = ...) -> None: ...
