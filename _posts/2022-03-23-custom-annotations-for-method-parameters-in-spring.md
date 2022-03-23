---
layout: post
title: Custom Annotations For Method Parameters In Spring
subtitle: Using custom annotations to prevent duplicate code
date: 2022-03-23 22:11:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, spring boot]
---

I'm sure you've passed in method parameters with special annotations for your RestController, such as `@PathVariable`.

```java
@GetMapping("/api/v1/posts/{id}")
public PostsResponseDto findById(@PathVariable Long id) {
    return postsService.findById(id);
}
```

As you may know, this is for when you want to pass in the variable in `{id}` to the method. 

But what if you want to create custom annotations with custom tasks? Why? Maybe the object you want to pass required lots of other parameters. Maybe you have duplicate code in various controller methods, and it'll be simple to handle that logic through the annotation.

 Well, we can do this by implementing the `HandlerMethodArgumentResolver`.

>Strategy interface for resolving method parameters into argument values in the context of a given request.

This interface has two methods: 
`suppportsParameter`: to check if the parameter is what we're looking for.
`resolveArgument`: where we return the desired object. 

Let's first define our annotation. For the sake of simplicity, let's say we want an annotation that will return the string "Hello".
```java
// ReturnHello.java
@Target(ElementType.PARAMETER)  // determines where the annotation can be used
@Retention(RetentionPolicy.RUNTIME)
public @interface ReturnHello {
    // @interface defines an annotation class -> @ReturnHello
}
```

Now we create the class that implements `HandlerMethodArgumentResolver`.

```java
// ReturnHelloArgumentResolver.java
@Component
public class ReturnHelloArgumentResolver implements HandlerMethodArgumentResolver {

    // checks if the parameter is supported by the class
    @Override
    public boolean supportsParameter(MethodParameter parameter) {
        boolean isReturnHelloAnnotation =
                parameter.getParameterAnnotation(ReturnHello.class) != null;
        return isReturnHelloAnnotation;
    }

    // return the instance or object if resolvable
    @Override
    public Object resolveArgument(MethodParameter parameter,
                                  ModelAndViewContainer mavContainer,
                                  NativeWebRequest webRequest,
                                  WebDataBinderFactory binderFactory) throws Exception {
        return "Hello";
    }
}
```

Finally, we need to register this argument resolver so that Spring can recognize it. We can do this in our class that implements `WebMvcConfigurer`.

```java
@RequiredArgsConstructor
@Configuration
public class WebConfig implements WebMvcConfigurer {
    private final ReturnHelloArgumentResolver returnHelloArgumentResolver;

    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> argumentResolvers){

        argumentResolvers.add(returnHelloArgumentResolver);
    }
}
```

Now we can use this in our controller.
```java
@GetMapping("/")
    public String index(Model model, @ReturnHello String helloString){
        // helloString == "Hello"
        ...
    }
```

Of course, if what we're returning is some complex logic other than just "Hello", you can see why it's easier just using an annotation. 
