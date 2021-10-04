# The Project

Spindle - a name as good as any other - is my attempt to learn idiomatic python by creating a library that will, hopefully, solve a real problem. 

# The Problem
Imagine a business entity modelled in an organisation with data. A very common scenario. However, due to various business requirements and historically political reasons, that single entity is represented differently in multiple independent systems. For example, imagine a watersports club that has three software packages to manage its membership. One to keep track of subscription fee payments, another to administer membership in various sections and yet another to book equipment (kayaks, paddleboards and such).

There is some overlap between the data in the three systems. The same attributes can be independently modified in any order at any time. We don't control the systems; there is no way to synchronise the updates. So we have to accept that the data will contain conflicting states. 

Yet, we want to make sense of the data. We would like to have a data set with the conflicts resolved ubiquitously. A data convergence, in a sense, but not necessarily automatic. 

What makes things more complex, we cannot rely on shared keys, change tracking or even timestamps on individual records. 

# Potential Solutions

## CRDT (Conflict-free Replicated Data Types)
The desire to have a converged data produced at multiple, independent sources might make this problem look like what [CRDT](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) tries to solve. Still, with my current understanding of it, I doubt it is a potential solution to the problem.

## Historical Modelling

[Historical Modelling](https://historicalmodeling.com/) allows reconstructing current state objects from partially ordered facts.
Unlike CRDT, it does not try to find an automatic, algorithmic solution to all merge conflicts but instead favours explicit conflict resolutions. One of the advantages of this approach is the ability to change conflict resolution strategy over an entity lifetime without affecting its state at the time of the change.
 
## The Shape of the Solution

Currently, my tGenerally speaking, I imagine the solution could consist of an object which gets instantiated per entity. Its state can be rehydrated by applying some local data if anything exists. It then can accept data models from various sources and produce messages with recommended updates to the data sources (if they are out of date with the latest state) as well as some state representation which can be stored and used later to rehydrate the object. 

A spindle - the instance of an object - is not expected to map properties between different data sources or match entities with different IDs. This is a separate problem which we can add to the library later, but at its core, the functionality is limited to merging single entity data, which comes from many out of date sources. 

# Learning Idiomatic Python

At the beginning of this project, Python is the programming language I know the least and so at least a part of this project
is to learn how to create idiomatic Python libraries. Expect a lot of changes and complete 're-writes'. 

For better or worse, my starting point, a model solution is [pandas](https://github.com/pandas-dev/pandas). I am in no position at the time of writing this, to judge how pythonic it is, but one has to start somewhere. Any suggestions for improvements are very welcome. 

# Considerations

* For the solution to be universal we should support multiple data stores, for internal state representation. 
* Some automatic conflict resolution might be good to have, but it should be configurable at design time. Once the conflict is resolved it should stay resolved in that one way even if the automatic conflict resolution method is changed later. 

