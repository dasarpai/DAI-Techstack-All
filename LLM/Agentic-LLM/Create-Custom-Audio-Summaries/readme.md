
This experiment/exploration is based on https://www.youtube.com/watch?v=6_VE58sj2Z8 (How to Create Custom Audio Summaries of ANYTHING (That Sound Exactly Like You))

## Prompt used

Prompt:

Instruction:
You will receive a set of notes as input. Please read them carefully and create a concise summary in Markdown using the following structure:
1. Start with a heading in H2 format (using ##) that clearly states the main topic.
2. Create a section titled “Summary” in an H3 heading (using ###). Summarize the entire note in up to five sentences.
3. Create a section titled “Details” in an H3 heading (using ###). Below it, list the topics discussed in the meeting as top-level bullet points (using *). Within each bullet, briefly mention who said or proposed what about that topic in up to two sentences.
Important Requirements:
Do not nest any bullets.
Use * (asterisk) for bullet points, not a hyphen.
Focus each bullet on the topic rather than the speaker, but include a short mention of who spoke about it.
Keep the language concise and clear.
Example Output Structure (replace the placeholders with actual content):
[Title of the Meeting Notes]
Summary
Write up to five sentences that briefly describe the overall context and key takeaways.
Details
[Topic]: Mention who brought it up or contributed to it, in up to two sentences.
