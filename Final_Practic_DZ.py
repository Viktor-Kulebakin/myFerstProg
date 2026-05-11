
import random

def load_data(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and ':' in line:
                    word, description = line.split(':', 1)
                    data.append((word.lower(), description.strip()))
        if not data:
            print(f"⚠️  Ошибка: Файл '{filename}' пуст или неверный формат")
            exit(1)
        return data
    except FileNotFoundError:
        print(f"⚠️  Ошибка: файл '{filename}' не найден.")
        exit(1)

def play_game():
    game_data = load_data('word.txt')
    while True:  # Цикл для повторной игры
        target_word, description = random.choice(game_data)
        displayed = ['_'] * len(target_word)
        word_letters = set(target_word)
        used_letters = set()
        attempts = 8

        print("\n" + "="*30)
        print("🎲 НОВАЯ ИГРА: ВИСЕЛИЦА")
        print("="*30)

        while attempts > 0 and '_' in displayed:
            print(f"Подсказка: {description}")
            print('Слово:', ' '.join(displayed))
            print(f"Попыток осталось: {attempts}")
            print(f"Использованные буквы: {', '.join(sorted(used_letters))}\n")

            user_input = input("Введите букву или попробуйте угадать слово: ").lower()

            if len(user_input) > 1: # Попытка угадать слово целиком
                if user_input == target_word:
                    print(f"\n🎉 Поздравляю, вы угадали слово: {target_word.upper()}")
                    break
                else:
                    print("❌ Неверно. Это не то слово.\n")
                    attempts -= 1
                    continue
        
            if len(user_input) != 1 or not user_input.isalpha(): # Проверка на ввод одной буквы
                print("⚠️ Ошибка: пожалуйста, введите одну букву.\n")
                continue

            if user_input in used_letters:
                print(f"↩️  -> Буква '{user_input}' уже была.\n")
                continue

            used_letters.add(user_input)

            if user_input in word_letters:
                for i, letter in enumerate(target_word):
                    if letter == user_input:
                        displayed[i] = letter
                print(f"✅ -> Есть такая буква!\n")
            else:
                attempts -= 1
                print(f"❌ -> Такой буквы нет.\n")
        
        if '_' not in displayed:
            print(f"\n🎉 Поздравляю, вы угадали слово: {target_word.upper()}")
        else:
            print(f"\n💀 Вы проиграли. Было загадано слово: {target_word.upper()}")
               
        replay = input("\nСыграть ещё раз? (да/нет): ").strip().lower()
        if replay not in ('да', 'д', 'yes', 'y'):
            print("👋 Спасибо за игру!")
            break

if __name__ == "__main__":
    play_game()