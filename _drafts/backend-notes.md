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
            * quorum can be set (where it needs to read data from at least n number of nodes, the higher the quorum, higher the consistency, and lower the availability)
    * CP (no availability): because only consistent data needs to be returned, if there is a network partition and some of the data is inconsistent, it must make the node with the inconsistent data unavailable. 
        * Ex: MongoDB, Amazon DynamoDB (primary-secondary server structure, master receives all read/write operations, secondaries receive replicated data from primary to maintain identical data. Write operation is stopped until new master slave is selected during failovers. So there is a single point of failure, but there is a secondary or slave server on hot standby ready to take over, which will happen in a matter of seconds, but still some downtime nonetheless. it can be configured so that it can be read from secondary servers, but this will lead to data inconsistency)
            * read availability can be tuned and increased by reading from secondary servers, but write cannot be always available
    * CA (not partition tolerance): in theory, this cannot exist in a distributed system. This is only possible in a single host where partition tolerance is not an issue.
        * Ex: MySQL, other RDBMS (although now modern RDBS can be distributed)
    * Note: Most DBs these days practically offer all three of these, with tunable configurations for various levels of consistencies (but technically they do still give up on one of these)

## Message Queues
* messages are stored in queue structures, they are processed only once by one consumer (works as a buffer that temporarily stores messages between two components)
* messages can be anything from requests, replies, or other types of information
* great for achieving asynchronous processing and decoupling components in complex systems
* components
    * producer: one creating the message and adding it to the msg queue
    * consumer: taking the item from the queue and processing it
    * message broker: component that stores messages in a queue (FIFO). Other functions include mesage validation, permission control, routing rules, failure recovery, etc.
    * exchanger: 
* types
    * point to point: delivers one message to only one consumer application. Multiple consumers can exist but only one will consume one message at a time.
    * publish/subscribe (pub/sub): delivers mesages to all subscribers that are subscribed to the corresponding topic (many consumers per message)
    * pull vs push model: 
        * push: queue notifies consumer when message is available
        * pull: consumer polls the queue to check if there is any message available
* load balancer vs message queue
    * both can be used to handle more traffic and scale: lb can be used to balance load between multiple backend servers, message q can be used with multiple consumers to consume the queue more quickly
    * load balancers will process things synchronously (ex. client requests image, it will wait for until image is retrieved before it responds back)
    * message queues on the other hand process things asynchronously (ex. client can request uploading a video and it can respond immediately. The backend server will then do the uploading and the user won't be left hanging)

## Polling vs. Web Sockets vs. Server-Sent Events
* Polling:
    * the client repeatedly checks and requests for data from the server
    * inefficient since most requests don't receive data but still use resources (establish connection, parse header, query for new data, generate response and deliver)
    * short vs long: long is the improved version of short, where a client establishes a connection with the server and keeps connection open until data is available (typically within a timeout period). It repeats this process after data is available or after a timeout -- wastes less resources
    * server has no good way to tell if client is disconnected
* Web Sockets:
    * establishes persistent connection between client (browser) and server
    * allows a two way communication between the two
        * good for things like chat apps
    * consumes less resources on the server
    * lower latency compared to polling as it doesn't require establishing new connections
    * connections are not automatically recovered and must be implemented separately 
    * most common method used for sending updates from server to client asynchronously
    * built on top of TCP/IP
* Server-Sent Events (SSE)
    * Unlike websockets, SSE connections can only send data to client (browser)
        * ex) stock price updates, news feed, notifications, etc
    * But what SSE can do can also be achieved with Web sockets, it is the more popular choice, more browsers support web sockets over SSEs
    * stock price updates, twitter updates, news feed, notifications, etc
    * sent over HTTP (doesn't require custom protocol)
    * has a limit on maximum number of open connections

## Stateful vs Stateless Systems
* by state, it can mean any information about the client session, or about a particular point in time with regard to a process (ex. user authenticated or not? banking transfer only possible after successful authentication)
* stateless:
    * stateless means the information about the state is not kept in the server (typically stored on the client side)
    * easier to scale stateless since the client request can be sent to any server (newly added server, or new server due to one of them being down, etc), since state info is kept with client
* stateful
    * stateful system/architecture keeps state data in the server, so it requires sending the client to the same server (or to keep all state info updated across all servers)

## Sharding vs Partitioning
* both imply splitting the data into smaller subsets
* sharding (also referred to as horizontal partitioning) means splitting the data across multiple servers
* partitioning means splitting the data into smaller subsets but within the same database

## Ajax
* ajax request/response does not refresh the whole web page
* can exchange data with web server asynchronously

## Rate Limiter Algorithms
* Token bucket: tokens are refilled at a certain rate, and bucket has a max token capacity -- requests are only processed when there are available tokens
    * pro: memory efficient since bucket has limited size, allows burst of traffic during short periods of time, simple algorithm
    * cons: bursts of traffic may not be suitable for some applications, refill rate and bucket size might be difficult to tune
* Leaking bucket: requests are added to a queue (bucket), and they are processed at a fixed rate only -- when bucket is full, requests are dropped
    * pro: memory efficient due to fixed bucket size, fixed processing rate (stable outflow), simple algorithm
    * con: difficult to tune the 2 parameters
* Fixed window counter: only allows fixed amount of requests per set timeframe (5 requests per minute), reset at every set timeframe
    * pro: memory efficient, easy to understand
    * con: spike in traffic at edge of windows, might allow more requests that set quota
* Sliding window log: allows certain number of requests per time frame, old requests outside of the timeframe are removed, requests over the limit are dropped
    * pro: accurate rate limiting
    * con: memory not as efficient because timestamp can be stored in memory even after it is rejected


## Consistent Hashing
* 
