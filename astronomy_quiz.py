print("If you are an astronomy lover, you are in the right place")
print("Quiz type: Basic Astronomy")
print("Quiz has started")
score = 0
questions = [ ]
questions.append({
    "question": "What galaxy do we live in?",
    "a": "Andromeda",
    "b": "Milky way",
    "c": "Whirlpool",
    "d": "Sombrero",
    "answer": "b"
})
questions.append({
    "question": "How many planets are there in the solar system?",
    "a": "6",
    "b": "7",
    "c": "8",
    "d": "9",
    "answer": "c"
})
questions.append({
    "question": "How many natural satellites does the Earth have?",
    "a": "1",
    "b": "2",
    "c": "0",
    "d": "4",
    "answer": "a"
})
questions.append({
    "question": "When a large star collapses under its own weight, what does it become?",
    "a": " A Black Hole",
    "b": "A blue dwarf",
    "c": "A nebula",
    "d": "A red giant",
    "answer": "a"
})
questions.append({
    "question": "What's believed to be at the center of our galaxy?",
    "a": "A super planet",
    "b": "A massive black hole",
    "c": "Nothing",
    "d": "God",
    "answer": "b"
})
questions.append({
    "question": "What is the event horizon ?",
    "a": "The amount of time remaining before the sun dies out",
    "b": "The period of time between sunset and full dark",
    "c": "The amount of time it takes Mercury to transit the sun",
    "d": "The boundary of a black hole at which light can no longer escape",
    "answer": "d"
})
for q in questions:
    print(q["question"])
    print("a)", q["a"])
    print("b)", q["b"])
    print("c)", q["c"])
    print("d)", q["d"])
    guess = input("Enter your answer (a/b/c/d): ")
    if guess == q["answer"] :
        print("Correct!")
        score += 1
    else : 
        print("Wrong!")
print("Game Over! Your score:" , score)