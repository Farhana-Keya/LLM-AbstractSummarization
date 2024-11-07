# from Prompt_selection import Get_summary_from_prompt
import pandas as pd

from Prompt_selection.prompting import Get_Prompting



class LLM_Result:
    def __init__(self):
        self.encoding = 'utf-8'
    def get_result_from_zero_shot_prompt(self,model_name):
        dataset = pd.read_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset.csv")
        # Create an instance of the EvaluationSummarization class
        summary = Get_Prompting()


        # Assuming dataset is your DataFrame and index is the row index
        for index, row in dataset.iterrows():
            if index == 501:
                break
            abstract = row['Abstract']

            # Generate the evaluation score using the GPT-4 model
            get_summary = summary.get_summary_from_zero_shot_prompting(model_name,abstract)

            print("index ", index)

            dataset.at[index, f'summary_{model_name}_zero_shot_prompting'] = get_summary

        # Save the dataset with summaries to a new CSV file
            dataset.to_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset.csv", index=False)

    def get_result_from_few_shot_prompt(self, model_name):
        dataset = pd.read_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset.csv")

        # Create an instance of the EvaluationSummarization class
        summary = Get_Prompting()

        # Assuming dataset is your DataFrame and index is the row index
        for index, row in dataset.iterrows():
            if index == 501:
                break
            abstract = row['Abstract']

            # Generate the evaluation score using the GPT-4 model
            get_summary = summary.get_summary_from_few_shot_prompting(model_name, abstract)

            print("index ", index)

            dataset.at[index, f'summary_{model_name}_few_shot_prompting'] = get_summary

        # Save the dataset with summaries to a new CSV file
            dataset.to_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset.csv", index=False)

    def get_result_from_chain_of_though_prompt(self, model_name):
        dataset = pd.read_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset.csv")

        # Create an instance of the EvaluationSummarization class
        summary = Get_Prompting()

        # Assuming dataset is your DataFrame and index is the row index
        for index, row in dataset.iterrows():
            if index == 501:
                break
            abstract = row['Abstract']

            # Generate the evaluation score using the GPT-4 model
            get_summary = summary.get_summary_from_chain_of_thought_prompting(model_name, abstract)

            print("index ", index)

            dataset.at[index, f'summary_{model_name}_chain_of_thought_prompting'] = get_summary

        # Save the dataset with summaries to a new CSV file
            dataset.to_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset.csv",index=False)









