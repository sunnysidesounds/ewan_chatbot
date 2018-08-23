
from chatterbot.conversation import Statement, Response
from chatterbot import utils
from chatterbot.trainers import Trainer
import os



class SmallTalkTrainer(Trainer):

    def __init__(self, storage, **kwargs):
        super(SmallTalkTrainer, self).__init__(storage, **kwargs)
        from data.corpus import Corpus

        self.corpus = Corpus()

    def train(self, *corpus_paths):

        # Allow a list of corpora to be passed instead of arguments
        if len(corpus_paths) == 1:
            if isinstance(corpus_paths[0], list):
                corpus_paths = corpus_paths[0]

        # Train the chat bot with each statement and response pair
        for corpus_path in corpus_paths:

            corpora = self.corpus.load_corpus(corpus_path)

            corpus_files = self.corpus.list_corpus_files(corpus_path)
            for corpus_count, corpus in enumerate(corpora):
                for conversation_count, conversation in enumerate(corpus):

                    if self.show_training_progress:
                        utils.print_progress_bar(
                            str(os.path.basename(corpus_files[corpus_count])) + ' Training',
                            conversation_count + 1,
                            len(corpus)
                        )

                    previous_statement_text = None

                    for text in conversation:
                        statement = self.get_or_create(text)
                        statement.add_tags(corpus.categories)

                        if previous_statement_text:
                            statement.add_response(
                                Response(previous_statement_text)
                            )

                        previous_statement_text = statement.text
                        self.chatbot.storage.update(statement)




