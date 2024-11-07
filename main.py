# from Evaluation.prompt  import api_key
# Press the green button in the gutter to run the script.

from Evaluation.GPT_4_evaluator import Evaluation_using_GPT_4
import pandas as pd

if __name__ == '__main__':
    print('PyCharm')

    # dataset = pd.read_csv("Benchmark_data_with_100_data.csv")

    # evaluator = Evaluation_using_GPT_4()
    # abstract = 'Abstract'

    # summary_GPT_4_Turbo'
    # summary = 'summary_GPT_4_Turbo'
    # evaluation = 'gpt_4_Turbo'

    # For GPT-4
    # summary = 'summary_gpt_4'
    # evaluation = 'gpt_4'

    #For gpt_3.5_turbo_1106
    # summary = 'summary_gpt_3.5_turbo_1106'
    # evaluation = 'gpt_3.5_turbo_1106'

    # For llama_2
    # summary = 'summary_llama_2'
    # evaluation = 'llama_2'
    # print("dataset length ", len(dataset))
    # evaluator. evaluate_summary_using_gpt_4(dataset,abstract,summary,evaluation)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# prompt selection .............

    # main= summary_mixtral:8x7b_zero_shot_prompting
    # main1= summary_mixtral:8x7b_few_shot_prompting
    # main2= summary_mixtral:8x7b_chain_of_though_prompting
    # main3= summary_mixtral:8x7b_few_shot_prompting
    # main4= summary_VAGOsolutions/Llama-3-SauerkrautLM-8b-Instruct_zero_shot_prompting
    # main5= summary_mixtral:8x7b_chain_of_though_prompting




    dataset = pd.read_csv("/home/farhana/Documents/Recommendation_System/dataset_creation/Benchmark_dataset1.csv")
    evaluator = Evaluation_using_GPT_4()
    abstract = 'Abstract'
    summary = 'summary_phi3:medium_few_shot_prompting'
    evaluation = 'phi3:medium_few_shot_prompting'
    # 10 times

    # summary = 'summary_gpt-3.5-turbo-1106_few_shot_prompting'
    # evaluation = 'gpt-3.5-turbo-1106_few_shot_prompting'


    # summary = 'summary_gpt-3.5-turbo-1106_chain_of_thought_prompting'
    # evaluation = 'gpt-3.5-turbo-1106_chain_of_thought_prompting'

    # summary = 'summary_gpt-4-1106-preview_zero_shot_prompting'
    # evaluation = 'gpt-4-1106-preview_zero_shot_prompting'

    # summary = 'summary_gpt-4-1106-preview_few_shot_prompting'
    # evaluation = 'gpt-4-1106-preview_few_shot_prompting'
    #
    # summary = 'summary_gpt-4-1106-preview_chain_of_thought_prompting'
    # evaluation = 'gpt-4-1106-preview_chain_of_thought_prompting'

    # summary = 'summary_mistralai/Mistral-7B-Instruct-v0.1_zero_shot_prompting'
    # evaluation = 'mistralai/Mistral-7B-Instruct-v0.1_zero_shot_prompting'


    #
    # summary = 'summary_mistralai/Mistral-7B-Instruct-v0.1_few_shot_prompting'
    # evaluation = 'mistralai/Mistral-7B-Instruct-v0.1_few_shot_prompting'
    #
    # summary = 'summary_mistralai/Mistral-7B-Instruct-v0.1_chain_of_though_prompting'
    # evaluation = 'mistralai/Mistral-7B-Instruct-v0.1_chain_of_though_prompting'

    # summary = 'summary_meta-llama/Llama-2-13b-chat-hf_zero_shot_prompting'
    # evaluation = 'meta-llama/Llama-2-13b-chat-hf_zero_shot_prompting'
    #
    # summary = 'summary_meta-llama/Llama-2-13b-chat-hf_few_shot_prompting'
    # evaluation = 'meta-llama/Llama-2-13b-chat-hf_few_shot_prompting'

    #
    # summary = 'summary_meta-llama/Llama-2-13b-chat-hf_chain_of_though_prompting'
    # evaluation = 'meta-llama/Llama-2-13b-chat-hf_chain_of_though_prompting'
    # summary = 'summary_tiiuae/falcon-40b-instruct_zero_shot_prompting'
    # evaluation = 'tiiuae/falcon-40b-instruct_zero_shot_prompting'

# 3 times

    #
    # summary = 'summary_tiiuae/falcon-40b-instruct_few_shot_prompting'
    # evaluation = 'tiiuae/falcon-40b-instruct_few_shot_prompting'


    # summary = 'summary_tiiuae/falcon-40b-instruct_chain_of_though_prompting'
    # evaluation = 'tiiuae/falcon-40b-instruct_chain_of_though_prompting'
    # print("dataset length ", len(dataset))
    evaluator. evaluate_summary_using_gpt_4(dataset,abstract,summary,evaluation)