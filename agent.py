"""
Autonomous Consultant Agent
A thinking system that turns messy ideas into structured strategy.
"""

class ConsultantAgent:
    def __init__(self):
        self.context = []

    def clarify(self, user_input):
        questions = [
            "What made this idea important to you?",
            "Who is this for: you, a customer, or a larger audience?",
            "What would success look like in 6 months?",
            "What is the biggest confusion you feel right now?"
        ]
        return questions

    def frame_problem(self, user_input, answers):
        return f"""
Based on your input and answers, the real problem is not the idea itself,
but the lack of clarity around direction and outcome.

You are trying to move forward without a defined identity, goal, or constraint.
This is a *framing problem*, not an idea problem.
"""

    def build_strategy(self, framed_problem):
        return """
Strategy:

1. Define who you want to become through this idea.
2. Narrow the domain to one clear use case.
3. Validate it with a small real-world experiment.
4. Turn learning into a repeatable system.
"""

    def next_actions(self):
        return [
            "Write a one-line identity statement.",
            "List 3 problems you personally face.",
            "Pick one and design a tiny solution.",
            "Test it with one real person."
        ]

    def run(self, user_input):
        questions = self.clarify(user_input)
        framed = self.frame_problem(user_input, questions)
        strategy = self.build_strategy(framed)
        actions = self.next_actions()

        return {
            "clarifying_questions": questions,
            "problem_framing": framed,
            "strategy": strategy,
            "next_actions": actions
        }


if __name__ == "__main__":
    agent = ConsultantAgent()
    user_input = input("Describe your idea or confusion: ")
    output = agent.run(user_input)

    print("\n--- Clarifying Questions ---")
    for q in output["clarifying_questions"]:
        print("-", q)

    print("\n--- Problem Framing ---")
    print(output["problem_framing"])

    print("\n--- Strategy ---")
    print(output["strategy"])

    print("\n--- Next Actions ---")
    for a in output["next_actions"]:
        print("-", a)
