from groq import Groq
client =Groq(api_key ="Put your API key here")
NAME = input("ENter your name : ")

print("AI ready Ha! quite liko band krnay kay liya")

while True:
    user_input = input("Aap  : ")
    if user_input.lower()== "quit":
        break
    response = client.chat.completions.create(
        model ="llama-3.3-70b-versatile",
        messages =
           [
            {"role": "system", "content": "Aap ek helpful assistant hain jo sirf Urdu mein jawab dete hain. Hamesha Urdu mein baat karo."},
            {"role": "user", "content": user_input}
        ]
    )

    print(f"{NAME} " ,response.choices[0].message.content)
    print()