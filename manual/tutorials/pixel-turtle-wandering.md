---
layout: default
---

# Pixel Turtle Wandering

How do we know something is moving? That sounds like an obvious question but have you ever thought about what is to be moving? What's the difference between standing still and moving forward? Does your heartbeat or breathing counts as moving? If we are moving around the sun, are we ever still??

Those are all questions we can think about and perhaps answer using **Pixel Turtle**!

## What words Pixel Turtle knows?

Let's start by with an experiment: Stand up or watch a friend standing up and imagine how many things can we do to **move around**? We usually don't think about all the ways we can move because we already know how to **move around** but if I ask you "please walk to that door" or "please turn yourself towards the window" we probably know what to do right?

That is because we know the words `walk` and `turn` and we know what you should do if someone ask us to do it. Of course we can always do something else like `run` or `crawl` or `jump` to the door but what happens if someone ask us to `fly` to the ceiling? Or what if I ask you to `jetpropulse123_kjf`?

We have then two different situations with the same problem: We probably can't. Either because we can't `fly` or because we don't know what does `jetpropulse123_kjf` mean. **Pixel Turtle** has the same problem! We could try out every word we know to see if Pixel Turtle knows it as well but if you are interested on a faster and less frustrating way to learn what it can do, there is a list of the words Pixel Turtle is born knowing, we can find the full list on the Pixel Turtle Library [Guide](../pixel-turtle.html) or [Reference](../reference/pixel-turtle.html).

But for this tutorial we will focus on those words and how to tell the Pixel Turtle you want it to move:

- `forward` and `backward` ([guide](../pixel-turtle.html#forward-and-backward)).
- `left` and `right` ([guide](../pixel-turtle.html#left-and-right)).
- `penUp` and `penDown` ([guide](../pixel-turtle.html#pen-up-and-pen-down)).

## How to ask Pixel Turtle to move?

If I turn to you and just say "a jump", how do we know if I am asking you to jump or if I am asking you if you know what jump is? We have other words such as "please" or "what is" and we can use "!" or "?" to make it even more clear. Well with Pixel Turtle is a bit different. If you want Pixel Turtle to tell if it knows the word `left` for example you would just type `left` and try to execute/evaluate the word. If Pixel Turtle doesn't know the word it will write down something like `NameError: name 'left' is not defined` on the console.

If `left` is defined (that means Pixel Turtle knows that word) it will print what `left` means to it. In this specific case it will tell us `left` is a `<function left at 0x3ffe8d80>` (that second number `0x3ffe8d80` is where the word `left` is stored in Pixel Turtle brains).

If a word is a `function` that means we can ask Pixel Turtle to "perform" it just as an action. To do that we must add `()` to the end of the word like this: `left()`. This will mean we are asking the turtle to "please turn left". The same applies to all other words that are functions.

## Telling Pixel Turtle how much to move

Let's take `forward()` for this next example. If I ask you to walk forward you probably know what to do, right? But when should you stop walking forward? We have many ways to tell another person how to `walk` or `turn` an amount. We could use an object as reference and say "please walk until that tree" or we could say how much you want the person to walk in steps, meters, yards, foot, etc. Pixel Turtle is no different!

Since there are no trees on the Pixel Turtle world yet we will focus on telling Pixel Turtle exactly how much we want it to move. The way to do it is by telling how many pixels to move between the `()`. For example you could say `forward(2)` and Turtle Pixel will understand we want it to move forward 2 pixels. Notice that you don't have to specify the quantity if the amount is 1: `forward()` and `forward(1)` are the same thing.

In the same spirit we could say `backward(4)`, `left(2)` or `right(3)`. One thing that might be useful sometimes is to use negative numbers. What do you think is the difference between `forward(-2)` and `backward(2)`?

## Drawing or not on the screen

Lastly but not less important you will notice that as you ask the Pixel Turtle to move around the screen it leaves a trail. This trail is something like a brush that the Pixel Turtle rubs against the floor as it walks. That allow us to draw things by asking the Pixel Turtle to move around. In case we want to move but we don't want to leave a trail you can just ask to lift the pen from the floor with `penUp()`. Once we are ready to start drawing again we can just ask the Pixel Turtle to put the pen down with `penDown()` and it will drag the pen around.
