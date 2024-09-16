from typing import Literal
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam


OpenAIRole = Literal["system", "assistant", "user"]
OpenAIContent = str | None
OpenAIMessage = ChatCompletionMessageParam
OpenAIMessages = list[OpenAIMessage]
