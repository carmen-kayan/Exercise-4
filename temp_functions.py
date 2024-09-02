#define the function using the parameter of temp_fahrenheit
def fahr_to_celsius(temp_fahrenheit):
    """Function for converting degrees Fahrenheit to degrees Celsius

    parameter:
        temp_fahrenheit <float> = temperature in degrees Fahrenheit

    return:
        temp_celsius <float> = temperature in degrees Celsius
    """
    #calculation to be performed:
    temp_celsius=(temp_fahrenheit-32)/1.8
    
    #what should be returned
    return temp_celsius

#Define a function called temp_classifier with parameter temp_celsius
def temp_classifier(temp_celsius):
    """A function to classify temperatures into 4 groups according to the table below:

    | class 0            | Temperatures below -2 degrees Celsius                                    |
    | class 1            | Temperatures equal or warmer than -2, but less than +2 degrees Celsius   |
    | class 2            | Temperatures equal or warmer than +2, but less than +15 degrees Celsius  |
    | class 3            | Temperatures equal or warmer than +15 degrees Celsius

    parameter: 
        temp_celsius <float> = temperature in degrees celsius

    return:
        "class 0", "class 1", "class 2" or "class 3"

    """
    #if the temperature is less than -2 it returns 0
    if temp_celsius<- 2:
        return 0
    
    #if the temperature is more than or equal to -2 but less than 2 it returns 1
    elif temp_celsius >=- 2 and temp_celsius < 2:
        return 1
    
    #if the temperature is more than or equal to 2 but less than 15 it returns 2
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    
    #if the temperature is more than or equal to 15 it returns "3
    else:
        return 3