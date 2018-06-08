---
layout: default
---

# Learning New Words

How many words do you know? Do you remember what all those words mean and who taught you them? It's hard isn't it? How come we can learn entire new words using only words we already know?

One thing is for sure, it's way easier to teach Pixel Turtle a new word than to teach another person a new word! Actually when you think about it sometimes it's way easier to understand new words if we explain them as if we were explaining to the Pixel Turtle.

## Defining Words

When you turn your Pixel Kit on for the first time you haven't taught Pixel Turtle any words and yet it does understand some words like `forward()` or `right()` and `penUp()`. We won't go much further on how come Pixel Turtle is born knowing them but we'll focus on how to teach new words it doesn't know yet.

As we learnt on [Pixel Wandering](./pixel-turtle-wandering.html#how-to-ask-pixel-turtle-to-move), we can check what words Pixel Turtle knows by trying to evaluate the word. If it knows the word it will tell us what does that word represent, otherwise it will tell us something like `NameError: name 'bazinga' is not defined`.

Pay attention to what this is saying to us: The word `bazinga` is not defined. So if we want to teach Pixel Turtle this new word we must **define** this word. In MicroPython (or just Python) the way we define a word is by using another word we haven't mentioned yet: `def`, which is short for define.

For example if we want to create a word for drawing a square, first we need to know how to draw a square, it should be something like this:

```python
forward(2)
left(2)
forward(2)
left(2)
forward(2)
left(2)
forward(2)
left(2)
```

That is a lot of code but we can teach Pixel Turtle that every time we say `square()` it will execute al those 8 instructions!

The way to use `def` is like this: We say we are defining a word, then we say what is the word that we want to define, we make sure to explain this word is something we can execute and we describe what Pixel Turtle should do when we say the new word. It would look something like this:

```python
def square():
    forward(2)
    left(2)
    forward(2)
    left(2)
    forward(2)
    left(2)
    forward(2)
    left(2)
```

Notice that in Python, the way we say some block of code belongs or is inside another block of code is by using this left margin we call **tabulation**. So the way we say the lines of code belong to the definition of `square()` is by adding a margin to the left on all 8 lines of code. We can call `square()` anywhere **after** it's defined.

Although we can teach any word to Pixel Turtle, there are some tricks and tips to do it in a simple way to write and specially to read later. Yes, it's really important that Pixel Turtle understand what to do but it's even more important that we are able to read the code and understand what it does!

## Don't Repeat Yourself

You can define words that uses other words you defined previously. Let's take the `square()` example we used previously. You will notice we repeated the same 2 lines 4 times:

```python
forward(2)
left(2)
```

We could name it a `corner()` and use it later inside `square()`:

```python
def corner():
    forward(2)
    left(2)

def square():
    corner()
    corner()
    corner()
    corner()
```

As a general rule, a good coder is lazy. Not lazy to do the dishes or lazy and waking up late but lazy in the sense of not enjoying to write the same code many times.

We usually create words if we are writing exactly the same thing many times in our code. This is specially handy when you want to change what you wrote: Instead of fixing your code in many places, you can just change your word definition and every time the word is called it will have the correct definition!

## Pick Easy and Clear Names

Put names that are easy to understand or that describe well what the word does without having to read the definition. If you understand what a word means without having to read the definition, that word is great!

Previously we create a word named `corner()` that makes the Pixel Turtle move `forward(2)` and turn `left(2)`. What if we want to create a `corner()` that turns `right(2)`? That makes me think `corner()` was a bad name because it doesn't specify what direction this corner turns to. Instead we could do something like:

```python
def corner_to_left():
    forward(2)
    left(2)

def square():
    corner_to_left()
    corner_to_left()
    corner_to_left()
    corner_to_left()
```

Notice that we can't use spaces for defining words so we used `_` instead. We could have defined without spaces or `_` as well, I just found it easier to read but `cornertoleft()` would work equally well.

## Flexible and Reusable Words

On previous examples we defined the word `square()` but if you think about, it actually defined a specific square with 3 pixels width and 3 pixels height. What if we want to make a smaller or a bigger square? We could easily define a `small_square()`, `huge_square()` or `2x2square()` but you see, we'll soon have way to many very similar definitions.

If you think about the words Pixel Turtle already know such as `forward()` or `left()` they all can have a number between the `()` that somehow changes how the word works. This number we put between the `()` is called a "parameter" or "argument".

To define a word that accepts arguments we just need to give it a name to the parameter and we can use it inside the definition. This is further explained on [naming things that change](./naming-things-that-change.html) but the short explanation is: Whatever is the value you use when calling the word, it will know.

```python
def corner_to_left(amount):
    forward(amount)
    left(2)

def square(size):
    corner_to_left(size)
    corner_to_left(size)
    corner_to_left(size)
    corner_to_left(size)
```

When we call `square(4)` for example, Pixel Turtle will know that the `size` will be `4` and will call `corner_to_left()` with the value `4` as the parameter. We can call `square()` with many numbers as argument and it will draw as many different sizes of squares as we want.

But what if we don't use any arguments? It will definitely break saying `TypeError: function takes 1 position arguments but 0 were given`. That message is telling us that `square()` requires 1 argument but we haven't given any. We either always call `square()` with an argument or whenever we are defining `square()` we say: If no arguments are given, this is the default value. That's how we could do it:

```python
def corner_to_left(amount=1):
    forward(amount)
    left(2)

def square(size=1):
    corner_to_left(size)
    corner_to_left(size)
    corner_to_left(size)
    corner_to_left(size)
```
