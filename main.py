import mood_responses

def main():
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_responses(mood))

if __name__ == "__main__":
    main()