class Evaluator:

    def evaluate(self, answer, keywords):
        matched_keywords = 0

        for keyword in keywords:
            if keyword.lower() in answer.lower():
                matched_keywords += 1

        if matched_keywords >= 2:
            return True

        return False