from flask import Blueprint, request, make_response, Response

# import logging

from .config import OpenAIContent, FLASK_ENV

# from .services.conversation import (
#     get_or_create_conversation,
#     add_message_to_conversation,
# )
# from .services.openai import get_assistant_content

# logger = logging.getLogger(__name__)

api_route_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


@api_route_blueprint.route("/", methods=["POST"])
def api_post() -> Response:
    # logger.info("Received POST request")
    if request.json is None:
        # logger.warning("Received request with no JSON data.")
        return make_response("No data", 400)

    try:
        data = request.json

        # message = get_user_message(data)
        # user_id = get_user_id_from_message(message)
        # user_content = get_content_from_message(message)

        # conversation = get_or_create_conversation(user_id)

        # add_message_to_conversation(
        #     conversation,
        #     role="user",
        #     content=user_content,
        # )

        # assistant_content: OpenAIContent = get_assistant_content(
        #     conversation.limited_messages
        # )
        # # TODO: Fake message for testing purposes. Remove.
        # assistant_content: OpenAIContent = "Não se preocupe, estou aqui para te ajudar a entender e gerenciar suas finanças pessoais de forma simples e eficiente. Posso te orientar desde a criação de um orçamento até a organização de investimentos para o futuro."

        # add_message_to_conversation(
        #     conversation,
        #     role="assistant",
        #     content=assistant_content,
        # )

        # send response
    except Exception as e:
        # logger.error(
        #     f"An error occurred: {str(e)}. Cause: {str(e.__cause__)}",
        #     exc_info=(FLASK_ENV == "development"),
        # )
        return make_response(str(e), 500)

    return make_response("OK", 200)
