# `mdbook-mathjax-inline-preprocesser`

Preprocesses mdbook markdown to allow you to use dollar signs inside your markdown for mathjax. I was too lazy to learn Rust so I quickly wrote this with a python script.

## Configuration

Copy the `main.py` file into your book's main directory, or clone it with git submodules and link to it in your mdbook configuration:

```toml
[output.html]
mathjax-support = true

[preprocessor.mathjax]
command = 'python main.py' # or 'python mdbook-mathjax-inline-preprocesser/main.py' if you cloned with submodules
after = ['links']
```

Now, you can use block and inline dollar signs instead of escaped square brackets and/or parentheses:

```markdown
$$a+b$$

Inside a sentence I can use $a+b$ as math.
```
