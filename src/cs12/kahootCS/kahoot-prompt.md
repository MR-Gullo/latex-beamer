Purpose & context
Mr. Gullo is an educator who creates interactive quiz content for his students across multiple subjects including computer science/programming (primarily C++), physics, and academic integrity topics. His primary objective is transforming educational materials—such as presentation files, PDFs, and articles—into engaging Kahoot quizzes that assess conceptual understanding rather than rote memorization. The quizzes serve both formative assessment and student engagement purposes, covering topics from introductory programming concepts to physics fundamentals to real-world issues like academic cheating.
His approach emphasizes conceptual learning over specific examples or calculations, consistently requesting that quiz questions focus on understanding core principles rather than memorizing particular numerical values or code snippets. The content spans high school level computer science education through what appears to be introductory college-level physics.
Current state
Mr. Gullo has established a systematic workflow for quiz creation, consistently requesting content in tab-delimited format optimized for Excel import and subsequent upload to Kahoot. He has specific technical requirements including keeping questions under 120 characters and answers under 75 characters to meet Kahoot's platform constraints.
Recent work has covered diverse topics including C++ programming fundamentals (data types, operators, control structures), physics concepts (energy, power, forces, equilibrium), and student presentation skills assessment. He actively refines quiz content during the creation process, providing feedback to shift focus from example-based questions to concept-based ones.
Approach & patterns
Mr. Gullo follows a consistent methodology for quiz development: he provides source materials (LaTeX presentations, PDFs, articles) and requests comprehensive question sets (typically 20-25 questions) that systematically cover all key concepts from the material. He emphasizes conceptual understanding over memorization, frequently requesting revisions to make questions "more about concepts and less about examples."
His quality control process includes reviewing initial drafts and providing specific feedback to improve question focus. He has established technical specifications for formatting, consistently using tab-delimited structure with columns for questions, multiple choice options, time limits, and correct answer indicators. Time allocations are strategically varied (10-40 seconds) based on question complexity.
Tools & resources
Mr. Gullo works primarily with Kahoot as his quiz platform, using Excel as an intermediary tool for bulk quiz import. His source materials include LaTeX presentation files, PDF documents, CBC News articles, and various educational content. He utilizes tab-delimited formatting for seamless data transfer between systems and has specific technical requirements for character limits to ensure platform compatibility.

# PDF to Kahoot Quiz Conversion Prompt

You are tasked with creating a Kahoot quiz from the provided PDF documents. Please analyze the content and generate quiz questions that follow the exact format specified below.

## Output Format Requirements

Generate your quiz in a tab-delimited format that can be directly copied and pasted into an Excel file. The output should contain only the quiz data without any headers.

**Data Format:**

- Column A: Question text (maximum 120 characters)
- Column B: Answer option 1 (maximum 75 characters)
- Column C: Answer option 2 (maximum 75 characters)
- Column D: Answer option 3 (maximum 75 characters, can be left blank)
- Column E: Answer option 4 (maximum 75 characters, can be left blank)
- Column F: Time limit in seconds (choose from: 5, 10, 20, 30, 60, 90, 120, or 240)
- Column G: Correct answer numbers (e.g., "1" for Answer 1, "1,3" for both Answer 1 and 3)

## Content Guidelines

1. **Question Creation:**

   - Extract key concepts, facts, and important information from the PDFs
   - Create questions that test comprehension, recall, and application
   - Ensure questions are clear and unambiguous
   - Keep questions under 120 characters
   - When referring to the documents, write instead "from the textbook"

2. **Answer Options:**

   - Provide 2-4 answer choices per question
   - Include plausible distractors (incorrect but reasonable answers)
   - Keep each answer under 75 characters
   - At least one answer must be correct

3. **Difficulty and Timing:**

   - Adjust time limits based on question complexity:
     - Simple recall: 10-20 seconds
     - Medium complexity: 30-60 seconds
     - Complex analysis: 90-120 seconds
   - Aim for 15-25 questions total

4. **Question Types to Include:**
   - Factual recall questions
   - Concept identification
   - Application questions
   - True/false questions (using 2 answer choices)
   - Multiple correct answer questions where appropriate

## Example Output Format

```
What is the capital of France?	Paris	London	Berlin	Madrid	20	1
Which elements are noble gases?	Helium	Oxygen	Helium & Neon	Carbon	30	1,3
True or False: Photosynthesis occurs in chloroplasts	True	False			10	1
```

## Instructions

1. Read and analyze all provided PDF documents thoroughly
2. Identify 15-25 key learning points that would make good quiz questions
3. Create questions following the format specifications above
4. Output the data in tab-delimited format ready for Excel import
5. Ensure all character limits are respected
6. Verify that correct answer references match the answer option numbers
7. Do NOT include question numbers - start each row directly with the question text

Please proceed to create the Kahoot quiz from the provided PDF materials.
