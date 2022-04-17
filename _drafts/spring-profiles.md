---
layout: post
title: Spring Boot Profiles
subtitle: Externalizing your app configurations
date: 2022-04-17 21:27:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [spring boot, java]
---

### Spring Boot Profiles
We can externalize our spring boot configurations so that we can use the same code under different conditions or environments. One example would be to run the application on different ports to achieve zero-downtime deployment, or more specifically, a blue/green deployment strategy. We can externalize our configurations through `application.properties` or `applications.yml` files. 

Spring Boot has a specific order of loading/overriding these property files, so we can use multiple configuration files for different purposes. Here is the overriding order, the top ones being higher in priority. You can find the full list on their [docs](https://docs.spring.io/spring-boot/docs/2.1.6.RELEASE/reference/html/boot-features-external-config.html).

> Profile-specific application properties outside of your packaged jar (`application-{profile}.properties` and YAML variants).
> Profile-specific application properties packaged inside your jar (`application-{profile}.properties` and YAML variants).
> Application properties outside of your packaged jar (`application.properties` and YAML variants).
> Application properties packaged inside your jar (`application.properties` and YAML variants).
> `@PropertySource` annotations on your `@Configuration` classes.
> Default properties (specified by setting `SpringApplication.setDefaultProperties`).

For instance, let's look at these two files. 
```yaml
# File: application.yml
server:
    port: 8080
```
```yaml
# File: application-prod.yml
server:
    port: 8081
```

Since the `application-{profile}.yml` has higher precedence than the `application.yml` file, the 8081 value will override the default 8080 value. 

Let's say that we have another file, `application-prod2.yml`.
```yaml
# File: application-prod2.yml
server:
    port: 8082
```

Now we must specify which profile to use. We can do this through system properties when executing the application.  
`java -jar -Dspring.profiles.active=prod2 myApplication.jar`

The command above will activate the `prod2` profile, so the application will run on port 8082. 

We can also add other active profiles using the `spring.profiles.include` property. These profiles will always be activated on top of the main profile that was specified through the `spring.profiles.active` property. 

You can find more info about [externalized configuration](https://docs.spring.io/spring-boot/docs/2.1.6.RELEASE/reference/html/boot-features-external-config.html) and [profiles](https://docs.spring.io/spring-boot/docs/2.1.6.RELEASE/reference/html/boot-features-profiles.html) on the Spring docs.