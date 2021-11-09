from src.gpt3_simple_primer.generator import GPT3Generator


'''Find the birthdays of famous people'''
birthday_finder = GPT3Generator()
birthday_finder.set_instructions('Find the birthdays of these famous people from history.')
birthday_finder.add_example('Albert Einstein', 'March 14, 1879')
birthday_finder.add_example('Bill Gates', 'October 28, 1955')
birthday_finder.add_example('Marie Curie', 'November 7, 1867')


'''Summarize books'''
book_summarizer = GPT3Generator()
book_summarizer.set_instructions('Given the name of a novel, summarize the plot in less than 100 words.')
book_summarizer.add_example('Pride and Prejudice', 'Pride and Prejudice follows the turbulent relationship between Elizabeth Bennet, the daughter of a country gentleman, and Fitzwilliam Darcy, a rich aristocratic landowner. They must overcome the titular sins of pride and prejudice in order to fall in love and marry.')


'''Idiom explanations'''
idiom_explainer = GPT3Generator()
idiom_explainer.set_instructions('An idiom is an expression or phrase whose meaning does not relate to the literal meaning of its words. Given an idiom, this is the intended meaning behind the phrase.')
idiom_explainer.add_example('your guess is as good as mine', 'I have no idea what is going on')
idiom_explainer.add_example('beat around the bush', 'to avoid talking about what is important')
idiom_explainer.add_example('take it with a grain of salt', 'do not take it too seriously')
