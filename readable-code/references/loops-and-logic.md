# Simplifying Loops and Logic

Reference for chapters 7–9 of *The Art of Readable Code*. Once names and layout are clean, the next readability bottleneck is mental simulation — tracing branches, evaluating expressions, tracking variable state.

---

## Control Flow That Reads Naturally (Ch. 7)

Every branch and loop should be written so the reader doesn't pause.

### Argument order in comparisons

Put the value **being interrogated** on the left, the **stable** value on the right.

```
if (length >= 10)              // ✓ natural
if (10 <= length)              // ✗ Yoda-ish

while (bytes_received < bytes_expected)   // ✓
while (bytes_expected > bytes_received)   // ✗
```

This mirrors English: *"if you make at least $100k/year"*, not *"if 100k/year is less than your salary"*.

### Order of if/else blocks

When you have a choice, prefer:

1. **Positive case before negative.** `if (debug)` before `if (!debug)`.
2. **The simpler/interesting case first.** Get the reader oriented before tackling complexity.
3. **The "do something" branch before the bail-out.**

(These often conflict — use judgment, but bias toward whichever puts the *meaningful* code at the top.)

### Return early

Guard clauses up top, real logic below. This is more readable than nesting the entire function inside an `if`.

```
def render(user):
    if not user:
        return None
    if user.is_banned:
        return BANNED_PAGE
    if not user.has_paid:
        return PAYWALL
    return render_full_profile(user)
```

The reader handles each exit independently, then reads the happy path linearly.

### Minimize nesting

Every level of indentation is a frame the reader must hold. Three levels deep is already painful; four is a smell.

**Common cause of unnecessary nesting:** stacking `if` branches when an early return would do.

```
// nested
if (user_result == SUCCESS) {
    if (permission_result != SUCCESS) {
        log("error reading permissions");
        return;
    }
    log("done");
} else {
    log("error reading user");
}

// flat — return early
if (user_result != SUCCESS) {
    log("error reading user");
    return;
}
if (permission_result != SUCCESS) {
    log("error reading permissions");
    return;
}
log("done");
```

The flat version reads top-to-bottom, no mental stack.

### Loops: same idea

`continue` inside a loop is the loop's "return early." Use it to skip uninteresting iterations and keep the body shallow.

### `do/while`, `goto`, deeply nested ternaries

- `do/while` is awkward because the condition reads *after* the body. Almost always rewriteable as `while` with a flag set in the body, or refactored entirely. Avoid.
- `goto` survives only in narrow cases (single-exit cleanup in C). Otherwise: never.
- Ternaries (`?:`) are fine for trivial cases:
  ```
  time_str += hour >= 12 ? "pm" : "am"
  ```
  But avoid nested or compound ternaries:
  ```
  return exponent >= 0 ? mantissa * (1 << exponent) : mantissa / (1 << -exponent);   // hard
  ```
  Use `if/else` when the choice or the expressions get complex.

### Hidden control flow

Some constructs change flow invisibly — the reader has to *know* something to follow execution:

- **Threads** — execution may be elsewhere.
- **Callbacks / async** — when does this run?
- **Virtual / overridden methods** — which implementation?
- **Exceptions** — every function call is a potential exit.
- **Operator overloading** — `a + b` might do anything.

Don't ban these — they have their place. But each one taxes the reader. Use them when the payoff is worth it; don't sprinkle them for elegance.

---

## Breaking Down Giant Expressions (Ch. 8)

Cognitive science: working memory holds about 3–4 chunks. Expressions exceeding that get misread.

### Explaining variables

Name a subexpression to label what it means.

```
# before
if line.split(':')[0].strip() == "root":
    ...

# after
username = line.split(':')[0].strip()
if username == "root":
    ...
```

The reader no longer has to parse `line.split(':')[0].strip()` to know what's being checked.

### Summary variables

Name a long boolean condition.

```
# before
if request.user.id == document.owner_id and not document.is_locked and user.has_permission('edit'):
    ...

# after
user_owns_document = (request.user.id == document.owner_id)
can_edit = user_owns_document and not document.is_locked and user.has_permission('edit')
if can_edit:
    ...
```

### De Morgan's Laws

Two equivalences you should be fluent in:

```
!(a && b)  ≡  !a || !b
!(a || b)  ≡  !a && !b
```

Use whichever form reads more naturally. Often pulling the `!` outward (`if (!(file_exists && file_readable))`) is clearer than distributing it. Sometimes the opposite.

### Don't abuse short-circuit logic

```
assert((!(bucket = FindBucket(key))) || !bucket->IsOccupied());
```
clever but cruel. Two ifs are kinder.

Compact short-circuits like `if (object && object->method())` are fine when the intent is obvious. The line is when the construct hides a side effect or a branch.

### Find a creative reframe

When logic feels too complex, try inverting the problem.

Boswell's example: "do these two ranges overlap?" became dense. Reframing as "do they *not* overlap?" — that's only two cases:

```
return !(other.end < begin || other.begin > end)
```

Much smaller than enumerating overlap conditions.

Likewise: computing the *opposite* of a set, then negating, often collapses logic.

### Breaking down giant statements

If you have a single huge statement combining many operations, split it into a sequence of intermediate variables — each named for what it represents:

```
final_url = "%s?%s%s" % (host, query_str, fragment)
```

becomes, when `query_str` and `fragment` are themselves complex, a sequence of three named variables. The reader scans the names; the curious one descends into each.

---

## Variables and Readability (Ch. 9)

Three properties of variables compound into readability cost:

1. **Count** — more variables → more state to track.
2. **Scope** — broader scope → more code that might touch it.
3. **Mutability** — more reassignments → more simulation to know its current value.

### 1. Eliminate variables that don't earn their place

A variable is worth keeping if it does one of:

- Breaks down a complex expression (explaining/summary variable).
- Adds clarification (a name worth more than the expression).
- Removes duplication.

If it does none of those, drop it.

**Useless temporary:**
```
now = datetime.datetime.now()
root_message.last_view_time = now
```
The variable does nothing. Just write the expression once.

**Intermediate result variable:**
```
var index_to_remove = null;
for (var i = 0; i < array.length; i++) {
    if (array[i] === target) {
        index_to_remove = i;
        break;
    }
}
if (index_to_remove !== null) {
    array.splice(index_to_remove, 1);
}
```

Handle the result the moment you find it:
```
for (var i = 0; i < array.length; i++) {
    if (array[i] === target) {
        array.splice(i, 1);
        return;
    }
}
```

**Control-flow flag:**
```
done = False
while not done:
    ...
    if x: done = True
```

Replace with an early `return` or `break`.

### 2. Shrink each variable's scope

The smaller the region of code where a variable is visible, the less the reader has to track.

Tactics by scope, smallest to largest:

- **Block scope** — declare inside the loop or `if` where it's used.
- **Function scope** — split a long method so a temporary lives in a helper.
- **Class scope** — fields used by only two methods should be locals, not fields. Avoid "intermediate state" fields.
- **File/module scope** — prefer locally-scoped, pure functions over module-level state.
- **Global scope** — almost never.

Language helps: in JavaScript use `let`/`const`, not `var`. In Python, structure with functions, not module globals. In Java/C++, prefer nested classes when a helper is only used by one outer class.

A useful test: can a reader understand the function without scrolling? If not, the variables' scopes are too big.

### 3. Prefer write-once variables

A variable that's assigned exactly once is trivial to track — its name *is* its value. The more times it changes, the more the reader has to simulate.

Tools:

- `const` (C++/JS), `final` (Java), `val` (Kotlin/Scala), immutable types.
- Compute then assign:
  ```
  const greeting = is_logged_in ? `Welcome, ${name}` : "Welcome, guest"
  ```
  instead of:
  ```
  let greeting = "Welcome, guest"
  if (is_logged_in) greeting = `Welcome, ${name}`
  ```
- When a variable must change, change it in one localized place (start of a function, inside a single loop), not throughout the body.

The combined heuristic: **fewer, smaller-scoped, write-once variables**. Each step down this list cuts mental load.
