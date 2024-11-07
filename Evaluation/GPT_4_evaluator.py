from Evaluation.prompt import EvaluationSummarization

import pandas as pd

class Evaluation_using_GPT_4:

    # abstract = "Deep Neural Networks (DNNs) are powerful models that have achieved excel- lent performance on difficult learning tasks. Although DNNs work well whenever large labeled training sets are available, they cannot be used to map sequences to sequences. In this paper, we present a general end-to-end approach to sequence learning that makes minimal assumptions on the sequence structure. Our method uses a multilayered Long Short-Term Memory (LSTM) to map the input sequence to a vector of a fixed dimensionality, and then another deep LSTM to decode the target sequence from the vector. Our main result is that on an English to French translation task from the WMT’14 dataset, the translations produced by the LSTM achieve a BLEU score of 34.8 on the entire test set, where the LSTM’s BLEU score was penalized on out-of-vocabulary words. Additionally, the LSTM did not have difficulty on long sentences. For comparison, a phrase-based SMT system achieves a BLEU score of 33.3 on the same dataset. When we used the LSTM to rerank the 1000 hypotheses produced by the aforementioned SMT system, its BLEU score increases to 36.5, which is close to the previous best result on this task. The LSTM also learned sensible phrase and sentence representations that are sensitive to word order and are relatively invariant to the active and the pas- sive voice. Finally, we found that reversing the order of the words in all source sentences (but not target sentences) improved the LSTM’s performance markedly, because doing so introduced many short term dependencies between the source and the target sentence which made the optimization problem easier"
    # summary = "The paper presents an end-to-end sequence learning method using multilayered Long Short-Term Memory (LSTM) for tasks like English to French translation, demonstrating high accuracy, increased BLEU score, and efficient handling of long sentences, as well as introducing a successful strategy of reversing word order in source sentences to improve performance."
    # prompt_call = EvaluationSummarization()
    # evaluator = prompt_call.generate_evaluation_with_prompts(abstract, summary)
    #
    # print("evaluator ",evaluator)
    # print("index0 ",evaluator[0])
    # print("index1 ", evaluator[1])
    # print("index2 ", evaluator[2])
    # print("index3 ", evaluator[3])
    # print("index4 ", evaluator[4])
    # print("index5 ", evaluator[5])
    # print("index6 ", evaluator[6])
    # print("index7 ", evaluator[7])

    # evaluation_result = """
    # Clarity: 4
    # The summary is quite clear and presents the main idea without much jargon. However, terms like "parameters" and "pruning" might not be clear to someone without a background in neural networks.
    #
    # Communication: 4
    # The summary effectively communicates the core findings, particularly the impact on storage and computation requirements and the preservation of accuracy. It could be improved by briefly explaining the significance of reducing parameters in models like AlexNet and VGG-16 for a non-specialist audience.
    #
    # Simplification: 3
    # The summary uses terms like "parameters," "pruning," and "retrain" which are common in machine learning but might not be understood by everyone. A brief explanation of these terms could make the summary more accessible.
    #
    # Readability: 4
    # The summary is well-structured and easy to follow, but the use of technical terms without explanation might hinder comprehension for some readers.
    #
    # Entity Inclusion: 5
    # The summary includes important entities such as the neural network models AlexNet and VGG-16, and mentions the specific dataset (ImageNet) used for validation.
    #
    # Accuracy: 5
    # The summary accurately reflects the content of the abstract, including the method used and the results achieved.
    #
    # Grammar: 5
    # The summary is grammatically correct with no errors.
    #
    # Conciseness: 4
    # The summary is concise, but there might be an opportunity to streamline it further by combining some of the points. For example, "learning and maintaining"
    # """
    # e= Extraction()
    # scores = e.extract_scores(evaluation_result)
    # print(scores)

    def __init__(self):
        self.encoding = 'utf-8'

    def evaluate_summary_using_gpt_4(self, dataset, abstract_name, summary_name, Evaluation):




        # Create an instance of the EvaluationSummarization class
        prompt_call = EvaluationSummarization()

        # Create the columns if they don't exist
        for category in ['clarity', 'communication', 'Readability', 'Accuracy']:
            column_name = f'{Evaluation}_{category}'
            if column_name not in dataset.columns:
                dataset[column_name] = None  # You can replace None with the default value you want

        # Assuming dataset is your DataFrame and index is the row index
        # for index , row in dataset.iterrows():
        for index, row in dataset.iloc[496:, :].iterrows():  # Start from index 6
            if index ==501:
                break
            # Extract the abstract and summary from the current row
            abstract = row[abstract_name]
            summary = row[summary_name]

            # Generate the evaluation score using the GPT-4 model
            evaluation_score = prompt_call.generate_evaluation_with_prompts(abstract, summary)

            print("index ",index)
            # print("length ",len(evaluation_score))
            # print("evaluation_score ",evaluation_score)

            # Check if evaluation_score has enough elements
            if len(evaluation_score) >= 4:
                # Assign the evaluation scores to the respective columns after explicitly casting to float
                dataset.at[index, f'{Evaluation}_clarity'] = float(evaluation_score[0])
                dataset.at[index, f'{Evaluation}_communication'] = float(evaluation_score[1])
                dataset.at[index, f'{Evaluation}_Readability'] = float(evaluation_score[2])
                dataset.at[index, f'{Evaluation}_Accuracy'] = float(evaluation_score[3])
                # dataset.at[index, f'{Evaluation}_entity_inclusion'] = float(evaluation_score[4])
                # dataset.at[index, f'{Evaluation}_accuracy'] = float(evaluation_score[5])
                # dataset.at[index, f'{Evaluation}_grammar'] = float(evaluation_score[6])
                # dataset.at[index, f'{Evaluation}_conciseness'] = float(evaluation_score[7])
            else:
                # Handle the case where evaluation_score doesn't have enough elements
                print(f"Warning: Insufficient elements in evaluation_score for index {index}")

        # Save the dataset with summaries to a new CSV file
        # dataset.to_csv("Benchmark_data_with_100_data.csv", index=False)
            dataset.to_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset.csv", index=False)

