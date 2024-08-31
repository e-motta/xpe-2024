from typing import Literal, TypedDict


OpenAIRole = Literal["system", "assistant", "user"]
OpenAIContent = str
OpenAIMessage = TypedDict(
    "OpenAIMessage",
    {
        "role": OpenAIRole,
        "content": OpenAIContent,
    },
)
OpenAIMessages = list[OpenAIMessage]
