---
layout: post
title: Web Application Architecture
subtitle: Basic Components of Web Applications Using Spring Boot
date: 2022-03-09 17:21:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, ddd, design, spring boot]
---

### Application Layers
There are many different ways to design a web application. But I'll talk about the most common method, or the "classic" way.

The application can be divided into 3 main layers: web, service, and repository layers.

![Application Layers](/img/posts/web-application-architecture/application-layers.png){:class="img-fluid rounded"}

#### Web Layer
This layer is responsible for showing information to the user and handling their interactions. This layer will include the controller class, annotated by `@Controller`, to provide REST endpoints, as well as view templates for the UI.  

```java
// PostsApiController.java
@RequiredArgsConstructor
@RestController
public class PostsApiController {
    private final PostsService postsService;

    @PostMapping("/api/v1/posts")
    public Long save(@RequestBody PostsSaveRequestDto requestDto) {
        return postsService.save(requestDto);
    }

    @GetMapping("/api/v1/posts/{id}")
    public PostsResponseDto findById(@PathVariable Long id) {
        return postsService.findById(id);
    }
}
```

#### Service Layer
The service layer serves as a bridge between the web and repository layer. This can be done through a service class, annotated by `@Service`. Depending on how it is implemented, this layer can hold the business logic.
But other implementations, such as the domain model[^domainmodel], will keep all the business logic inside the domain object, or the entity class (defined by the `@Entity` annotation), and tries to keep the service layer as simple as possible. This layer is also responsible for exposing the public API of the service, allowing interactions with external services or other applications.

```java
// PostsService.java
@RequiredArgsConstructor
@Service
public class PostsService {
    private final PostsRepository postsRepository;

    @Transactional
    public Long save(PostsSaveRequestDto requestDto){
        return postsRepository.save(requestDto.toEntity()).getId();
    }

    public PostsResponseDto findById(Long id){
        Posts entity = postsRepository.findById(id).orElseThrow(()->
                new IllegalArgumentException("The post does not exist. id = " + id));

        return new PostsResponseDto(entity);
    }    
}
```

Notice how the service layer will only return DTOs and not the entity classes themselves. And when performing a task, like saving a post, it will receive the DTO, convert it to an entity, and save it to the DB through the repository class.

#### Repository Layer
Access to the database is achieved through this layer. Using the `@Repository` annotation (or inheriting from the JpaRepository or other similar interfaces), you can read or write to the DB through the basic CRUD operations it provides.

```java
// PostsRepository.java
public interface PostsRepository extends JpaRepository<Posts, Long> {
    // JpaRepository<EntityClass, PK type> -> Generates basic CRUD methods

    // For custom queries:
    // @Query("SELECT p from Posts p ORDER BY p.id DESC")
    // List<Posts> findAllDesc();
}
```

Here is the entity class, Posts:
```java
// Posts.java
@Getter
@NoArgsConstructor
@Entity // defines an entity class -> represents DB table
public class Posts {

    @Id // specifies PK field
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    // specifies rule for PK generation. IDENTITY -> auto increment option
    private Long id;

    @Column(length = 500, nullable = false)
    private String title;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String content;

    // uses default column settings if not specified
    private String author;

    @Builder
    public Posts(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }

    public void update(String title, String content) {
        this.title = title;
        this.content = content;
    }
}

```

### How do the layers communicate with each other?
I mentioned that the service layer bridges the other two layers. But how is this achieved? We need to introduce some concepts from [domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design).

#### DTOs
DTO stands for data transfer object. Its main objective is to transfer data from one layer to another, more specifically between the web and service layers. Because DTOs only transfer data, they should not contain any business logic. Entities obtained from the repository layer are converted to DTOs before they are sent to the web layer. And data from the web layer is sent to the service layer in the form of DTOs before they are converted to entities, which are then used in the repository layer to make changes to the DB.

Here's an example of a DTO:
```java
// PostsSaveRequestDto.java
@Getter
@NoArgsConstructor
public class PostsSaveRequestDto {
    private String title;
    private String content;
    private String author;

    @Builder
    public PostsSaveRequestDto(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }

    public Posts toEntity(){
        return Posts.builder()
                .title(title)
                .content(content)
                .author(author)
                .build();
    }
}
```

Why use DTOs instead of entities themselves?

Keeping these separated helps keep the layers more loosely coupled. If we need to make changes to the entity classes, we can avoid updating these changes to all the other classes that would have depended on these entities by keeping the DTOs the same. It is also easier to serialize and send the DTO class instead of the more complex entity class.

#### Domain Layer
This layer holds domain objects (or entity classes), as well as [value objects](https://en.wikipedia.org/wiki/Value_object#:~:text=In%20computer%20science%2C%20a%20value,money%20or%20a%20date%20range.). This layer is what connects the service and repository layer. If we follow the domain model, entity classes will hold the business logic. So the service layer performs actions through the functions that are already defined in the domain objects.

---
[^domainmodel]: More information can be found in this [post](https://lorenzo-dee.blogspot.com/2014/06/quantifying-domain-model-vs-transaction-script.html) about domain model vs. transaction script.
