# The Project

Spindle - a name as good as any other - is my attempt to learn idiomatic python by creating a library that will, hopefully, solve a real problem. 

# The Problem
Imagine a business entity modelled in an organisation with data. A very common scenario. However, due to various business requirements and historically political reasons, that single entity is represented differently in multiple independent systems. For example, imagine a watersports club that has three software packages to manage its membership. One to keep track of subscription fee payments, another to administer membership in various sections and yet another to book equipment (kayaks, paddleboards and such).

There is some overlap between the data in the three systems. The same attributes can be independently modified in any order at any time. We don't control the systems; there is no way to synchronise the updates. So we have to accept that the data will contain conflicting states. 

Yet, we want to make sense of the data. We would like to have a data set with the conflicts resolved ubiquitously. A data convergence, in a sense, but not necessarily automatic. 

What makes things more complex, we cannot rely on shared keys, change tracking or even timestamps on individual records. 

# Potential Solutions

## CRDT (Conflict-free Replicated Data Types)
The desire to have a converged data produced at multiple, independent sources might make this problem look like what CRDT tries to solve. Still, with my current understanding of it, I doubt it is a potential solution to the problem. 

## Historical Modelling

[Historical Modelling](https://historicalmodeling.com/) allows reconstructing current state objects from partially ordered facts.
Unlike CRDT, it does not try to find an automatic, algorithmic solution to all merge conflicts but instead favours explicit conflict resolutions. One of the advantages of this approach is the ability to change conflict resolution strategy over an entity lifetime without affecting its state at the time of the change.
 

# Learning Idiomatic Python

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
