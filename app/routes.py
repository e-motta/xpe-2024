from flask import Blueprint, request, make_response, Response, jsonify

import logging

from .config import FLASK_ENV

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

        assistant_content = get_assistant_content(conversation.messages)

        add_message_to_conversation(
            conversation,
            role="assistant",
            content=assistant_content,
        )

        response_body = {
            "assistant_content": assistant_content,
            "metadata": {
                "user_id": user_id,
            },
        }

        return jsonify(response_body)
    except Exception as e:
        logger.error(
            f"An error occurred: {str(e)}. Cause: {str(e.__cause__)}",
            exc_info=(FLASK_ENV == "development"),
        )
        return make_response(str(e), 400)
