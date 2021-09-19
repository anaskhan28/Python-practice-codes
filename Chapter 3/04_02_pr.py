letter = ''' Dear <|NAME|>,
Greetings from Deloite Company. We are greaful to announce
that your resume and your skills are impacacble to work with us.
And You are selected!
regards and wonderful day ahead
bill
 Date : <|DATE|>
 '''
name = input("Enter your name\n")
date = input("Enter your date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)