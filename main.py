import json

def load_questions_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data['questions']

def administer_test(questions):
    total_score = 0
    user_responses = []

    for i, question in enumerate(questions):
        print(f"問題 {i+1}: {question['question']}")
        print("選項：")
        for j, choice in enumerate(question['choices']):
            print(f"{j+1}. {choice['choice']}")

        response = input("請選擇你的回答（輸入選項編號）：")
        while not response.isdigit() or int(response) < 1 or int(response) > len(question['choices']):
            response = input("請輸入有效的選項編號：")

        selected_choice = question['choices'][int(response) - 1]
        user_responses.append(selected_choice)
        total_score += selected_choice['score']
        print()

    return total_score, user_responses

def classify_personality(score):
    if score >= 25:
        return "浪漫主義者"
    elif score >= 18:
        return "平衡追求者"
    else:
        return "實用主義者"

def main():
    json_file_path = "questions.json"
    questions = load_questions_from_json(json_file_path)
    print("歡迎參加愛情心理測驗！")
    print("請回答以下問題：\n")

    total_score, user_responses = administer_test(questions)
    personality_type = classify_personality(total_score)

    print("\n測驗結束，以下是你的測驗結果：")
    print("***************************")
    print("你的回答：")
    for i, response in enumerate(user_responses):
        print(f"問題 {i+1}: {response['choice']}（{response['score']}分）")
    print("***************************")
    print(f"總分：{total_score}分")
    print(f"你的人格類型：{personality_type}")

if __name__ == '__main__':
    main()
