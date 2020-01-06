#encoding =utf-8

import pyautogui, time

# Set these to the correct coordinates  for your computer

nameField = (648, 319)
submitButton = (651, 817)
submitButtonColor = (75, 141, 249)
submitAotherLink = (760, 224)

#
formData = [{
    'name': 'Alice',
    'fear': 'eavesdroppers',
    'source': 'wand',
    'robocop': 4,
    'comments': 'Tell Bob I said hi'
}, {
    'name': 'Bob',
    'fear': 'bees',
    'source': 'crytstal ball',
    'robocop': 1,
    'comments': 'Please take the puppets out of the break room'
}, {
    'name':
    'Alex Murphy',
    'fear':
    'ED-209',
    'source':
    'money',
    'robocop':
    5,
    'comments':
    'Protect the innocent.Serve the public trust. Uphold the law.'
}]
pyautogui.PAUSE = 0.5

for person in formData:
    # Give  the user a chance to kill the script
    print('>>> 5 SECOND PAUSE TO LET  USER PRESS CTRL-C <<<')
    time.sleep(5)

    #wait until the form page hss loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
                                          submitButtonColor):
        time.sleep(0.5)

    print('Entering %s info....' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    #Fill out the Name  field.
    pyautogui.typewrite(person['name'] + '\t')

    #Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')

    #Fill out the Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    #Fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t']) 

    #Fill out the Additional comments field.
    pyautogui.typewrite(person['comments']+'\t')

    #Click Submit.
    pyautogui.perss('enter')

    #Wait until form page has loaded
    print('Clicket Submit')
    time.sleep(5)

    #Click the Submit another response link.
    pyautogui.click(submitAotherLink[0],submitAotherLink[1])