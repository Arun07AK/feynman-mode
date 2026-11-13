# The thread prompts

Each topic's prompt is two parts: a short scope block, then the teaching template word for word.

## Why it is built this way

The template carries the teaching method. The scope block adds only what the tutor cannot know: what to teach, where to start and when to stop. An earlier version of this harness used a long, detailed brief per topic with method rules, examples and traps, and the threads it produced were poor. The short version taught far better. Treat every extra line as a cost.

## The scope block

```
I want you to teach me <topic> from scratch.

WHAT TO TEACH (topic <n> of my <course>)
1. … 4 to 8 numbered concepts, each with the exam's own form of any formula
Notation: … (only where my course differs from the textbook)
Leave out: …

WHERE TO START
I already know …. Do not re-teach these. Begin at concept 1 and take the concepts in order.

WHEN THE TOPIC IS DONE
It is done when I can do these N things without help:
1. … 2 to 4 things the exam asks me to do
Check each with one fresh problem that I solve myself. When I have done all N, tell me plainly that topic <n> is complete, and stop.
```

For a subject where "one fresh problem" does not fit (recall, design, essays), change the check to the form the subject analysis chose, such as "one fresh question that I answer from memory". Keep the three headings and the closing instruction.

## Rules for the block

- Write it from the curriculum work: the concepts the course teaches, at the depth the exam needs; the course's terminology, notation and the exam's form of each formula; the prerequisites the learner already has; and a "done" list taken from what past papers actually ask.
- Size the block to the topic. A simple topic gets few concepts and is taught quickly; a hard one may need more. Never split a simple idea to fill the list.
- The thread must stand alone. It teaches from scratch without assuming the learner watched a lecture or read the slides, and it knows where its scope ends.
- No teaching method, examples, exam text, traps or source names in the block. The template carries the method.
- Keep the block under about 1,900 characters.
- Add a line only when a real thread went wrong without it. A course convention the tutor gets wrong goes in `Notation` or one concept line.

## The teaching template

Append `assets/teaching-template.txt` exactly as it is. Do not paraphrase, reorder or extend it. It was written by Arun AK and is the version that was tested in real threads.

If the learner has their own teaching template, use theirs instead, also word for word.

## Pilot before rollout

**Run one topic in a real thread and get the learner's verdict before writing the rest.** A prompt that passes every checker can still teach badly. Pick a hard topic for the pilot. If the thread teaches badly, find the cause in the scope, the split or the order before touching the template.

## Launching

- The learner learns in the real chat product, not a chat built into the site. "Learn in ChatGPT" (or the learner's tutor) is the first action on every topic and opens the conversation in one click with the prompt already sent.
  - ChatGPT: `https://chatgpt.com/?q=<url-encoded prompt>`
  - Claude: `https://claude.ai/new?q=<url-encoded prompt>`
- Keep the whole URL under 16,000 characters.
- Every prompt is standalone. Do not rely on a project, custom instructions or memory in the chat product.
- Let the learner save the thread's link, reopen it and mark the topic learnt. Do not invent APIs or assume the site can read a conversation.
- Check that the one-click launch works today. If it does not, use the most frictionless supported alternative, such as copying the prompt and opening the chat.

## Building and checking

Build prompts with one small function that reads the curriculum data, so the template is stored once. Write each built prompt to a text file and run:

```
python3 scripts/check_prompts.py <folder of .txt prompts>
```

It checks the three headings, the block's size, the concept and done counts, that the template is present word for word, and the launch URL length.
