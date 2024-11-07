
class Extraction:
    # def extract_scores(self,evaluation_result):
    #     # Split the input text into lines
    #     lines = evaluation_result.split('\n')
    #
    #     # Create a dictionary to store scores
    #     scores = {}
    #     score =[]
    #     # Iterate through each line to extract scores
    #     for line in lines:
    #         # Split the line into words
    #         words = line.split()
    #
    #         # Check if the line contains a valid score entry
    #         if len(words) >= 2 and words[0] in ['Clarity:', 'Communication:', 'Simplification:', 'Readability:',
    #                                            'Entity', 'Accuracy:', 'Grammar:', 'Conciseness:']:
    #             # Extract the category and score
    #             category = ' '.join(words[:-1])  # Join all words except the last one
    #             s =  float(words[-1])
    #             score.append(float(words[-1]))
    #
    #             # Store the category and score in the dictionary
    #             scores[category] = s
    #     print("dictionary ",scores)
    #     return score

    def extract_scores(self, evaluation_result):
        # Split the input text into lines
        lines = evaluation_result.split('\n')

        # Create a dictionary to store scores
        scores = {}
        score=[]
        # Iterate through each line to extract scores
        for line in lines:
            # Split the line into words
            words = line.split()

            # Check if the line contains a valid score entry
            if len(words) >= 2 and words[-1].isdigit():
                # Extract the category and score
                # category = ' '.join(words[:-1])  # Join all words except the last one
                score.append(float(words[-1]))

                # Store the category and score in the dictionary
                # scores[category] = score

        return score

# Example usage:
