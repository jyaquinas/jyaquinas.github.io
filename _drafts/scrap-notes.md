---
layout: post
title: scrap
subtitle: 
date: 2022-02-22 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

## Questions & Concepts To Cover
* What does @builder do -> what is builder pattern
    * https://www.geeksforgeeks.org/builder-design-pattern/
    * https://refactoring.guru/design-patterns/builder
    * https://projectlombok.org/features/Builder

* How to change H2 language to mysql? -> mysql5innoDBdialect (depracated)

* domain-driven design (evans 2003) | domain model vs transaction script (web, service, repository, dto, domain)
    * https://www.infoq.com/articles/ddd-in-practice/
    * https://medium.com/microtica/the-concept-of-domain-driven-design-explained-3184c0fd7c3f
    * https://lorenzo-dee.blogspot.com/2014/06/quantifying-domain-model-vs-transaction-script.html
    * https://medium.com/hackernoon/making-a-case-for-domain-modeling-17cf47030732#:~:text=Transaction%20script%20is%20far%20from,much%20more%20extensible%2C%20maintainable%20code
    * https://itzone.com.vn/en/article/entity-domain-model-and-dto-why-so-many/
    * https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-domain-model#:~:text=Entities%20represent%20domain%20objects%20and,the%20attributes%20that%20comprise%20them.
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

* @webmvctest vs @springboottest & testresttemplate
    * jpa doesnt work in webmvctest? only inits controller and controller advice
    * HttpEntity
    * ResponseEntity

* Spring/JPA Annotations 
    * @Transactional
        * https://dzone.com/articles/how-does-spring-transactional
    * @Autowired
    * @Service

* Dirty checking - JPA entity
    * https://jojoldu.tistory.com/415
    * https://www.netsurfingzone.com/hibernate/dirty-checking-in-hibernate/
    * automatically checks if objects have been modified and will update regularly (when session flushed or transaction is commited)

* why pass .class


---
## Misc Subjects
* What is java bean?
    * objects that are managed by spring IoC container

### Application Layers?
* it is not recommended to use the entity class as the request/response class
    * DB table is based on this entity class, and making many changes to the entity class can be costly
    * recommended to separate the view and DB layer
    * use a Dto class, and generate the entity class through it - `toEntity()`


### Data Access Object (DAO) vs Data Transfer Object (DTO)
* DAO -> class that has CRUD operations
* DTO -> object that holds data
* POJO (plain old java object) -> java object that defines an entity

### Running Tests With Spring
```java
@RunWith(SpringRunner.class)
@SpringBootTest // initializes the H2database for test
public class PostsRepositoryTest {

    @Autowired
    PostsRepository postsRepository;

    @After  // function executed after test
    public void cleanup(){
        postsRepository.deleteAll();
    }

    @Test
    public void saveAndGetPosts(){
        String title = "Test Post";
        String content = "Test content";

        // Create posts instance through builder pattern (lombok @Builder)
        // save() -> inserts/updates to table
        postsRepository.save(Posts.builder()
                .title(title)
                .content(content)
                .author("author@email.com")
                .build());

        // returns all rows of table (or instances of type)
        List<Posts> postList = postsRepository.findAll();

        Posts posts = postList.get(0);
        assertThat(posts.getTitle()).isEqualTo(title);
        assertThat(posts.getContent()).isEqualTo(content);

    }
}
```

#### Checking Executed Queries
If you'd like to check the actual queries that were executed during the tests, create a file named 'application.properties' under src/main/resources.
Add the following line:
`spring.jpa.show_sql=true`
`spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect`

Then you'll be able to see the queries in the test results.
```shell
Hibernate: drop table if exists posts CASCADE 
Hibernate: create table posts (id bigint generated by default as identity, author varchar(255), content TEXT not null, title varchar(500) not null, primary key (id))
...
```


