from voluptuous import PREVENT_EXTRA, Schema

user = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

support = Schema(
    {
        "url": str,
        "text": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

single_user_schema = Schema(
    {
        "data": user,
        "support": support,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

users_list_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user],
        "support": support
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_single_user = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

unregister_single_user = Schema(
    {
        "error": str
    }
)

login_successful = Schema(
    {
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_unsuccessful = Schema(
    {
        "error": str
    }
)

create_single_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)
