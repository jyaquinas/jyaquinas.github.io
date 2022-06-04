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
* Persistence options:
    * RDB (redis DB)
        * point in time snapshots
        * good for backups and disaster recoveries
        * faster restarts with big datasets compared to AOF
        * supports partial resch after restart and failovers (for replicas)
        * data after the snapshot can be lost
    * AOF (Append only file)
        * logs every write operation, dataset can be reconstructed from this
        * supports different sync policies (every second by default)
        * sync is done through a background thread
        * AOF files are typically larger compared to those of RDB
    * RDB + AOF
    * No persistence
* https://redis.io/docs/manual/persistence/

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
    
## 301 vs 302 Redirect
* 301
    * means that requested url is "permanently" moved, so subsequent requests will be made to the new redirected url
* 302
    * means that requested url is "temporarily" moved, so requests are first sent to the first url before they are redirected again to the new url
    * useful for things like analytics 
    
## CAP Theorem (Consistency, availability, partition tolerance)
* Consistency: all users read the most recent write, all nodes will contain the same data simultaneously 
* Availability: every request receives a non-error response, the system is operational at all times (even if some nodes are unavailable)
* Partition Tolerance: system continues to function despite a network partition (communication break), it will not fail permanently
* CAP theorem states that only 2 of these can be satisfied
    * In a distributed system, network partiton is unavoidable, which leaves us with AP, or CP
    * AP (no consistency): say we have a write request but a network partition occurs during the write operation. This will lead to data inconsistency. Because the system needs to be available, the read requests will simply be redirected to the available ones. But before all the data is synced, some users will receive stale data. 
        * Ex: Cassandra (cluster of nodes where all take read/write operations, any node serves as a primary host, no single point of failure, but data across nodes take time to synchronize, "eventual consistency")
    * CP (no availability): because only consistent data needs to be returned, if there is a network partition and some of the data is inconsistent, it must make the node with the inconsistent data unavailable. 
        * Ex: MongoDB, Amazon DynamoDB (primary-secondary server structure, master receives all read/write operations, secondaries receive replicated data from primary to maintain identical data. Write operation is stopped until new master slave is selected during failovers. So there is a single point of failure, but there is a secondary or slave server on hot standby ready to take over, which will happen in a matter of seconds, but still some downtime nonetheless. it can be configured so that it can be read from secondary servers, but this will lead to data inconsistency)
    * CA (not partition tolerance): in theory, this cannot exist in a distributed system. This is only possible in a single host where partition tolerance is not an issue.
        * Ex: MySQL, other RDBMS (although now modern RDBS can be distributed)
    * Note: Most DBs these days practically offer all three of these, with tunable configurations for various levels of consistencies (but technically they do still give up on one of these)

## Consistent Hashing
* 
