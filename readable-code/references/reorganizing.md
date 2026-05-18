# Reorganizing Your Code

Reference for chapters 10–13 of *The Art of Readable Code*. Bigger moves than naming and expression-level tweaks: where code lives, how it's split, and whether it should exist at all.

---

## Extracting Unrelated Subproblems (Ch. 10)

Engineering is decomposition. Apply the principle to code: separate the **high-level goal** from the **subproblems** it happens to need.

### The process

For any block of code:

1. **Ask: what is the high-level goal of this code?**
2. **For each line, ask: is this directly serving the goal, or is it solving an unrelated subproblem?**
3. **If enough lines are solving an unrelated subproblem, extract them.**

The key property of the extracted function: it should be *oblivious to why it's being called*. It solves a standalone problem.

### Example

```
// Goal: find the location closest to a given point.
var findClosestLocation = function(lat, lng, array) {
    var closest;
    var closest_dist = Number.MAX_VALUE;
    for (var i = 0; i < array.length; i++) {
        // unrelated subproblem: spherical distance
        var lat_rad = radians(lat);
        var lng_rad = radians(lng);
        var lat2_rad = radians(array[i].latitude);
        var lng2_rad = radians(array[i].longitude);
        var dist = Math.acos(Math.sin(lat_rad) * Math.sin(lat2_rad) +
                             Math.cos(lat_rad) * Math.cos(lat2_rad) *
                             Math.cos(lng2_rad - lng_rad));
        if (dist < closest_dist) {
            closest = array[i];
            closest_dist = dist;
        }
    }
    return closest;
};
```

Extract the spherical-distance subproblem:

```
var sphericalDistance = function(lat1, lng1, lat2, lng2) { ... };

var findClosestLocation = function(lat, lng, array) {
    var closest;
    var closest_dist = Number.MAX_VALUE;
    for (var i = 0; i < array.length; i++) {
        var dist = sphericalDistance(lat, lng, array[i].latitude, array[i].longitude);
        if (dist < closest_dist) {
            closest = array[i];
            closest_dist = dist;
        }
    }
    return closest;
};
```

The outer function now reads as its high-level intent. `sphericalDistance` is reusable, testable in isolation, and the reader can decide whether to descend into it.

### Variants of "unrelated subproblem"

**Pure utility code.** String formatting, date math, math helpers. If your codebase doesn't have a `format_dollars()` or `seconds_to_human()`, add one when you need it.

**Simplifying an existing interface.** Wrap an awkward library API in a thin function that fits how your code wants to use it:

```
def get_cookie(name):
    return urllib.unquote(re.search(rf'{name}=([^;]+)', request.cookies).group(1))
```

Now no one in your codebase repeats that regex and unquote.

**Reshaping data to your needs.** If callers always have to transform the result of a function, push the transform into a wrapper.

**Spotting missing primitives.** When you see the same 3-line pattern five times across the codebase, name it. The codebase grows a vocabulary.

### Warning: don't over-extract

A helper used in exactly one place, never reused, can hurt: the reader has to navigate to a separate function to follow the code. Extract when:

- the subproblem can be named cleanly,
- the extracted function is genuinely independent of the caller's context,
- *or* it's reused at least twice.

Otherwise inline can be clearer.

---

## One Task at a Time (Ch. 11)

Code that does multiple tasks at once is harder to follow. Defragment so each block does **one task at a time** in sequence.

### The process

1. **List the tasks** the code is doing. "Validate input." "Compute X." "Format output." Be loose — a task can be small ("make sure this object is valid") or vague ("iterate every node").
2. **Separate the tasks** — into different functions, or at least into clearly delimited sections within one function.

This is broader than "functions should do one thing." Even within a single function, *sequencing tasks linearly* beats interleaving them.

### Example: vote-changing logic

A blog comment can be voted Up, Down, or unvoted. A vote change updates a score. The interwoven version:

```
function vote_changed(old_vote, new_vote) {
    var score = get_score();
    if (new_vote !== old_vote) {
        if (new_vote === 'Up') {
            score += (old_vote === 'Down' ? 2 : 1);
        } else if (new_vote === 'Down') {
            score -= (old_vote === 'Up' ? 2 : 1);
        } else if (new_vote === '') {
            score += (old_vote === 'Up' ? -1 : 1);
        }
    }
    set_score(score);
}
```

The tasks are entangled. Split them: (1) convert each vote to a numeric delta, (2) compute the change, (3) apply.

```
function vote_value(vote) {
    if (vote === 'Up')   return  1;
    if (vote === 'Down') return -1;
    return 0;
}

function vote_changed(old_vote, new_vote) {
    var delta = vote_value(new_vote) - vote_value(old_vote);
    set_score(get_score() + delta);
}
```

Same behavior, half the code, *one task at a time*.

### Tasks can be tiny

Even pulling out `vote_value` — itself a one-liner per case — flips the function from "tangled" to "obvious." Don't dismiss small task-splits.

---

## Turning Thoughts into Code: The Rubber-Duck Method (Ch. 12)

> You do not really understand something unless you can explain it to your grandmother. — Einstein

Source code is your primary medium for explaining what the program does. Write it the way you'd explain it.

### The three-step process

1. **Describe what the code needs to do in plain English** — like talking to a colleague.
2. **Notice the key words and phrases** in your description.
3. **Write code that matches the description.**

### Example

PHP authorization logic, hard-to-follow:

```
$is_admin = is_admin_request();
if ($document) {
    if (!$is_admin && ($document['username'] != $_SESSION['username'])) {
        return not_authorized();
    }
} else {
    if (!$is_admin) {
        return not_authorized();
    }
}
// render page
```

Describe it in English:

> There are two ways you can be authorized: (1) you are an admin, or (2) you own the current document (if there is one). Otherwise, not authorized.

Rewrite to match:

```
if (is_admin_request()) {
    // authorized
} elseif ($document && $document['username'] == $_SESSION['username']) {
    // authorized
} else {
    return not_authorized();
}
// render page
```

The new version maps line-for-line to the English. Three negations gone.

### Use it for debugging too

"Rubber-duck debugging" works because explaining the bug aloud forces you to be precise. The answer usually emerges from the explanation. If you can't describe the bug clearly, you don't understand it — fix that first.

### Use it for whole problems

Boswell's bigger example: a stock-purchase analysis problem. Describing it in plain English exposed it as a Unix-toolkit job (`sort`, `join`, `awk`) — no program needed. Plain-English description regularly reveals that you don't need to write code at all, which leads to…

---

## Writing Less Code (Ch. 13)

> The most readable code is no code at all.

Every line costs forever: testing, maintenance, screen real estate, cognitive load on every reader. Default to writing less.

### Question requirements

Programmers overestimate which features matter. A surprising fraction of "requirements" can be:

- Cut entirely (no user wanted it).
- Deferred (no one needs it now; build when there's evidence).
- Simplified (a 10x cheaper version covers 90% of the case).

Before implementing: ask *who* needs this, *how often*, and *what breaks if we don't ship it?* The answer often kills the feature.

### Stay small

Periodically prune:

- Dead code (unreferenced).
- Unused features (no real users).
- Over-general code (parameterized for cases that never happened).
- Fields nobody reads.

Apply the boy-scout rule: every PR can leave the codebase slightly smaller.

### Know your standard library

Most "code I need to write" already exists. Spend 15 minutes a quarter browsing your language's stdlib + the top frameworks in use. The ROI is enormous because:

- You stop reinventing slower, buggier versions.
- You recognize patterns when reading others' code.
- You write less code.

Concrete habit: when about to write a 10+ line helper, search the stdlib first.

### Reuse over reinvent

Beyond the stdlib: small Unix tools, scripting languages, shell pipelines, existing libraries, even GitHub Gists. A `sort | uniq -c | sort -rn` pipeline is shorter, faster, and more correct than a custom Python script.

The decision tree:
1. Can I delete the requirement? → delete.
2. Is there a stdlib/library that does it? → use it.
3. Can I do it with existing scripts/tools? → use them.
4. Only then: write code.

### When you do write code, write less of it

- Fewer functions.
- Fewer abstractions until two real users justify them.
- Fewer config options. (Each is a permutation to test and a question for the reader.)
- Smaller functions, smaller classes, fewer files.

Every line is a liability. Code is the cost; behavior is the value. Optimize the ratio.
