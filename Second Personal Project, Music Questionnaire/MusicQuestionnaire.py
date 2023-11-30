"""Music Questionnaire

Author: William Jedrzejczak.

Version: 9/18/2023
"""


class MoodQuestionnaire:
    def __init__(self):
        self.mood_mapping = {
            'happy': 'pop',
            'sad': 'blues',
            'energetic': 'rock',
            'calm': 'ambient',
        }
        self.user_mood = None
        self.user_preferences = {
            'tempo': 0,
            'lyrics': 0,
            'instrumental': 0,
        }

    def ask_question(self, question, options):
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        answer = int(input("Enter the number corresponding to your choice: "))
        while answer not in range(1, len(options) + 1):
            print("Invalid choice. Please select a valid option.")
            answer = int(input("Enter the number corresponding to your choice: "))
        return options[answer - 1]

    def get_user_mood(self):
        print("Welcome to the Advanced Mood-Based Music Genre Selector!")

        self.user_mood = self.ask_question("How do you feel today?", ['Happy', 'Sad', 'Energetic', 'Calm'])

        if self.user_mood.lower() not in self.mood_mapping:
            print("Invalid mood. Exiting the program.")
            return

        print("\nGreat! Now let's delve deeper to refine your music preferences.")

        self.user_preferences['tempo'] = int(input("On a scale of 1 to 10, how much do you prefer upbeat and fast-paced music? "))
        self.user_preferences['lyrics'] = int(input("On a scale of 1 to 10, how important are lyrics to you in a song? "))
        self.user_preferences['instrumental'] = int(input("On a scale of 1 to 10, how much do you enjoy instrumental music? "))

        print("\nAnalyzing your responses...")

        # Apply scoring to determine the most suitable genre
        max_score = max(self.user_preferences.values())
        preferred_categories = [key for key, value in self.user_preferences.items() if value == max_score]

        if len(preferred_categories) == 1:
            preferred_category = preferred_categories[0]
            recommended_genre = self.mood_mapping[self.user_mood.lower()]
            print(f"\nBased on your responses, I recommend listening to {recommended_genre} music, which aligns with your preference for {preferred_category}.")
        else:
            print("\nYour preferences are diverse. Here are some recommendations based on your different preferences:")
            for category in preferred_categories:
                recommended_genre = self.mood_mapping[self.user_mood.lower()]
                print(f"- For your preference in {category}, I recommend {recommended_genre} music.")


questionnaire = MoodQuestionnaire()
questionnaire.get_user_mood()
