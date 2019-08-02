class Colors:
    underline = '\033[04m'
    red = '\33[31m'
    lightblue = '\033[94m'
    end = '\033[0m'


print(f"""
######################################################################################
{Colors.underline}{Colors.lightblue}Madlib Game:{Colors.end} {Colors.lightblue}The Mona Lisa{Colors.end}          
                                                                                     
# After hiding the painting in his __________ for two years, he grew ________ and
tried to sell it to a/an __________ in Florence, but was caught. 
######################################################################################
""")

print("fill the blanks:")
print()

print("Enter a Noun")
noun1 = input()
print("Enter an Adjective")
adjective = input()
print("Enter a Noun")
noun2 = input()
print()
print(f"{Colors.lightblue}After hiding the painting in his {Colors.underline}{Colors.red}{noun1}{Colors.end} {Colors.lightblue}for two years, he grew {Colors.underline}{Colors.red}{adjective}{Colors.end} {Colors.lightblue}and tried to sell it to a/an {Colors.underline}{Colors.red}{noun2}{Colors.end} {Colors.lightblue}in Florence, but was caught.")

