Problem Solving lesson
Here is your system prompt for this task, you must do it │
│ in this file: '/Users/joelgullo/dev/latex-beamer/src/cs12/slides/10_problem-set-1-loops.tex' Here is the context for whats needed in the │
│ presentation including the latex of a previous draft and the associated pictures in the latex draft. there is also the problem set and example │
│ code files as solutions to ensure you include all the things that students need to complete the problems. You must not show students solutions. The lesson is titled problem solving. │
│ here is that context:
<system>
You are an expert LaTeX programmer and computer science educator tasked with creating a Beamer presentation on specific sections of a computer science textbook chapter. Your goal is to organize the content into clear, informative slides while adhering to a specific style and structure.

Please follow these instructions carefully:
`</system>`

<preamble_instructions>

1. All output must begin with the following LaTeX preamble exactly as shown (this is required and non-negotiable):

\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../shared/templates/ds9_theme}

% Title page configuration
\title[Short Title]{CS12 CH:`<specified sections>`}
\subtitle{`<appropriate subtitle>`}
\author[Mr. Gullo]{Mr. Gullo}
\date[`<short date>`]{`<full date>`}

</preamble_instructions>

<content_instructions> 2. Read through the provided PDF content and extract the relevant information for the specified sections.

3. Include the following content in your presentation with detailed attention to each component:

   a. **Learning objectives slide** - Present clear, consolidated bullet points outlining what students will understand after the lesson, extracted directly from the specified textbook sections. These should be specific, measurable learning outcomes.

   b. **Key concepts and definitions slides** - Important computer science terms, principles, and conceptual explanations presented in digestible chunks with clear explanations. Break complex concepts into multiple slides if necessary for clarity.

   c. **Essential equations slide** - Critical formulas from the sections with brief explanations of when and how to use them, including clear variable definitions and units.

   d. **Concept visualization slides** - For each abstract computer science concept that would benefit from visual representation, create a two-frame sequence:

   **Context Frame**: Begin with a frame that introduces the concept and explains what will be visualized, setting up the audience's understanding before presenting the visual element.

   **Visualization Frame**: Follow with a dedicated frame containing either:

   - Custom diagrams created using external tools (data structures, algorithms, memory layout, etc.)
   - External images referenced using \alert{[description]} placeholders (photographs, diagrams, real-world examples)

   For custom diagrams, use simple, easily readable visuals with:

   - Large, clear labels and units
   - Appropriate scales and markers
   - Thick lines for visibility during projection
   - Minimal complexity focusing on key conceptual understanding
   - Consistent styling with the DS9 theme colors

   e. **Template code exercises** - Create structured coding exercises with starter template code and commented TODOs for students to complete. Explicitly reference the provided .cpp files for these examples.

   - **Template Setup**: Provide a well-structured starting point with proper includes, main function setup, and variable declarations.
   - **Commented TODOs**: Include clear, numbered TODO comments indicating what students need to implement.
   - **Exercise Context**: Provide the problem statement and expected outcomes clearly.

   f. **Summary slide** - Key takeaways, main concepts review, and connections between ideas presented in the lesson.

4. Use appropriate LaTeX commands for equations, lists, and other formatting elements as needed.
5. For all visual elements including custom diagrams, use placeholders with descriptions in alert boxes like this: \alert{[description of relevant image]} where appropriate to enhance understanding.
   </content_instructions>

<technical_formatting_guidelines>

## LaTeX Formatting Requirements

- Use clear, descriptive frame titles that help with navigation and organization
- Employ proper LaTeX formatting for mathematical equations using appropriate math environments
- Use itemized lists with proper spacing and hierarchy
- **Escape special characters**: Characters like `{`, `}`, `%`, `&`, `_`, `#` have special meaning in LaTeX. To display them as text, you must precede them with a backslash.
  - ✅ Correct: `\{`, `\%`, `\&`
  - ❌ Incorrect: `{`, `%`, `&`
- Ensure consistent formatting throughout the presentation
- Use `\alert{[description of external image]}` for all image and diagram placeholders
- Place each included image in its own dedicated frame with a very short caption (one line maximum) to ensure the image and caption fit properly within the frame boundaries

## **C++ Code Requirements**

- Use `using namespace std;` after includes
- No `std::` prefixes (use `cout`, `cin`, `endl`)
- Consistent namespace pattern in all C++ code blocks

## **CRITICAL: Fragile Frames for Code Blocks**

**When using code highlighting packages like `minted`, `listings`, or `verbatim` environments within Beamer frames, you MUST use the `[fragile]` option:**

- ✅ Correct: `\begin{frame}[fragile]`
- ❌ Incorrect: `\begin{frame}` (will cause "Paragraph ended before \FV@BeginScanning was complete" errors)

**This applies to any frame containing:**

- `\begin{minted}{language}` blocks
- `\begin{lstlisting}` blocks
- `\begin{verbatim}` environments
- Any other verbatim-like content

**Example of proper fragile frame usage:**

```latex
\begin{frame}[fragile]
\frametitle{Code Example}
\begin{minted}[fontsize=\small]{cpp}
int main() {
    return 0;
}
\end{minted}
\end{frame}
```

## Visualization Standards

When creating concept visualization slides, adhere to these technical standards:

- Create simple, easily readable visuals focusing on conceptual understanding rather than complex details
- Use large, clear labels with proper units clearly indicated
- Choose appropriate scales and markers that highlight the important features
- Use thick lines for visibility during classroom projection
- Maintain minimal complexity to avoid overwhelming students with unnecessary details
- Use consistent styling that complements the DS9 theme colors
- Ensure all text in visuals is large enough to be readable from the back of a classroom

## Title and Preamble Formatting Guidelines

### Title Formatting Requirements

- **Short title in brackets**: Must NOT contain ampersands (&) - use "and" instead
  - ✅ Correct: `\title[Graphs and Equations]{...}`
  - ❌ Incorrect: `\title[Graphs & Equations]{...}` (causes compilation error)
- **Subtitle**: Ampersands can be used with proper escaping: `\&`
- **Date formatting**: Use consistent date format matching the example

### Common Preamble Issues to Avoid

- Ampersands in short titles cause "Misplaced alignment tab character" errors
- Color names with underscores cause "I do not know the key" errors
- Missing `[fragile]` option on frames with code blocks causes compilation errors
- Always test compilation after generation
  </technical_formatting_guidelines>

<planning_instructions>
Before generating the final output, wrap your planning process in <presentation_outline> tags:

1. Extract and list key concepts and definitions from each specified section, organizing them logically for presentation flow.
2. Identify and plan specific concept visualization opportunities for each section, determining which abstract computer science concepts would benefit most from visual illustrations. Use external tools for creating clear, simple diagrams.
3. Carefully select and outline template code exercises from the provided PDF content, ensuring they cover different aspects of the content and provide clear starting points for student implementation. Plan how each will include starter code and commented TODOs.
4. Plan your complete presentation structure, including the order of slides and specific content for each frame. Consider the logical flow from learning objectives through concept introduction, visualization, practice, and summary.
5. Include \section{[Content to include in outline]} markers to ensure that the presentation outline has the correct topics and sections properly organized and populated.
6. Plan the integration of visual elements, specifying which concepts will be illustrated and how they will enhance student understanding.

It's perfectly acceptable for this planning section to be quite comprehensive and detailed. The time spent in thorough planning will result in a much more effective and well-organized final presentation.
</planning_instructions>

<output_example>
Example output structure showing proper formatting and organization:

\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Short Title]{CS12 CH:`<specified sections>`}
\subtitle{`<appropriate subtitle>`}
\author[Mr. Gullo]{Mr. Gullo}
\date[`<short date>`]{`<full date>`}

\begin{document}
\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
[Content with clear learning outcomes]
\end{frame}

\begin{frame}[fragile]
\frametitle{Code Example}
\begin{minted}[fontsize=\small]{language}
code content here
\end{minted}
\end{frame}

[Additional content frames following the specified structure]

\begin{frame}[fragile]

\frametitle{Integer Operations Exercise}

\textbf{Exercise File:} \texttt{02_dataTypesIntegers.cpp} (Template with TODOs)

\textbf{Objective:} Complete the TODOs to demonstrate integer operations.\pause

\begin{minted}[fontsize=\scriptsize, frame=lines, linenos, breaklines]{cpp}
#include <iostream>
using namespace std;

int main()
{
int x = 34;
int y = 5;

    // TODO 1: Add x and y, display the result
    // TODO 2: Subtract y from x, display the result
    // TODO 3: Multiply x and y, display the result
    // TODO 4: Divide x by y, display the result
    // TODO 5: Calculate remainder of x divided by y
    // TODO 6: Compare x and y for equality, display result

    return 0;

}
\end{minted}

\end{frame}

\end{document}
</output_example>

<compilation_testing>

## Compilation Testing Guidelines

After generating the LaTeX code, mentally verify these common issues:

### Pre-Compilation Checklist

1. **Title formatting**: Ensure no ampersands (&) in short title brackets
2. **Color names**: Verify all colors use correct names without underscores
3. **Fragile frames**: Ensure all frames with code blocks have `[fragile]` option
4. **Diagram placeholders**: Verify all visual elements use proper alert box syntax
5. **Special Characters**: Verify all special characters like `_`, `%`, `{`, `}` are properly escaped with a backslash `\`.
6. Expected Compilation Process

- First run: `pdflatex filename.tex`
- Common warnings are acceptable (overfull boxes, rerun suggestions)
- Fatal errors must be addressed immediately

### Common Error Patterns to Avoid

- "Misplaced alignment tab character" → Check for & in short titles
- "I do not know the key" → Check color names for underscores
- "Paragraph ended before \FV@BeginScanning was complete" → Add `[fragile]` to frames with code blocks
- "Undefined control sequence" → Verify all LaTeX commands are correct and special characters are escaped.
  </compilation_testing>

<final_instructions>
Please proceed with your comprehensive presentation outline using the <presentation_outline> tags, then generate the complete LaTeX Beamer presentation. You must use an artifact for the final output. Ensure that all requirements from both the content instructions and technical guidelines are met, with particular attention to the template-based exercise integration. The presentation should flow logically from introduction through structured coding exercises, maintaining the educational and professional standards expected for computer science instruction.

When generating the presentation, convert the original content while explicitly referencing the provided .cpp files, including clear template setups and commented TODOs for student implementation.

**IMPORTANT**: Follow all formatting guidelines especially for titles, colors, fragile frames, and special characters to ensure successful compilation.

## **IMPORTANT: Mathematical Operators in LaTeX**

When using comparison operators in LaTeX documents:

1. **Always wrap comparison operators in math mode** using $...$:

   - ✅ Correct: `$<$`, `$>$`, `$\leq$`, `$\geq$`, `$==$`, `$\neq$`, `$\le$`, `$\ge$`
   - ❌ Incorrect: `<`, `>`, `<=`, `>=`, `==`, `!=`, `le`, `ge`

2. **Comparison operators in code blocks don't need math mode** since they're displayed as code:

   - ✅ Correct: `while(x < 500)` (inside minted/listings)
   - ✅ Correct: `$x < 5$` (in regular text)

3. **Use proper LaTeX symbols** for better rendering:
   - Use `$\leq$` instead of `$<=$`
   - Use `$\geq$` instead of `$>=$`
   - Use `$\neq$` instead of `$!=$`
   - Use `$==$` instead of `$==`` in mathematical contexts

</final_instructions>

<file_contents>
File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/Problem Set 1_Solutions.ipynb

```jupyter
{"cells":[{"cell_type":"markdown","id":"bec2e6af","metadata":{},"source":["# Problem Set 1\n"]},{"cell_type":"code","execution_count":1,"id":"67ffed53","metadata":{"trusted":false},"outputs":[],"source":["#include <iostream>\n","\n","using namespace std;"]},{"cell_type":"markdown","id":"8b8e71cb","metadata":{},"source":["## Problem: Basics of while and for loops\n","a. Write a C++ program  that uses a while loop to output the multiples of 7 between 0 and 77 inclusive."]},{"cell_type":"code","execution_count":null,"id":"6d9dafc1","metadata":{"trusted":false},"outputs":[],"source":["#include <iostream>\n","\n","using namespace std;\n","\n","int main(){\n","\n","   // while loop for the multiples of 5 between [0, 50]\n","   int currentValue = 7;\n","   int endValue = 77;\n","\n","   // cout the first value (done so that the commas are correct)\n","   cout << 0;\n","\n","   while(currentValue <= endValue){\n","      cout << \", \" << currentValue;\n","      currentValue += 7;\n","   }\n","\n","   cout << endl;\n","\n","   // for loop to output the sequence 1000, 800, 600, ..., -1000\n","\n","   // cout the first value (done so that the commas are correct)\n","   cout << 1000;\n","\n","   for(int i = 800; i >= -1000; i -= 200)\n","      cout << \", \" << i;\n","\n","   cout << endl;\n","\n","\n","   return 0;\n","}\n"]},{"cell_type":"markdown","id":"1298f592","metadata":{},"source":["Output:0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77,1000, 800, 600, 400, 200, 0, -200, -400, -600, -800, -1000\n"]},{"cell_type":"markdown","id":"f1ae93b6","metadata":{},"source":["b. Write a C++ program that uses a for loop to output the following sequence of numbers: 1000, 800, 600, …, -1000"]},{"cell_type":"code","execution_count":null,"id":"c46e65c6","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"3d1f3d51","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"317b98ed","metadata":{},"source":["## Problem: Division?\n","a. For integers $a \\geq 0$ and $b \\gt 0$, find the result of $a/b$ without using the `/`, `*` or `%` operators."]},{"cell_type":"code","execution_count":null,"id":"6c08a8a5","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"773c039f","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"43dc5af4","metadata":{},"source":["b.  For integers $a \\geq 0$ and $b \\gt 0$, find the result of $a \\% b$ without using the /, * or % operators."]},{"cell_type":"code","execution_count":null,"id":"2f67a428","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"be24a46f","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"c50b6cc4","metadata":{},"source":["## Problem: Largest Prime Factor\n","\n","Write a C++ program that finds the largest prime factor of any positive integer greater than 1. You must use the algorithm described in class where you successively divide by the next smallest factor until only 1 remains."]},{"cell_type":"code","execution_count":null,"id":"29216f04","metadata":{"trusted":false},"outputs":[],"source":["#include <iostream>\n","\n","using namespace std;\n","\n","int main(){\n","   int testNumber, largestPrime;\n","   int currentFactor = 2;\n","\n","   cout << \"Please enter a positive integer greater than 1: \";\n","   cin >> testNumber;\n","\n","   /*\n","      This algorithm works by checking and dividing out factors starting\n","      at 2. For simplicity in the code I don't make any optimizations\n","      in choosing the currentFactor variable. For example I continue to check\n","      even numbers beyond 2.\n","\n","      We know that any number that divides the testNumber is prime because\n","      all smaller factors have been checked and removed. This means we don't need\n","      to check primality.\n","   */\n","\n","   while(testNumber > 1){\n","      if(testNumber % currentFactor == 0){\n","         largestPrime = currentFactor;\n","         testNumber /= currentFactor;\n","      }else{\n","         currentFactor++;\n","      }\n","   }\n","\n","   cout << \"The largest prime factor is: \" << largestPrime << endl;\n","\n","   return 0;\n","}\n"]},{"cell_type":"markdown","id":"c60e15ba","metadata":{},"source":["## Problem: Smallest Multiple\n","\n","The number 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\n","\n","Write a C++ program to determine the smallest positive number that is evenly divisible by all the numbers from 1 to 20."]},{"cell_type":"code","execution_count":null,"id":"58db1fed","metadata":{},"outputs":[],"source":["#include <iostream>\n","#include <cmath>\n","\n","using namespace std;\n","\n","/*\n","   This program calculates f(a, b) = a*10^b + a*10^(b-1) + ... + a\n","   using a loop.\n","*/\n","\n","\n","int main(){\n","   int smallestNumber = 0;\n","\n","   // this is known as a flag. Once it is set to true we know we are done\n","   bool areWeDone = false;\n","\n","   /*\n","      One optimization that I'm going to make is to only check\n","      multiples of the primes less than 20.\n","      We can make improvements to this idea and construct the\n","      answer, but I'll leave that as an exercise.\n","   */\n","   int primeMult = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19;\n","\n","   while(!areWeDone){      // for bool types, this is equivalent to saying areWeDone != true\n","      // assume it is true\n","      areWeDone = true;\n","      smallestNumber += primeMult;\n","\n","      // now check to see if it has all 20 factors\n","      for(int i = 2; i <= 20; i++){\n","         if(smallestNumber % i != 0){\n","            areWeDone = false;\n","            break;      // break statements exit the current loop (the inner for loop)\n","         }\n","      }\n","   }\n","\n","   cout << \"The smallest number divisible by the integers 1..20 is: \" << smallestNumber << endl;\n","\n","\n","   return 0;\n","}\n"]},{"cell_type":"markdown","id":"b6b97ce6","metadata":{},"source":["Output: The smallest number divisible by the integers 1..20 is: 232792560\n"]},{"cell_type":"markdown","id":"d03f0482","metadata":{},"source":["## Problem: Sum of Powers\n","\n","For integers $a \\neq 0$ and $b \\geq 0$, write a code chunk to find the sum $a^b + a^{b-1} + ... + a^1 + a^0$."]},{"cell_type":"code","execution_count":null,"id":"ce95c139","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"2d80c0ea","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"90eb8200","metadata":{},"source":["## Problem: Greatest Common Factor\n","Write a C++ code chunk to find the the greatest common factor of two positive integers a and b. Use your program to find the greatest common factor of 75598 and 278593."]},{"cell_type":"code","execution_count":null,"id":"73c94c1e","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"10638e4c","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"e1a01de0","metadata":{},"source":["## Problem: Square of a Sum\n","\n","For integer $n \\geq 1$, wrtie a code chunk to find the square of the sum of the first $n$ positive integers: $(1 + 2 + ... + n)^2$"]},{"cell_type":"code","execution_count":null,"id":"7e3cdab7","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"f344c203","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"1fc7fdc3","metadata":{},"source":["## Problem: Fibonocci Sequence\n","### Part 1\n","\n","The fibonocci sequence is defined as:  \n","$$\\left\\{\\begin{matrix}\n","f_0 = f_1 = 1\n","\\\\ f_n = f_{n-1} + f_{n-2}\n","\\end{matrix}\\right.$$\n","\n","The first 5 terms are as follows: 1, 1, 2, 3, 5.  \n","\n","Write a code chunk to print the first 10 Fibonocci Numbers."]},{"cell_type":"code","execution_count":null,"id":"288a7c6d","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"2f5e204b","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"08fdac9c","metadata":{},"source":["### Part 2\n","\n","Given two positive integers $0 \\leq a \\leq b$, display the terms of the Fibonocci Sequence as follows.  \n","$$f_a, f_{a+1}, ..., f_b$$ \n","For example, $a = 5$ and $b = 9$ \n","would display:\n","$$8, 13, 21, 34, 55$$"]},{"cell_type":"code","execution_count":null,"id":"28b5bdff","metadata":{"trusted":false},"outputs":[],"source":["#include <iostream>\n","\n","using namespace std;\n","\n","/*\n","   prints the fibonacci numbers from fib_a to fib_b\n","   where a < b\n","*/\n","\n","int main(){\n","   // I'm going to keep track of three terms: n, n-1 and n-2\n","   int fibN = 1;\n","   int fibN_1 = 0;\n","   int fibN_2 = 0;\n","\n","   int a, b;\n","\n","   cout << \"Please enter a and b (where a < b): \";\n","   cin >> a >> b;\n","\n","   // find the ath term (but don't print)\n","   for(int i = 1; i <= a; i++){\n","      // shift the three terms\n","      fibN_2 = fibN_1;\n","      fibN_1 = fibN;\n","      fibN = fibN_1 + fibN_2;\n","   }\n","\n","   // now print from the ath to the bth term\n","\n","   for(int i = a; i <= b; i++){\n","      cout << fibN << \" \";\n","\n","      // shift the three terms\n","      fibN_2 = fibN_1;\n","      fibN_1 = fibN;\n","      fibN = fibN_1 + fibN_2;\n","   }\n","\n","   return 0;\n","}\n"]},{"cell_type":"markdown","id":"ad5bb2b2","metadata":{},"source":["Output:\n","\n","For example, $a = 5$ and $b = 9$ \n","would display:\n","$$8, 13, 21, 34, 55$$"]},{"cell_type":"markdown","id":"d7f3f48f","metadata":{},"source":["### Part 3\n","\n","Repeat the previous exersice for all positive integers $a$ and $b$ where your program displays the Fibonocci numbers from $a$ to $b$.\n","\n","Note: \n","* when $a \\leq b$ your program should display $f_a, f_{a+1}, f_{a+2} ..., f_b$.  \n","* when $a \\gt  b$ your program should display $f_a, f_{a-1}, f_{a-2} ..., f_b$ \n"]},{"cell_type":"code","execution_count":null,"id":"baeb970b","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"9eedd48c","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"650dcbad","metadata":{},"source":["## Problem: Palindromic Numbers\n","\n","### Part 1\n","A palindromic number reads the same both ways. For example 9, 232, and 7007 are all palindromic numbers.\n","\n","Write a code chunk that checks whether any positive integer $m$ is palindromic and outputs the result as follows:\n","* \"Is a palindrome\"\n","* \"Is not a palindrome\""]},{"cell_type":"code","execution_count":null,"id":"7a0d216a","metadata":{"trusted":false},"outputs":[],"source":[]},{"cell_type":"markdown","id":"cd8b5586","metadata":{},"source":["Output:"]},{"cell_type":"markdown","id":"6fe31f9e","metadata":{},"source":["### Part 2\n","\n","Find the largest palindromic number made from the product of two 4-digit numbers.\n"]},{"cell_type":"code","execution_count":null,"id":"7d480802","metadata":{"trusted":false},"outputs":[],"source":["#include <iostream>\n","\n","using namespace std;\n","\n","// finds the largest palindromic number that is a product of\n","// two 3 digit numbers\n","\n","int main(){\n","   int largestPalindrome = 0;\n","   int product, reverseDigits;\n","\n","   // I'm going to use a brute force approach with two nested for loops\n","   // we can make a lot of improvements but I'm going for something easy\n","   // to read\n","\n","   for(int i = 999; i >= 100 ; i--){\n","      for(int j = i; j >= 100; j--){\n","         // the inner loop starts at i, this avoids repeating any products\n","         product = i * j;\n","         reverseDigits = 0;\n","\n","         // we need to reverse the digits without destroying the original\n","         // so we'll make a copy of the product\n","         int temp = product;\n","\n","         while(temp > 0){\n","            reverseDigits = reverseDigits * 10 + temp % 10;\n","            temp /= 10;\n","         }\n","\n","         if(product == reverseDigits && product > largestPalindrome)\n","            largestPalindrome = product;\n","      }\n","   }\n","\n","   cout << \"The largest palindrome is: \" << largestPalindrome << endl;\n","\n","   return 0;\n","}\n"]}],"metadata":{"kernelspec":{"display_name":"C++17","language":"C++17","name":"xcpp17"},"language_info":{"codemirror_mode":"text/x-c++src","file_extension":".cpp","mimetype":"text/x-c++src","name":"c++","version":"17"}},"nbformat":4,"nbformat_minor":5}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/2025_11_05_7ad03b559307df5f5397g/2025_11_05_7ad03b559307df5f5397g.tex

```latex
\documentclass[10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage[version=4]{mhchem}
\usepackage{stmaryrd}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
\graphicspath{ {./images/} }

\begin{document}
\section*{Let's look at problem solving}
\section*{Exercise 5: (From ProjectEuler.net)}
\begin{itemize}
  \item The prime factors of 13195 are 5,7 , 13 and 29.
  \item What is the largest prime factor of the number 600851475143 ?
\end{itemize}

\section*{Exercise 5: (From ProjectEuler.net)}
\begin{itemize}
  \item Let me apply a problem-solving technique to the question
  \item "What is the largest prime factor of the number 600851475143?"
\end{itemize}

\section*{Common errors and optimization}
\begin{verbatim}
int testNum = 600851475143; // ERROR! Too big for regular int
long long testNum = 600851475143; // works too, but wastes the sign bit
unsigned long long testNum = 600851475143;
\end{verbatim}

\begin{verbatim}
int signed_num = 5; // Stored as: 0|000...0101 (sign bit|number)
int negative_num = -5; // Stored as: 1|000...0101 (sign bit|number)
unsigned int unsigned_num = 5; // Stored as: 000...0101 (only bits for number)
\end{verbatim}

\begin{itemize}
  \item Step 1: Explore the Question
  \item Finding the Largest Prime Factor
  \item What's Our Goal?
  \item Find the largest prime factor of \(600,851,475,143\)\\
-But wait... what's a prime factor?
\end{itemize}

\section*{Step 1 (cont.): Understanding Basics}
\begin{itemize}
  \item A prime number only divides by 1 and itself
  \item Example: 2 is prime!
  \item Only divides by 1 and 2
  \item Example: 4 is NOT prime
  \item Divides by 1,2 , and 4
  \item Step 2: Code Something Simple First
  \item Let's Start Small!
  \item Try finding prime factors of 12 first:
  \item Start with smallest prime (2)
  \item Keep dividing until you can't
  \item Move to next number
  \item Repeat!
  \item Step 3: Run With Examples
  \item Breaking Down 12
  \item \(12 \div 2=6 \quad\) Found 2 !
  \item \(6 \div 2=3 \quad\) Found 2 again!
  \item \(3 \div 3=1 \quad\) Found 3 !
  \item So \(12=2 \times 2 \times 3\)
\end{itemize}

\section*{- Step 4: Get Something Working}
-We don't need to check if numbers are prime!\\
-Why? Because we:

\begin{itemize}
  \item Start with smallest numbers
  \item Divide them out immediately
  \item If it divides evenly, it must be prime!
  \item Step 5: Make Optimizations
  \item Use same process for 600,851,475,143
  \item Let computer do the hard work
  \item Keep track of largest prime found
  \item That's our answer!
  \item Step 5 (cont.): The Code\\
largestPrime = current\_n; // Remember biggest prime testNum /= current\_n; // Divide it out
  \item Keep going until testNum \(=1\)
  \item Last prime found is our answer!
\end{itemize}

\section*{- Key Takeaways}
\begin{itemize}
  \item Break big problems into small ones
  \item Test with simple numbers first
  \item Look for shortcuts (like not checking primes)
  \item Let the computer do the heavy lifting!
\end{itemize}

Problem Set Starters:

\section*{Problem 4: Smallest Multiple}
\begin{itemize}
  \item 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\\
-Write a C++ program to determine the smallest positive number that is evenly divisible by all the numbers from 1 to 20 ?
\end{itemize}

\section*{Step 1: Explore the Question}
\begin{itemize}
  \item Can we look at a simplified version of the question?
  \item What if we solve the question by hand for numbers from 1-4?\\
-What patterns do we see?
  \item Can we break the question down into smaller problems and solve each separately?
\end{itemize}

\section*{Step 2: Code something that works on the simplified question.}
\begin{itemize}
  \item This is especially true for questions that involve large numbers\\
-By reducing the complexity we can test our solution as we go
\end{itemize}

\section*{Step 3: Run your code with any given solutions.}
\begin{itemize}
  \item " 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder." is given.
  \item This should be the first program you write and test.
\end{itemize}

\section*{Step 4: Get something working}
\begin{itemize}
  \item Get a solution that works.
  \item Even if it takes awhile to run.
\end{itemize}

\section*{Step 5: Make optimizations}
\begin{itemize}
  \item We need to find numbers that are evenly divisible by numbers from 1 to 20.
  \item This number needs to be a multiple of \(2,3,5\), \(7,11,13,17\) and \(19 \ldots\)
  \item So we only check multiples of
\end{itemize}

\[
2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19
\]

\begin{itemize}
  \item This greatly decreases the number of tests we need to perform
\end{itemize}

\section*{Step 6: Try another approach}
\begin{itemize}
  \item Perhaps you noticed the relationship between the smallest multiple of the numbers from 1 to 20 and their prime factorizations?
  \item We can use this to construct the answer. Further reducing the number of tests we need to do.
\end{itemize}

\section*{How can we apply step 1 to question 7 ?}
\begin{itemize}
  \item The Fibonacci sequence is defined as follows:
  \item \(f_{n}=\left\{\begin{array}{c}f_{0}=f_{1}=1 \\ f_{n}=f_{n-1}+f_{n-2}\end{array}\right.\)
  \item The first 5 terms are as follows: \(1,1,2,3,5, \ldots\)
  \item Write a C++ program that accepts two integers\\
\(0 \leq a \leq 50\) and \(0 \leq b \leq 50\)\\
and then uses a loop to calculate and output the Fibonacci numbers from \(f_{a}\) to \(f_{b}\).
\end{itemize}

\section*{Step 1: Explore the Question}
-Can we look at a simplified version of the question?

\begin{itemize}
  \item Can we break the question down into smaller problems and solve each separately?
\end{itemize}

\section*{How can we apply step 1 to question 8?}
\begin{itemize}
  \item A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is \(9009=91 \times 99\).
  \item Write a C++ program that finds the largest palindrome made from the\\
\includegraphics[max width=\textwidth, center]{2025_11_05_7ad03b559307df5f5397g-23}\\
product of two 3-digit numbers.
\end{itemize}

\section*{Step 1: Explore the Question}
-Can we look at a simplified version of the question?

\begin{itemize}
  \item Can we break the question down into smaller problems and solve each separately?
\end{itemize}

\end{document}
```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/09_fibonocci_more.cpp

```cpp
#include <iostream>

using namespace std;

// displays the list of fibonocci numbers from fib_a to fib_b

int main(){
   // I'm going to keep track of three terms: n, n-1 and n-2
   // the current term is fib0
   int fibN = 1;
   int fibN_1 = 0;
   int fibN_2 = 0;

   int a, b;

   cout << "Please enter the integers a and b: ";
   cin >> a >> b;

   // find the ath term (but don't print)
   for(int i = 1; i <= a; i++){
      // shift the three terms
      fibN_2 = fibN_1;
      fibN_1 = fibN;
      fibN = fibN_1 + fibN_2;
   }

   if(a <= b){
      // count up from a to b. No change from question 8
      for(int i = a; i <= b; i++){
         cout << fibN << " ";

         // shift the three terms up
         fibN_2 = fibN_1;
         fibN_1 = fibN;
         fibN = fibN_1 + fibN_2;
      }
   }else{
      // count down from a back to b. The opposite from question 8
      for(int i = a; i >= b; i--){
         cout << fibN << " ";

         // shift the three terms down
         fibN = fibN_1;
         fibN_1 = fibN_2;
         fibN_2 = fibN - fibN_1;
      }
   }

   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/06_smallestMultiple.cpp

```cpp
#include <iostream>
#include <cmath>

using namespace std;

/*
   This program calculates f(a, b) = a*10^b + a*10^(b-1) + ... + a
   using a loop.
*/


int main(){
   int smallestNumber = 0;

   // this is known as a flag. Once it is set to true we know we are done
   bool areWeDone = false;

   /*
      One optimization that I'm going to make is to only check
      multiples of the primes less than 20.
      We can make improvements to this idea and construct the
      answer, but I'll leave that as an exercise.
   */
   int primeMult = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19;

   while(!areWeDone){      // for bool types, this is equivalent to saying areWeDone != true
      // assume it is true
      areWeDone = true;
      smallestNumber += primeMult;

      // now check to see if it has all 20 factors
      for(int i = 2; i <= 20; i++){
         if(smallestNumber % i != 0){
            areWeDone = false;
            break;      // break statements exit the current loop (the inner for loop)
         }
      }
   }

   cout << "The smallest number divisible by the integers 1..20 is: " << smallestNumber << endl;


   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/08_fibonocci.cpp

```cpp
#include <iostream>

using namespace std;

/*
   prints the fibonacci numbers from fib_a to fib_b
   where a < b
*/

int main(){
   // I'm going to keep track of three terms: n, n-1 and n-2
   int fibN = 1;
   int fibN_1 = 0;
   int fibN_2 = 0;

   int a, b;

   cout << "Please enter a and b (where a < b): ";
   cin >> a >> b;

   // find the ath term (but don't print)
   for(int i = 1; i <= a; i++){
      // shift the three terms
      fibN_2 = fibN_1;
      fibN_1 = fibN;
      fibN = fibN_1 + fibN_2;
   }

   // now print from the ath to the bth term

   for(int i = a; i <= b; i++){
      cout << fibN << " ";

      // shift the three terms
      fibN_2 = fibN_1;
      fibN_1 = fibN;
      fibN = fibN_1 + fibN_2;
   }

   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/10_palindromeProduct.cpp

```cpp
#include <iostream>

using namespace std;

// finds the largest palindromic number that is a product of
// two 3 digit numbers

int main(){
   int largestPalindrome = 0;
   int product, reverseDigits;

   // I'm going to use a brute force approach with two nested for loops
   // we can make a lot of improvements but I'm going for something easy
   // to read

   for(int i = 999; i >= 100 ; i--){
      for(int j = i; j >= 100; j--){
         // the inner loop starts at i, this avoids repeating any products
         product = i * j;
         reverseDigits = 0;

         // we need to reverse the digits without destroying the original
         // so we'll make a copy of the product
         int temp = product;

         while(temp > 0){
            reverseDigits = reverseDigits * 10 + temp % 10;
            temp /= 10;
         }

         if(product == reverseDigits && product > largestPalindrome)
            largestPalindrome = product;
      }
   }

   cout << "The largest palindrome is: " << largestPalindrome << endl;

   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/07_sumSquareDifference.cpp

```cpp
#include <iostream>

using namespace std;

/*
   This program calculates f(a, b) = a*10^b + a*10^(b-1) + ... + a
   using a loop.
*/


int main(){
   const int MAX_N = 100;

   int sumOfSquares = 0;
   int squareOfSums = 0;

   // find the sum of squares

   for(int i = 1; i <= MAX_N; i++)
      sumOfSquares += i * i;


   // find the square of sums

   for(int i = 1; i <= MAX_N; i++)
      squareOfSums += i;

   squareOfSums *= squareOfSums;

   // output the difference

   cout << "For n = " << MAX_N
        << " the difference between the square of sum ("
        << squareOfSums << ") and the sum of squares ("
        << sumOfSquares << ") is "
        << squareOfSums - sumOfSquares << endl;

   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/04_largestPrimeFactor.cpp

```cpp
#include <iostream>

using namespace std;

int main(){
   int testNumber, largestPrime;
   int currentFactor = 2;

   cout << "Please enter a positive integer greater than 1: ";
   cin >> testNumber;

   /*
      This algorithm works by checking and dividing out factors starting
      at 2. For simplicity in the code I don't make any optimizations
      in choosing the currentFactor variable. For example I continue to check
      even numbers beyond 2.

      We know that any number that divides the testNumber is prime because
      all smaller factors have been checked and removed. This means we don't need
      to check primality.
   */

   while(testNumber > 1){
      if(testNumber % currentFactor == 0){
         largestPrime = currentFactor;
         testNumber /= currentFactor;
      }else{
         currentFactor++;
      }
   }

   cout << "The largest prime factor is: " << largestPrime << endl;

   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/04_unsignedLongLong.cpp

```cpp
#include <iostream>

using namespace std;

int main(){

   unsigned int i = 0;
   unsigned long ul = 0;
   unsigned long long ull = 0;

   cout << "unsigned int:\n";
   cout << "\tSize:    " << sizeof(int) << '\n';
   cout << "\tLargest: " << i - 1 << '\n';

   // note: since there are no negative numbers (unsigned) subtracting
   //       one from zero will tell us the largest value

   cout << "unsigned long:\n";
   cout << "\tSize:    " << sizeof(long int) << '\n';
   cout << "\tLargest: " << ul - 1 << '\n';

   cout << "unsigned long long:\n";
   cout << "\tSize:    " << sizeof(unsigned long long) << '\n';
   cout << "\tLargest: " << ull - 1 << '\n';

   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/03_basics.cpp

```cpp
#include <iostream>

using namespace std;

int main(){

   // while loop for the multiples of 5 between [0, 50]
   int currentValue = 7;
   int endValue = 77;

   // cout the first value (done so that the commas are correct)
   cout << 0;

   while(currentValue <= endValue){
      cout << ", " << currentValue;
      currentValue += 7;
   }

   cout << endl;

   // for loop to output the sequence 1000, 800, 600, ..., -1000

   // cout the first value (done so that the commas are correct)
   cout << 1000;

   for(int i = 800; i >= -1000; i -= 200)
      cout << ", " << i;

   cout << endl;


   return 0;
}

```

File: /Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/10_problemSet/solutions/05_shiftingASum.cpp

```cpp
#include <iostream>
#include <cmath>

using namespace std;

/*
   This program calculates f(a, b) = a*10^b + a*10^(b-1) + ... + a
   using a loop.
*/


int main(){
   int a, b;
   int currentPlace = 1;
   int sum = 0;


   cout << "Please enter a and b: ";
   cin >> a >> b;

   for(int i = 0; i <= b; i++)
      sum += a * pow(10, i);

   cout << "The shifted sum is: " << sum << endl;

   return 0;
}

```

</file_contents>
