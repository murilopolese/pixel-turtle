---
layout: default
---

# Naming Things That Change

Can you think of something that doesn't have a name? Or some with have many names? Do you know something that changed its name? Or things that changed itself so much that their names don't make any sense any more? Have you ever thought why things have their names? Do you know something with a good name?

Although they can be difficult questions to answer, they can be answered. And actually, by figuring out how to name things we will learn much more than how to label stuff.

## Describing and Referring

When we name things we add a feature to that thing that is very important: We are able to talk about it without having to describe it. For example, imagine you are with friends and one of them is wearing something on top of their head, it's made out of cloth, probably cotton, it has one button on top, a rigid surface sticking out of half of the bottom borders and it's green.

Now, imagine that you have to ask your friend where they got this thing made out of cloth, probably cotton, with a button... Well, we probably don't want to describe how things are every time you want to refer to it, therefore we can create shortcuts for talking about it: we name it. Let's agree that the thing on your friend's head is a hat. Then we could easily ask: Where did you get that hat?

But what are we describing and referring with Pixel Turtle? Mostly numbers. But why, numbers, why? Because unfortunately that is all Pixel Turtle is born knowing. Everything else we want it to know, we have to teach it.

We are not born knowing to talk, but we can scream. How we transform scream into talk is what we know as "learn to talk". You would be shocked with the amount of things Pixel Turtle can learn with just numbers and names.

## Giving names in MicroPython

Let's start simple, I'd like Pixel Turtle to know that the sky right now is white. First things first, does Pixel Turtle knows what is white? It happens that it knows already what `white` is! The way we say that the sky is white it's something like this:

```python
sky = white
```

And you can read this as "sky is white", "sky equals to white", "set sky to white" or even "assign white to sky".

From now on, if you ask Pixel Turtle how's the sky it will answer `white`.

## Things change!

As time goes by we know the sky changes its color to black. But hey, have you noticed we say that the sky changed color and not there is something else then the sky? It's still the sky but it's different. Then when the sky changes its color to black we can say:

```python
sky = black
```

You could also tell Pixel Kit how many stars are on the sky, you could tell if it's night or that your name is "Banana Banana". To facilitate talking about naming thing we usually there is a name and a value. In our case the name is `sky` and sometimes its value is `white`, sometimes is `black`.

It's because there are things that can change their **values** it's also common to talk about the **names** as **variables**.

## What can we name?

It's important to understand Pixel Turtle's limitations when we are giving names.

First of all, the actual names: Names can only have letters and numbers without space. You can have names that when you read might sound like two words, like `hatColor` or `stars_in_the_sky`.

Now for the values, it can be numbers, other names, text (people call it "string") or a list. For number and other names it's just type in as they are:

```python
favoriteColor = green
eyes = 2
```

For strings we need to put a `'` or `"` around the text:

```python
name = 'Banana Banana'
```

Now for lists, you can create lists of anything, even lists of lists. All you have to do is to wrap them with `[]` and separate by `,`:

```python
colors = [white, black, red, blue, green, yellow, purple, cyan]
bff = ['h4ck3r_fr13nd', 'kiwikiwi', 'bee']
bananaYellow = [10, 10, 0]
```

For lists there is something special, you can refer to the whole list or to a specific item in the list. For example, what is the third item inside `colors`? It's the `color[2]`. Why `2`?

Here is something really weird about Pixel Turtle. It starts counting not on 1 but on 0! So the 1st item on `colors` is `colors[0]`, the 2nd item is `colors[1]` and the 3rd is `color[2]`. There is nothing wrong with it, it's just different!

## Unlocking powers

Perhaps the coolest thing about naming things it's not how you name or what you name but the powers it unlocks!

If there is one power that is the coolest it's to be able to tell Pixel Kit how to help you!

If you are bored and want to play a game or if you want to change the color of your room, you can tell Pixel Turtle to do something that will help you to get what you want!

It's not necessary, but naming things makes it much easier to do many things with Pixel Turtle. It's probably true to say that if you can explain something to Pixel Turtle in it's language, both Pixel Turtle and you can learn this thing.
