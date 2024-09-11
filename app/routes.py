from flask import Blueprint, request, make_response, Response

import logging

from .config import OpenAIContent, FLASK_ENV

from .services.conversation import (
    get_or_create_conversation,
    add_message_to_conversation,
)
from .services.openai import get_assistant_content
from .services.frontend import get_user_message_content, get_user_id

logger = logging.getLogger(__name__)

api_route_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


@api_route_blueprint.route("/conversation", methods=["POST"])
def conversation_post() -> Response:
    logger.info("Received POST request")
    if request.json is None:
        logger.warning("Received request with no JSON data.")
        return make_response("No data", 400)

    try:
        data = request.json

        message_content = get_user_message_content(data)
        user_id = get_user_id(data)

        if message_content is None or user_id is None:
            logger.warning(f"Received request with invalid data: {data}")
            return make_response("Bad data", 400)

        conversation = get_or_create_conversation(user_id)

        add_message_to_conversation(
            conversation,
            role="user",
            content=message_content,
        )

        # assistant_content: OpenAIContent = get_assistant_content(
        #     conversation.limited_messages
        # )
        # TODO: Fake message for testing purposes. Remove.
        assistant_content: OpenAIContent = (
            "Não se preocupe, estou aqui para te ajudar a entender e gerenciar suas finanças pessoais de forma simples e eficiente. Posso te orientar desde a criação de um orçamento até a organização de investimentos para o futuro."
        )

        add_message_to_conversation(
            conversation,
            role="assistant",
            content=assistant_content,
        )

        # send response
    except Exception as e:
        logger.error(
            f"An error occurred: {str(e)}. Cause: {str(e.__cause__)}",
            exc_info=(FLASK_ENV == "development"),
        )
        return make_response(str(e), 400)

    return make_response("OK", 200)
