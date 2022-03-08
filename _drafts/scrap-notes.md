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

* @webmvctest vs @springboottest & testresttemplate
    * jpa doesnt work in webmvctest? only inits controller and controller advice
    * HttpEntity
    * ResponseEntity

* Spring/JPA Annotations 
    * @Transactional
        * https://dzone.com/articles/how-does-spring-transactional
        * https://stackoverflow.com/questions/26387399/javax-transaction-transactional-vs-org-springframework-transaction-annotation-tr
        * Transactional (readOnly = true)
    * @Autowired
    * @Service

* Dirty checking - JPA entity
    * https://jojoldu.tistory.com/415
    * https://www.netsurfingzone.com/hibernate/dirty-checking-in-hibernate/
    * automatically checks if objects have been modified and will update regularly (when session flushed or transaction is commited)

* why pass .class
* look into index.js file (mustache)
    * ajax
    * CRUD -> html func (post, get, put, delete)


---
## Misc Subjects
* What is java bean?
    * objects that are managed by spring IoC container
* Linux wildcards -> file searching
    * `*` match one or more occurrences of characters, including none
    * `?` match single occurrence of character
    * `[]` match any occurrence of characters in the enclosed bracket
    * ./tmp/* matches files and folders in ./tmp
    * ./tmp/** matches files, folders, and subfolders in ./tmp
    * https://stackoverflow.com/questions/3529997/unix-wildcard-selectors-asterisks
* for large projects with more complex data, it may be required to perform complex join operations for obtaining/searching for data
    * it is common to use spring data jpa for CUD operations, and use other frameworks for read operations (querydsl, jooq, mybatis)
* Shell 
    * ps -> lists processes
        * https://linuxize.com/post/ps-command-in-linux/
        * https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/
        * -e: list full process list
        * -f: full format
        * can be used with filter commands like `grep`
    * awk
        * https://www.geeksforgeeks.org/awk-command-unixlinux-examples/
        * `awk '{print $2, $4}'` : prints 2nd and 4th word (whitespace separated) -> $0 represents entire line
        * by default `awk {print} filename.txt` prints entire file line by line
    * tput
        * https://linuxcommand.org/lc3_adv_tput.php
        * can manipulate the terminal's appearance, like color, etc
        * `tput smso` start 'standout' mode
        * `tput rmso` end 'standout' mode
        * `tput sgr0` turn off all attributes
    * set
        * https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux
        *  we will get a list of all shell variables, environmental variables, local variables, and shell functions
    * `$$`
        * https://tldp.org/LDP/abs/html/internalvariables.html
        * process id of script itself
    * assigning results of a command to a variable
        * wrap around ``
        * `` array=`find . -maxdepth 1 -name '*.txt'` ``
        * results are saved into the array variable
        * use the command `set` in csh
            * `` set array=`find . -maxdepth 1 -name '*.txt'` ``
    * find maxdepth
        * https://www.geeksforgeeks.org/mindepth-maxdepth-linux-find-command-limiting-search-specific-directory/
        
        

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


