import logging
from openai.types.chat.chat_completion import ChatCompletion

from ..config import OpenAIContent, OpenAIMessage, OpenAIMessages
from ..models import Message
from ..integrations.openai import generate_chat_completion

logger = logging.getLogger(__name__)


def _convert_message_model_to_openai(message: Message) -> OpenAIMessage:
    return {  # type: ignore
        "role": message.role,
        "content": message.content,
    }


def _retrieve_completion_content(completion: ChatCompletion) -> OpenAIContent:
    return completion.choices[0].message.content


def _get_completion_content(messages: OpenAIMessages) -> OpenAIContent:
    try:
        completion = generate_chat_completion(messages)
        return _retrieve_completion_content(completion)
    except Exception as e:
        logger.error(f"OpenAI response error: {str(e)}")
        raise Exception("Error generating completion from OpenAI.") from e


def _filter_messages(messages: list[Message], messages_limit: int):
    return [messages[0], *messages[-messages_limit - 1 :]]


def get_assistant_content(
    messages: list[Message], messages_limit=None
) -> OpenAIContent:
    if messages_limit:
        messages = _filter_messages(messages, messages_limit)

    openai_messages = [
        _convert_message_model_to_openai(message) for message in messages
    ]
    try:
        content = _get_completion_content(openai_messages)
        logger.info(f"OpenAI response OK")
    except Exception as e:
        content = "Tive um problema, poderia refazer a pergunta?"
        logger.error(f"OpenAI response error: {str(e)}")

    return content
