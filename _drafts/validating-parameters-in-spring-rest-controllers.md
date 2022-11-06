---
layout: post
title: Validating Parameters in Spring Rest Controllers
subtitle: Validate complex parameters using bean validation
date: 2022-11-06 21:11:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, spring, validation]
---

### What is Bean Validation
> The Bean Validation API is a Java specification which is used to apply constraints on object model via annotations

Why use bean validation instead of something like `@RequestParam`?

We can use `@RequestParam` annotation to map the method parameter to a web request parameter. But when the number of parameters becomes too large, it becomes more difficult to manage (and also hard to read..?). Let's look at the following example.

```java
    @GetMapping("/validateThroughMultiRequestParam")
    ResponseEntity<String> validateThroughMultiRequestParam(@RequestParam int id,
                                                            @RequestParam String name,
                                                            @RequestParam String lastName,
                                                            @RequestParam(defaultValue = "2") int age){
        Person person = Person.builder()
                .name(name)
                .lastName(lastName)
                .id(id)
                .age(age)
                .build();
        return ResponseEntity.ok(person.toString());
    }
```

You can already imagine what it would look like to have a bunch of `@RequestParam`s. It would be much simpler if we could just bundle these parameters into a single POJO, and use bean validation in order to validate each of the POJOs properties. 

### Validating POJOs
Let's create a `Person` POJO. We can use validation annotations, such as `@NotNull` or `@NotBlank`, in order to set validation constraints on the desired properties. 

For a full list of contraints, check this [page](https://docs.jboss.org/hibernate/beanvalidation/spec/2.0/api/javax/validation/constraints/package-summary.html).

```java
@Getter
@Setter
@ToString
@Builder
public class Person {
    @NotNull
    private int id;

    @NotBlank
    private String name;

    @NotBlank
    private String lastName;

    @Min(20)
    private int age;

}
```

Now all we need to do on the controller side is add the `@Valid` annotation on the POJO in order to do a validation check on the parameter object. If the constraints are not met, an exception will be thrown. 

We can now simplify our GET request.
```java
    @GetMapping("/validateComplexRequestParam")
    ResponseEntity<String> validateComplexRequestParam(@Valid Person person){
        return ResponseEntity.ok(person.toString());
    }
```

Let's add a function inside the controller for handling the exceptions.
```java
    @ExceptionHandler({ConstraintViolationException.class, BindException.class})
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ResponseBody
    String handleConstraintViolationException(Exception e){
        return "Request Param is not valid: " + e;
    }
```

We can now run the following tests.
```java
    @Test
    void whenComplexRequestParamIsValid_thenReturnsStatus200() throws Exception {
        MvcResult mvcResult = mvc.perform(get("/validateComplexRequestParam")
                        .queryParam("id", "5")
                        .queryParam("name", "Jake")
                        .queryParam("lastName", "Smith")
                        .queryParam("age", "30"))
                .andExpect(status().isOk()).andReturn();

        System.out.println(mvcResult.getResponse().getContentAsString());
    }

    @Test
    void whenComplexRequestParamLastNameIsNotValid_thenReturnsStatus400() throws Exception {
        MvcResult mvcResult = mvc.perform(get("/validateComplexRequestParam")
                        .queryParam("id", "5")
                        .queryParam("name", "Jake")
                        .queryParam("lastName", "")
                        .queryParam("age", "30"))
                .andExpect(status().isBadRequest()).andReturn();

        System.out.println(mvcResult.getResponse().getContentAsString());
    }
```

The second test should return a status 400 because the empty last name does not meet the `@NotBlank` constraint. It will output this error:
> Request Param is not valid: org.springframework.validation.BindException: org.springframework.validation.BeanPropertyBindingResult: 1 errors
> Field error in object 'person' on field 'lastName': rejected value []; codes [NotBlank.person.lastName,NotBlank.lastName,NotBlank.java.lang.String,NotBlank]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [person.lastName,lastName]; arguments []; default message [lastName]]; default message [must not be blank]

### Using Contraints on Method Parameters
We can also use the contraint annotations on the controller method parameters directly, instead of having them inside the POJO properties.

```java
    @GetMapping("/validateSimpleRequestParam")
    ResponseEntity<String> validateSimpleRequestParam(@RequestParam @Min(2) int value){
        return ResponseEntity.ok(String.valueOf(value));
    }
```

But in order to make this work, we must add the `@Validated` annotation on the controller class level. This will tell Spring to check for contraint annotations on method parameters.

```java
@Validated
@RestController
public class ValidationController {
    ...
}
```

And FYI, this also works with the `@PathVariable` annotation. 

### Validating Request Body
Okay so, can we also validate request bodies? Sure.

```java
    @PostMapping("/validateBody")
    ResponseEntity<String> validateBody(@Valid @RequestBody Person person){
        return ResponseEntity.ok(person.toString());
    }
```

Shall we run some tests?

```java
    @Test
    void whenBodyIsValid_thenReturnsStatus200() throws Exception {
        Person person = Person.builder()
                .id(5)
                .name("Jake")
                .lastName("Smith")
                .age(30)
                .build();
        String body = objectMapper.writeValueAsString(person);

        MvcResult mvcResult = mvc.perform(post("/validateBody")
                        .contentType("application/json")
                        .content(body))
                .andExpect(status().isOk()).andReturn();
    }

    @Test
    void whenBodyParamLastNameIsNotValid_thenReturnsStatus400() throws Exception {
        Person person = Person.builder()
                .id(5)
                .name("Jake")
                .lastName("")
                .age(30)
                .build();
        String body = objectMapper.writeValueAsString(person);

        MvcResult mvcResult = mvc.perform(post("/validateBody")
                        .contentType("application/json")
                        .content(body))
                .andExpect(status().isBadRequest()).andReturn();

        System.out.println(mvcResult.getResponse().getContentAsString());
    }
```

And again, the second test will through an error like this:
> Request Param is not valid: org.springframework.web.bind.MethodArgumentNotValidException: Validation failed for argument [0] in org.springframework.http.ResponseEntity<java.lang.String> com.springframework.springDemo.controller.ValidationController.validateBody(com.springframework.springDemo.dto.Person): [Field error in object 'person' on field 'lastName': rejected value []; codes [NotBlank.person.lastName,NotBlank.lastName,NotBlank.java.lang.String,NotBlank]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [person.lastName,lastName]; arguments []; default message [lastName]]; default message [must not be blank]]

### Controller Class
Here's the full controller class.

```java
package com.springframework.springDemo.controller;

import com.springframework.springDemo.dto.Person;
import jakarta.validation.ConstraintViolationException;
import jakarta.validation.Valid;
import jakarta.validation.constraints.Min;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindException;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

@Validated
@RestController
public class ValidationController {

    @ExceptionHandler({ConstraintViolationException.class, BindException.class})
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ResponseBody
    String handleConstraintViolationException(Exception e){
        return "Request Param is not valid: " + e;
    }

    @GetMapping("/validateSimpleRequestParam")
    ResponseEntity<String> validateSimpleRequestParam(@RequestParam @Min(2) int value){
        return ResponseEntity.ok(String.valueOf(value));
    }

    @GetMapping("/validateComplexRequestParam")
    ResponseEntity<String> validateComplexRequestParam(@Valid Person person){
        return ResponseEntity.ok(person.toString());
    }

    @GetMapping("/validateThroughMultiRequestParam")
    ResponseEntity<String> validateThroughMultiRequestParam(@RequestParam int id,
                                                            @RequestParam String name,
                                                            @RequestParam String lastName,
                                                            @RequestParam(defaultValue = "2") int age){
        Person person = Person.builder()
                .name(name)
                .lastName(lastName)
                .id(id)
                .age(age)
                .build();
        return ResponseEntity.ok(person.toString());
    }

    @PostMapping("/validateBody")
    ResponseEntity<String> validateBody(@Valid @RequestBody Person person){
        return ResponseEntity.ok(person.toString());
    }
}
```

