import time

def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    print("Press Enter when you're ready to start.")
    input()
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    words = user_input.split()
    word_count = len(words)
    accuracy = calculate_accuracy(text, user_input)
    speed = calculate_speed(word_count, elapsed_time)
    print("Results:")
    print("Time elapsed:", round(elapsed_time, 2), "seconds")
    print("Word count:", word_count)
    print("Accuracy:", round(accuracy, 2), "%")
    print("Speed:", round(speed, 2), "words per minute")

def calculate_accuracy(original_text, user_input):
    correct_chars = sum(1 for a, b in zip(original_text, user_input) if a == b)
    total_chars = len(original_text)
    accuracy = (correct_chars / total_chars) * 100
    return accuracy

def calculate_speed(word_count, elapsed_time):
    minutes = elapsed_time / 60
    speed = word_count / minutes
    return speed

# Run the speed typing test
speed_typing_test()
