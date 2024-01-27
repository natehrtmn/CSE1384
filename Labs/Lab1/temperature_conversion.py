prompt1 = 'Enter "Celsius", "Fahrenheit", or "Kelvin" to state the units of the temperature you input, or enter "Quit" to exit: '
prompt2 = 'Enter "Celsius", "Fahrenheit", or "Kelvin" to state the units of the temperature you want to convert to: '
prompt3 = 'Enter the value of your input temperature: '
bad_input_prompt = 'Entered value isn\'t recognized'

user_input = None

while (user_input != 'Quit'):

    #Gets the input units from the user 
    user_input = input(prompt1).title()
    while (user_input not in ('Celsius', 'Fahrenheit', 'Kelvin')):
        print(bad_input_prompt)
        user_input = input(prompt1).title()

    units_input = user_input

    #Gets the output units from the user
    user_input = input(prompt2).title()
    while (user_input not in ('Celsius', 'Fahrenheit', 'Kelvin') or user_input == units_input):
        print(bad_input_prompt, 'or is the same as previous input')
        user_input = input(prompt2).title()

    units_output = user_input

    #Gets the input number from the user
    user_input = float(input(prompt3))
    while (not isinstance(user_input, float)):
        print(bad_input_prompt)
        user_input = float(input(prompt3))

    number_input = user_input

    #Converst the value ===========================================================

    #Celsius to Fahrenheit
    if (units_input == 'Celsius' and units_output == 'Fahrenheit'):
        number_output = (number_input * (9/5)) + 32

    #Celsius to Kelvin
    elif (units_input == 'Celsius' and units_output == 'Kelvin'):
        number_output = number_input + 273.15
    
    #Fahrenheit to Celsius
    elif (units_input == 'Fahrenheit' and units_output == 'Celsius'):
        number_output = (number_input - 32) * (5/9)
    
    #Fahrenheit to Kelvin
    elif (units_input == 'Fahrenheit' and units_output == 'Kelvin'):
        number_output = (number_input - 32) * (5/9) + 273.15

    #Kelvin to Celsius
    elif (units_input == 'Kelvin' and units_output == 'Celsius'):
        number_output = number_input - 273.15

    #Kelvin to Fahrenheit
    elif (units_input =='Kelvin' and units_output == 'Fahrenheit'):
        number_output = ((number_input - 273) * (9/5)) + 32

    print(f'{number_input} {units_input} = {number_output} {units_output}')

print('Goodbye!')
