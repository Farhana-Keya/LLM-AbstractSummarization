from Evaluation.Extraction_value import Extraction
import re
import openai
from pathlib import Path


api_key = ""

class EvaluationSummarization:
    def __init__(self):
        self.encoding = 'utf-8'
        openai.api_key = api_key

    def generate_evaluation_with_prompts(self, paper_abstract, summary):
        chain_of_thought_prompt = f"""
      Evaluate the provided one-sentence summary:

      {summary}

       of a scientific paper's abstract:

      {paper_abstract}
       Consider the following criteria and rate the summary from 1 to 5 for each:

      1. Clarity: How effectively does the summary maintain clarity and avoid unnecessary jargon?
      2. Communication: To what extent does the summary convey the core findings and significance of the research along with its impact on future research or applications.
      3. Readability: How easily can the summary be read and comprehended?
      4. Accuracy: To what degree is the summary typographically and grammatically sound?

      Provide ratings for each criterion to assess the overall quality of the summary.

        """

        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chain_of_thought_prompt}
            ],
            temperature=0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        # print("value ",response["choices"][0]["message"]["content"])

        value_extract = Extraction()
        return value_extract.extract_scores(response["choices"][0]["message"]["content"])

