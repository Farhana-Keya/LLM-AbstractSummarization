import re
from openai import OpenAI
import random
import pandas as pd


api_key = ""
client = OpenAI(api_key=api_key)

class Get_Prompting:
    def __init__(self):
        self.encoding = 'utf-8'

    def get_summary_from_zero_shot_prompting(self, model_name, paper_abstract):

        zero_shot_prompt = f"""
            ### Instruction: Write a summary for aiming to assist researchers in capturing the gist of the contribution of scientific papers.Summarize the following 
            paper abstract in one concise sentence,focusing on a clear and concise description of the research contribution. Make sure to highlight in your summary the research problem, 
            the specific approach chosen and the obtained results if provided.

            ### Input:

            paper abstract: {paper_abstract}

            Response format: 
            Write only one concise sentence 


            ### Response: 
            """

        response = client.chat.completions.create(model=model_name,
        messages=[
            {"role": "system", "content": "You are a research assistant."},
            {"role": "user", "content": zero_shot_prompt}
        ],
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)

        return response.choices[0].message.content

    def get_summary_from_few_shot_prompting(self, model_name, paper_abstract):
        # Assign two variables to random integers from 1 to 8 ensuring they are unique

        few_shot_examples = pd.read_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Few_shot_examples .csv")

        random_numbers = random.sample(range(0, 8), 2)

        # Assign the values to two variables
        var1, var2 = random_numbers
        few_shot_prompt = f"""
            ### Instruction: Provide a one-sentence summary of the following research paper abstract:

            ### Input:
            1. Example : Abstract: {few_shot_examples['Abstract'][var1]}
                  Summary: {few_shot_examples['Summary'][var1]}
            2. Example : Abstract: {few_shot_examples['Abstract'][var2]}
                   Summary: {few_shot_examples['Summary'][var2]}

            3. paper abstract: {paper_abstract}

            Response format: 
            3. Write only one concise sentence 

           ### Response:
           """
        response = client.chat.completions.create(model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": few_shot_prompt}
        ],
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)

        return response.choices[0].message.content.replace("Summary: ", "")

    def get_summary_from_chain_of_thought_prompting(self, model_name, paper_abstract):

        chain_of_thought_prompt = f"""
         ### Instruction: Craft a one-sentence summary for the given research paper abstract using this chain of thought,
             the resulting summary should fit within the constraints provided and give the plain text only for overall constraints
             provided:

            ### Input: 
            Chain of thought:
                1. **Context Setting:**
                 - Imagine you're presenting the key findings of a scientific paper to a diverse audience.
                 - Assume you have limited time, and your goal is to convey the essence of the paper efficiently.

                 2. **Initial Thoughts:**
                 - Begin by considering the broader field or domain to which the research belongs.
                 - Think about why the research problem addressed in the paper is relevant and important.

                 3. **Key Contributions:**
                 - Identify the main contributions of the paper – what sets it apart from existing work?
                 - Consider the novel methodologies, algorithms, or insights presented.

                4. **Results and Impact:**
                - Reflect on the results and their implications for the field.
                - Envision how the findings might impact future research or applications.

                5. **Audience Understanding:**
                - Keep in mind that your audience may have varied expertise levels.
                - Aim for clarity and simplicity while maintaining accuracy.

                6. **Synthesis:**
                - Combine your thoughts into a cohesive one-sentence summary.
                - Focus on capturing the core message and significance of the research.

            paper abstract: {paper_abstract}

            Response format: 
            3. Write only one concise sentence 

           ### Response:
        """
        response = client.chat.completions.create(model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": chain_of_thought_prompt}
        ],
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)

        return response.choices[0].message.content



