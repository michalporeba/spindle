# Spindle

An attempt to learn idiomatic python by creating a library - a variation on historical modelling. 

# Background 

## Historical Modelling

[Historical Modelling](https://historicalmodeling.com/) allows reconstructing current state objects from partially ordered facts.
In its canonical implementation all data is represented by messages. All updates to objects can be done only by sending
more messages.

However, with some modifications, it might be a suitable solution to resolve data conflicts between disparate data soruces
which cannot be immediately updated, or reliably controlled. 

## Learning Idiomatic Python

At the beginning of this project, Python is the programming language I know the least and so at least a part of this project
is to learn how to create idiomatic Python libraries. Expect a lot of changes and complete 're-writes'. 

# Considerations

What is the most idiomatic way of delivering functionality in python libraries? What paradigm should I use? 
Should I use OOP and mutable object maintaining state? Or perhaps functional, immutable would be better? 

Sample object oriented code could look like so: 

```python
e = spindle(id, facts=null)
e.update_with(facts)
e.update_with(models)
e.facts()
e.facts(only_new=true)
e.current()
e.conflicts()
```

Sample functional code could look like so:

```python
e = spindle.create(id, facts, models)
e = spindle.update_with(e, facts)
e = spindle.update_with(e, models)
spindle.facts(e)
spindle.facts(e, only_new=true)
spindle.current(e)
spindle.conflicts(e)
```
