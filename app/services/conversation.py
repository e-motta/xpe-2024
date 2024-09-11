from ..config import INITIAL_PROMPT, ANSWER_SENTENCE_LIMIT, OpenAIContent, OpenAIRole
from ..models import Conversation, Message


def get_or_create_conversation(user_id: str) -> Conversation:
    conversation = Conversation.get_by_user_id(user_id)

    if conversation:
        return conversation
    else:
        new_conversation = Conversation(
            user_id=user_id,
            messages=[Message(role="system", content=INITIAL_PROMPT)],
        )
        new_conversation.save()
        return new_conversation


def _create_new_conversation_message(
    role: OpenAIRole, content: OpenAIContent
) -> Message:
    if role == "user":
        content += f". Responda em {ANSWER_SENTENCE_LIMIT} frases ou menos."
    new_message = Message(role=role, content=content)
    return new_message


def add_message_to_conversation(
    conversation: Conversation, role: OpenAIRole, content: OpenAIContent
) -> None:
    new_message: Message = _create_new_conversation_message(role, content)
    conversation.messages.append(new_message)
    conversation.save()
