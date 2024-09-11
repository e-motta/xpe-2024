"""
{
    "content": {"some message"},
    "metadata": {
        "user_id": "some id",
    },
}
"""


def get_user_message_content(data: dict):
    return data.get("content")


def get_user_id(data: dict):
    return data.get("metadata", {}).get("user_id")
