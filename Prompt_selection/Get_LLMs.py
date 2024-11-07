from Prompt_selection.Result import LLM_Result

getResult = LLM_Result()

model_name = "gpt-3.5-turbo-1106"
print("zero shot")
getResult.get_result_from_zero_shot_prompt(model_name)
print("few shot")
getResult.get_result_from_few_shot_prompt(model_name)
print("Chain of thought")
getResult.get_result_from_chain_of_though_prompt(model_name)
#
# model_name = "gpt-4-1106-preview"
# getResult.get_result_from_zero_shot_prompt(model_name)
# getResult.get_result_from_few_shot_prompt(model_name)
# getResult.get_result_from_chain_of_though_prompt(model_name)




