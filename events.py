# events.py

events = [
    {
        "question": "당신은 길을 걷다가 신비한 동굴을 발견했습니다. 동굴에 들어가시겠습니까?",
        "choices": {
            "enter": "당신은 동굴 안으로 들어갔습니다. 보물을 발견했습니다!",
            "leave": "당신은 동굴을 떠났습니다. 길을 계속 걸어갑니다."
        }
    },
    {
        "question": "당신은 마법사를 만났습니다. 마법사가 당신에게 주문을 가르쳐주겠다고 합니다. 배우시겠습니까?",
        "choices": {
            "learn": "당신은 마법을 배웠습니다. 강해졌습니다!",
            "ignore": "당신은 마법사를 무시했습니다. 마법사는 화를 내며 떠났습니다."
        }
    },
    # 18 more events...
    {
        "question": "당신은 길에서 늑대를 만났습니다. 싸우시겠습니까?",
        "choices": {
            "fight": "당신은 늑대와 싸워 이겼습니다!",
            "flee": "당신은 늑대에게서 도망쳤습니다. 다행히도 아무 일도 일어나지 않았습니다."
        }
    }
    # Add more events here
]

if __name__ == "__main__":
    import random
    event = random.choice(events)
    print(event["question"])
    for choice, outcome in event["choices"].items():
        print(f"- {choice}: {outcome}")
