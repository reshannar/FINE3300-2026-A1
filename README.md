# FINE3300-2026-A1
Assignment 1 for Python for Finance

Part 1: 

I created a dropdown list like option to select the specific date the user would like the exchange rate to be from. To limit the amount of inputs and conditions, the way the program is created forces the user to use just the one date, they cannot enter in a range. Using the date the user selected, the program selects the rate (from USD to CAD) from that date but it isn't solidified as the rate to be used for the conversion until the user also inputs what the currency they are converting from and to are. Once the from and to currencies are chosen, the program runs an if statement to determine if the rate will need to be changed from its current "USD to CAD" form into a "CAD to USD" form. 

Part 2: 

For the AI portion, the prompt I used, which is commented within the code the AI created, was the way that I interpreted the question and how it should be solved. I tried to be as specific about the requirements and method as possible. I used Claude in order to create the program.

Interpretation of Results: 

The program that Claude created seems a lot more involved than the one that I created. My program appears to be much shorter and simpler, which could be good and bad. Simpler code is easier to process and easier to fix, but it doesn't catch all or close to all scenarioes which Claude's version does. The Vibe Coding also has a much more complex and in-depth class and methods. The comments used are much more sparse as well compared to my version which is largely due to my habit of commenting out code that doesn't work so I know what I've tried. The Claude code and output is definitely a lot more sophisticated than what I wrote for the code, but it also feels a lot more clunky and reminds me of the exercise that coding professors and teachers make beginner students do to understand how algorithms work. For example, the way I chose to make the distinction between "USD to CAD" and "CAD to USD" is much simpler than Claude's version. In mine, the code consists of two user inputs and a single if/elif statement. Claude's version uses 3-4 different prompts, methods, and objects, either within the class or outside of it to determine the final calculation to use for the rate. To summarize, my code in part 1 of the assignment relies more heavily on the user input to do the internal calculations to arrive at the final result while Claude's version relies more on the computer and commands doing the heavy lifting. 