class Evaluator:

    def evaluate(self, answer, keywords):

        answer_lower = answer.lower()

        matched_keywords = []

        for keyword in keywords:
            if keyword.lower() in answer_lower:
                matched_keywords.append(keyword)

        total_keywords = len(keywords)
        matched_count = len(matched_keywords)

        if total_keywords == 0:
            return {
                "correct": False,
                "score": 0,
                "matched_keywords": [],
                "feedback": "This question cannot be evaluated."
            }

        score = round((matched_count / total_keywords) * 10)

        if score >= 7:
            correct = True
            feedback = "Excellent answer! You covered the important concepts."

        elif score >= 5:
            correct = True
            feedback = "Good answer, but you can explain the concept in more detail."

        else:
            correct = False
            feedback = "Your answer needs improvement. Try covering more key concepts."

        return {
            "correct": correct,
            "score": score,
            "matched_keywords": matched_keywords,
            "feedback": feedback
        }