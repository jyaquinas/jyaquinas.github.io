---
layout: post
title: Domain-Driven Design
subtitle: Basic components of DDD
date: 2022-03-03 21:31:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, ddd, design]
---


---
* domain-driven design (evans 2003) | domain model vs transaction script (web, service, repository, dto, domain)
---
* Value Objects (are like complex data types): 
    * structural equality: value objects are equal if values are equal (must redefine `equals` and `hashcode` func) - have no identity (unlike entities)
    * they are immutable (no setters, only getters returning immutable objects - changing value requires creating new instance)
    * doesnt have lifespan
    * self validating -> if not valid, object should not be created (to avoid adding validation code here and there, only validate within the value object)
    * examples: Length, Age, etc (instead of using general int)
    * pros: type safety, reduce duplication (can be shared among multiple entities, etc), easier to read
    * cons: can lead to too much code base if wrapping every primitive value to a value object
    * JPA annotation -> `@Embeddable` (1:1) or `@ElementCollection` (1:n) used
* Entities (domain objects)
    * identifier equality: has identity, if id equal, they are equal
    * mutable
    * has lifespan
    * have corresponding tables in DB
    * between service and repository layer
    * JPA annotation -> `@Entity`
* DTO: 
    * purpose is to transfer data
    * helps separate service and UI layers
    * contain no logic (domain objects can have logic)
    * DTO <-> Entity conversion occurs within service layer - `@Service` annotation
    * Why not use entity directly? making frequent changes to entity can be costly (updating the DB)
    * easier to serialize/send this data structure than the more complex entity class
* Transaction script vs domain model
    * Transaction scripts separate logic by transaction units, so it groups all the relevant business logic into this single transaction. This leads to having anemic domain objects (DOs without logic, only getters and setters), and implementic the logic at the transaction level -> not OOP
    * domain model groups all relevant behaviors/logic with the relevant DO (DO holds data and behavior). Transactions then don't need to define logic, only decide the order of the actions already defined in the DOs -> OOP, much more manageable
* application layers
    * can also be viewed as Presentation layer (web layer), Business logic layer (service layer), Data Access layer (repository layer)
    * Web layer: `@Controller` class - controllers, exception handlers, filters, view templates, etc
    * Service Layer: `@Service` class - connects web/controller and dao/repository layer - application and infrastructure services (business logic?)
    * Repository Layer: repository interfaces - access to DB
    * DTO: transfer data between repository/service and web/controller
    * Domain Layer: Entity classes, value objects, domain services, etc
---
links:
* https://www.infoq.com/articles/ddd-in-practice/
* https://medium.com/microtica/the-concept-of-domain-driven-design-explained-3184c0fd7c3f
* https://lorenzo-dee.blogspot.com/2014/06/quantifying-domain-model-vs-transaction-script.html
* https://medium.com/hackernoon/making-a-case-for-domain-modeling-17cf47030732#:~:text=Transaction%20script%20is%20far%20from,much%20more%20extensible%2C%20maintainable%20code
* https://itzone.com.vn/en/article/entity-domain-model-and-dto-why-so-many/
* https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-domain-model#:~:text=Entities%20represent%20domain%20objects%20and,the%20attributes%20that%20comprise%20them.