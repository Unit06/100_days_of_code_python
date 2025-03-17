#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def parse_name(text):
    temp_names = text.strip().split('\n')
    temp_names = [name for name in temp_names if name]
    return temp_names


def create_invitations(names):
    invitation_template = source_letter
    # invitations = []

    for name in names:
        # Replace the placeholder with the actual name
        personalized_invitation = invitation_template.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(personalized_invitation)

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    source_letter = file.read()

with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.read()

names_massive = parse_name(names)
create_invitations(names_massive)



# print(source_letter)
# print(names_massive)
