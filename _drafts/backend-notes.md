---
layout: post
title: ---
subtitle: ---
date: 2022-06-01 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

## Circuit Breaker Pattern
* pattern used for preventing an application to retry an operation that is likely to fail
* Not to confuse with 'Retry pattern', in which the goal is to retry an operation with the expectation that it will succeed
* Why it is needed?
    * without the circuit breaker, an operation will wait until timeout (it is better to notify user that system is down rather than keep them waiting -- unresponsive app). Meanwhile, thousands of more operations can be queued, which could eventually lead to cascading failures (resources such as memory, connections, and threads could be exhausted eventually)
    * The goal is to only start making requests when the system is available again (and prevent making useless requests when the system is down)
* Circuit breaker states:
    * closed: request from application is routed to operation
    * open: request from application immediately fails and returned back to the application. this state is maintained for a certain timeout period, before it is changed to the 'half-open' state
    * half-open: limited number of requests are allowed and routed to operation. If successful, state changed to 'closed', else, it will be changed back to 'open'
* How it works?
    * from the closed state, it keeps track of the number of failures, and if the failure count exceeds the threshold value, the state changes to the 'open' state for a certain timeout period.
    * after the timeout duration in the open state, it will go to the half-open state, allowing few requests to be passed to the operation
    * if the operation succeeds, state changed to 'closed'. If it fails, it is changed back to the 'open' state.
* https://docs.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

## Redis Persistence
*    

## Microservices
> In short, the microservice architectural style is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API.
> -Martin Fowler

* typically packaged as an API so that it can interact with other services or componenets
* more manageable since each service is treated as a separate component with its own logic
* better scalability - each service can be independently scaled based on need
* not dependent on a specific technology stack
* faster development and deployment
* some disadvantages (as opposed to monolithic applications):
    * higher complexity (need to handle failures, load balancing, network latency, etc)
    * testing/debugging is more difficult
    
