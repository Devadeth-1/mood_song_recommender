
from textblob import TextBlob
# This program will ask the user how they are feeling and play a song based on their mood.



mood = input("How are you feeling today? ").lower()
blob_variable = TextBlob(mood).correct()
# Check the sentiment of the mood
sentiment_variable = blob_variable.sentiment.polarity
# Print the sentiment   

if sentiment_variable > 0.5:
    print("🎵 Ith Pwoli Moood!!!")
    
elif  sentiment_variable < -0.5:
    
    print("🎵 Ith Shokappaattu ")

# elif "angry" in mood:
#     print("🎵 Playing: 'Numb' by Linkin Park'")

# elif "love" in mood:
#     print("🎵 Playing: 'Perfect' by Ed Sheeran'")

else:
    print("🎵 Playing: Ith Edk Moood ")    


print(sentiment_variable)

    