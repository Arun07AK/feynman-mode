# Feynman Mode

A skill for Claude Code that builds a complete learning harness for any subject: one AI tutor conversation per topic, a well-taught human lecture beside each, practice on real past papers, and a small website that holds it all together.

## The idea

Lesson pages written in advance work for easy ideas. Hard ideas come out oversimplified or overwhelming, and you end up asking a chatbot anyway. So this skill prepares the conversations instead of writing lessons:

- **A tutor thread per topic.** One click opens ChatGPT (or Claude) with a prompt that teaches the topic from scratch, one small step at a time, intuition before formulas, and stops when you can do what the exam asks.
- **A lecture per topic.** Chosen for how well it teaches the hardest idea, and you pick from two or three samples.
- **A website that coordinates.** Roadmap, priorities from past papers, practice on real questions, progress. It does not teach.

The skill analyses each subject before designing anything. A calculation-heavy course and a theory-heavy course come out with different topic splits, different definitions of "done" and different practice.

## Install

Clone into your skills folder:

```bash
git clone https://github.com/<your-username>/feynman-mode ~/.claude/skills/feynman-mode
```

Then, in Claude Code, open the folder with your course material and say:

```
Build a learning harness for <subject>. My syllabus, slides and past papers are in this folder.
```

## What you need

- Your own material: syllabus, slides or notes, and past papers if you have them. The skill does not download course material for you.
- A ChatGPT or Claude account for the tutor threads.
- A few decisions along the way: approving the learning design, judging one pilot thread, and choosing lectures from samples.

## What is inside

| File | Purpose |
|---|---|
| `SKILL.md` | The workflow and the working rules |
| `references/subject-analysis.md` | How the subject is analysed before anything is designed |
| `references/curriculum.md` | Building the curriculum and its scope |
| `references/thread-prompts.md` | The tutor prompt pattern and how threads are launched |
| `references/lectures.md` | How lectures are judged and mapped |
| `references/practice.md` | Past-paper priorities, practice and mocks |
| `references/website.md` | Interface principles |
| `references/checking.md` | Final checks and the report |
| `assets/teaching-template.txt` | The teaching template every thread uses |
| `scripts/check_prompts.py` | Checks built prompts |

## Credit

The teaching template and the method were written and tested by Arun AK while preparing for a university machine learning exam. The template is used word for word.

## Licence

MIT. See `LICENSE`.
