# Testing and Readability

Reference for chapter 14 of *The Art of Readable Code*. Test code is read by every future contributor as the unofficial documentation of how the real code works. If it's scary, people stop touching it — and the real code stops being tested.

---

## Why Test Readability Matters

When test code is big and scary, two failure modes appear:

1. **Coders avoid modifying the real code** — "we don't want to mess with that, updating all the tests would be a nightmare." Real code calcifies.
2. **Coders stop adding new tests** when they add new code. Coverage decays silently, and confidence rots.

The cure is the same as for production code: make tests read so naturally that adding one feels like writing a sentence.

> **Test code should be readable so other coders are comfortable changing or adding tests.**

---

## A Worked Example

The book starts with a deliberately ugly test and improves it through every section. The function under test:

```
// Sort 'docs' by score (highest first) and remove negative-scored documents.
void SortAndFilterDocs(vector<ScoredDocument>* docs);
```

Original test (8 distinct problems — see the end of this doc):

```
void Test1() {
    vector<ScoredDocument> docs;
    docs.resize(5);
    docs[0].url = "http://example.com"; docs[0].score = -5.0;
    docs[1].url = "http://example.com"; docs[1].score = 1;
    docs[2].url = "http://example.com"; docs[2].score = 4;
    docs[3].url = "http://example.com"; docs[3].score = -99998.7;
    docs[4].url = "http://example.com"; docs[4].score = 3.0;
    SortAndFilterDocs(&docs);
    assert(docs.size() == 3);
    assert(docs[0].score == 4);
    assert(docs[1].score == 3.0);
    assert(docs[2].score == 1);
}
```

The remaining sections show the techniques that fix it.

---

## 1. Hide Non-Essential Setup Behind Helpers

The reader doesn't care that you built a `vector<ScoredDocument>` and assigned URLs. They care: "given these scores in, what scores come out?" Make the test read that way.

```
void CheckScoresBeforeAfter(string input, string expected_output) {
    vector<ScoredDocument> docs = ScoredDocsFromString(input);
    SortAndFilterDocs(&docs);
    string output = ScoredDocsToString(docs);
    assert(output == expected_output);
}

void Test_SortAndFilterDocs() {
    CheckScoresBeforeAfter("-5, 1, 4, -99998.7, 3", "4, 3, 1");
}
```

Each test is now one line. Adding another test is trivial:

```
CheckScoresBeforeAfter("0, -0.1", "0");
CheckScoresBeforeAfter("", "");
```

**General principle:** hide less important details so more important details are prominent.

---

## 2. Make Error Messages Informative

A failing assertion that just says "test failed" sends the reader to a debugger. A good one tells you *what differed*.

```
assert(output == expected_output);
// →  "Assertion failed: (output == expected_output)"
```

vs.

```
BOOST_REQUIRE_EQUAL(output, expected_output);
// →  '"1, 3, 4" != "4, 3, 1"'
```

Use the richer assertion helpers your language/framework offers:

| Language | Use |
|---|---|
| C++ | `BOOST_REQUIRE_EQUAL`, `EXPECT_EQ` (gtest) |
| Python | `self.assertEqual()`, `pytest`'s rewritten asserts |
| Java | JUnit `assertEquals(expected, actual, message)` |
| JavaScript | `chai`'s `expect(...).to.equal(...)`, Jest's deep matchers |

If even those aren't enough, write a custom checker that prints both values, the diff, and the relevant inputs. The cost is paid once; the benefit recurs every time a test fails.

---

## 3. Choose Good Test Inputs

> **Pick the simplest set of inputs that completely exercises the code.**

Two failure modes:

- **Too simple — misses cases.** `"1, 2, 3" → "3, 2, 1"` never triggers the "filter negatives" branch.
- **Too complex — noise distracts.** `-99998.7` is a "loud" value: the reader spends time wondering why it's that specific number.

For the sort+filter example:

```
CheckScoresBeforeAfter("1, -1, 2", "2, 1");          // basic case + filter
CheckScoresBeforeAfter("", "");                       // empty
CheckScoresBeforeAfter("0", "0");                     // boundary: zero is kept
CheckScoresBeforeAfter("-1, -2", "");                 // all filtered
```

Each input is the simplest value that exercises one behavior. If you need a "very negative number," use `-1e100` — a crisp, unmistakable extreme value, not `-99998.7`.

### One function per behavior

Don't pack every case into one test. Split:

```
Test_SortAndFilterDocs_BasicSorting()
Test_SortAndFilterDocs_NegativeFiltering()
Test_SortAndFilterDocs_EmptyInput()
Test_SortAndFilterDocs_ZeroBoundary()
```

When one fails, you know exactly which behavior broke without reading the test body.

---

## 4. Name Tests Descriptively

`Test1()`, `Test2()` is malpractice. The test function name is the comment that appears in failure messages, test runners, and CI dashboards.

**Pattern:** `Test_<Function>[_<Situation>]`

```
Test_SortAndFilterDocs()
Test_SortAndFilterDocs_BasicSorting()
Test_SortAndFilterDocs_NegativeValues()
Test_SortAndFilterDocs_TieBreaking()
```

Don't worry about length. Test functions are never called from your codebase — they're only ever displayed. A long, precise name is pure benefit.

---

## 5. Test-Friendly Development

Code that's easy to test usually has:

- A well-defined interface (not many side channels).
- Minimal hidden state.
- Few setup requirements.
- Pure functions where possible.

When you write code expecting to test it, you naturally produce decoupled, focused designs. Even without full TDD, *keeping testing in mind while writing the real code* shifts decisions toward simpler structure.

### When testing makes real code worse

The book's caution: don't worship testability. Sometimes the cheapest way to make a class testable is to:

- Inject 8 mocks.
- Split one clear class into three contrived ones.
- Expose internals via `package`-visible accessors.
- Add seams that confuse the reader.

If the cure costs more readability than the disease, *the disease wins*. Skip the test, or test at a higher level (integration), or accept that this class is tested through its callers.

---

## 6. Don't Let Tests Pollute Real Code

Tests should mostly read the real code's public interface. Resist patterns that drag testing concerns into production:

- `if (testing) { ... }` branches in real code.
- Public mutators that exist solely so tests can poke state.
- Constructors with extra parameters only test code passes.

Better: use language features (friend classes in C++, package-private in Java, `@VisibleForTesting` annotations, dependency injection at construction) that keep the surface clean.

---

## The Eight Problems with the Original Test

The book ends Ch. 14 by listing what was wrong with `Test1()` — useful as a checklist when reviewing any test:

1. **Long and full of unimportant details.** A test should be describable in one sentence; the code shouldn't be much longer.
2. **Adding another test is hard.** Tempts copy-paste-modify; tests grow with duplication.
3. **Failure messages aren't useful.** `assert(docs.size() == 3)` tells you nothing about what `docs` contains.
4. **Tests everything at once.** Sorting and filtering should be separate tests.
5. **Inputs aren't simple.** `-99998.7` is noise.
6. **Inputs don't exercise the code completely.** Edge cases (empty, all negative, ties) missing.
7. **Missing edge case tests.** Tied scores? Zero? Empty input?
8. **The test function name is meaningless.** `Test1()` provides zero information at failure time.

Apply the checklist to your own tests — each item points back to a section above.

---

## A Note on TDD vs. Test-After

The book deliberately stays out of the TDD debate. The chapter's point holds either way: **once a test exists, make it readable.** Whether you wrote it before or after the real code, future readers will treat it as documentation.

For TDD-specific workflow (red/green/refactor), see the `tdd` skill.
