from __future__ import annotations
from typing import (
  Any,
  Optional,
  Literal,
  TypedDict,
  Generic,
  TypeVar,
  NotRequired,
  cast,
  TYPE_CHECKING,
)
from re import Pattern
from datetime import date, datetime
from decimal import Decimal
from teo import ObjectId, Enumerable, File, Range, OptionVariant

from . import std


PostScalarFields = Literal['authorId', 'content', 'id', 'published', 'title']

PostSerializableScalarFields = Literal[
  'authorId', 'content', 'id', 'published', 'title'
]

PostRelations = Literal['author']

PostDirectRelations = Literal['author']

PostIndirectRelations = Literal[None]

UserScalarFields = Literal['email', 'id', 'name']

UserSerializableScalarFields = Literal['email', 'id', 'name']

UserRelations = Literal['posts']

UserDirectRelations = Literal['posts']

UserIndirectRelations = Literal[None]


# **Post select**
#
# This synthesized interface doesn't have a description
class PostSelect(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[bool]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[bool]]


# **Post include**
#
# This synthesized interface doesn't have a description
class PostInclude(TypedDict):
  # **Author**
  #
  # This synthesized field doesn't have a description.
  author: NotRequired[Optional[UserArgs | bool]]


# **Post where input**
#
# This synthesized interface doesn't have a description
class PostWhereInput(TypedDict):
  # **And**
  #
  # This synthesized field doesn't have a description.
  AND: NotRequired[Optional[list[PostWhereInput]]]

  # **Not**
  #
  # This synthesized field doesn't have a description.
  NOT: NotRequired[Optional[PostWhereInput]]

  # **Or**
  #
  # This synthesized field doesn't have a description.
  OR: NotRequired[Optional[list[PostWhereInput]]]

  # **Author**
  #
  # This synthesized field doesn't have a description.
  author: NotRequired[Optional[UserRelationFilter]]

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int | std.Filter[int]]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str | None | std.StringNullableFilter]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int | std.Filter[int]]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool | std.BoolFilter]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str | std.StringFilter]]


# **Post where unique input**
#
# This synthesized interface doesn't have a description
class PostWhereUniqueInput(TypedDict):
  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: int


# **Post scalar where with aggregates input**
#
# This synthesized interface doesn't have a description
class PostScalarWhereWithAggregatesInput(TypedDict):
  # **And**
  #
  # This synthesized field doesn't have a description.
  AND: NotRequired[Optional[list[PostWhereInput]]]

  # **Not**
  #
  # This synthesized field doesn't have a description.
  NOT: NotRequired[Optional[PostWhereInput]]

  # **Or**
  #
  # This synthesized field doesn't have a description.
  OR: NotRequired[Optional[list[PostWhereInput]]]

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int | std.IntNumberWithAggregatesFilter[int]]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[
    Optional[str | None | std.StringNullableWithAggregatesFilter]
  ]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int | std.IntNumberWithAggregatesFilter[int]]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool | std.BoolWithAggregatesFilter]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str | std.StringWithAggregatesFilter]]


# **Post relation filter**
#
# This synthesized interface doesn't have a description
class PostRelationFilter(TypedDict):
  # **Is**
  #
  # This synthesized field doesn't have a description.
  is_: NotRequired[Optional[PostWhereInput]]

  # **Is Not**
  #
  # This synthesized field doesn't have a description.
  isNot: NotRequired[Optional[PostWhereInput]]


# **Post list relation filter**
#
# This synthesized interface doesn't have a description
class PostListRelationFilter(TypedDict):
  # **Every**
  #
  # This synthesized field doesn't have a description.
  every: NotRequired[Optional[PostWhereInput]]

  # **None**
  #
  # This synthesized field doesn't have a description.
  none: NotRequired[Optional[PostWhereInput]]

  # **Some**
  #
  # This synthesized field doesn't have a description.
  some: NotRequired[Optional[PostWhereInput]]


# **Post order by input**
#
# This synthesized interface doesn't have a description
class PostOrderByInput(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[std.Sort]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[std.Sort]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[std.Sort]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[std.Sort]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[std.Sort]]


# **Post count aggregate input type**
#
# This synthesized interface doesn't have a description
class PostCountAggregateInputType(TypedDict):
  # **All**
  #
  # This synthesized field doesn't have a description.
  _all: NotRequired[Optional[bool]]

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[bool]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[bool]]


# **Post sum aggregate input type**
#
# This synthesized interface doesn't have a description
class PostSumAggregateInputType(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]


# **Post avg aggregate input type**
#
# This synthesized interface doesn't have a description
class PostAvgAggregateInputType(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]


# **Post min aggregate input type**
#
# This synthesized interface doesn't have a description
class PostMinAggregateInputType(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[bool]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[bool]]


# **Post max aggregate input type**
#
# This synthesized interface doesn't have a description
class PostMaxAggregateInputType(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[bool]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[bool]]


# **Post create input**
#
# This synthesized interface doesn't have a description
class PostCreateInput(TypedDict):
  # **Author**
  #
  # This synthesized field doesn't have a description.
  author: NotRequired[Optional[UserCreateNestedOneWithoutPostsInput]]

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: str


# **Post create without author input**
#
# This synthesized interface doesn't have a description
class PostCreateWithoutAuthorInput(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: str


# **Post update input**
#
# This synthesized interface doesn't have a description
class PostUpdateInput(TypedDict):
  # **Author**
  #
  # This synthesized field doesn't have a description.
  author: NotRequired[Optional[UserUpdateNestedOneWithoutPostsInput]]

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str]]


# **Post update without author input**
#
# This synthesized interface doesn't have a description
class PostUpdateWithoutAuthorInput(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str]]


# **Post create nested one input**
#
# This synthesized interface doesn't have a description
class PostCreateNestedOneInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[PostWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[PostConnectOrCreateInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[PostCreateInput]]


# **Post create nested one without author input**
#
# This synthesized interface doesn't have a description
class PostCreateNestedOneWithoutAuthorInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[PostWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[PostConnectOrCreateWithoutAuthorInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[PostCreateInput]]


# **Post create nested many input**
#
# This synthesized interface doesn't have a description
class PostCreateNestedManyInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[Enumerable[PostConnectOrCreateInput]]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[PostCreateInput]]]


# **Post create nested many without author input**
#
# This synthesized interface doesn't have a description
class PostCreateNestedManyWithoutAuthorInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[
    Optional[Enumerable[PostConnectOrCreateWithoutAuthorInput]]
  ]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[PostCreateInput]]]


# **Post update nested one input**
#
# This synthesized interface doesn't have a description
class PostUpdateNestedOneInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[PostWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[PostConnectOrCreateInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[PostCreateInput]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[bool]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[bool]]

  # **Set**
  #
  # This synthesized field doesn't have a description.
  set: NotRequired[Optional[PostWhereUniqueInput]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[Optional[PostUpdateWithWhereUniqueInput]]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[Optional[PostUpsertWithWhereUniqueInput]]


# **Post update nested one without author input**
#
# This synthesized interface doesn't have a description
class PostUpdateNestedOneWithoutAuthorInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[PostWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[PostConnectOrCreateWithoutAuthorInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[PostCreateInput]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[bool]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[bool]]

  # **Set**
  #
  # This synthesized field doesn't have a description.
  set: NotRequired[Optional[PostWhereUniqueInput]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[Optional[PostUpdateWithWhereUniqueWithoutAuthorInput]]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[Optional[PostUpsertWithWhereUniqueWithoutAuthorInput]]


# **Post update nested many input**
#
# This synthesized interface doesn't have a description
class PostUpdateNestedManyInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[Enumerable[PostConnectOrCreateInput]]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[PostCreateInput]]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Delete Many**
  #
  # This synthesized field doesn't have a description.
  deleteMany: NotRequired[Optional[Enumerable[PostWhereInput]]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[Optional[Enumerable[PostUpdateWithWhereUniqueInput]]]

  # **Update Many**
  #
  # This synthesized field doesn't have a description.
  updateMany: NotRequired[Optional[Enumerable[PostUpdateManyWithWhereInput]]]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[Optional[Enumerable[PostUpsertWithWhereUniqueInput]]]


# **Post update nested many without author input**
#
# This synthesized interface doesn't have a description
class PostUpdateNestedManyWithoutAuthorInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[
    Optional[Enumerable[PostConnectOrCreateWithoutAuthorInput]]
  ]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[PostCreateInput]]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Delete Many**
  #
  # This synthesized field doesn't have a description.
  deleteMany: NotRequired[Optional[Enumerable[PostWhereInput]]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[Enumerable[PostWhereUniqueInput]]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[
    Optional[Enumerable[PostUpdateWithWhereUniqueWithoutAuthorInput]]
  ]

  # **Update Many**
  #
  # This synthesized field doesn't have a description.
  updateMany: NotRequired[
    Optional[Enumerable[PostUpdateManyWithWhereWithoutAuthorInput]]
  ]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[
    Optional[Enumerable[PostUpsertWithWhereUniqueWithoutAuthorInput]]
  ]


# **Post connect or create input**
#
# This synthesized interface doesn't have a description
class PostConnectOrCreateInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: PostCreateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post connect or create without author input**
#
# This synthesized interface doesn't have a description
class PostConnectOrCreateWithoutAuthorInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: PostCreateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post update with where unique input**
#
# This synthesized interface doesn't have a description
class PostUpdateWithWhereUniqueInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post update with where unique without author input**
#
# This synthesized interface doesn't have a description
class PostUpdateWithWhereUniqueWithoutAuthorInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post upsert with where unique input**
#
# This synthesized interface doesn't have a description
class PostUpsertWithWhereUniqueInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: PostCreateInput

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post upsert with where unique without author input**
#
# This synthesized interface doesn't have a description
class PostUpsertWithWhereUniqueWithoutAuthorInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: PostCreateInput

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post update many with where input**
#
# This synthesized interface doesn't have a description
class PostUpdateManyWithWhereInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereInput


# **Post update many with where without author input**
#
# This synthesized interface doesn't have a description
class PostUpdateManyWithWhereWithoutAuthorInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereInput


# **Post result**
#
# This synthesized interface doesn't have a description
class PostResult(TypedDict):
  # **Author**
  #
  # This synthesized field doesn't have a description.
  author: UserResult

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: int

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: int

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: bool

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: str


# **Post count aggregate result**
#
# This synthesized interface doesn't have a description
class PostCountAggregateResult(TypedDict):
  # **All**
  #
  # This synthesized field doesn't have a description.
  _all: NotRequired[Optional[int]]

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[int]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[int]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[int]]


# **Post sum aggregate result**
#
# This synthesized interface doesn't have a description
class PostSumAggregateResult(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]


# **Post avg aggregate result**
#
# This synthesized interface doesn't have a description
class PostAvgAggregateResult(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[float]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[float]]


# **Post min aggregate result**
#
# This synthesized interface doesn't have a description
class PostMinAggregateResult(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str]]


# **Post max aggregate result**
#
# This synthesized interface doesn't have a description
class PostMaxAggregateResult(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str]]


# **Post aggregate result**
#
# This synthesized interface doesn't have a description
class PostAggregateResult(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[PostAvgAggregateResult]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[PostCountAggregateResult]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[PostMaxAggregateResult]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[PostMinAggregateResult]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[PostSumAggregateResult]]


# **Post group by result**
#
# This synthesized interface doesn't have a description
class PostGroupByResult(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[PostAvgAggregateResult]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[PostCountAggregateResult]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[PostMaxAggregateResult]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[PostMinAggregateResult]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[PostSumAggregateResult]]

  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str]]


# **Post args**
#
# This synthesized interface doesn't have a description
class PostArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]


# **Post find many args**
#
# This synthesized interface doesn't have a description
class PostFindManyArgs(TypedDict):
  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[PostWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[PostSerializableScalarFields]]

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[PostOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[PostWhereInput]]


# **Post find first args**
#
# This synthesized interface doesn't have a description
class PostFindFirstArgs(TypedDict):
  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[PostWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[PostSerializableScalarFields]]

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[PostOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[PostWhereInput]]


# **Post find unique args**
#
# This synthesized interface doesn't have a description
class PostFindUniqueArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post create args**
#
# This synthesized interface doesn't have a description
class PostCreateArgs(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: PostCreateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]


# **Post update args**
#
# This synthesized interface doesn't have a description
class PostUpdateArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post upsert args**
#
# This synthesized interface doesn't have a description
class PostUpsertArgs(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: PostCreateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post copy args**
#
# This synthesized interface doesn't have a description
class PostCopyArgs(TypedDict):
  # **Copy**
  #
  # This synthesized field doesn't have a description.
  copy: PostUpdateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post delete args**
#
# This synthesized interface doesn't have a description
class PostDeleteArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereUniqueInput


# **Post create many args**
#
# This synthesized interface doesn't have a description
class PostCreateManyArgs(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: Enumerable[PostCreateInput]

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]


# **Post update many args**
#
# This synthesized interface doesn't have a description
class PostUpdateManyArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: PostUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereInput


# **Post delete many args**
#
# This synthesized interface doesn't have a description
class PostDeleteManyArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereInput


# **Post copy many args**
#
# This synthesized interface doesn't have a description
class PostCopyManyArgs(TypedDict):
  # **Copy**
  #
  # This synthesized field doesn't have a description.
  copy: PostUpdateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: PostWhereInput


# **Post count args**
#
# This synthesized interface doesn't have a description
class PostCountArgs(TypedDict):
  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[PostWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[PostSerializableScalarFields]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[PostOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostCountAggregateInputType]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[PostWhereInput]]


# **Post aggregate args**
#
# This synthesized interface doesn't have a description
class PostAggregateArgs(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[PostAvgAggregateInputType]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[PostCountAggregateInputType]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[PostMaxAggregateInputType]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[PostMinAggregateInputType]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[PostSumAggregateInputType]]

  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[PostWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[PostSerializableScalarFields]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[PostOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[PostWhereInput]]


# **Post group by args**
#
# This synthesized interface doesn't have a description
class PostGroupByArgs(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[PostAvgAggregateInputType]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[PostCountAggregateInputType]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[PostMaxAggregateInputType]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[PostMinAggregateInputType]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[PostSumAggregateInputType]]

  # **By**
  #
  # This synthesized field doesn't have a description.
  by: Enumerable[PostSerializableScalarFields]

  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[PostWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[PostSerializableScalarFields]]

  # **Having**
  #
  # This synthesized field doesn't have a description.
  having: NotRequired[Optional[PostScalarWhereWithAggregatesInput]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[PostOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[PostWhereInput]]


# **Post scalar update input**
#
# This synthesized interface doesn't have a description
class PostScalarUpdateInput(TypedDict):
  # **Author Id**
  #
  # This synthesized field doesn't have a description.
  authorId: NotRequired[Optional[int]]

  # **Content**
  #
  # This synthesized field doesn't have a description.
  content: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Published**
  #
  # This synthesized field doesn't have a description.
  published: NotRequired[Optional[bool]]

  # **Title**
  #
  # This synthesized field doesn't have a description.
  title: NotRequired[Optional[str]]


# **Post sign in checker ids**
#
# This synthesized interface doesn't have a description
class PostSignInCheckerIds(TypedDict):
  pass


# **Post sign in checker companions**
#
# This synthesized interface doesn't have a description
class PostSignInCheckerCompanions(TypedDict):
  pass


# **Post sign in input**
#
# This synthesized interface doesn't have a description
class PostSignInInput(TypedDict):
  # **Credentials**
  #
  # This synthesized field doesn't have a description.
  credentials: PostSignInArgs

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[PostInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[PostSelect]]


# **Post sign in args**
#
# This synthesized interface doesn't have a description
class PostSignInArgs(TypedDict):
  pass


# **User select**
#
# This synthesized interface doesn't have a description
class UserSelect(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[bool]]


# **User include**
#
# This synthesized interface doesn't have a description
class UserInclude(TypedDict):
  # **Posts**
  #
  # This synthesized field doesn't have a description.
  posts: NotRequired[Optional[PostFindManyArgs | bool]]


# **User where input**
#
# This synthesized interface doesn't have a description
class UserWhereInput(TypedDict):
  # **And**
  #
  # This synthesized field doesn't have a description.
  AND: NotRequired[Optional[list[UserWhereInput]]]

  # **Not**
  #
  # This synthesized field doesn't have a description.
  NOT: NotRequired[Optional[UserWhereInput]]

  # **Or**
  #
  # This synthesized field doesn't have a description.
  OR: NotRequired[Optional[list[UserWhereInput]]]

  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str | std.StringFilter]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int | std.Filter[int]]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str | None | std.StringNullableFilter]]

  # **Posts**
  #
  # This synthesized field doesn't have a description.
  posts: NotRequired[Optional[PostListRelationFilter]]


# **User where unique input**
#
# This synthesized interface doesn't have a description
class UserWhereUniqueInput(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]


# **User scalar where with aggregates input**
#
# This synthesized interface doesn't have a description
class UserScalarWhereWithAggregatesInput(TypedDict):
  # **And**
  #
  # This synthesized field doesn't have a description.
  AND: NotRequired[Optional[list[UserWhereInput]]]

  # **Not**
  #
  # This synthesized field doesn't have a description.
  NOT: NotRequired[Optional[UserWhereInput]]

  # **Or**
  #
  # This synthesized field doesn't have a description.
  OR: NotRequired[Optional[list[UserWhereInput]]]

  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str | std.StringWithAggregatesFilter]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int | std.IntNumberWithAggregatesFilter[int]]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[
    Optional[str | None | std.StringNullableWithAggregatesFilter]
  ]


# **User relation filter**
#
# This synthesized interface doesn't have a description
class UserRelationFilter(TypedDict):
  # **Is**
  #
  # This synthesized field doesn't have a description.
  is_: NotRequired[Optional[UserWhereInput]]

  # **Is Not**
  #
  # This synthesized field doesn't have a description.
  isNot: NotRequired[Optional[UserWhereInput]]


# **User list relation filter**
#
# This synthesized interface doesn't have a description
class UserListRelationFilter(TypedDict):
  # **Every**
  #
  # This synthesized field doesn't have a description.
  every: NotRequired[Optional[UserWhereInput]]

  # **None**
  #
  # This synthesized field doesn't have a description.
  none: NotRequired[Optional[UserWhereInput]]

  # **Some**
  #
  # This synthesized field doesn't have a description.
  some: NotRequired[Optional[UserWhereInput]]


# **User order by input**
#
# This synthesized interface doesn't have a description
class UserOrderByInput(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[std.Sort]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[std.Sort]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[std.Sort]]


# **User count aggregate input type**
#
# This synthesized interface doesn't have a description
class UserCountAggregateInputType(TypedDict):
  # **All**
  #
  # This synthesized field doesn't have a description.
  _all: NotRequired[Optional[bool]]

  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[bool]]


# **User sum aggregate input type**
#
# This synthesized interface doesn't have a description
class UserSumAggregateInputType(TypedDict):
  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]


# **User avg aggregate input type**
#
# This synthesized interface doesn't have a description
class UserAvgAggregateInputType(TypedDict):
  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]


# **User min aggregate input type**
#
# This synthesized interface doesn't have a description
class UserMinAggregateInputType(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[bool]]


# **User max aggregate input type**
#
# This synthesized interface doesn't have a description
class UserMaxAggregateInputType(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[bool]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[bool]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[bool]]


# **User create input**
#
# This synthesized interface doesn't have a description
class UserCreateInput(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: str

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]

  # **Posts**
  #
  # This synthesized field doesn't have a description.
  posts: NotRequired[Optional[PostCreateNestedManyWithoutAuthorInput]]


# **User create without posts input**
#
# This synthesized interface doesn't have a description
class UserCreateWithoutPostsInput(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: str

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]


# **User update input**
#
# This synthesized interface doesn't have a description
class UserUpdateInput(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]

  # **Posts**
  #
  # This synthesized field doesn't have a description.
  posts: NotRequired[Optional[PostUpdateNestedManyWithoutAuthorInput]]


# **User update without posts input**
#
# This synthesized interface doesn't have a description
class UserUpdateWithoutPostsInput(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]


# **User create nested one input**
#
# This synthesized interface doesn't have a description
class UserCreateNestedOneInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[UserWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[UserConnectOrCreateInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[UserCreateInput]]


# **User create nested one without posts input**
#
# This synthesized interface doesn't have a description
class UserCreateNestedOneWithoutPostsInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[UserWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[UserConnectOrCreateWithoutPostsInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[UserCreateInput]]


# **User create nested many input**
#
# This synthesized interface doesn't have a description
class UserCreateNestedManyInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[Enumerable[UserConnectOrCreateInput]]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[UserCreateInput]]]


# **User create nested many without posts input**
#
# This synthesized interface doesn't have a description
class UserCreateNestedManyWithoutPostsInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[
    Optional[Enumerable[UserConnectOrCreateWithoutPostsInput]]
  ]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[UserCreateInput]]]


# **User update nested one input**
#
# This synthesized interface doesn't have a description
class UserUpdateNestedOneInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[UserWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[UserConnectOrCreateInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[UserCreateInput]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[bool]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[bool]]

  # **Set**
  #
  # This synthesized field doesn't have a description.
  set: NotRequired[Optional[UserWhereUniqueInput]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[Optional[UserUpdateWithWhereUniqueInput]]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[Optional[UserUpsertWithWhereUniqueInput]]


# **User update nested one without posts input**
#
# This synthesized interface doesn't have a description
class UserUpdateNestedOneWithoutPostsInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[UserWhereUniqueInput]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[UserConnectOrCreateWithoutPostsInput]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[UserCreateInput]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[bool]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[bool]]

  # **Set**
  #
  # This synthesized field doesn't have a description.
  set: NotRequired[Optional[UserWhereUniqueInput]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[Optional[UserUpdateWithWhereUniqueWithoutPostsInput]]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[Optional[UserUpsertWithWhereUniqueWithoutPostsInput]]


# **User update nested many input**
#
# This synthesized interface doesn't have a description
class UserUpdateNestedManyInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[Optional[Enumerable[UserConnectOrCreateInput]]]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[UserCreateInput]]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Delete Many**
  #
  # This synthesized field doesn't have a description.
  deleteMany: NotRequired[Optional[Enumerable[UserWhereInput]]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[Optional[Enumerable[UserUpdateWithWhereUniqueInput]]]

  # **Update Many**
  #
  # This synthesized field doesn't have a description.
  updateMany: NotRequired[Optional[Enumerable[UserUpdateManyWithWhereInput]]]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[Optional[Enumerable[UserUpsertWithWhereUniqueInput]]]


# **User update nested many without posts input**
#
# This synthesized interface doesn't have a description
class UserUpdateNestedManyWithoutPostsInput(TypedDict):
  # **Connect**
  #
  # This synthesized field doesn't have a description.
  connect: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Connect Or Create**
  #
  # This synthesized field doesn't have a description.
  connectOrCreate: NotRequired[
    Optional[Enumerable[UserConnectOrCreateWithoutPostsInput]]
  ]

  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: NotRequired[Optional[Enumerable[UserCreateInput]]]

  # **Delete**
  #
  # This synthesized field doesn't have a description.
  delete: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Delete Many**
  #
  # This synthesized field doesn't have a description.
  deleteMany: NotRequired[Optional[Enumerable[UserWhereInput]]]

  # **Disconnect**
  #
  # This synthesized field doesn't have a description.
  disconnect: NotRequired[Optional[Enumerable[UserWhereUniqueInput]]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: NotRequired[
    Optional[Enumerable[UserUpdateWithWhereUniqueWithoutPostsInput]]
  ]

  # **Update Many**
  #
  # This synthesized field doesn't have a description.
  updateMany: NotRequired[
    Optional[Enumerable[UserUpdateManyWithWhereWithoutPostsInput]]
  ]

  # **Upsert**
  #
  # This synthesized field doesn't have a description.
  upsert: NotRequired[
    Optional[Enumerable[UserUpsertWithWhereUniqueWithoutPostsInput]]
  ]


# **User connect or create input**
#
# This synthesized interface doesn't have a description
class UserConnectOrCreateInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: UserCreateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User connect or create without posts input**
#
# This synthesized interface doesn't have a description
class UserConnectOrCreateWithoutPostsInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: UserCreateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User update with where unique input**
#
# This synthesized interface doesn't have a description
class UserUpdateWithWhereUniqueInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User update with where unique without posts input**
#
# This synthesized interface doesn't have a description
class UserUpdateWithWhereUniqueWithoutPostsInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User upsert with where unique input**
#
# This synthesized interface doesn't have a description
class UserUpsertWithWhereUniqueInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: UserCreateInput

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User upsert with where unique without posts input**
#
# This synthesized interface doesn't have a description
class UserUpsertWithWhereUniqueWithoutPostsInput(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: UserCreateInput

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User update many with where input**
#
# This synthesized interface doesn't have a description
class UserUpdateManyWithWhereInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereInput


# **User update many with where without posts input**
#
# This synthesized interface doesn't have a description
class UserUpdateManyWithWhereWithoutPostsInput(TypedDict):
  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereInput


# **User result**
#
# This synthesized interface doesn't have a description
class UserResult(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: str

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: int

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]

  # **Posts**
  #
  # This synthesized field doesn't have a description.
  posts: list[PostResult]


# **User count aggregate result**
#
# This synthesized interface doesn't have a description
class UserCountAggregateResult(TypedDict):
  # **All**
  #
  # This synthesized field doesn't have a description.
  _all: NotRequired[Optional[int]]

  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[int]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[int]]


# **User sum aggregate result**
#
# This synthesized interface doesn't have a description
class UserSumAggregateResult(TypedDict):
  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]


# **User avg aggregate result**
#
# This synthesized interface doesn't have a description
class UserAvgAggregateResult(TypedDict):
  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[float]]


# **User min aggregate result**
#
# This synthesized interface doesn't have a description
class UserMinAggregateResult(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]


# **User max aggregate result**
#
# This synthesized interface doesn't have a description
class UserMaxAggregateResult(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]


# **User aggregate result**
#
# This synthesized interface doesn't have a description
class UserAggregateResult(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[UserAvgAggregateResult]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[UserCountAggregateResult]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[UserMaxAggregateResult]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[UserMinAggregateResult]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[UserSumAggregateResult]]


# **User group by result**
#
# This synthesized interface doesn't have a description
class UserGroupByResult(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[UserAvgAggregateResult]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[UserCountAggregateResult]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[UserMaxAggregateResult]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[UserMinAggregateResult]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[UserSumAggregateResult]]

  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]


# **User args**
#
# This synthesized interface doesn't have a description
class UserArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]


# **User find many args**
#
# This synthesized interface doesn't have a description
class UserFindManyArgs(TypedDict):
  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[UserWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[UserSerializableScalarFields]]

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[UserOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[UserWhereInput]]


# **User find first args**
#
# This synthesized interface doesn't have a description
class UserFindFirstArgs(TypedDict):
  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[UserWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[UserSerializableScalarFields]]

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[UserOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[UserWhereInput]]


# **User find unique args**
#
# This synthesized interface doesn't have a description
class UserFindUniqueArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User create args**
#
# This synthesized interface doesn't have a description
class UserCreateArgs(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: UserCreateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]


# **User update args**
#
# This synthesized interface doesn't have a description
class UserUpdateArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User upsert args**
#
# This synthesized interface doesn't have a description
class UserUpsertArgs(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: UserCreateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User copy args**
#
# This synthesized interface doesn't have a description
class UserCopyArgs(TypedDict):
  # **Copy**
  #
  # This synthesized field doesn't have a description.
  copy: UserUpdateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User delete args**
#
# This synthesized interface doesn't have a description
class UserDeleteArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereUniqueInput


# **User create many args**
#
# This synthesized interface doesn't have a description
class UserCreateManyArgs(TypedDict):
  # **Create**
  #
  # This synthesized field doesn't have a description.
  create: Enumerable[UserCreateInput]

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]


# **User update many args**
#
# This synthesized interface doesn't have a description
class UserUpdateManyArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Update**
  #
  # This synthesized field doesn't have a description.
  update: UserUpdateInput

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereInput


# **User delete many args**
#
# This synthesized interface doesn't have a description
class UserDeleteManyArgs(TypedDict):
  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereInput


# **User copy many args**
#
# This synthesized interface doesn't have a description
class UserCopyManyArgs(TypedDict):
  # **Copy**
  #
  # This synthesized field doesn't have a description.
  copy: UserUpdateInput

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: UserWhereInput


# **User count args**
#
# This synthesized interface doesn't have a description
class UserCountArgs(TypedDict):
  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[UserWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[UserSerializableScalarFields]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[UserOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserCountAggregateInputType]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[UserWhereInput]]


# **User aggregate args**
#
# This synthesized interface doesn't have a description
class UserAggregateArgs(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[UserAvgAggregateInputType]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[UserCountAggregateInputType]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[UserMaxAggregateInputType]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[UserMinAggregateInputType]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[UserSumAggregateInputType]]

  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[UserWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[UserSerializableScalarFields]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[UserOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[UserWhereInput]]


# **User group by args**
#
# This synthesized interface doesn't have a description
class UserGroupByArgs(TypedDict):
  # **Avg**
  #
  # This synthesized field doesn't have a description.
  _avg: NotRequired[Optional[UserAvgAggregateInputType]]

  # **Count**
  #
  # This synthesized field doesn't have a description.
  _count: NotRequired[Optional[UserCountAggregateInputType]]

  # **Max**
  #
  # This synthesized field doesn't have a description.
  _max: NotRequired[Optional[UserMaxAggregateInputType]]

  # **Min**
  #
  # This synthesized field doesn't have a description.
  _min: NotRequired[Optional[UserMinAggregateInputType]]

  # **Sum**
  #
  # This synthesized field doesn't have a description.
  _sum: NotRequired[Optional[UserSumAggregateInputType]]

  # **By**
  #
  # This synthesized field doesn't have a description.
  by: Enumerable[UserSerializableScalarFields]

  # **Cursor**
  #
  # This synthesized field doesn't have a description.
  cursor: NotRequired[Optional[UserWhereUniqueInput]]

  # **Distinct**
  #
  # This synthesized field doesn't have a description.
  distinct: NotRequired[Optional[UserSerializableScalarFields]]

  # **Having**
  #
  # This synthesized field doesn't have a description.
  having: NotRequired[Optional[UserScalarWhereWithAggregatesInput]]

  # **Order By**
  #
  # This synthesized field doesn't have a description.
  orderBy: NotRequired[Optional[Enumerable[UserOrderByInput]]]

  # **Page Number**
  #
  # This synthesized field doesn't have a description.
  pageNumber: NotRequired[Optional[int]]

  # **Page Size**
  #
  # This synthesized field doesn't have a description.
  pageSize: NotRequired[Optional[int]]

  # **Skip**
  #
  # This synthesized field doesn't have a description.
  skip: NotRequired[Optional[int]]

  # **Take**
  #
  # This synthesized field doesn't have a description.
  take: NotRequired[Optional[int]]

  # **Where**
  #
  # This synthesized field doesn't have a description.
  where: NotRequired[Optional[UserWhereInput]]


# **User scalar update input**
#
# This synthesized interface doesn't have a description
class UserScalarUpdateInput(TypedDict):
  # **Email**
  #
  # This synthesized field doesn't have a description.
  email: NotRequired[Optional[str]]

  # **Id**
  #
  # This synthesized field doesn't have a description.
  id: NotRequired[Optional[int]]

  # **Name**
  #
  # This synthesized field doesn't have a description.
  name: NotRequired[Optional[str]]


# **User sign in checker ids**
#
# This synthesized interface doesn't have a description
class UserSignInCheckerIds(TypedDict):
  pass


# **User sign in checker companions**
#
# This synthesized interface doesn't have a description
class UserSignInCheckerCompanions(TypedDict):
  pass


# **User sign in input**
#
# This synthesized interface doesn't have a description
class UserSignInInput(TypedDict):
  # **Credentials**
  #
  # This synthesized field doesn't have a description.
  credentials: UserSignInArgs

  # **Include**
  #
  # This synthesized field doesn't have a description.
  include: NotRequired[Optional[UserInclude]]

  # **Select**
  #
  # This synthesized field doesn't have a description.
  select: NotRequired[Optional[UserSelect]]


# **User sign in args**
#
# This synthesized interface doesn't have a description
class UserSignInArgs(TypedDict):
  pass


class PostModel:
  async def find_many(self, query: PostFindManyArgs, /) -> list[Post]:
    return cast(Any, None)

  async def find_unique(self, query: PostFindUniqueArgs, /) -> Optional[Post]:
    return cast(Any, None)

  async def find_first(self, query: PostFindFirstArgs, /) -> Optional[Post]:
    return cast(Any, None)

  async def create(self, input: PostCreateInput, /) -> Post:
    return cast(Any, None)

  async def count_objects(self, query: PostCountArgs, /) -> int:
    return cast(Any, None)

  async def count_fields(
    self, query: PostCountArgs, /
  ) -> PostCountAggregateResult:
    return cast(Any, None)

  async def aggregate(
    self, query: PostAggregateArgs, /
  ) -> PostAggregateResult:
    return cast(Any, None)

  async def group_by(
    self, query: PostGroupByArgs, /
  ) -> list[PostAggregateResult]:
    return cast(Any, None)

  async def sql(self, sql: str) -> list[Any]:
    return cast(Any, None)


class Post:
  def is_new(self) -> bool:
    return cast(Any, None)

  def is_modified(self) -> bool:
    return cast(Any, None)

  async def set(self, input: PostUpdateInput, /) -> None:
    return cast(Any, None)

  async def update(self, input: PostScalarUpdateInput, /) -> None:
    return cast(Any, None)

  async def save(self) -> None:
    return cast(Any, None)

  async def delete(self) -> None:
    return cast(Any, None)

  async def to_teon(self) -> PostResult:
    return cast(Any, None)

  id: int
  title: str
  content: Optional[str]
  published: bool
  author_id: int

  async def author(self) -> User:
    return cast(Any, None)

  async def set_author(self, new_value: User, /) -> None:
    return cast(Any, None)


class UserModel:
  async def find_many(self, query: UserFindManyArgs, /) -> list[User]:
    return cast(Any, None)

  async def find_unique(self, query: UserFindUniqueArgs, /) -> Optional[User]:
    return cast(Any, None)

  async def find_first(self, query: UserFindFirstArgs, /) -> Optional[User]:
    return cast(Any, None)

  async def create(self, input: UserCreateInput, /) -> User:
    return cast(Any, None)

  async def count_objects(self, query: UserCountArgs, /) -> int:
    return cast(Any, None)

  async def count_fields(
    self, query: UserCountArgs, /
  ) -> UserCountAggregateResult:
    return cast(Any, None)

  async def aggregate(
    self, query: UserAggregateArgs, /
  ) -> UserAggregateResult:
    return cast(Any, None)

  async def group_by(
    self, query: UserGroupByArgs, /
  ) -> list[UserAggregateResult]:
    return cast(Any, None)

  async def sql(self, sql: str) -> list[Any]:
    return cast(Any, None)


class User:
  def is_new(self) -> bool:
    return cast(Any, None)

  def is_modified(self) -> bool:
    return cast(Any, None)

  async def set(self, input: UserUpdateInput, /) -> None:
    return cast(Any, None)

  async def update(self, input: UserScalarUpdateInput, /) -> None:
    return cast(Any, None)

  async def save(self) -> None:
    return cast(Any, None)

  async def delete(self) -> None:
    return cast(Any, None)

  async def to_teon(self) -> UserResult:
    return cast(Any, None)

  id: int
  email: str
  name: Optional[str]

  async def posts(self) -> list[Post]:
    return cast(Any, None)

  async def set_posts(self, new_value: list[Post], /) -> None:
    return cast(Any, None)

  async def add_to_posts(self, new_value: list[Post], /) -> None:
    return cast(Any, None)

  async def remove_from_posts(self, new_value: list[Post], /) -> None:
    return cast(Any, None)


class EchoPathArguments(TypedDict):
  data: str


class Teo:
  async def transaction[T](self, teo: Teo, /) -> T:
    return cast(Any, None)

  post: PostModel
  user: UserModel
