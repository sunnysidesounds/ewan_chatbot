
from chatterbot.conversation import Statement, Response
from chatterbot import utils
from chatterbot.trainers import Trainer
from sources.recipes.queries import RecipeQueries


class RecipeTrainer(Trainer):

    data = RecipeQueries()


    def train(self):

        conversation = "hello"

        previous_statement_text = None

        results = self.data.get_all_generic_ingredient()
        print(results)

        for conversation_count, text in enumerate(conversation):
            if self.show_training_progress:
                utils.print_progress_bar(
                    'Recipe Trainer',
                    conversation_count + 1, len(conversation)
                )

            statement = self.get_or_create(text)

            if previous_statement_text:
                statement.add_response(
                    Response(previous_statement_text)
                )

            previous_statement_text = statement.text
            self.chatbot.storage.update(statement)