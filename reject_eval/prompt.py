eval_system = """
You are a data scientist. based on the provided data tables information, Determine if this question can be answered.

## Use the following format:
Question: The user question you need to judge
Answer: Directly give a judgment of whether the question can be answered, and give a 'yes' or 'no' response.
"""

eval_instruction = """
## Here is the description information about each dataframe:
{df_info}

Question: {input}
Answer: """

