---
name: feynman-mode
description: Build a complete learning harness for any subject, course or exam. The harness works out how this particular subject should be learned, writes one self-contained tutor prompt per topic (each opens a ChatGPT or Claude conversation that teaches the topic from scratch, intuition before formulas), pairs every topic with a well-taught human lecture, and builds a small website holding the roadmap, practice on real past papers, and progress. Use when someone wants to learn or revise a whole subject, prepare for an exam from a syllabus, slides or past papers, or asks for a study system, learning path or course site built around AI tutoring.
---

# Feynman Mode

A learning harness has three parts, and each has one job.

- **Tutor threads teach.** One real chat conversation per topic (ChatGPT by default), able to teach the topic completely on its own.
- **The website coordinates.** It holds what to learn, in what order and why, launches each thread, and keeps the roadmap, practice, revision and progress. It does not teach.
- **A human lecture beside every topic** gives a second way in. A thread never depends on it.

Why this shape: static lesson pages handle easy ideas, but hard ideas come out oversimplified, abstract or overwhelming, and the learner ends up in a chat or a lecture anyway. A conversation can go one small step at a time, wait, and re-explain. So the effort goes into preparing excellent conversations, not into writing lessons.

The aim is real intuition, mastery, retention and exam readiness. It is not cramming, slide summaries, or pages that look good and teach little.

## The one rule that makes this work

**Analyse the subject before designing anything, and let the design follow from the analysis.** Two subjects should come out with visibly different harnesses. Never reuse the topic sizes, practice format or page layout of a previous subject because they worked there.

## Workflow

Work through these steps in order. Read each reference file when you reach its step, not before.

1. **Intake.** Ask only what you cannot find in the learner's material:
   - the subject, and the exam or goal with its date and scope;
   - where their material is (syllabus, slides, notes, past papers);
   - what they have already studied;
   - courses they own, teachers they have liked, and sources to avoid;
   - which tutor they use (ChatGPT unless they say otherwise) and where to build.
   The learner provides the sources. If something needs their login, ask them to sign in. Do not download course material yourself or substitute a stand-in.
2. **Analyse the subject.** Read `references/subject-analysis.md`. Give the learner a one-page learning design and wait for their go.
3. **Build the curriculum and scope.** Read `references/curriculum.md`.
4. **Write the thread prompts.** Read `references/thread-prompts.md`. This is the most important step, so put most of your effort here. Pilot one topic in a real thread and get the learner's verdict before writing the rest.
5. **Find the lectures.** Read `references/lectures.md`. Skip only if the learner said at intake that they do not want lectures.
6. **Set priorities and practice from past papers.** Read `references/practice.md`.
7. **Build the website.** Read `references/website.md`.
8. **Check and report.** Read `references/checking.md`.

## How to work

- Act as an autonomous research and build agent. The learner should not have to manage the architecture, tools or method. Educational quality comes before speed.
- Plan first and wait for the learner's go. Then build in phases they can review, module by module in study order, each one finished and checked before the next.
- Pilot before rollout for every new kind of thing: one topic, used by the learner, judged, then the rest.
- Keep it technically simple: static files, no infrastructure the job does not need. Curriculum accuracy, the thread prompts and the lecture mapping matter more than front-end engineering.
- Keep prompts and pages short. Before adding a rule, a safeguard or a feature, ask whether the result is bad without it.
- Track every deck, topic, prompt, lecture mapping and page as its own line in a `TASKS.md`, updated as each is finished and checked. That file is the record of progress, not the conversation.
- When the learner states a preference, write it into the project's instructions file the first time, so they never have to say it twice.

## What stays out unless the learner asks

- **Pages that teach.** Static lessons and essays duplicate the thread. If the learner asks for something beside the thread, it should be visual, connect what the thread taught without re-explaining it, and be piloted on one topic first.
- **Invented exam questions.** Practice uses real past questions only.
- **Planners.** No schedule generator, recommender or "today's plan". The learner follows a plain index.
- **Made videos.** If asked for, the effort goes into the script before rendering.

## Done means

A complete, reliable system that takes the learner from scratch to strong understanding of everything in scope, mainly through tutor threads, with a researched lecture beside every topic: no missing syllabus content, no avoidable friction, and no preference the learner had to state twice.
