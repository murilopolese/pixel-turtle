---
layout: default
---

# Pixel Geometry

What is the simplest drawing you can make? Take a moment to think about that before you continue. What are the 3 simplest things you can draw? And what is the most complex or beautiful drawing you have ever done or seen?

How would you describe those drawings to someone without drawing them? For example, how could you describe how to draw a house, a tree or how to draw a person to someone over the phone? Geometry is all about describing shapes according with their looks and properties. Eventually we might learn how to draw very complicated and beautiful things by knowing how to draw simple and small shapes.

Even if you are not good drawing by hand I will tell you who is an excellent drawing artist: Pixel Turtle. It can draw **anything** to you exactly how we explain to do it. But before it starts drawing pieces of art for us we need to learn what are the simplest drawings Pixel Turtle can do.

## Can't Get Simpler Than This

The simplest shape Pixel Turtle can draw is a dot. We'll call it a **pixel** which is the smallest thing you can draw on your Pixel Kit. In fact when you turn on your Pixel Kit you will see straight away a green pixel on your screen. That is the first thing Pixel Turtle does when appears on your screen.

Every time Pixel Turtle moves on the screen with the [pen down](../pixel-turtle.html#pen-up-and-pen-down) it stamps its current color under its current position.

## Drawing Straight Lines

The second most simple thing you can draw with Pixel Turtle are straight lines. The reason for it to be so simple is that the only thing Pixel Turtle needs to do to draw straight lines is to move `forward()` or `backward()`.

Wherever Pixel Turtle is on the screen, if you move `forward()` it will **always** draw a straight line. Don't trust me? Try those:

```python
clear()
forward(2)
```

```python
clear()
left(3)
forward(3)
```

```python
clear()
left(3)
backward(4)
```

## Angles

The next simplest thing Pixel Turtle can draw is two connected straight lines. "You must be kidding" you might be thinking, but hey! I told you that was simple, right? It is indeed very simple but there is a catch: How do you know one long line isn't two connected lines?

For instance, what is the difference between those sets of instructions?

```python
forward(4)
```

```python
forward(2)
forward(2)
```

The easiest way to spot two lines is because they form an angle between them. If you can't spot an angle it's easier to consider the whole thing as one straight line. The angle itself it's subject to a different discussion but here we'll learn how to make angles with Pixel Turtle.

The secret for making angles is: Move `forward()` or `backward()` and turn `left()` or `right()` by any amount. For example:

```python
forward(2)
left()
forward(2)
```

```python
backward(2)
right(3)
forward(2)
```

Well, almost any amount! Check it out what happens when you turn `left(8)` or `right(8)`.

## Closing Shapes

We can keep moving and turning as much as we like to the left, right, up or down but there is something special that happens when the Pixel Turtle makes it to where the drawing began: It closes a shape. Closed shapes are the next simplest thing Pixel Turtle can make.

The easiest way to close a shape is by repeating a simple set of instructions of moving `forward()` and turning `left()`. For example, execute the following set of instructions until it closes the drawing:

```python
forward()
left()
```

```python
forward()
left(2)
```

```python
forward(3)
left(3)
```

```python
forward(2)
left(3)
forward(2)
left(5)
```

```python
forward(1)
left(3)
forward(1)
left(6)
```
