print('Hello, welcome to Alisa Triviago!')
ans = input('Are you ready to play (yes/no):')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input ('1. What is my name?')
    if ans.lower() == 'alisa atkinson':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ('2. What is my age?')
    if ans == '37':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
        
    ans = input ('3. What do I do for a living?')
    if ans.lower() == 'technical writer' or ans.lower() == 'writer':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ('4. What animal do I like better dogs or cats?')
    if ans.lower() == 'dogs':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ('5. Who is my favorite super hero Batman or Superman?')
    if ans.lower() == 'Superman':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

print('Thank you for playing, you got', score, "questions correct.")
mark = (score/total_q) * 100

print("Mark: ", str(mark) + '%')
print('Goodbye')
