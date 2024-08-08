import requests

preapproved_answers = {
    "login issue": "If you are experiencing login issues, please check your credentials and try again. If the problem persists, contact the support team.",
    "module load": "To load a module, use the command `module load <module_name>`. For a list of available modules, use the command `module avail`.",
    "job submission": "To submit a job, use the command `sbatch <script_name>`. Make sure your script includes the necessary SLURM directives.",
    "contact support": "You can contact support by emailing support@hpc.nyu.edu or calling the helpdesk at (555) 555-5555."
}

def get_answer(question):
    for keyword, answer in preapproved_answers.items():
        if keyword in question.lower():
            return answer
    return "Sorry, I don't understand your question. Please try again."

def main():
    print("Welcome to the AI Chatbot!")
    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = get_answer(question)
        print(f"Answer: {answer}")

if __name__ == '__main__':
    main()
