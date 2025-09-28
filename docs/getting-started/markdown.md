# Markdown Guide for Documentation & Research

Welcome to your Markdown reference! This guide is intended to help new members write clean, consistent documentation, research papers, and guides in Markdown.

You’ll learn:

-   Basic Markdown syntax (& pitfalls)
-   How to structure longer documents
-   Some MkDocs-Material-specific tips (like light/dark images)

---

## Where to Place Your Markdown Files

-   Repositories often include a **`docs/`** folder for documentation.
-   For research papers, use something like `docs/research/` and name files in **lowercase with hyphens**, e.g. `rf-methodology.md`.
-   For guides, tutorials, or setup instructions, place under `docs/guides/` or `docs/getting-started/` etc.

Keep files modular and purpose-driven.

---

## Basic Markdown Syntax

### Headers

Use `#` for headings:

```md
# Top Level Title

## Section Heading

### Subsection

#### Subsubsection
```

-   Each document should have exactly one `#` title at the top.
-   Use **title case** (capitalize key words) but avoid ending headings with punctuation (unless question mark).

---

### Paragraphs & Line Breaks

-   Separate paragraphs with a blank line.
-   A single new line does _not_ break a paragraph.
-   To force a line break **inside** a paragraph, append two spaces at the end of the line:

```md
This is the first sentence.␣␣  
This sentence will appear below, but in the same paragraph.
```

---

### Emphasis

-   Italic: `_italic_` or `*italic*`
-   Bold: `**bold**` or `__bold__`
-   Bold + Italic: `***both***`

Use emphasis sparingly — mainly to highlight important terms or warnings.

---

### Lists

**Unordered lists**:

```md
-   Item A
-   Item B
    -   Subitem (indented)
        -   Subsubitem
-   Item C
```

**Ordered lists**:

```md
1. Step one
2. Step two
3. Step three
```

You don’t need perfect numbering — Markdown auto-numbers. Just use `1.` everywhere if that’s easier.

---

### Task Lists (Checklists)

Useful for planning or task tracking:

```md
-   [ ] Incomplete task
-   [x] Completed task
```

Only use them when you intend them to be interactive or status-based. Don’t overuse in prose.

---

### Code & Fenced Code Blocks

**Inline code**: wrap short terms or commands with backticks:

```
Use `git status` to check changes.
```

**Fenced blocks**: for multi-line code or command sequences, use triple backticks and optionally specify a language for syntax highlighting:

````md
```cpp
void setup() {
    Serial.begin(115200);
}
```
````

````

Avoid trailing spaces on blank lines inside code blocks (they sometimes introduce rendering artifacts).

---

### Tables

Markdown supports simple tables:

```md
| Component | Description        | Qty |
|-----------|--------------------|----:|
| ESP32      | Microcontroller     |   1 |
| BMP390     | Barometric sensor   |   1 |
| SD Card    | Logging medium      |   1 |
````

-   Use `:` to control alignment: `:---` for left, `:---:` for center, `---:` for right alignment.
-   Keep tables narrow (≤ 3–4 columns) if possible. If your content is long, use a list instead.

---

### Links & Images

**Links**:

```md
[PlatformIO Docs](https://docs.platformio.org)
```

If a URL is long:

```md
<https://example.com/some/long-url>
```

**Images**:

```md
![Alt text describing image](../assets/images/diagram.png)
```

-   Always include sensible **alt text** for accessibility.
-   Prefer relative paths for internal images.
-   Store images under `docs/assets/images/` or similar.

---

### Light / Dark Mode Image Swapping (Material for MkDocs)

Materials supports automatically swapping images depending on theme using `#only-light` and `#only-dark` fragments. ([squidfunk.github.io](https://squidfunk.github.io/mkdocs-material/reference/images/?utm_source=chatgpt.com))

```md
![Title for light mode](../assets/images/diagram-light.png#only-light)
![Title for dark mode](../assets/images/diagram-dark.png#only-dark)
```

In a custom color scheme you may need extra CSS:

```css
[data-md-color-scheme="custom-light"] img[src$="#only-dark"] {
    display: none;
}
[data-md-color-scheme="custom-dark"] img[src$="#only-light"] {
    display: none;
}
```

> **Be cautious**: some users have reported inconsistencies when using `md_in_html` extension or wrapping these with `<figure>` tags. ([github.com](https://github.com/squidfunk/mkdocs-material/issues/5428?utm_source=chatgpt.com))

---

### Dividers & Blockquotes

-   **Horizontal rule**: `---` on a line by itself.
-   **Blockquote**: prefix with `>`:

    ```md
    > This is a quote or callout block.
    ```

You can nest quotes by adding more `>`.

---

### Footnotes

You can add footnotes for additional context or references:

```md
The rocket achieved peak altitude[^1].

[^1]: Data from July 15 flight logs.
```

Use footnotes sparingly; most external references should be inline links.

---

## Structuring a Research Paper or Guide

Here’s a recommended structure for research or technical writeups:

```md
# Title of Paper or Guide

_Author Name • Date_

## Abstract

Concise summary of objectives and findings.

## Background / Introduction

Set up the problem, context, prior work.

## Methods / Approach

What you did, how you tested, experimental setup.

## Results / Observations

Present data, charts, tables.

## Discussion / Analysis

Interpret your results, discuss limitations, next steps.

## Conclusion

Summarize findings and recommendations.

## References

Links, articles, datasheets, footnotes.
```

Use consistent headings and logical flow.

---

## Final Checklist Before Submitting

-   [ ] Filename lowercase and hyphenated (no spaces).
-   [ ] Top of file has `# Title` heading.
-   [ ] Document divided into coherent sections.
-   [ ] Lists, tables, code, and images render correctly.
-   [ ] External links or references provided.
-   [ ] Images stored in `/docs/assets/images/` with alt text.
-   [ ] No placeholder or “TODO” text left behind.

Once all boxes are ticked, your document is ready for review and publication!

---

If you like, I can also generate a _freeze.json_ snippet to capture sample renders (tables, code, light/dark image) which you can embed screenshots of — would you like me to build that for markdown.md?
